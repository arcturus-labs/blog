/* Progressive enhancement only: ordinary document flow on narrow/short screens,
   reduced motion, no JS, and print. No wheel interception or scroll snapping. */
(() => {
  'use strict';
  document.documentElement.classList.add('has-js');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const wide = matchMedia('(min-width: 901px) and (min-height: 660px)');
  const stories = [...document.querySelectorAll('[data-story]')].map(section => ({
    section, groups: [...section.querySelectorAll('.moment-group')], moments: [...section.querySelectorAll('.moment')],
    links: [...section.querySelectorAll('.story-outline li a')], index: -1
  }));
  let queued = false;
  const year = document.getElementById('copyright-year');
  if (year) year.textContent = String(new Date().getFullYear());
  const dwellSections = document.querySelectorAll('.turning-point,.proof-intro');
  function layoutMedia(story) {
    const columnWidth = story.section.querySelector('.moments').clientWidth;
    const steps = new Map();
    story.groups.forEach(group => {
      if (!steps.has(group.dataset.step)) steps.set(group.dataset.step, []);
      steps.get(group.dataset.step).push(group);
      group.style.removeProperty('--copy-height');
    });
    steps.forEach(groups => {
      const img = groups[0].querySelector('img');
      const ratio = (img.naturalWidth || Number(img.getAttribute('width'))) /
        (img.naturalHeight || Number(img.getAttribute('height')));
      const setWidth = width => groups.forEach(group => group.style.setProperty('--media-width', `${width}px`));
      const copyHeight = () => Math.max(...groups.flatMap(group => [...group.querySelectorAll('.moment-copy')]).map(copy => copy.getBoundingClientRect().height));
      // Opt-in evidence overlays center readable HTML over dimmed artwork.
      // Other story scenes retain their existing picture-plus-copy layout.
      if (groups[0].classList.contains('quote-overlay')) {
        setWidth(Math.min(columnWidth, innerHeight * .82 * ratio));
        return;
      }
      const maxImageHeight = Math.min(innerHeight * .52, 560);
      const available = innerHeight * .84;
      let width = Math.min(columnWidth, maxImageHeight * ratio);
      // Narrower media means narrower copy. Iterate to reserve enough room for
      // both, then apply one common width/copy-height to every group in a step.
      for (let i = 0; i < 4; i++) {
        setWidth(width);
        const allowedHeight = Math.max(180, available - 24 - copyHeight());
        const nextWidth = Math.min(columnWidth, maxImageHeight * ratio, allowedHeight * ratio);
        if (Math.abs(nextWidth - width) < 1) break;
        width = nextWidth;
      }
      setWidth(width);
      const textHeight = copyHeight();
      groups.forEach(group => group.style.setProperty('--copy-height', `${textHeight}px`));
    });
  }
  function activate(story, index) {
    if (index === story.index) return;
    story.index = index;
    const current = story.moments[index].closest('.moment-group');
    story.moments.forEach((moment, i) => {
      const active = i === index;
      moment.classList.toggle('active', active);
      moment.inert = !active;
      if (active) moment.removeAttribute('aria-hidden');
      else moment.setAttribute('aria-hidden', 'true');
      // The next illustration should already be decoded when it comes into view.
      if (Math.abs(i - index) <= 1) moment.closest('.moment-group').querySelectorAll('img').forEach(img => { img.loading = 'eager'; });
    });
    // The picture belongs to its group, so it changes only when the group does.
    story.groups.forEach(group => group.classList.toggle('active', group === current));
    const step = current.dataset.step;
    story.links.forEach(link => {
      const active = link.dataset.step === step;
      link.classList.toggle('active', active);
      if (active) link.setAttribute('aria-current', 'step');
      else link.removeAttribute('aria-current');
    });
  }
  function configure() {
    const pinned = wide.matches && !reduced.matches;
    dwellSections.forEach(section => section.classList.toggle('is-dwell', pinned));
    // Preserve the original proof layout rather than shrinking its books/type.
    // Tall scenes scroll into view normally, then hold for one viewport of
    // scrolling once their bottom is visible. All content remains reachable.
    const proof = document.getElementById('proof');
    if (pinned) {
      const height = Math.max(innerHeight, proof.querySelector('.proof-stage').scrollHeight);
      proof.style.setProperty('--proof-height', `${height}px`);
      proof.style.setProperty('--proof-top', `${Math.min(0, innerHeight - height)}px`);
    } else {
      proof.style.removeProperty('--proof-height');
      proof.style.removeProperty('--proof-top');
    }
    stories.forEach(story => {
      story.section.classList.toggle('is-pinned', pinned);
      story.index = -1;
      if (pinned) {
        // One screen of scrolling per moment, plus time to arrive and dwell.
        story.section.style.height = `${(story.moments.length + 1) * innerHeight}px`;
        layoutMedia(story);
      } else {
        story.section.style.removeProperty('height');
        story.moments.forEach(moment => { moment.inert = false; moment.removeAttribute('aria-hidden'); moment.classList.remove('active'); });
        story.groups.forEach(group => { group.classList.remove('active'); group.style.removeProperty('--media-width'); group.style.removeProperty('--copy-height'); });
        story.links.forEach(link => { link.removeAttribute('aria-current'); link.classList.remove('active'); });
      }
    });
    update();
  }
  function update() {
    queued = false;
    const cue = document.querySelector('.scroll-cue-fade');
    const cueOpacity = Math.max(0, 1 - scrollY / Math.min(240, innerHeight * .3));
    cue.style.opacity = String(cueOpacity);
    cue.inert = cueOpacity === 0;
    const header = document.querySelector('.opening-nav');
    header.style.opacity = String(Math.max(0, 1 - scrollY / 260));
    header.inert = scrollY > 260;
    stories.forEach(story => {
      if (!story.section.classList.contains('is-pinned')) return;
      const rect = story.section.getBoundingClientRect();
      const travel = story.section.offsetHeight - innerHeight;
      const progress = Math.max(0, Math.min(1, -rect.top / travel));
      activate(story, Math.min(story.moments.length - 1, Math.floor(progress * story.moments.length)));
    });
  }
  function requestUpdate() { if (!queued) { queued = true; requestAnimationFrame(update); } }
  function navigate(target, behavior = 'smooth') {
    // A group's id names its first moment; a later moment keeps its own id.
    const moment = target.classList.contains('moment-group') ? target.querySelector('.moment') : target;
    const story = stories.find(s => s.moments.includes(moment));
    if (story && story.section.classList.contains('is-pinned')) {
      const index = story.moments.indexOf(moment);
      const travel = story.section.offsetHeight - innerHeight;
      scrollTo({ top: scrollY + story.section.getBoundingClientRect().top + (index + .35) / story.moments.length * travel, behavior });
      activate(story, index);
    } else target.scrollIntoView({ behavior, block: 'start' });
  }
  // Allow real source anchors, meaningful hashes and keyboard activation.
  document.querySelectorAll('a[href^="#"]').forEach(link => link.addEventListener('click', event => {
    // "#top" is the true top of the page (the headline sits mid-screen, so #hero-title is not).
    const toTop = link.hash === '#top' && !document.getElementById('top');
    const target = toTop ? document.getElementById('hero-title') : document.getElementById(link.hash.slice(1));
    if (!target || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    if (toTop) scrollTo({ top: 0, behavior: reduced.matches ? 'instant' : 'smooth' });
    else navigate(target, reduced.matches ? 'instant' : 'smooth');
    history.pushState(null, '', link.hash);
    if (link.closest('.scroll-cue,.skip') || link.hash === '#hero-title' || toTop) {
      target.tabIndex = -1;
      target.focus({ preventScroll: true });
    }
  }));
  addEventListener('popstate', () => {
    if (location.hash === '#top' && !document.getElementById('top')) { scrollTo({ top: 0, behavior: 'instant' }); return; }
    const target = document.getElementById(location.hash.slice(1)); if (target) navigate(target, 'instant');
  });
  addEventListener('scroll', requestUpdate, { passive: true });
  let resizeTimer;
  addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(configure, 120); });
  wide.addEventListener('change', configure);
  reduced.addEventListener('change', configure);
  configure();
  document.fonts.ready.then(configure);
  document.querySelectorAll('.scene img').forEach(img => img.addEventListener('load', () => {
    clearTimeout(resizeTimer); resizeTimer = setTimeout(configure, 50);
  }));
  if (location.hash) requestAnimationFrame(() => {
    const target = document.getElementById(location.hash.slice(1));
    if (target) navigate(target, 'instant');
  });
})();

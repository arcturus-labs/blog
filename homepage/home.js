/* Homepage behavior. Progressive enhancement only: without this script, with reduced motion,
   on short or narrow screens, the page is ordinary document flow. No wheel interception. */
(() => {
  'use strict';
  document.documentElement.classList.add('has-js');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const wide = matchMedia('(min-width: 901px) and (min-height: 640px)');
  const $ = s => document.querySelector(s);
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const year = $('#copyright-year');
  if (year) year.textContent = String(new Date().getFullYear());

  const scene = $('.reason-scene');
  const picks = [...document.querySelectorAll('.pick')];
  const dwell = document.querySelectorAll('.turning-point,.proof-intro,.glance');
  const proof = $('#proof');
  let queued = false;

  function configure() {
    const pinned = wide.matches && !reduced.matches;
    scene.classList.toggle('is-pinned', pinned);
    dwell.forEach(s => s.classList.toggle('is-dwell', pinned));
    const glance = $('.glance');
    if (pinned) {
      const height = Math.max(innerHeight, glance.querySelector('.glance-stage').scrollHeight);
      glance.style.setProperty('--glance-height', `${height}px`);
      glance.style.setProperty('--glance-top', `${Math.min(0, innerHeight - height)}px`);
    } else {
      glance.style.removeProperty('--glance-height');
      glance.style.removeProperty('--glance-top');
    }
    if (pinned) {
      const stage = proof.querySelector('.proof-stage');
      const height = Math.max(innerHeight, stage.scrollHeight);
      proof.style.setProperty('--proof-height', `${height}px`);
      proof.style.setProperty('--proof-top', `${Math.min(0, innerHeight - height)}px`);
    } else {
      proof.style.removeProperty('--proof-height');
      proof.style.removeProperty('--proof-top');
      scene.style.removeProperty('--rp');
      picks.forEach(p => { p.inert = false; });
    }
    update();
  }

  function update() {
    queued = false;
    const cue = $('.scroll-cue-fade');
    const cueOpacity = Math.max(0, 1 - scrollY / Math.min(240, innerHeight * .3));
    cue.style.opacity = String(cueOpacity);
    cue.inert = cueOpacity === 0;
    const nav = $('.opening-nav');
    nav.style.opacity = String(Math.max(0, 1 - scrollY / 260));
    nav.inert = scrollY > 260;
    if (scene.classList.contains('is-pinned')) {
      const travel = scene.offsetHeight - innerHeight;
      const rp = clamp(-scene.getBoundingClientRect().top / travel, 0, 1);
      scene.style.setProperty('--rp', rp.toFixed(4));
      // The choices become interactive as they appear, so nobody tabs into something invisible.
      picks.forEach(p => { p.inert = rp < 0.3; });
    }
  }
  const request = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };

  document.querySelectorAll('a[href^="#"]').forEach(link => link.addEventListener('click', event => {
    const target = document.getElementById(link.hash.slice(1));
    if (!target || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: reduced.matches ? 'instant' : 'smooth', block: 'start' });
    history.pushState(null, '', link.hash);
    target.tabIndex = -1;
    target.focus({ preventScroll: true });
  }));

  addEventListener('scroll', request, { passive: true });
  let resizeTimer;
  addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(configure, 120); });
  wide.addEventListener('change', configure);
  reduced.addEventListener('change', configure);
  configure();
  document.fonts.ready.then(configure);
  scene.querySelectorAll('img').forEach(img => img.addEventListener('load', configure));

  // ---- Videos: seamless loop, drag, never tied to vertical scrolling ----
  const strip = $('.talks-strip');
  if (!strip) return;
  let pos = 0, lastSet = 0, last = 0, resumeAt = 0, visible = false, hovering = false, dragging = false, moved = 0, startX = 0, startLeft = 0;
  const track = strip.querySelector('.talks-track');
  const originals = [...track.children];
  function clones() {
    track.querySelectorAll('[data-clone]').forEach(e => e.remove());
    if (reduced.matches) return;
    originals.forEach(card => {
      const clone = card.cloneNode(true);
      clone.dataset.clone = '';
      clone.setAttribute('aria-hidden', 'true');
      clone.tabIndex = -1;
      clone.inert = true;
      track.append(clone);
    });
  }
  clones();
  reduced.addEventListener('change', clones);
  const cycle = () => track.querySelector('[data-clone]')?.offsetLeft - originals[0].offsetLeft;
  strip.addEventListener('keydown', e => {
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    e.preventDefault();
    strip.scrollLeft += e.key === 'ArrowRight' ? 180 : -180;
    pos = strip.scrollLeft; pauseFor(5000);
  });
  strip.addEventListener('touchstart', () => pauseFor(60000), { passive: true });
  strip.addEventListener('touchend', () => pauseFor(5000), { passive: true });
  const speed = 22; // pixels per second: slow enough to read, fast enough to notice
  const pauseFor = ms => { resumeAt = performance.now() + ms; };
  new IntersectionObserver(entries => { visible = entries[0].isIntersecting; }, { threshold: 0.2 }).observe(strip);
  strip.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse') hovering = true; });
  strip.addEventListener('pointerleave', () => { hovering = false; pauseFor(1500); });
  strip.addEventListener('focusin', () => pauseFor(8000));
  strip.addEventListener('scroll', () => { if (Math.abs(strip.scrollLeft - lastSet) > 1.5) { pauseFor(3500); pos = strip.scrollLeft; } }, { passive: true });
  strip.addEventListener('pointerdown', e => {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    dragging = true; moved = 0; startX = e.clientX; startLeft = strip.scrollLeft;
  });
  strip.addEventListener('pointermove', e => {
    if (!dragging) return;
    const dx = e.clientX - startX;
    moved = Math.max(moved, Math.abs(dx));
    if (moved > 5) { strip.classList.add('dragging'); strip.setPointerCapture(e.pointerId); }
    strip.scrollLeft = startLeft - dx;
  });
  const endDrag = e => {
    if (!dragging) return;
    dragging = false; strip.classList.remove('dragging'); pauseFor(5000);
    try { strip.releasePointerCapture(e.pointerId); } catch (_) {}
  };
  strip.addEventListener('pointerup', endDrag);
  strip.addEventListener('pointercancel', endDrag);
  strip.addEventListener('click', e => { if (moved > 5) { e.preventDefault(); e.stopPropagation(); moved = 0; } }, true);
  function tick(time) {
    const dt = Math.min(0.1, (time - last) / 1000);
    last = time;
    const max = strip.scrollWidth - strip.clientWidth;
    if (!reduced.matches && !document.hidden && visible && !hovering && !dragging && !strip.contains(document.activeElement) && time > resumeAt && max > 4) {
      // Keep our own fractional position: browsers may round scrollLeft to whole pixels.
      if (Math.abs(strip.scrollLeft - lastSet) > 1.5) pos = strip.scrollLeft;
      pos += speed * dt;
      const span = cycle();
      if (span && pos >= span) pos %= span;
      strip.scrollLeft = pos;
      lastSet = strip.scrollLeft;
    }
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();

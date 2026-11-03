/* Return to draft_site's continuous star field and depth-based scroll parallax.
   No phase darkening. Dawn/star fade is reserved for the bottom of the page.
   Bounded DPR, 30fps ceiling, reduced-motion and hidden-tab handling; no pause UI. */
(() => {
  'use strict';
  const cv = document.getElementById('sky');
  const ctx = cv.getContext('2d');
  if (!ctx) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let width = 0, height = 0, stars = [], raf = 0, lastTime = 0;
  let mx = 0, my = 0, tx = 0, ty = 0;
  const clamp = x => Math.min(1, Math.max(0, x));
  const smooth = (a, b, x) => { x = clamp((x - a) / (b - a)); return x * x * (3 - 2 * x); };
  const color = (a, b, t) => `rgb(${a.map((v, i) => Math.round(v + (b[i] - v) * t)).join(',')})`;
  function resize() {
    width = innerWidth; height = innerHeight;
    const dpr = Math.min(devicePixelRatio || 1, 1.75);
    cv.width = Math.round(width * dpr); cv.height = Math.round(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    let seed = 7;
    const random = () => (seed = seed * 16807 % 2147483647) / 2147483647;
    const n = Math.round(Math.min(width < 700 ? 85 : 220, width * height / 7200));
    stars = Array.from({ length: n }, () => {
      const four = random() < .12;
      return { x: random(), y: random(), depth: .2 + random() * .8,
        r: four ? 4 + random() * 6 : .5 + random() * 1.2,
        four, phase: random() * 6.28, speed: .4 + random() * .7 };
    });
    draw(performance.now());
  }
  function fourStar(x, y, r) {
    ctx.beginPath(); ctx.moveTo(x, y - r);
    ctx.quadraticCurveTo(x, y, x + r, y); ctx.quadraticCurveTo(x, y, x, y + r);
    ctx.quadraticCurveTo(x, y, x - r, y); ctx.quadraticCurveTo(x, y, x, y - r); ctx.fill();
  }
  function draw(time) {
    const max = document.documentElement.scrollHeight - height;
    const progress = max > 0 ? clamp(scrollY / max) : 0;
    const dawn = 0, sun = 0; // Exploration page: continuous night.
    const gradient = ctx.createLinearGradient(0, 0, 0, height);
    gradient.addColorStop(0, color([4,9,26], [22,40,76], dawn));
    gradient.addColorStop(.62, color([11,30,58], [66,62,104], dawn));
    gradient.addColorStop(1, color([11,30,58], [196,108,78], dawn * dawn));
    ctx.globalAlpha = 1; ctx.fillStyle = gradient; ctx.fillRect(0, 0, width, height);
    const motion = !reduced.matches;
    tx += ((motion && width > 700 ? mx : 0) - tx) * .05;
    ty += ((motion && width > 700 ? my : 0) - ty) * .05;
    if (sun > 0) {
      const x = width * .65, radius = Math.min(width, height) * .085, y = height * (1.03 - .12 * sun);
      const glow = ctx.createRadialGradient(x, y, radius * .4, x, y, Math.max(width, height) * .55);
      glow.addColorStop(0, `rgba(255,200,130,${.45 * sun})`); glow.addColorStop(1, 'rgba(255,200,130,0)');
      ctx.fillStyle = glow; ctx.fillRect(0, 0, width, height);
      ctx.fillStyle = `rgba(255,222,170,${sun})`; ctx.beginPath(); ctx.arc(x, y, radius, 0, Math.PI * 2); ctx.fill();
    }
    if (dawn > 0) {
      ctx.fillStyle = `rgba(7,12,26,${Math.min(1, .92 * smooth(.5, 1, dawn) + sun)})`;
      ctx.beginPath(); ctx.moveTo(0, height); ctx.lineTo(0, height * .955);
      for (let x = 0; x <= width; x += 20) ctx.lineTo(x, height * (.945 + .012 * Math.sin(x * .006) + .008 * Math.sin(x * .017 + 1)));
      ctx.lineTo(width, height); ctx.closePath(); ctx.fill();
    }
    const fade = 1;
    stars.forEach(star => {
      const twinkle = motion ? .75 + .25 * Math.sin(time / 1000 * star.speed + star.phase) : .85;
      ctx.globalAlpha = twinkle * fade * (.35 + .5 * star.depth);
      ctx.fillStyle = '#fff';
      const x = star.x * width + tx * star.depth * 14;
      let y = (star.y * height - (motion ? scrollY * star.depth * .18 : 0)) % height;
      if (y < 0) y += height;
      y += ty * star.depth * 10;
      if (star.four) fourStar(x, y, star.r);
      else { ctx.beginPath(); ctx.arc(x, y, star.r, 0, Math.PI * 2); ctx.fill(); }
    });
    ctx.globalAlpha = 1;
  }
  function loop(time) {
    if (time - lastTime >= 33) { draw(time); lastTime = time; }
    raf = requestAnimationFrame(loop);
  }
  function restart() {
    cancelAnimationFrame(raf);
    if (!document.hidden && !reduced.matches) raf = requestAnimationFrame(loop);
    else if (!document.hidden) draw(performance.now());
  }
  addEventListener('resize', resize);
  addEventListener('scroll', () => { if (reduced.matches) draw(performance.now()); }, { passive: true });
  addEventListener('pointermove', e => { mx = e.clientX / width - .5; my = e.clientY / height - .5; }, { passive: true });
  document.addEventListener('visibilitychange', restart);
  reduced.addEventListener('change', restart);
  resize(); restart();
})();

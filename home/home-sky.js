/* Continuous star field with slow westward drift and depth-based scroll parallax (no mouse parallax).
   No phase darkening. Dawn/star fade is reserved for the bottom of the page.
   Bounded DPR, 30fps ceiling, reduced-motion and hidden-tab handling; no pause UI. */
(() => {
  'use strict';
  const cv = document.getElementById('sky');
  const ctx = cv.getContext('2d');
  if (!ctx) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let width = 0, height = 0, stars = [], raf = 0, lastTime = 0;
  let meteor = null, nextMeteor = Infinity;
  const meteorDelay = () => 5000 + Math.random() * 10000;
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
    const dawn = smooth(.72, 1, progress), sun = smooth(.9, 1, progress);
    const gradient = ctx.createLinearGradient(0, 0, 0, height);
    gradient.addColorStop(0, color([4,9,26], [22,40,76], dawn));
    gradient.addColorStop(.62, color([11,30,58], [66,62,104], dawn));
    gradient.addColorStop(1, color([11,30,58], [196,108,78], dawn * dawn));
    ctx.globalAlpha = 1; ctx.fillStyle = gradient; ctx.fillRect(0, 0, width, height);
    const footer = document.querySelector('footer').getBoundingClientRect();
    const ground = Math.min(height * .945, footer.top - 24);
    const motion = !reduced.matches;
    if (sun > 0) {
      const x = width * .65, radius = Math.min(width, height) * .085, y = ground + radius * .35 + height * .12 * (1 - sun);
      const glow = ctx.createRadialGradient(x, y, radius * .4, x, y, Math.max(width, height) * .55);
      glow.addColorStop(0, `rgba(255,200,130,${.45 * sun})`); glow.addColorStop(1, 'rgba(255,200,130,0)');
      ctx.fillStyle = glow; ctx.fillRect(0, 0, width, height);
      ctx.fillStyle = `rgba(255,222,170,${sun})`; ctx.beginPath(); ctx.arc(x, y, radius, 0, Math.PI * 2); ctx.fill();
    }
    if (dawn > 0) {
      ctx.fillStyle = `rgba(7,12,26,${Math.min(1, .92 * smooth(.5, 1, dawn) + sun)})`;
      ctx.beginPath(); ctx.moveTo(0, height); ctx.lineTo(0, ground);
      for (let x = 0; x <= width; x += 20) ctx.lineTo(x, ground + 6 * Math.sin(x * .006) + 4 * Math.sin(x * .017 + 1));
      ctx.lineTo(width, ground + 6 * Math.sin(width * .006) + 4 * Math.sin(width * .017 + 1));
      ctx.lineTo(width, height); ctx.closePath(); ctx.fill();
    }
    const dawnWash = smooth(.87, 1, progress);
    stars.forEach(star => {
      const twinkle = motion ? .75 + .25 * Math.sin(time / 1000 * star.speed + star.phase) : .85;
      ctx.fillStyle = '#fff';
      // Slow westward drift (about 3–6 px/sec), with seamless wrapping.
      const drift = motion ? time / 1000 * (3 + 3 * star.depth) : 0;
      let x = (star.x * width - drift) % width;
      if (x < 0) x += width;
      let y = (star.y * height - (motion ? scrollY * star.depth * .36 : 0)) % height;
      if (y < 0) y += height;
      // Dawn washes out the low sky first, leaving the high stars visible.
      const altitudeFade = 1 - dawnWash * smooth(.15, .8, y / height);
      if (sun > 0 && y >= ground) return; // Never paint stars over the ground.
      ctx.globalAlpha = twinkle * altitudeFade * (.35 + .5 * star.depth);
      if (star.four) fourStar(x, y, star.r);
      else { ctx.beginPath(); ctx.arc(x, y, star.r, 0, Math.PI * 2); ctx.fill(); }
    });
    if (motion) drawMeteor(time, dawnWash, sun > 0 ? ground : height);
    ctx.globalAlpha = 1;
  }
  function drawMeteor(time, dawnWash, horizon) {
    if (time >= nextMeteor) {
      const direction = Math.random() < .5 ? -1 : 1;
      const angle = .2 + Math.random() * .35;
      meteor = { start: time, duration: 850 + Math.random() * 400,
        x: width * (.25 + Math.random() * .5), y: height * (.08 + Math.random() * .3),
        dx: Math.cos(angle) * direction, dy: Math.sin(angle),
        distance: Math.min(width * .35, 480) };
      nextMeteor = time + meteorDelay();
    }
    if (!meteor) return;
    const t = (time - meteor.start) / meteor.duration;
    if (t >= 1) { meteor = null; return; }
    const x = meteor.x + meteor.dx * meteor.distance * t;
    const y = meteor.y + meteor.dy * meteor.distance * t;
    if (y >= horizon) return;
    const length = Math.min(width * .16, 150) * Math.min(1, t * 5);
    const tailX = x - meteor.dx * length, tailY = y - meteor.dy * length;
    const visibility = 1 - dawnWash * smooth(.15, .8, y / height);
    ctx.globalAlpha = Math.min(1, Math.sin(Math.PI * t) * 1.1 * visibility);
    const trail = ctx.createLinearGradient(tailX, tailY, x, y);
    trail.addColorStop(0, 'rgba(190,215,255,0)');
    trail.addColorStop(1, 'rgba(225,237,255,.8)');
    ctx.strokeStyle = trail; ctx.lineWidth = 2.4; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(tailX, tailY); ctx.lineTo(x, y); ctx.stroke();
    ctx.fillStyle = '#eef5ff';
    ctx.beginPath(); ctx.arc(x, y, 3, 0, Math.PI * 2); ctx.fill();
  }
  function loop(time) {
    if (time - lastTime >= 33) { draw(time); lastTime = time; }
    raf = requestAnimationFrame(loop);
  }
  function restart() {
    cancelAnimationFrame(raf);
    meteor = null;
    nextMeteor = performance.now() + meteorDelay();
    if (!document.hidden && !reduced.matches) raf = requestAnimationFrame(loop);
    else if (!document.hidden) draw(performance.now());
  }
  addEventListener('resize', resize);
  addEventListener('scroll', () => { if (reduced.matches) draw(performance.now()); }, { passive: true });
  document.addEventListener('visibilitychange', restart);
  reduced.addEventListener('change', restart);
  resize(); restart();
})();

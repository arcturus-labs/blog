/* A still version of the homepage star field. Draw once and on resize only:
   no animation loop, timers, scroll effects, or pointer tracking. */
(() => {
  'use strict';
  const canvas = document.createElement('canvas');
  canvas.id = 'blog-stars';
  canvas.setAttribute('aria-hidden', 'true');
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  document.body.prepend(canvas);

  function draw() {
    const width = innerWidth, height = innerHeight;
    const dpr = Math.min(devicePixelRatio || 1, 1.75);
    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    let seed = 7;
    const random = () => (seed = seed * 16807 % 2147483647) / 2147483647;
    const count = Math.round(Math.min(width < 700 ? 85 : 220, width * height / 7200));
    ctx.fillStyle = '#fff';
    for (let i = 0; i < count; i++) {
      const four = random() < .12;
      const x = random() * width, y = random() * height;
      const depth = .2 + random() * .8;
      const radius = four ? 4 + random() * 6 : .5 + random() * 1.2;
      // Consume the homepage's phase/speed values too, to keep its seeded sky.
      random(); random();
      ctx.globalAlpha = .85 * (.35 + .5 * depth);
      ctx.beginPath();
      if (four) {
        ctx.moveTo(x, y - radius);
        ctx.quadraticCurveTo(x, y, x + radius, y);
        ctx.quadraticCurveTo(x, y, x, y + radius);
        ctx.quadraticCurveTo(x, y, x - radius, y);
        ctx.quadraticCurveTo(x, y, x, y - radius);
      } else {
        ctx.arc(x, y, radius, 0, Math.PI * 2);
      }
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  }
  draw();
  addEventListener('resize', draw);
})();

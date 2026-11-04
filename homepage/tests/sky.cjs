/* Deterministic canvas checks: node homepage/tests/sky.cjs */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require('node:path').join(__dirname, '../home-sky.js'), 'utf8');
function render(scrollY, motion = false, time = 0) {
  const stars = [];
  let point;
  const gradient = { addColorStop() {} };
  const ctx = {
    setTransform() {}, createLinearGradient: () => gradient, createRadialGradient: () => gradient,
    fillRect() {}, beginPath() {}, closePath() {}, lineTo() {}, quadraticCurveTo() {},
    moveTo(x, y) { point = {x, y}; }, arc(x, y) { point = {x, y}; },
    fill() { if (this.fillStyle === '#fff') stars.push({...point, alpha: this.globalAlpha}); }
  };
  vm.runInNewContext(source, {
    document: { hidden: false, documentElement: {scrollHeight: 10000},
      getElementById: () => ({getContext: () => ctx}),
      querySelector: () => ({getBoundingClientRect: () => ({top: 750})}), addEventListener() {} },
    innerWidth: 1280, innerHeight: 900, devicePixelRatio: 1, scrollY,
    matchMedia: () => ({matches: !motion, addEventListener() {}}),
    performance: {now: () => time}, addEventListener() {}, cancelAnimationFrame() {}, requestAnimationFrame() {}
  });
  return stars;
}
const night = render(0), dawn = render(9100);
assert(night.length > 100);
const high = dawn.filter(s => s.y < 120);
assert(high.length > 5);
for (const star of high) {
  const original = night.find(s => s.x === star.x && s.y === star.y);
  assert(original);
  assert.equal(star.alpha, original.alpha, 'high stars retain their night brightness');
}
assert(dawn.filter(s => s.y > 600).every(s => s.alpha < .1), 'low stars fade strongly into dawn');
assert(dawn.filter(s => s.y > 700).every(s => s.alpha < .01), 'horizon stars disappear');
assert(dawn.every(s => s.y < 726), 'no stars over the ground');
const first = render(0, true, 1000), later = render(0, true, 2000);
for (let i = 0; i < first.length; i++) {
  const drift = (first[i].x - later[i].x + 1280) % 1280;
  assert(drift >= 3.59 && drift <= 6.01, 'stars drift slowly left');
  assert.equal(first[i].y, later[i].y, 'time drift is horizontal');
}
const scrolled = render(100, true, 1000);
for (let i = 0; i < first.length; i++) {
  const displacement = (first[i].y - scrolled[i].y + 900) % 900;
  assert(displacement >= 7.19 && displacement <= 36.01, 'depth-based scroll parallax');
  assert.equal(first[i].x, scrolled[i].x, 'scroll parallax is vertical');
}
assert(!source.includes('pointermove'), 'no pointer parallax listener');
assert.deepEqual(render(0, false, 1000), render(0, false, 2000), 'reduced motion disables drift');
console.log('Sky altitude-fade, drift and scroll-parallax checks passed');

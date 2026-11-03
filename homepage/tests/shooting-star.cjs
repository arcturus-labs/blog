/* node homepage/tests/shooting-star.cjs */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require('node:path').join(__dirname, '../home-sky.js'), 'utf8');
function setup(random = .5, reduced = false) {
  let now = 0, frame, strokes = [];
  const events = {};
  const gradient = {addColorStop() {}};
  const ctx = {setTransform() {}, createLinearGradient: () => gradient,
    createRadialGradient: () => gradient, fillRect() {}, beginPath() {}, closePath() {},
    lineTo() {}, moveTo() {}, quadraticCurveTo() {}, arc() {}, fill() {},
    stroke() { if (this.globalAlpha > 0) strokes.push(now); }};
  const document = {hidden: false, documentElement: {scrollHeight: 10000},
    getElementById: () => ({getContext: () => ctx}),
    querySelector: () => ({getBoundingClientRect: () => ({top: 10000})}),
    addEventListener(name, fn) {events[name] = fn;}};
  const math = Object.create(Math); math.random = () => random;
  vm.runInNewContext(source, {document, innerWidth:1280, innerHeight:900,
    devicePixelRatio:1, scrollY:0, Math:math,
    matchMedia: () => ({matches:reduced, addEventListener() {}}),
    performance:{now:()=>now}, addEventListener() {},
    cancelAnimationFrame() {frame = null;}, requestAnimationFrame(fn) {frame=fn; return 1;}});
  return {strokes, tick(t) {now=t; if(frame) frame(t);},
    visible(value) {document.hidden=!value;events.visibilitychange();}};
}
for (const [random, delay] of [[0,5000],[.5,10000],[.999,14990]]) {
  const s=setup(random);
  s.tick(delay-100); assert.equal(s.strokes.length,0,'no premature meteor');
  s.tick(delay); s.tick(delay+400); assert.equal(s.strokes.length,1,'meteor has a visible trail');
  s.tick(delay+1400); assert.equal(s.strokes.length,1,'trail expires');
  s.tick(delay*2); s.tick(delay*2+400); assert.equal(s.strokes.length,2,'next randomized interval');
}
const hidden=setup(); hidden.tick(10000);hidden.visible(false);hidden.tick(10500);
assert.equal(hidden.strokes.length,0,'hidden tab pauses');
hidden.visible(true);hidden.tick(11000);assert.equal(hidden.strokes.length,0,'no burst after return');
const reduced=setup(.5,true);reduced.tick(10500);assert.equal(reduced.strokes.length,0,'reduced motion disables meteors');
console.log('Shooting-star timing, trail, visibility and reduced-motion checks passed');

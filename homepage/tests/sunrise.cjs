/* Deterministic canvas checks for the bottom-of-page sunrise: node homepage/tests/sunrise.cjs */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../home-sky.js'), 'utf8');
const W = 1280, H = 900, MAX = 10000 - H;

function setup({ reduced = false, scrollY = MAX } = {}) {
  let now = 0, frame, snap;
  const reset = () => { snap = { sun: null, sky: null, starAlpha: 0 }; };
  reset();
  const listeners = {};
  const ctx = {
    setTransform() {}, fillRect() {}, beginPath() {}, closePath() {}, lineTo() {}, moveTo() {},
    quadraticCurveTo() {}, stroke() {},
    createRadialGradient: () => ({ addColorStop() {} }),
    createLinearGradient() {
      const gradient = { stops: [], addColorStop(offset, color) { this.stops.push(color); } };
      if (!snap.sky) snap.sky = gradient;
      return gradient;
    },
    arc(x, y, r) { if (r > 10) snap.sun = { x, y, r }; },
    fill() { if (this.fillStyle === '#fff') snap.starAlpha = Math.max(snap.starAlpha, this.globalAlpha); },
  };
  const sandbox = {
    document: { hidden: false, documentElement: { scrollHeight: 10000 },
      getElementById: () => ({ getContext: () => ctx }),
      querySelector: () => ({ getBoundingClientRect: () => ({ top: 750 }) }),
      addEventListener(name, fn) { listeners[name] = fn; } },
    innerWidth: W, innerHeight: H, devicePixelRatio: 1, scrollY,
    matchMedia: () => ({ matches: reduced, addEventListener() {} }),
    performance: { now: () => now }, addEventListener() {},
    cancelAnimationFrame() { frame = null; }, requestAnimationFrame(fn) { frame = fn; return 1; },
  };
  vm.createContext(sandbox);
  vm.runInContext(source, sandbox);
  const brightness = gradient => gradient.stops.slice(0, 3).reduce((total, color) =>
    total + color.match(/\d+/g).slice(0, 3).reduce((a, v) => a + Number(v), 0), 0);
  return {
    sandbox,
    // Advance to time t (ms) in 100 ms frames; returns what the last frame painted.
    run(t) {
      let last;
      while (now < t) { now = Math.min(t, now + 100); if (frame) { reset(); frame(now); } last = snap; }
      return { sun: last.sun, sky: last.sky && brightness(last.sky), starAlpha: last.starAlpha };
    },
    // One frame after a long gap, as when a hidden tab becomes visible again.
    jump(t) { now = t; reset(); if (frame) frame(now); return { sun: snap.sun }; },
    visible(value) { sandbox.document.hidden = !value; listeners.visibilitychange(); },
    get now() { return now; },
  };
}

// 1. At the bottom the sun starts just peeking over the horizon, then rises up and to the left.
const s = setup();
const start = s.run(200);
assert(start.sun, 'sun is drawn at the bottom of the page');
const mid = s.run(12700), end = s.run(25200), later = s.run(40000);
assert(mid.sun.y < start.sun.y && mid.sun.x < start.sun.x, 'sun moves up and to the left');
assert(end.sun.y < mid.sun.y && end.sun.x < mid.sun.x, 'sun keeps rising');
const run = start.sun.x - end.sun.x, rise = start.sun.y - end.sun.y;
assert(Math.abs(run - rise) < .01, `equal left and upward travel is exactly 45 degrees (${run} vs ${rise})`);
assert(rise > 300, 'sun climbs well into the sky');
assert.equal(end.sun.r, start.sun.r, 'sun keeps its size');
assert.deepEqual([later.sun.x, later.sun.y], [end.sun.x, end.sun.y], 'sunrise settles and stops');
assert(end.sun.y > 0 && end.sun.x > 0, 'sun stays on screen');

// 2. The sky brightens as the sun rises, and the night stars give way.
assert(mid.sky > start.sky && end.sky > mid.sky, 'sky brightens through the sunrise');
assert(start.starAlpha > .1, 'high stars are visible when the sun first peeks over');
assert(end.starAlpha < .005, 'stars have faded by the time the sun is up');

// 3. Scrolling back up resets it gracefully: gradually, never in one jump.
s.sandbox.scrollY = 0;
const frames = [];
for (let t = 40000; t < 45000; t += 100) frames.push(s.run(t + 100).sky);
const steps = frames.slice(1).map((v, i) => Math.abs(v - frames[i]));
assert(Math.max(...steps) < (end.sky - frames[frames.length - 1]) * .2, 'sky fades back in small steps');
assert(frames[0] > frames[frames.length - 1], 'sky returns toward night');
assert(frames[frames.length - 1] < start.sky + 1, 'reset completes within a few seconds');
s.sandbox.scrollY = MAX;
const again = s.run(s.now + 100).sun;
assert(Math.abs(again.x - start.sun.x) < 1 && Math.abs(again.y - start.sun.y) < 1, 'after a full reset the sun starts low again');

// 4. A brief scroll away only partly retreats, then resumes from where it was.
const p = setup();
const high = p.run(25200).sun;
p.sandbox.scrollY = 0; p.run(p.now + 1000);
p.sandbox.scrollY = MAX;
const partial = p.run(p.now + 100).sun;
assert(partial.y > high.y && partial.y < start.sun.y, 'a short absence retreats only part of the way');

// 5. A hidden tab never jumps the sunrise ahead.
const h = setup();
const before = h.run(5000).sun;
h.visible(false); h.visible(true);
const after = h.jump(65000).sun; // a minute passed while hidden, delivered as a single frame
assert(Math.abs(after.y - before.y) < 5, `returning from a hidden tab does not leap ahead (${before.y} -> ${after.y})`);
const resumed = h.run(65500).sun;
assert(resumed.y < after.y && resumed.y > after.y - 10, 'then it resumes rising at its normal pace');

// 6. Reduced motion keeps the existing static dawn: no sunrise animation.
const r = setup({ reduced: true });
const still = r.run(200).sun;
const stillLater = r.run(30000).sun;
assert.deepEqual([stillLater.x, stillLater.y], [still.x, still.y], 'reduced motion does not animate the sun');

// 7. Away from the bottom the sun never rose, so nothing changed there.
const t = setup({ scrollY: 0 });
assert.equal(t.run(30000).sun, null, 'no sun at the top of the page');
console.log('Sunrise path, brightening, graceful reset, hidden-tab and reduced-motion checks passed');

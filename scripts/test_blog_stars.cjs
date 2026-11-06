/* node scripts/test_blog_stars.cjs */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require('node:path').join(__dirname, '../docs/assets/scripts/blog-stars.js'), 'utf8');
const events = {}, stars = [];
let point;
const canvas = {setAttribute(name, value) {this[name] = value;}};
const ctx = {setTransform() {}, beginPath() {},
  moveTo(x, y) {point = {x, y, four: true};},
  quadraticCurveTo() {}, arc(x, y, r) {point = {x, y, r, four: false};},
  fill() {stars.push({...point, alpha: this.globalAlpha});}};
canvas.getContext = () => ctx;
const sandbox = {innerWidth:1440, innerHeight:900, devicePixelRatio:2,
  document:{createElement:()=>canvas, body:{prepend() {}}},
  addEventListener(name, fn) {events[name] = fn;}};
vm.runInNewContext(source, sandbox);
assert.equal(canvas['aria-hidden'], 'true');
assert.equal(stars.length, 180);
assert(stars.some(s=>s.four) && stars.some(s=>!s.four));
assert.equal(canvas.width, 2520, 'DPR is bounded');
assert.deepEqual(Object.keys(events), ['resize'], 'no scroll, pointer or animation listeners');
const first = [...stars]; stars.length = 0; events.resize();
assert.deepEqual(stars, first, 'the seeded field stays identical on redraw');
sandbox.innerWidth = 390; stars.length = 0; events.resize();
assert(stars.length <= 85, 'mobile star count is bounded');
assert(stars.every(s => s.x >= 0 && s.x <= 390));
console.log('Static blog stars: seeded, bounded, resize-only and decorative');

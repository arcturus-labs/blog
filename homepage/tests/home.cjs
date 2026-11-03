/* Homepage checks. Serve the homepage/ directory (python3 -m http.server 8001 -d homepage) at 127.0.0.1:8001 first.
   NODE_PATH=... node tests/home.cjs . Never subscribes anyone. */
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const url = 'http://127.0.0.1:8001/index.html';
const root = path.resolve(__dirname, '..');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const out = [];
  try {
    for (const cfg of [
      { name: 'wide', viewport: { width: 1840, height: 1000 } },
      { name: 'desktop', viewport: { width: 1440, height: 900 } },
      { name: 'laptop', viewport: { width: 1280, height: 720 } },
      { name: 'small-laptop', viewport: { width: 1024, height: 668 } },
      { name: 'tablet', viewport: { width: 820, height: 1180 } },
      { name: 'phone', viewport: { width: 390, height: 844 } },
      { name: 'small-phone', viewport: { width: 320, height: 568 } },
      { name: 'reduced', viewport: { width: 1280, height: 720 }, reducedMotion: 'reduce' },
      { name: 'no-js', viewport: { width: 1280, height: 720 }, javaScriptEnabled: false }
    ]) {
      const { name, ...options } = cfg;
      const page = await browser.newPage(options);
      const errors = [], failed = [];
      page.on('pageerror', e => errors.push(e.message));
      page.on('requestfailed', r => failed.push(r.url()));
      await page.goto(url);
      await page.evaluate(() => document.fonts.ready);
      await sleep(300);
      const tag = 'home ' + name;
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, tag + ' overflow');
      const text = await page.locator('body').innerText();
      for (const bad of ['—', 'Preview only', 'View larger', 'Illustrative interfaces', 'Build it with']) assert.equal(text.includes(bad), false, `${tag}: ${bad}`);
      assert.equal(await page.locator('sup,.story-meter,.other-paths').count(), 0, tag);
      assert.equal(await page.locator('h1').count(), 1);
      assert.match(await page.locator('.reason-title').textContent(), /You’re here for a reason\./);
      // The three choices lead to the three story pages that exist.
      const hrefs = await page.locator('.pick a').evaluateAll(a => a.map(x => x.getAttribute('href')));
      assert.deepEqual(hrefs, ['agentic-web.html', 'workflows.html', 'software-factories.html']);
      for (const h of hrefs) assert(fs.existsSync(path.join(root, h)), h + ' missing');
      assert.equal(await page.locator('.testimonials figure').count(), 4);
      assert.equal(await page.locator('.talk:not([data-clone])').count(), 16);
      assert.equal(await page.locator('.talk:not([data-clone]) .channel-icon').count(), 16);
      assert.equal(await page.locator('#videos-title').innerText(), 'Talks, workshops, and conversations with John Berryman.');
      assert.match(await page.locator('h1').innerText(), /Building the future\nof AI products\nand workflows/);
      assert.equal(await page.locator('.turning-point').count(), 0);
      assert.equal(await page.locator('.glance .glance-title').count(), 1);
      assert.match(await page.locator('.testimonials').innerText(), /Founder, CETA Global; Head of Global Mental Health at Google/);
      assert.equal(await page.locator('.book-right .authorship').count(), 1);
      assert.equal(await page.locator('footer a[href="https://www.youtube.com/@Arcturus-Labs"]').count(), 1);
      assert.equal(await page.locator('.book-tab').evaluate(e => getComputedStyle(e).position), 'fixed');
      assert.equal(await page.locator('.book-tab').getAttribute('href'), 'https://calendly.com/jfberryman/15min');
      assert.equal(await page.locator('footer').evaluate(e => getComputedStyle(e).backgroundColor), 'rgb(7, 12, 26)');
      assert.deepEqual(await page.locator('.pick-text').allTextContents(), ['We’re losing our website traffic to chat.', 'Our expert staff is toiling away on tasks that should be automated.', 'Competitors ship at the speed of AI. We’re stuck in the stone age.']);
      assert.equal(await page.locator('.posts li').count(), 3);
      assert.equal(await page.locator('#subscribe-form').getAttribute('action'), 'https://app.convertkit.com/forms/7337584/subscriptions');
      const pinned = await page.locator('.reason-scene.is-pinned').count();
      if (pinned) {
        const travel = await page.evaluate(() => { const s = document.querySelector('.reason-scene'); return s.offsetHeight - innerHeight; });
        const top = await page.evaluate(() => { const s = document.querySelector('.reason-scene'); return scrollY + s.getBoundingClientRect().top; });
        const states = [];
        for (const rp of [.05, .3, .5, .7, .85, .99]) {
          await page.evaluate(y => scrollTo({ top: y, behavior: 'instant' }), top + travel * rp);
          await sleep(250);
          states.push(await page.evaluate(() => ({
            title: Number(getComputedStyle(document.querySelector('.reason-title')).opacity),
            picks: [...document.querySelectorAll('.pick')].map(p => Number(getComputedStyle(p).opacity)),
            shots: [...document.querySelectorAll('.pick .shot')].map(p => Number(getComputedStyle(p).opacity)),
            stars: [...document.querySelectorAll('.pick .star')].map(p => Number(getComputedStyle(p).opacity)),
            actions: [...document.querySelectorAll('.pick-action')].map(p => Number(getComputedStyle(p).opacity)),
            inert: [...document.querySelectorAll('.pick')].map(p => p.inert),
            inView: [...document.querySelectorAll('.pick-text,.pick-action,.shot')].every(e => { const r = e.getBoundingClientRect(); return r.top >= 0 && r.bottom <= innerHeight; })
          })));
        }
        assert(states[0].title < 1 && states[1].title === 1, tag + ' title entrance');
        assert(states[1].picks[0] > states[1].picks[1] && states[1].picks[1] >= states[1].picks[2], tag + ' staggered choices');
        assert(states[2].picks.every(o => o > 0.95), tag + ' all choices present by halfway');
        assert(states[1].shots.every(o => o === 1) && states[1].actions.every(o => o === 1), tag + ' constellations arrive with choices');
        assert.equal(states[1].stars.length, 0, tag + ' no placeholder stars');
        // Dwell: everything is complete and unchanged across the last stretch of scrolling.
        for (const k of [3, 4, 5]) { assert(states[k].picks.every(o => o === 1) && states[k].actions.every(o => o === 1), tag + ' dwell ' + k); assert.equal(states[k].inView, true, tag + ' choices fully in view ' + k); }
        assert.deepEqual(states[5].inert, [false, false, false]);
        assert.deepEqual(states[0].inert, [true, true, true]);
        if (name === 'laptop') {
          await page.evaluate(y => scrollTo({ top: y, behavior: 'instant' }), top + travel * .99); await sleep(200);
          await page.screenshot({ path: '/tmp/home-final-reason.png' });
        }
      } else {
        // Not pinned: every choice and picture is fully visible without scrolling magic.
        await page.locator('.reason-scene').scrollIntoViewIfNeeded();
        for (const img of await page.locator('.pick .shot').all()) { await img.scrollIntoViewIfNeeded(); await img.evaluate(i => i.decode()); assert.equal(Number(await img.evaluate(i => getComputedStyle(i).opacity)), 1); }
        assert.equal(await page.locator('.pick[inert]').count(), 0);
      }
      assert.deepEqual(await page.evaluate(() => [...document.images].filter(i => i.complete && i.loading !== 'lazy' && !i.naturalWidth).map(i => i.src)), []);
      // Hero
      await page.evaluate(() => scrollTo({ top: 0, behavior: 'instant' })); await sleep(3300);
      const hero = await page.evaluate(() => { const c = document.querySelector('.hero-copy').getBoundingClientRect(); return { m: [c.left, innerWidth - c.right], o: document.querySelector('.hero-sub').getBoundingClientRect().bottom > document.querySelector('.scroll-cue').getBoundingClientRect().top }; });
      assert(Math.abs(hero.m[0] - hero.m[1]) < 1 && !hero.o, tag + ' hero');
      await page.screenshot({ path: `/tmp/home-${name}-hero.png` });
      // Videos carousel
      const strip = page.locator('.talks-strip');
      await strip.scrollIntoViewIfNeeded(); await sleep(300);
      const overflowing = await strip.evaluate(s => s.scrollWidth - s.clientWidth);
      assert(overflowing > 4, tag + ' strip should overflow');
      assert.equal(await strip.evaluate(s => getComputedStyle(s).overflowY), 'hidden');
      assert(await page.locator('.talk:not([data-clone])').evaluateAll(a => a.every(x => /https:\/\/(www.youtube.com|youtu.be)\//.test(x.href))));
      assert.equal(await page.locator('[data-clone]:not([aria-hidden="true"]),[data-clone]:not([tabindex="-1"])').count(), 0);
      if (name === 'laptop') {
        // Auto-scroll moves slowly without any input, and does not touch page scrolling.
        const y0 = await page.evaluate(() => scrollY);
        await page.mouse.move(5, 5);
        await sleep(300);
        const start = await strip.evaluate(s => s.scrollLeft);
        await sleep(2800);
        const moved = await strip.evaluate(s => s.scrollLeft);
        assert(Math.abs(moved - start) > 20 && Math.abs(moved - start) < 200, `auto-scroll should be slow but visible: ${start} -> ${moved}`);
        assert.equal(await page.evaluate(() => scrollY), y0, 'auto-scroll must not move the page');
        // Dragging with the mouse scrolls the strip and does not click the link underneath.
        const box = await strip.boundingBox();
        await page.mouse.move(box.x + 500, box.y + 120);
        await page.mouse.down();
        await page.mouse.move(box.x + 300, box.y + 120, { steps: 8 });
        await page.mouse.up();
        const dragged = await strip.evaluate(s => s.scrollLeft);
        assert(dragged > moved + 100 || dragged < moved - 100, `drag moved the strip: ${dragged} vs ${moved}`);
        assert.equal(page.url(), url, 'drag should not navigate');
        // A vertical wheel over the strip scrolls the PAGE, never the strip.
        const before = await strip.evaluate(s => s.scrollLeft); const py = await page.evaluate(() => scrollY);
        await page.mouse.move(box.x + 400, box.y + 100);
        await page.mouse.wheel(0, 400); await sleep(400);
        assert(await page.evaluate(() => scrollY) > py + 100, 'vertical wheel scrolled the page');
        assert(Math.abs((await strip.evaluate(s => s.scrollLeft)) - before) < 3, 'vertical wheel must not move the strip');
        // Keyboard users can reach and scroll it.
        await strip.focus(); const k0 = await strip.evaluate(s => s.scrollLeft);
        await page.keyboard.press('ArrowRight'); await sleep(300);
        assert((await strip.evaluate(s => s.scrollLeft)) > k0, 'arrow key scrolls strip');
        await strip.evaluate(s => { s.blur(); const cards = s.querySelectorAll('.talk'); s.scrollLeft = cards[16].offsetLeft - cards[0].offsetLeft - 8; });
        await page.mouse.move(5, 5);
        await sleep(6000);
        assert((await strip.evaluate(s => s.scrollLeft)) < 200, 'endless carousel wraps forward');

      }
      if (name === 'reduced') {
        await strip.evaluate(s => { s.scrollLeft = 0; }); await sleep(2200);
        assert.equal(await strip.evaluate(s => s.scrollLeft), 0, 'no auto-scroll with reduced motion');
      }
      if (name === 'phone') {
        // Touch swipe uses native horizontal scrolling and still allows vertical page scroll.
        assert.equal(await strip.evaluate(s => getComputedStyle(s).touchAction), 'pan-x pan-y');
        await page.locator('.reason-scene').scrollIntoViewIfNeeded(); await sleep(200);
        await page.screenshot({ path: '/tmp/home-phone-reason.png' });
      }
      if (['laptop', 'desktop', 'wide'].includes(name)) {
        const fit = await page.locator('.proof-stage').evaluate(e => ({ height: e.scrollHeight, viewport: innerHeight }));
        assert(fit.height <= fit.viewport, tag + ' complete proof fits');
        await page.locator('#proof').scrollIntoViewIfNeeded();
        await page.screenshot({ path: `/tmp/home-${name}-proof.png` });
        console.log(tag, 'proof', JSON.stringify(fit));
      }
      await page.locator('footer').scrollIntoViewIfNeeded();
      await sleep(150);
      await page.screenshot({ path: `/tmp/home-${name}-footer.png` });
      // Proof dwell + anchors + footer
      if (name === 'laptop') {
        await page.locator('a.nav-call').scrollIntoViewIfNeeded().catch(() => {});
        await page.evaluate(() => scrollTo({ top: 0, behavior: 'instant' })); await sleep(100);
        await page.locator('a.nav-call').click(); await sleep(1500);
        assert((await page.locator('#contact').boundingBox()).y < 200, 'Book a call jumps to contact');
        await page.screenshot({ path: '/tmp/home-contact.png' });
        const brand = await page.locator('footer .footer-brand').getAttribute('href');
        assert.equal(brand, 'index.html');
        const year = await page.locator('#copyright-year').textContent();
        assert.equal(year, String(new Date().getFullYear()));
      }
      assert.deepEqual(errors, [], tag);
      assert.deepEqual(failed, [], tag);
      out.push({ view: name, pinned: !!pinned });
      await page.close();
    }
    // Links from the other pages to the homepage now resolve.
    for (const f of ['workflows.html', 'software-factories.html']) {
      const html = fs.readFileSync(path.join(root, f), 'utf8');
      assert(!html.includes('../draft_site/index.html'), f);
      assert(html.includes('href="index.html"'), f);
    }
    console.log(JSON.stringify({ ok: true, runs: out.length }));
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });

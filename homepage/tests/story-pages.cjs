/* Generic checks for story pages built from the shared template.
   PAGES="workflows.html,software-factories.html" NODE_PATH=... node tests/story-pages.cjs
   Serve the homepage/ directory (python3 -m http.server 8001 -d homepage) at 127.0.0.1:8001 first. Never subscribes anyone. */
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const pages = (process.env.PAGES || 'workflows.html').split(',');
const base = process.env.BASE_URL || 'http://127.0.0.1:8001/';
(async () => {
  const browser = await chromium.launch({ headless: true });
  const results = [];
  try {
    for (const file of pages) {
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
        const errors = [];
        page.on('pageerror', e => errors.push(e.message));
        const failed = [];
        page.on('requestfailed', r => failed.push(r.url()));
        await page.goto(base + file);
        await page.evaluate(() => document.fonts.ready);
        const tag = `${file} ${name}`;
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, tag + ' overflow');
        // Pinned inactive moments are hidden; inspect all narrative text, not only the active scene.
        const body = (await page.locator('body').textContent()).replace(/\s+/g, ' ');
        for (const bad of ['—', 'Preview only', 'View larger', 'Illustrative interfaces']) assert.equal(body.includes(bad), false, `${tag}: ${bad}`);
        assert.equal(await page.locator('sup,.story-meter,.section-next,.other-paths,.scene a,.scene figcaption').count(), 0, tag);
        assert.equal(await page.locator('.problem .moment').count() >= 3, true);
        if (file === 'workflows.html') {
          assert.equal(await page.locator('#problem .story-outline li').count(), 3, tag + ' problem outline');
          assert.equal(await page.locator('#solution .story-outline li').count(), 4, tag + ' virtuous-cycle outline');
          assert.equal(await page.locator('.quote-overlay').count(), 3, tag + ' toil evidence overlays');
          assert.equal(await page.locator('#s4').count(), 1, tag + ' fourth solution');
          assert.match(await page.locator('h1').innerText(), /Scale their expertise,/);
          for (const text of ['41%', '4.9 hours', '60–70%']) {
            assert(body.includes(text), tag + ' missing evidence ' + text);
          }
          assert.match(await page.locator('#p2 blockquote').textContent(), /I wasn't a financial advisor/);
          assert.equal(await page.locator('.scene img[src*="wf-constellation"]').count(), 9, tag + ' constellation scenes');
          assert.equal((await page.locator('#turn-title').textContent()).replace(/\s+/g, ' ').trim(), 'Augment your experts on day one.Keep humans in charge.Automate tasks dependably.', tag + ' solution lead-in');
          assert.match(await page.locator('#p2 .mobile-heading').innerText(), /How can you trust/);
          assert.equal(await page.locator('#p2 .moment-copy > p').count(), 0, tag + ' quote stands alone');
          assert.equal(await page.locator('#s2-study,#s2-first-drafts').count(), 0, tag + ' removed statistic moments');
          assert.equal(await page.locator('#solution .moment[data-step="1"]').count(), 1, tag + ' solution 2 is a single moment');
          assert.equal(await page.locator('#s2-expert-judgment').count(), 0, tag + ' removed Joe Choy slide');
          assert(!body.includes('Joe Choy') && !body.includes('strong starting point'), tag + ' no lawyer quote');
          assert(!body.includes('5,172') && !body.includes('25–35%'), tag + ' removed numeric moments');
          const lead = await page.locator('#turn-title').evaluate(e => ({ align: getComputedStyle(e).textAlign, turn: getComputedStyle(e.querySelector('.hero-turn')).textAlign }));
          assert.deepEqual(lead, { align: 'center', turn: 'center' }, tag + ' centered lead-in');
          assert(body.includes('determined to be low-risk and highly dependable'), tag + ' solution 3 copy');
          assert(body.includes('rerun the benchmarks to ensure workflow quality stays on track'), tag + ' solution 4 copy');
          assert.equal(await page.locator('#s4 .moment-copy p').count(), 1, tag + ' removed trailing sentence');
        }
        if (file === 'software-factories.html') {
          assert.equal(await page.locator('#problem .story-outline li').count(), 3, tag + ' factory problem outline');
          assert.equal(await page.locator('#solution .story-outline li').count(), 3, tag + ' factory solution outline');
          assert.equal(await page.locator('#problem .moment').count(), 3, tag + ' factory problems');
          assert.equal(await page.locator('#solution .moment').count(), 4, tag + ' factory solution moments');
          assert.equal(await page.locator('.scene img[src*="sf-constellation"]').count(), 7, tag + ' factory artwork');
          assert(body.includes('Getting started iseasier than you think'), tag + ' approved factory hero');
          assert(!body.includes('easier than you think.'), tag + ' no hero period');
          assert(body.includes('Future-proof your software factory.'), tag + ' portable process');
          assert.match(await page.locator('#p1 blockquote').textContent(), /Within weeks, hundreds of engineers/);
          assert.equal(await page.locator('#p1 .moment-copy > p').count(), 0, tag + ' quote replaces paragraph');
          assert.equal(await page.locator('#p1 cite a').getAttribute('href'), 'https://ideas.fin.ai/p/we-gave-claude-code-to-everyone-at');
          assert.match(await page.locator('#p1 img').getAttribute('src'), /p1-assembly-v2/);
          assert(body.includes('A faster way to build software is taking shape.'), tag + ' upbeat opportunity');
          assert(body.includes('But an AI software factory is worthless'), tag + ' factory dependability');
          assert.match(await page.locator('#p3 img').getAttribute('src'), /p3-gear-electronics/);
          assert(body.includes('Will your software factory be out of date'), tag + ' technology concern');
          const lead = await page.locator('#turn-title').evaluate(e => ({
            align: getComputedStyle(e).textAlign,
            turn: getComputedStyle(e.querySelector('.hero-turn')).textAlign,
            width: e.getBoundingClientRect().width,
            viewport: innerWidth
          }));
          assert.equal(lead.align, 'center', tag + ' centered factory transition');
          assert.equal(lead.turn, 'center', tag + ' centered factory transition relief');
          assert(lead.width <= lead.viewport, tag + ' factory transition width');
          assert.equal((await page.locator('#turn-title').textContent()).trim(), 'Start with hands-on collaborationBuild toward hands-off automation');
          assert.equal(await page.locator('#s2-verify').count(), 1, tag + ' independent verification');
        }
        const moments = await page.locator('.moment').count();
        const pinned = await page.locator('.is-pinned').count();
        if (pinned) {
          for (const id of ['problem', 'solution']) {
            const count = await page.locator(`#${id} .moment`).count();
            const seen = new Map();
            for (let i = 0; i < count; i++) {
              await page.evaluate(({ id, i }) => {
                const s = document.getElementById(id);
                scrollTo({ top: scrollY + s.getBoundingClientRect().top + (i + .45) * innerHeight, behavior: 'instant' });
              }, { id, i });
              await sleep(350);
              const f = await page.locator(`#${id} .moment.active`).evaluate(async m => {
                const img = m.querySelector('img'); await img.decode();
                const copy = m.querySelector('.moment-copy').getBoundingClientRect();
                const image = img.getBoundingClientRect();
                const outline = m.closest('[data-story]').querySelector('.story-outline').getBoundingClientRect();
                return { id: m.id, step: m.dataset.step, overlay: m.classList.contains('quote-overlay'), copyTop: copy.top, copyCenter: (copy.top + copy.bottom) / 2, copyBottom: copy.bottom, copyLeft: copy.left, copyWidth: copy.width, center: (image.top + copy.bottom) / 2,
                         image: [image.x, image.y, image.width, image.height], outlineBottom: outline.bottom, outlineTop: outline.top, h: innerHeight };
              });
              assert(f.copyBottom <= f.h - 5, `${tag} ${f.id} copy clipped`);
              assert(f.outlineBottom <= f.h && f.outlineTop >= 0, `${tag} outline clipped`);
              assert(Math.abs(f.copyLeft - f.image[0]) < 1 && Math.abs(f.copyWidth - f.image[2]) < 1, `${tag} ${f.id} copy/image misaligned`);
              assert(Math.abs((f.overlay ? f.copyCenter : f.center) - f.h / 2) < 3, `${tag} ${f.id} not centered`);
              if (f.overlay) {
                assert(f.copyTop >= 0, `${tag} ${f.id} overlay text clipped at top`);
                const opacity = await page.locator(`#${f.id} .scene`).evaluate(e => Number(getComputedStyle(e).opacity));
                assert(opacity > 0 && opacity < .4, `${tag} ${f.id} artwork not dimmed behind text`);
              }
              assert.equal(await page.locator(`#${id} [aria-current="step"]`).count(), 1);
              if (seen.has(f.step)) assert.deepEqual(f.image, seen.get(f.step), `${tag} ${f.id} image moved`);
              seen.set(f.step, f.image);
              if (name === 'laptop') await page.screenshot({ path: `/tmp/${file.replace('.html','')}-${f.id}.png` });
            }
          }
        } else {
          for (const img of await page.locator('.scene img').all()) { await img.scrollIntoViewIfNeeded(); await img.evaluate(i => i.decode()); }
        }
        assert.deepEqual(await page.evaluate(() => [...document.images].filter(i => i.complete && !i.naturalWidth).map(i => i.src)), []);
        await page.evaluate(() => scrollTo({ top: 0, behavior: 'instant' }));
        await sleep(3300);
        const hero = await page.evaluate(() => {
          const c = document.querySelector('.hero-copy').getBoundingClientRect();
          return { m: [c.left, innerWidth - c.right], overlap: document.querySelector('.hero-sub').getBoundingClientRect().bottom > document.querySelector('.scroll-cue').getBoundingClientRect().top };
        });
        assert(Math.abs(hero.m[0] - hero.m[1]) < 1, tag + ' hero margins');
        assert.equal(hero.overlap, false, tag + ' hero overlaps cue');
        await page.screenshot({ path: `/tmp/${file.replace('.html','')}-${name}-hero.png` });
        if (name === 'phone') { await page.locator('.solution .moment').last().scrollIntoViewIfNeeded(); await sleep(300); await page.screenshot({ path: `/tmp/${file.replace('.html','')}-phone-story.png` }); }
        if (name === 'laptop') {
          await page.evaluate(() => { const t = document.querySelector('.turning-point'); scrollTo({ top: scrollY + t.getBoundingClientRect().top + 80, behavior: 'instant' }); });
          await sleep(100);
          const a = await page.locator('.turn-stage').boundingBox();
          await page.evaluate(() => scrollBy({ top: 250, behavior: 'instant' })); await sleep(100);
          assert.equal(a.y, (await page.locator('.turn-stage').boundingBox()).y, tag + ' transition dwell');
          await page.screenshot({ path: `/tmp/${file.replace('.html','')}-transition.png` });
          await page.locator('.solution a[data-step="2"]').click(); await sleep(1200);
          assert.equal(await page.locator('#solution .moment.active').getAttribute('data-step'), '2');
          await page.locator('#proof').scrollIntoViewIfNeeded(); await sleep(300);
          await page.screenshot({ path: `/tmp/${file.replace('.html','')}-proof.png` });
          assert.equal(await page.locator('.testimonials figure').count(), 4);
        }
        if (options.viewport.width >= 1280 && options.viewport.height >= 720) {
          const proof = await page.locator('.proof-stage').evaluate(e => ({ height: e.getBoundingClientRect().height, viewport: innerHeight }));
          assert(proof.height <= proof.viewport + 1, `${tag} compact proof exceeds one screen`);
          assert.equal(await page.locator('link[href="compact-proof.css"]').count(), 1, tag + ' shared proof stylesheet');
          assert.equal(await page.locator('.book-right .authorship').count(), 1, tag + ' shared proof authorship');
        }
        assert.equal(await page.locator('#subscribe-form').getAttribute('action'), 'https://app.convertkit.com/forms/7337584/subscriptions');
        assert.deepEqual(errors, [], tag);
        assert.deepEqual(failed, [], tag);
        results.push({ page: file, view: name, moments, pinned: !!pinned });
        await page.close();
      }
    }
    console.log(JSON.stringify({ ok: true, runs: results.length }, null, 1));
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });

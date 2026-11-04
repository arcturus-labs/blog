/* Run with Playwright installed: NODE_PATH=/path/to/node_modules node tests/smoke.cjs
   Does NOT subscribe anyone. Kit requests in form-flow tests are intercepted.
   Serve the homepage/ directory (python3 -m http.server 8001 -d homepage) at 127.0.0.1:8001 first. */
const { chromium } = require('playwright');
const fs = require('node:fs/promises');
const path = require('node:path');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const base = process.env.BASE_URL || 'http://127.0.0.1:8001/agentic-web.html';
const worker = 'https://kit.arcturus-labs.com/verify_subscription';
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const browser = await chromium.launch({ headless: true });
  const results = [];
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
      const errors = [];
      page.on('pageerror', e => errors.push(e.message));
      await page.goto(base);
      await page.evaluate(() => document.fonts.ready);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, name + ' overflow');
      assert.equal(await page.locator('sup,.story-meter,.section-next,.other-paths,.moment-label').count(), 0);
      assert.equal(await page.locator('.scene a,.scene figcaption').count(), 0);
      assert.equal(await page.locator('#subscription-status').textContent(), '');
      assert.equal(await page.locator('#s2-invite').count(), 0);
      assert.equal(await page.locator('#s2 .moment-copy p').count(), 1);
      assert.match(await page.locator('#s2 .gold').textContent(), /When possible/);
      assert.match(await page.locator('#p3 .gold').textContent(), /switching context/);
      assert.match(await page.locator('#s3 .gold').textContent(), /leave it at the door/);
      assert.equal(await page.locator('.takeaway').count(), 0);
      assert.match(await page.locator('#p1 .gold').textContent(), /versus 15% without one/);
      assert.match(await page.locator('#s1 .gold').textContent(), /accessible content/);
      assert.equal(await page.locator('#s2 em').textContent(), 'into an experience you own.');
      const goldColors = await page.locator('#p1 .gold').evaluate(e=>[getComputedStyle(e).color,getComputedStyle(e.querySelector('strong')).color]);
      assert.equal(goldColors[0],goldColors[1]);
      if (name !== 'no-js') assert.equal(await page.locator('#copyright-year').textContent(), String(new Date().getFullYear()));
      const text = await page.locator('body').innerText();
      for (const forbidden of ['Preview only', 'Illustrative interfaces', 'View larger', 'Already taking shape', 'Nikki Baird', '—']) {
        assert.equal(text.includes(forbidden), false, name + ': ' + forbidden);
      }
      const pinned = await page.locator('.is-pinned').count();
      const bounds = [];
      if (pinned) {
        for (const id of ['problem', 'solution']) {
          const count = await page.locator('#' + id + ' .moment').count();
          const stepRects = new Map();
          for (let i = 0; i < count; i++) {
            await page.evaluate(({ id, i }) => {
              const section = document.getElementById(id);
              scrollTo({ top: scrollY + section.getBoundingClientRect().top + (i + .45) * innerHeight, behavior: 'instant' });
            }, { id, i });
            await sleep(350);
            const frame = await page.locator('#' + id + ' .moment.active').evaluate(async m => {
              const group = m.closest('.moment-group'); const img = group.querySelector('img'); await img.decode();
              const copy = group.querySelector('.moment-copies').getBoundingClientRect(); // the copies' shared reserved box
              const image = img.getBoundingClientRect();
              const outline = m.closest('[data-story]').querySelector('.story-outline').getBoundingClientRect();
              return { id: group.id, step: group.dataset.step, copyBottom: copy.bottom, copyLeft: copy.left, copyWidth: copy.width, groupCenter: (image.top+copy.bottom)/2, image: [image.x,image.y,image.width,image.height], outlineBottom: outline.bottom, height: innerHeight };
            });
            assert(frame.copyBottom <= frame.height - 5, `${name} ${frame.id} text clipped: ${frame.copyBottom}`);
            assert(frame.outlineBottom <= frame.height, `${name} outline clipped`);
            assert(Math.abs(frame.copyLeft-frame.image[0]) < 1, `${name} ${frame.id} copy not aligned to image`);
            assert(Math.abs(frame.copyWidth-frame.image[2]) < 1, `${name} ${frame.id} copy width differs`);
            assert(Math.abs(frame.groupCenter-frame.height/2) < 3, `${name} ${frame.id} group not centered`);
            assert.equal(await page.locator('#' + id + ' [aria-current="step"]').count(), 1);
            const previous = stepRects.get(frame.step);
            if (previous) assert.deepEqual(frame.image, previous, `${name} ${frame.id} image shifted`);
            stepRects.set(frame.step, frame.image);
            bounds.push(frame);
            if (name === 'laptop') await page.screenshot({ path: `/tmp/arcturus3-${frame.id}.png` });
          }
        }
        assert.equal(bounds.length, 8);
      } else {
        assert.equal(await page.locator('.moment[aria-hidden="true"]').count(), 0);
        assert.equal(await page.locator('#s3 img').count(), 1, 'solution 3 shows its picture once');
        // Scroll each illustration into view so lazy loading is actually tested.
        for (const image of await page.locator('.scene img').all()) {
          await image.scrollIntoViewIfNeeded(); await image.evaluate(i => i.decode());
        }
      }
      assert.deepEqual(await page.evaluate(() => [...document.images].filter(i => i.complete && !i.naturalWidth).map(i => i.src)), []);
      await page.evaluate(() => scrollTo({ top: 0, behavior: 'instant' }));
      await sleep(4000);
      const hero = await page.evaluate(() => {
        const r = document.querySelector('.hero-copy').getBoundingClientRect();
        return { margins: [r.left, innerWidth-r.right], overlap: document.querySelector('.hero-sub').getBoundingClientRect().bottom > document.querySelector('.scroll-cue').getBoundingClientRect().top };
      });
      assert(Math.abs(hero.margins[0] - hero.margins[1]) < 1);
      assert.equal(hero.overlap, false);
      await page.screenshot({ path: `/tmp/arcturus3-${name}-hero.png` });
      if (name === 'phone') {
        await page.locator('#s3-aware').scrollIntoViewIfNeeded(); await sleep(350);
        await page.screenshot({ path: '/tmp/arcturus3-phone-story.png' });
      }
      if (name === 'laptop') {
        await page.evaluate(() => {
          const t = document.querySelector('.turning-point');
          scrollTo({top:scrollY+t.getBoundingClientRect().top+80,behavior:'instant'});
        });
        await sleep(100);
        const turnBefore = await page.locator('.turn-stage').boundingBox();
        await page.evaluate(() => scrollBy({top:250,behavior:'instant'})); await sleep(100);
        const turnAfter = await page.locator('.turn-stage').boundingBox();
        assert.equal(turnBefore.y,turnAfter.y,'transition must dwell');
        await page.screenshot({path:'/tmp/arcturus4-transition.png'});
        await page.evaluate(() => {
          const proof = document.getElementById('proof');
          const overflow = Math.max(0, proof.querySelector('.proof-stage').scrollHeight-innerHeight);
          scrollTo({top:scrollY+proof.getBoundingClientRect().top+overflow+80,behavior:'instant'});
        });
        await sleep(100);
        const proofBefore = await page.locator('.proof-stage').boundingBox();
        await page.evaluate(() => scrollBy({top:250,behavior:'instant'})); await sleep(100);
        const proofAfter = await page.locator('.proof-stage').boundingBox();
        assert.equal(proofBefore.y,proofAfter.y,'proof introduction must dwell');
        assert(proofAfter.height >= 720);
        assert.equal(await page.locator('.proof-stage .book').count(), 2);
        assert.equal(await page.locator('.proof-stage .testimonials figure').count(), 4);
        const proofContent = await page.locator('.proof-content').boundingBox();
        assert(proofContent.y >= proofAfter.y && proofContent.y+proofContent.height <= proofAfter.y+proofAfter.height, 'proof content must stay inside its natural-height stage');
        assert.equal(await page.locator('.testimonials blockquote').first().evaluate(e=>getComputedStyle(e).fontSize), '15.2px');
        assert.match(await page.locator('.testimonials').innerText(), /Arin Sime/);
        await page.screenshot({path:'/tmp/arcturus4-proof-dwell.png'});
        await page.locator('#email').focus();
        assert.equal(await page.locator('.email-row').evaluate(e=>getComputedStyle(e).borderRadius), '8px');
        assert.equal(await page.locator('.email-row').evaluate(e=>getComputedStyle(e).outlineStyle), 'solid');
        assert.equal(await page.locator('#email').evaluate(e=>getComputedStyle(e).outlineStyle), 'none');
        const footerFonts = await page.locator('footer').evaluate(e=>[e.querySelector('.footer-brand'),e.querySelector('nav a')].map(a=>{const s=getComputedStyle(a);return [s.fontFamily,s.fontSize,s.fontWeight,s.color]}));
        assert.deepEqual(footerFonts[0],footerFonts[1]);
        await page.locator('#contact').scrollIntoViewIfNeeded(); await sleep(350);
        await page.screenshot({ path: '/tmp/arcturus3-contact.png' });
        await page.locator('#proof').scrollIntoViewIfNeeded(); await sleep(350);
        await page.screenshot({ path: '/tmp/arcturus3-proof.png' });
        await page.locator('.solution a[href="#s3"]').click(); await sleep(1200);
        assert.equal(await page.locator('#solution .moment-group.active').getAttribute('id'), 's3');
        // Cue fades, doesn't abruptly disappear, and comes back at the top.
        for (const [y, low, high] of [[0,.99,1],[60,.1,.99],[240,0,0],[0,.99,1]]) {
          await page.evaluate(y => scrollTo({ top: y, behavior: 'instant' }), y); await sleep(80);
          const opacity = Number(await page.locator('.scroll-cue-fade').evaluate(e => getComputedStyle(e).opacity));
          assert(opacity >= low && opacity <= high);
        }
      }
      assert.deepEqual(errors, []);
      results.push({ name, pinned, moments: 8, fixedMedia: true, overflow: false, errors });
      await page.close();
    }

    // Use the existing worker's allowed localhost:8000 origin, but serve ONLY
    // our draft path through Playwright. This does not change the running blog.
    for (const scenario of ['pending','subscribed','server-error','http-error','bad-json','unknown','network-error']) {
      const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
      await page.route('http://localhost:8000/**', async route => {
        const url = new URL(route.request().url());
        const relative = url.pathname.split('/')[1];
        const mime = relative.endsWith('.js') ? 'application/javascript' : relative.endsWith('.css') ? 'text/css' : relative.endsWith('.webp') ? 'image/webp' : relative.endsWith('.jpg') ? 'image/jpeg' : relative.endsWith('.png') ? 'image/png' : relative.endsWith('.ico') ? 'image/x-icon' : 'text/html';
        await route.fulfill({ body: await fs.readFile(path.join(root, relative)), contentType: mime });
      });
      let calls = 0;
      await page.route(worker, async route => {
        calls++;
        assert.deepEqual(route.request().postDataJSON(), { email: 'test@example.com' });
        await sleep(100);
        if (scenario === 'network-error') return route.abort('failed');
        const data = scenario === 'pending' ? {subscribed:false,pending:true,error:null} : scenario === 'subscribed' ? {subscribed:true,error:null} : scenario === 'server-error' ? {error:'not available'} : {};
        await route.fulfill({ status: scenario === 'http-error' ? 500 : 200, contentType: 'application/json', body: scenario === 'bad-json' ? 'invalid' : JSON.stringify(data) });
      });
      await page.goto('http://localhost:8000/agentic-web.html');
      await page.locator('#email').fill('bad-address');
      await page.locator('#subscribe-form button').click(); assert.equal(calls,0);
      await page.locator('#email').fill('test@example.com');
      await page.locator('#subscribe-form button').click();
      await page.waitForFunction(() => !document.querySelector('#subscribe-form button').disabled);
      const status = await page.locator('#subscription-status').innerText();
      assert.equal(calls,1);
      if (scenario === 'pending') assert.match(status,/Check your inbox to confirm/);
      else if (scenario === 'subscribed') assert.match(status,/already on the list/);
      else assert.match(status,/couldn’t confirm/);
      assert.equal(await page.locator('#email').evaluate(i=>i.readOnly),false);
      results.push({ form: scenario, calls, status });
      await page.close();
    }
    // No-JS native POST destination, public form ID and field name are real.
    const nojs = await browser.newPage({ javaScriptEnabled: false });
    await nojs.goto(base);
    assert.equal(await nojs.locator('#subscribe-form').getAttribute('action'),'https://app.convertkit.com/forms/7337584/subscriptions');
    assert.equal(await nojs.locator('#email').getAttribute('name'),'email_address');
    assert.equal(await nojs.locator('#subscribe-form button').isEnabled(),true);
    await nojs.close();
    console.log(JSON.stringify(results,null,2));
  } finally { await browser.close(); }
})().catch(error=>{ console.error(error); process.exitCode=1; });

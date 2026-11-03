/* npm install --no-save playwright (or set NODE_PATH to an existing installation).
   With `mkdocs serve` on port 8000:
       node scripts/test_home_browser.cjs
   All signup POSTs are intercepted; this never creates a subscriber. */
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const base = process.env.HOME_TEST_URL || 'http://127.0.0.1:8000';
const worker = 'https://kit.arcturus-labs.com/verify_subscription';
(async () => {
  const browser = await chromium.launch();
  try {
    const context = await browser.newContext();
    // Do not inflate production analytics during tests.
    await context.route(/google-analytics\.com|googletagmanager\.com/, r => r.abort());
    let reply = { subscribed: false, pending: true }, status = 200, calls = 0;
    await context.route(worker, async route => {
      calls++;
      const req = route.request();
      assert.equal(req.method(), 'POST');
      assert.deepEqual(req.postDataJSON(), {email:'home-port@example.com'});
      await route.fulfill({status, contentType:'application/json', body:JSON.stringify(reply)});
    });
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    for (const slug of ['index','agentic-web','workflows','software-factories']) {
      await page.goto(`${base}/${slug}.html`);
      const form = page.locator('#subscribe-form');
      await page.locator('#email').fill('home-port@example.com');
      for (const test of [
        [{subscribed:false,pending:true},200,/Check your inbox to confirm/],
        [{subscribed:true},200,/already on the list/],
        [{error:'unavailable'},503,/couldn’t confirm/],
        [{unexpected:true},200,/couldn’t confirm/]
      ]) {
        [reply,status] = test;
        const before = calls;
        // Trigger through the actual form's submit event, even if offscreen.
        await form.evaluate(f => f.requestSubmit());
        await page.waitForFunction(() => !document.querySelector('#subscribe-form').hasAttribute('aria-busy'));
        assert.equal(calls,before+1);
        assert.match(await page.locator('#subscription-status').innerText(),test[2]);
        assert.equal(await form.locator('button').isEnabled(),true);
        assert.equal(await page.locator('#email').getAttribute('readonly'),null);
      }
      assert.equal(await page.locator('header nav a').first().getAttribute('href'),'/blog/');
      if (slug !== 'index') {
        await page.locator('header .brand').click();
        await page.waitForURL(`${base}/index.html`);
      }
      console.log(`${slug}: signup pending/existing/error/malformed + navigation passed`);
    }
    await page.goto(base+'/');
    const urls = await page.locator('.posts a').evaluateAll(as => as.map(a=>a.getAttribute('href')));
    assert.equal(urls.length,5);
    const dates = await page.locator('.posts time').evaluateAll(ts=>ts.map(t=>t.dateTime));
    assert.deepEqual(dates,[...dates].sort().reverse());
    for (const u of urls) {
      const response = await page.goto(base+u);
      assert.equal(response.status(),200);
      assert.ok((await page.locator('h1').innerText()).trim());
    }
    await page.goto(base+'/');
    await page.locator('header nav a').first().click();
    await page.waitForURL(base+'/blog/');
    // Material's Home nav must return to the replacement homepage.
    const home = page.locator('a.md-nav__link').filter({hasText:/^\s*Home\s*$/}).first();
    await home.click();
    assert.ok(['/','/index.html'].includes(new URL(page.url()).pathname));
    assert.equal(await page.locator('.posts li').count(),5);
    assert.deepEqual(errors,[]);
    const nojs = await browser.newContext({javaScriptEnabled:false});
    for(const slug of ['index','agentic-web','workflows','software-factories']) {
      const pg = await nojs.newPage();
      await pg.goto(`${base}/${slug}.html`);
      const f = pg.locator('#subscribe-form');
      assert.equal(await f.getAttribute('action'),'https://app.convertkit.com/forms/7337584/subscriptions');
      assert.equal(await f.getAttribute('method'),'post');
      assert.equal(await f.locator('input[type=email]').getAttribute('name'),'email_address');
      await pg.close();
    }
    console.log('five recent posts, blog round-trip, JS errors and no-JS fallback: passed');
  } finally { await browser.close(); }
})().catch(e=>{console.error(e);process.exitCode=1;});

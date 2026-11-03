/* Same public Kit form and credential-protected worker as the live blog.
   Native form submission remains the fallback (including file:// and no JS).
   Never store subscriber state or claim confirmation from an unverified submit. */
(() => {
  'use strict';
  const form = document.getElementById('subscribe-form');
  const input = document.getElementById('email');
  const button = form.querySelector('button');
  const status = document.getElementById('subscription-status');
  const worker = 'https://kit.arcturus-labs.com/verify_subscription';
  // The existing worker explicitly permits these origins. Do not send a POST
  // from an unapproved origin: the signup could succeed while CORS hides it.
  const inlineOrigins = new Set(['https://arcturus-labs.com', 'http://localhost:8000', 'http://127.0.0.1:8000']);
  if (!inlineOrigins.has(location.origin)) return;
  let submitting = false;
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (submitting || !form.reportValidity()) return;
    const email = input.value.trim();
    if (!email) return;
    submitting = true;
    button.disabled = true;
    input.readOnly = true;
    form.setAttribute('aria-busy', 'true');
    status.removeAttribute('data-error');
    status.textContent = 'Subscribing…';
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 15000);
    try {
      const response = await fetch(worker, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }), signal: controller.signal,
        credentials: 'omit', referrerPolicy: 'no-referrer'
      });
      const result = await response.json();
      if (!response.ok || result.error) throw new Error('server');
      if (result.subscribed === true) {
        status.textContent = 'This email is already on the list. If you haven’t confirmed yet, check your inbox.';
      } else if (result.pending === true) {
        status.textContent = 'Check your inbox to confirm your subscription.';
      } else throw new Error('unrecognized');
    } catch (error) {
      status.setAttribute('data-error', '');
      status.textContent = error.name === 'AbortError'
        ? 'We couldn’t confirm the request in time. Check your inbox before trying again.'
        : 'We couldn’t confirm your subscription. Check your inbox or try again in a moment.';
    } finally {
      clearTimeout(timer);
      submitting = false;
      input.readOnly = false;
      button.disabled = false;
      form.removeAttribute('aria-busy');
    }
  });
})();

// ── Header title → home ──────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
    const headerTitle = document.querySelector('.md-header__title');
    if (headerTitle) {
        headerTitle.addEventListener('click', function() {
            window.location.href = '/';
        });
    }
});

// ── Subscription gate ─────────────────────────────────────────────────────────
// Links tagged with the `data-gated` attribute show a subscribe modal for
// unauthorized visitors. Verifies against the Cloudflare Worker, which checks
// ConvertKit subscriber status. Uses the same cookie names as
// stateful-objects-of-discourse so users who verified there skip the modal.
(function() {
    var COOKIE_AUTH   = 'subscription_authorized';
    var COOKIE_EMAIL  = 'subscription_email';
    var WORKER_URL    = 'https://kit.arcturus-labs.com/verify_subscription';

    function getCookie(name) {
        var m = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return m ? m.pop() : '';
    }

    function setCookie(name, value) {
        var d = new Date();
        d.setFullYear(d.getFullYear() + 1);
        document.cookie = name + '=' + encodeURIComponent(value)
            + ';expires=' + d.toUTCString()
            + ';path=/;SameSite=Strict';
    }

    function isAuthorized() {
        if (window.location.href.includes('bypass-subscription')) return true;
        return getCookie(COOKIE_AUTH) === 'true';
    }

    function removeModal() {
        var el = document.getElementById('sub-gate-overlay');
        if (el) el.remove();
    }

    function showModal(targetUrl) {
        var savedEmail = decodeURIComponent(getCookie(COOKIE_EMAIL) || '');
        var overlay = document.createElement('div');
        overlay.id = 'sub-gate-overlay';
        overlay.innerHTML =
            '<div id="sub-gate-modal">' +
            '  <h2>Get Access</h2>' +
            '  <p>Enter your email to access the repo. If you\'re already subscribed to the Arcturus Labs newsletter you\'ll go straight through. If not, you\'ll get a quick confirmation email first.</p>' +
            '  <form id="sub-gate-form">' +
            '    <input type="email" id="sub-gate-email" placeholder="your@email.com" required value="' + savedEmail + '" />' +
            '    <button type="submit" id="sub-gate-btn">Get Access</button>' +
            '    <p id="sub-gate-msg"></p>' +
            '  </form>' +
            '</div>';
        document.body.appendChild(overlay);

        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) removeModal();
        });

        document.getElementById('sub-gate-form').addEventListener('submit', function(e) {
            e.preventDefault();
            var email = document.getElementById('sub-gate-email').value.trim();
            var btn   = document.getElementById('sub-gate-btn');
            var msg   = document.getElementById('sub-gate-msg');
            btn.disabled    = true;
            btn.textContent = 'Checking…';
            msg.textContent = '';

            setCookie(COOKIE_EMAIL, email);

            fetch(WORKER_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: email }),
            })
            .then(function(r) { return r.json(); })
            .then(function(data) {
                if (data.subscribed) {
                    setCookie(COOKIE_AUTH, 'true');
                    removeModal();
                    window.open(targetUrl, '_blank');
                } else if (data.pending) {
                    msg.textContent = data.message;
                    btn.disabled    = false;
                    btn.textContent = 'Get Access';
                } else {
                    msg.textContent = data.error || 'Something went wrong. Please try again.';
                    btn.disabled    = false;
                    btn.textContent = 'Get Access';
                }
            })
            .catch(function() {
                msg.textContent = 'Network error. Please try again.';
                btn.disabled    = false;
                btn.textContent = 'Get Access';
            });
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('a[data-gated]').forEach(function(link) {
            link.addEventListener('click', function(e) {
                if (isAuthorized()) return;
                e.preventDefault();
                showModal(link.href);
            });
        });
    });
})();
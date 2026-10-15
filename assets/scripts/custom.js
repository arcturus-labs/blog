// ── Slide-in subscription bar (blog posts) ───────────────────────────────────
// Shows after 60s on page, 50% scroll depth, or exit intent — whichever first.
// Dismissed for 30 days once closed or submitted.
(function() {
    var COOKIE_BAR  = 'sub_bar_dismissed';
    var MIN_TIME    = 60000;   // 60 seconds
    var MIN_SCROLL  = 0.50;    // 50% for blog posts
    var MIN_SCROLL_INDEX = 0.25; // 25% for blog index (past first few posts)
    var SHOWN        = false;

    function getCookie(name) {
        var m = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return m ? m.pop() : '';
    }

    function setCookie(name, value, days) {
        var d = new Date();
        d.setDate(d.getDate() + (days || 30));
        document.cookie = name + '=' + encodeURIComponent(value)
            + ';expires=' + d.toUTCString()
            + ';path=/;SameSite=Strict';
    }

    function isBlogPage() {
        // Blog post pages have .md-content--post; blog index uses the blog template
        return document.querySelector('.md-content--post') !== null
            || window.location.pathname.startsWith('/blog');
    }

    function isAlreadySubscribed() {
        return getCookie('ck_subscribed') === 'yes';
    }

    function isDismissed() {
        return getCookie(COOKIE_BAR) === 'true';
    }

    function showBar() {
        if (SHOWN) return;
        SHOWN = true;

        var bar = document.createElement('div');
        bar.id = 'sub-slide-bar';
        bar.innerHTML =
            '<button class="sub-slide-bar__close" aria-label="Close">&times;</button>' +
            '<div class="sub-slide-bar__inner">' +
            '  <img class="sub-slide-bar__avatar" src="/assets/images/john_berryman_face.jpg" alt="John Berryman">' +
            '  <span class="sub-slide-bar__text"><strong>Want to follow along?</strong> Get new posts in your inbox &ndash; practical guides on AI software and agentic application design. No spam, ever.</span>' +
            '  <form class="sub-slide-bar__form" action="https://app.convertkit.com/forms/7337584/subscriptions" method="post" target="_blank">' +
            '    <input type="email" name="email_address" placeholder="you@example.com" required>' +
            '    <button type="submit">Subscribe</button>' +
            '  </form>' +
            '</div>';
        document.body.appendChild(bar);

        // Animate in
        requestAnimationFrame(function() {
            bar.classList.add('sub-slide-bar--visible');
        });

        // Close button
        bar.querySelector('.sub-slide-bar__close').addEventListener('click', function() {
            dismiss();
        });

        // Dismiss on form submit + mark as subscriber
        bar.querySelector('form').addEventListener('submit', function() {
            setCookie(COOKIE_BAR, 'true', 30);
            setCookie('subscription_authorized', 'true', 365);
        });
    }

    function dismiss() {
        setCookie(COOKIE_BAR, 'true', 30);
        var bar = document.getElementById('sub-slide-bar');
        if (bar) {
            bar.classList.remove('sub-slide-bar--visible');
            setTimeout(function() { if (bar.parentNode) bar.parentNode.removeChild(bar); }, 400);
        }
    }

    function setupTriggers() {
        if (!isBlogPage() || isDismissed() || isAlreadySubscribed()) return;

        // 1. Time on page
        setTimeout(function() {
            if (!SHOWN && document.visibilityState === 'visible') showBar();
        }, MIN_TIME);

        // 2. Scroll depth — percent through the scrollable distance
        var scrollFired = false;
        function scrollPercent() {
            var h = document.documentElement;
            var track = h.scrollHeight - h.clientHeight;
            if (track <= 0) return 0;
            return h.scrollTop / track;
        }
        var isIndex = !document.querySelector('.md-content--post');
        var threshold = isIndex ? MIN_SCROLL_INDEX : MIN_SCROLL;
        window.addEventListener('scroll', function() {
            if (scrollFired || SHOWN) return;
            if (scrollPercent() >= threshold) {
                scrollFired = true;
                showBar();
            }
        }, { passive: true });

        // 3. Exit intent (cursor leaves top of viewport)
        document.addEventListener('mouseout', function(e) {
            if (SHOWN) return;
            if (e.clientY <= 0 && e.relatedTarget === null) {
                showBar();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupTriggers);
    } else {
        setupTriggers();
    }
})();

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
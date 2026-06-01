const CONVERTKIT_API = "https://api.convertkit.com/v3";
const FORM_ID = "7337584";

function corsHeaders(origin, env) {
  const allowed = env.ALLOWED_ORIGIN || "https://arcturus-labs.com";
  const allowedOrigins = [allowed, "http://localhost:8000", "http://127.0.0.1:8000"];
  const useOrigin = allowedOrigins.includes(origin) ? origin : allowed;
  return {
    "Access-Control-Allow-Origin": useOrigin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };
}

// Mirrors stateful-objects-of-discourse/backend/app/routes/subscription/routes.py
async function handleVerify(request, env) {
  const { email } = await request.json();
  if (!email) {
    return Response.json({ subscribed: false, error: "Email is required." }, { status: 400 });
  }

  const trimmedEmail = email.trim();

  try {
    const checkUrl = new URL(`${CONVERTKIT_API}/subscribers`);
    checkUrl.searchParams.set("api_secret", env.CONVERTKIT_API_SECRET);
    checkUrl.searchParams.set("email_address", trimmedEmail);

    const checkRes = await fetch(checkUrl);
    if (!checkRes.ok) {
      const errBody = await checkRes.json().catch(() => ({}));
      console.error("ConvertKit subscriber check failed", checkRes.status, errBody);
      return Response.json({ subscribed: false, error: "Verification service unavailable. Please try again later." });
    }

    const subscriberData = await checkRes.json();
    if (subscriberData.total_subscribers && subscriberData.total_subscribers > 0) {
      return Response.json({ subscribed: true, error: null });
    }
  } catch (err) {
    console.error("ConvertKit subscriber check exception", err);
    return Response.json({ subscribed: false, error: "Verification error." });
  }

  try {
    const subRes = await fetch(`${CONVERTKIT_API}/forms/${FORM_ID}/subscribe`, {
      method: "POST",
      headers: { "Content-Type": "application/json; charset=utf-8" },
      body: JSON.stringify({
        api_key: env.CONVERTKIT_API_KEY,
        email: trimmedEmail,
      }),
    });

    if (!subRes.ok) {
      const errBody = await subRes.json().catch(() => ({}));
      console.error("ConvertKit subscribe failed", subRes.status, errBody);
      return Response.json({ subscribed: false, error: "Subscription failed. Please try again." });
    }
  } catch (err) {
    console.error("ConvertKit subscribe exception", err);
    return Response.json({ subscribed: false, error: "Subscription error." });
  }

  // New signup – same as Flask (not yet confirmed). Blog JS treats null error as pending UX.
  return Response.json({
    subscribed: false,
    error: null,
    pending: true,
    message: "Almost there! Check your email to confirm your subscription, then come back and enter your email again to access the repo.",
  });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const headers = corsHeaders(origin, env);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers });
    }

    const url = new URL(request.url);

    if (request.method === "POST" && url.pathname === "/verify_subscription") {
      try {
        const res = await handleVerify(request, env);
        Object.entries(headers).forEach(([k, v]) => res.headers.set(k, v));
        return res;
      } catch (err) {
        console.error("verify_subscription error", err);
        return Response.json({ subscribed: false, error: "Server error." }, { status: 500, headers });
      }
    }

    return new Response("Not found", { status: 404, headers });
  },
};

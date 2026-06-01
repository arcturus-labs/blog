const CONVERTKIT_API = "https://api.convertkit.com/v3";

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

async function handleVerify(request, env) {
  const { email } = await request.json();
  if (!email) {
    return Response.json({ subscribed: false, error: "Email is required." }, { status: 400 });
  }

  // Check if already a subscriber.
  const checkUrl = `${CONVERTKIT_API}/subscribers?api_secret=${env.CONVERTKIT_API_SECRET}&email_address=${encodeURIComponent(email)}`;
  const checkRes = await fetch(checkUrl);
  const checkData = await checkRes.json();

  if (checkData.total_subscribers > 0) {
    return Response.json({ subscribed: true, error: null });
  }

  // Not subscribed – add them to the newsletter form.
  const subRes = await fetch(`${CONVERTKIT_API}/forms/${env.CONVERTKIT_FORM_ID}/subscribe`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ api_key: env.CONVERTKIT_API_KEY, email }),
  });

  if (!subRes.ok) {
    return Response.json({ subscribed: false, error: "Subscription failed. Please try again." });
  }

  // Subscribed but not yet confirmed – tell them to check email.
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
        return Response.json({ subscribed: false, error: "Server error." }, { status: 500, headers });
      }
    }

    return new Response("Not found", { status: 404, headers });
  },
};

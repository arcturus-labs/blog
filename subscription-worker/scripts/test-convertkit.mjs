#!/usr/bin/env node
/**
 * Quick sanity check for Kit/ConvertKit credentials in .dev.vars.
 * Usage: node scripts/test-convertkit.mjs your@email.com
 */
import { readFileSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const email = process.argv[2];
if (!email) {
  console.error("Usage: node scripts/test-convertkit.mjs your@email.com");
  process.exit(1);
}

const varsPath = resolve(__dirname, "../.dev.vars");
const vars = Object.fromEntries(
  readFileSync(varsPath, "utf8")
    .split("\n")
    .filter((line) => line && !line.startsWith("#"))
    .map((line) => line.split("=", 2))
    .map(([k, v]) => [k.trim(), v.trim()])
);

const { CONVERTKIT_API_SECRET, CONVERTKIT_API_KEY } = vars;
const FORM_ID = "7337584";

if (!CONVERTKIT_API_SECRET || !CONVERTKIT_API_KEY || CONVERTKIT_API_SECRET.includes("your_")) {
  console.error("Fill in real values in subscription-worker/.dev.vars first.");
  process.exit(1);
}

const checkUrl = `https://api.convertkit.com/v3/subscribers?api_secret=${encodeURIComponent(CONVERTKIT_API_SECRET)}&email_address=${encodeURIComponent(email)}`;
const checkRes = await fetch(checkUrl);
const checkData = await checkRes.json();
console.log("Subscriber check:", checkRes.status, checkData);

const subRes = await fetch(`https://api.convertkit.com/v3/forms/${FORM_ID}/subscribe`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ api_key: CONVERTKIT_API_KEY, email }),
});
const subData = await subRes.json().catch(() => ({}));
console.log("Form subscribe:", subRes.status, subData);

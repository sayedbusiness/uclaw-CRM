# make.com automations — United Citizen Law

This folder holds the ready‑to‑import make.com **blueprint** for the CRM's non‑contact automations. The contact/call automations run inside the CRM itself; these are the "everything else" layer.

## What's already live in your make.com account
- A scenario named **"UCL CRM events"** (webhook, **turned ON**) — verified receiving CRM data.
- Its webhook URL: `https://hook.us2.make.com/j871u4ln9sovb9ul79d9loyt0vcm48dk`
  → paste this into the CRM at **Settings → make.com webhook URL**.

## The blueprint — `ucl-crm-events.blueprint.json`
One webhook → **Router** → **7 Slack alert branches** (each an HTTP module, so **no OAuth** — just your Slack webhook URL):

| Branch | Fires when | Message |
|---|---|---|
| New lead | `trigger = lead_created` | 🔥 New lead — name · case · phone · language |
| HOT lead → page Sam | new lead **and** case is truck / catastrophic / wrongful‑death | 🚨 HOT LEAD — page Sam |
| Case signed | `trigger = stage_changed` **and** stage = Signed | ✅ CASE SIGNED + fire medical‑records request |
| New review | `trigger = review_received` | ⭐ New review — respond within the hour |
| Nightly EOD | `trigger = eod_midnight` | 📊 Nightly EOD |
| SOL deadline | `trigger = sol_alert` | ⏰ Statute‑of‑limitations deadline approaching |
| Stale lead sweep | `trigger = stale_lead` | 🕓 Stale lead (3+ days, no contact) |

## How to install (about 60 seconds)
1. **Get a Slack Incoming Webhook URL:** Slack → Apps → add **Incoming Webhooks** → Add to Slack → pick a channel → copy the URL.
2. **Bake it in:** open `ucl-crm-events.blueprint.json`, find/replace `REPLACE_WITH_YOUR_SLACK_WEBHOOK_URL` with your Slack URL (all 7 spots). *(Or send me the URL and I'll do this for you.)*
3. **Import:** in make.com open the **UCL CRM events** scenario → **⋯ → Import blueprint → Choose JSON blueprint** → select this file → **Import**. It reuses the existing webhook, so the URL above stays the same.
4. **Turn it on** and you're live. The router sends each CRM event to the right Slack alert.

## Optional: the 2 Google‑Sheets automations
Lead‑logging and signed‑status‑update to a spreadsheet need a **Google connection** (one "Authorize" click in make.com). Add those two `Google Sheets → Add/Update a row` modules after connecting Google — I can build them live once the connection exists.

## Notes
- Free plan = **2 active scenarios, 1,000 ops/month** — this all fits in the one webhook scenario.
- The `review_received`, `eod_midnight`, `sol_alert`, and `stale_lead` branches are built and waiting; they light up as the CRM pushes those events (EOD already has a nightly trigger in the CRM).

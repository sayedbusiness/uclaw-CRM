# make.com automations — United Citizen Law

Ready‑to‑import make.com **blueprint** for the CRM's non‑contact automations. The contact/call automations run inside the CRM itself; these are the "everything else" layer.

## Already live in your make.com account
- Scenario **"UCL CRM events"** (webhook, **ON**) — verified receiving CRM data.
- Webhook URL: `https://hook.us2.make.com/j871u4ln9sovb9ul79d9loyt0vcm48dk`
  → paste into the CRM at **Settings → make.com webhook URL**.

## The blueprint — 9 automations, one webhook → Router

`ucl-crm-events.blueprint.json` (placeholder Slack URL — safe/committed) and
`ucl-crm-events.LIVE.blueprint.json` (your real Slack URL baked in — **git‑ignored, never committed**).

**7 Slack branches** (HTTP → Slack, no OAuth):

| Branch | Fires when |
|---|---|
| 🔥 New lead | `lead_created` |
| 🚨 HOT lead → page Sam | new lead + truck / catastrophic / wrongful‑death |
| ✅ Case signed | stage → Signed |
| ⭐ New review | `review_received` |
| 📊 Nightly EOD | `eod_midnight` |
| ⏰ SOL deadline | `sol_alert` |
| 🕓 Stale lead sweep | `stale_lead` |

**2 Google‑Sheets branches** (append a row to your lead tracker — needs a Google connection):

| Branch | Fires when | Writes |
|---|---|---|
| Lead → Sheet log | `lead_created` | a "New lead" row |
| Signed → Sheet log | stage → Signed | a "Signed" row |

### Google Sheet template (create this once)
New Google Sheet → rename the tab to **`Leads`** → put these headers in **row 1** (columns A–H):

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Timestamp | Event | Name | Case | Phone | Language | Stage | Workflow |

## Install (about 60 seconds)
1. **Slack** is already baked into the LIVE file — nothing to do there.
2. **Google:** in make.com → **Credentials → Add connection → Google Sheets → Authorize** (one click, only you can do this).
3. **Create the Sheet** above; copy its ID from the URL (`/d/<THIS_PART>/edit`).
4. **Import:** open the **UCL CRM events** scenario → **⋯ → Import blueprint → Choose JSON blueprint** → select `ucl-crm-events.LIVE.blueprint.json` → **Import**. Reuses the existing webhook, so the URL stays the same.
5. In the **two Google‑Sheets modules**, pick your Google connection + the `Leads` sheet (the column mapping is already set). The 7 Slack modules need nothing.
6. Turn the scenario **On**.

## Notes
- Free plan = **2 active scenarios, 1,000 ops/month** — everything fits in this one webhook scenario.
- A Slack Incoming Webhook URL is a **secret** — that's why the LIVE file is git‑ignored. Don't paste it into public places.
- `review_received`, `eod_midnight`, `sol_alert`, `stale_lead` branches are built and light up as the CRM pushes those events.

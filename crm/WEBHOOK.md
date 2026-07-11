# Connecting UCL Case Desk to everything else

Case Desk is local-first: data lives in the browser, costs $0/month, and exports anywhere. Three connection levels, from zero-setup to fully wired:

## Level 1 — Today, no servers (works immediately)
- **Website form → team:** the site posts to Formspree (free tier) → the team gets an email → open Case Desk → **+ New Lead → "Paste from email"** auto-fills the fields. 10 seconds per lead.
- **From any old tool:** export CSV → **Import / Export** tab → match columns once → done.
- **Backups:** Export "Full backup (JSON)" every Friday (task the team; or automation #30's dashboard reminds them).

## Level 2 — Outbound webhook (n8n picks everything up)
In **Settings → Webhook URL**, paste an n8n Webhook node URL. Case Desk then POSTs JSON on:
- `lead.created` — fires automations #1 (team alarm), #2 (instant reply), #5 (SOL gate)
- `lead.stage_changed` — fires #7 (Signed → retainer), #9 (Resolved → review ask), #10 (status updates)

Payload shape (already matches the website form):
```json
{
  "event": "lead.created",
  "at": "2026-07-10T21:00:00Z",
  "lead": { "id":"…", "name":"…", "phone":"9165551234", "case_type":"Car accident",
            "language":"Español", "source":"Website form", "stage":"New",
            "hot": false, "accident_date":"2026-07-01", "sol_date":"2028-07-01" }
}
```
Failed sends queue in an outbox (Settings shows the count) and retry on demand — no lead event is ever silently lost.
Note: webhooks are blocked inside the claude.ai preview sandbox; host the file anywhere (Level 3) and they fire normally.

## Level 3 — Hosted (~$0–6/month, 10 minutes)
Drop `crm/index.html` on Vercel/Netlify (free) or the same $6 VPS running n8n. Then:
1. The team opens it at `crm.uclaw.net` on any device (add a PIN gate or Cloudflare Access — free — before real client data goes in).
2. Point the website form's `FORM_ENDPOINT` at an n8n Webhook that (a) texts the team (#1) and (b) appends the lead to a shared store the CRM reads. For multi-device sync, the natural upgrade is the same file backed by Supabase (free tier) — the data model is already flat JSON; ~an afternoon of work when the firm outgrows single-device.

**Privacy note:** before real client names go in, host it (Level 3) with access control, and keep weekly JSON backups. localStorage is per-browser and unencrypted — fine for evaluation, not for production client data on a shared computer.

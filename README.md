# United Citizen Law — Growth Engine

Complete growth package for **United Citizen Law** (uclaw.net), a Sacramento personal-injury firm — built by **Apex Growth Corp**. Rebuilt multilingual website, a GoHighLevel-class CRM, and a 32-automation system.

---

## What's in here

| Folder / file | What it is |
|---|---|
| **`crm/index.html`** | **UCL Command Center** — the CRM. Single self-contained file, `$0` license. Open it in any browser. |
| **`site/`** | The rebuilt website: `index.html` (homepage) + 8 practice-area pages + `team.html`, plus `_generate.py` (regenerates the practice/team pages) and `team/` photos. |
| **`AUTOMATIONS.md`** | The 32 automations, each in plain English + a one-page summary, with build specs. |
| **`GROWTH-PLAN.md`** | The whole strategy written so an 8th-grader can follow it (glossary included). |
| **`AUDIT.md`** | The original SEO/conversion teardown (score 42/100, the six critical defects). |
| **`report.html`** | Shareable one-page growth blueprint. |
| **`crm/WEBHOOK.md`** | How to connect the CRM to your real phone/SMS/automation tools. |

---

## The CRM — UCL Command Center

Open `crm/index.html` in a browser. **Demo login:** `demo@uclaw.net` / `demo1234` (or create a real firm account — email + salted-SHA-256 password, data saved privately per account in that browser).

**Features**
- **Dashboard** — live KPIs (speed-to-lead, connect rate, SOL alerts, review cadence).
- **Conversations** — threaded SMS / email / notes inbox, back-and-forth messaging.
- **Contacts pipeline** — kanban stages **plus** lead temperature (**Cold → Warm → Contacted → Closed**).
- **Dialer** — dial pad, quick-dial, disposition logging, **call recordings** (records from mic in-app for demo; paste a Twilio recording URL for live calls), and a **Simulate incoming call** button.
- **Incoming-call ring** — a full-screen ringing modal (with ringtone) that persists until you Accept/Decline; wire it to a live number via the inbound-poll URL in Settings.
- **Team** — see every teammate and how many calls they made (today / all-time / connected), leads assigned, and signed.
- **Automations** — trigger → action workflows that **run live** (SMS, tasks, tags, stage moves, timed waits). Each workflow is toggle **on/off** and runs either **in-CRM** (contact & call actions) or via **make.com** (everything else, with an in-CRM fallback if make.com is unreachable).
- **Nightly EOD → Slack** — at midnight, one message per teammate with their day's numbers (or hit "Send EOD to Slack now").
- **Reviews** (18-day-rule tracker) · **Settings** (make.com / Slack / n8n / Twilio webhooks, active agent, CSV import-export, JSON backup).

**Going live (Settings → Connections):**
- **SMS / calls:** n8n (or a relay) webhook, or Twilio SID/token/from-number.
- **Non-contact automations:** your make.com webhook URL.
- **Slack EOD:** your Slack incoming-webhook URL. *(For reliable midnight firing without a browser open, run the EOD as a scheduled make.com/n8n scenario — the in-CRM scheduler fires when the app is open.)*
- **Incoming-call ring:** an inbound-poll URL that your phone system posts to.

---

## The website

`site/` is a **multi-file static site** — deploy the whole folder together (Vercel, Netlify, or GitHub Pages) so the internal links between the homepage and the practice/team pages resolve.

- **Homepage** (`site/index.html`): founder-story hero, one-question-at-a-time case-review wizard, live 5-language switching (EN + ES complete; Dari/Urdu/Arabic conversion layer — have a native speaker review before production), clickable team bios with photos, and a contact footer.
- **Practice pages:** car, truck, motorcycle, rideshare, pedestrian, dog-bite, slip-and-fall, wrongful-death — each with LegalService + FAQ schema and a single H1.
- **Regenerate** the practice + team pages: `cd site && python3 _generate.py`.

**Before production:** set `FORM_ENDPOINT` (Formspree, or the CRM/n8n webhook) and `PREVIEW_MODE=false` in `site/index.html`; verify the Google review count and map pin before shipping the schema.

---

*Attorney advertising. Past results do not guarantee future outcomes. Dari/Urdu/Arabic copy is a conversion layer pending native review.*

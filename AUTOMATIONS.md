# United Citizen Law — The 32 Automations, Fully Explained
**July 10, 2026 · Apex Growth Corp**

*Each automation below tells you four things: **what it is** (plain English), **what happens** (the exact step-by-step), **why it matters** (time or money, with numbers where they exist), and **how it's built** (the real workflow spec — we build these in n8n, an automation tool that connects apps together like LEGO; each spec names the trigger and the flow so any builder can implement it).*

**The stack these run on (chosen for cost — full price table at the bottom):** **UCL Case Desk** (the custom CRM we built — $0 license, connects to anything via CSV + webhooks) as the system of record · **self-hosted n8n** on a ~$6/month server as the glue · **Twilio** pay-per-use for SMS/voice (~$0.008 per text) · DIY call tracking through Twilio numbers (CallRail optional later) · a budget AI API for drafting. ⚡ = week-one build.

**Routing rule (per Sayed, confirmed):** every alert, call, and follow-up goes to the **intake team** — Sam is paged ONLY for leads flagged **HOT** (commercial vehicle, catastrophic injury, fatality) and unhappy-client alarms (#32). Case Desk has this protocol built into its HOT flag and Settings.

**The one rule behind everything:** in personal injury, an unanswered lead calls the next firm within minutes. Under 5 minutes to respond = 80–90% chance you connect. Over 30 minutes = under 30%. Half this catalog exists to make "under 5 minutes, 24/7, in 5 languages" happen without any human remembering to do anything.

---

## 📋 SUMMARY — the whole system in one page (start here)

**In one sentence:** these 32 automations are a tireless digital staff member who answers every lead in under a minute (in 5 languages), keeps clients happy and reviewing, runs the marketing, and guards every legal deadline — so Sam's team spends their time on cases, not busywork.

**They come in four layers.** Each layer has one job:

| Layer | Its one job | # | The headline result |
|---|---|---|---|
| **A · Catch every lead** | Never let an injured person wait or slip away | 8 | Answer in <60 sec, 24/7, in their language → connect with ~80–90% of leads instead of ~30% |
| **B · Wow every client** | Turn signed clients into 5-star reviews & referrals | 6 | A fresh Google review roughly every 2 weeks; clients feel looked-after start to finish |
| **C · Market on autopilot** | Keep the firm #1 on Google & AI, hands-off | 10 | Higher map ranking, cheaper ad leads, content that writes & posts itself |
| **D · Protect the firm** | Chase records, watch deadlines, run the back office | 8 | No missed statute-of-limitations, faster settlements, a Monday-morning dashboard |

**What it can do — the 32 in plain English:**

*Layer A — Catch every lead (the money layer):*
1. **Instant Lead Alarm + Auto-Dial** — lights up the team's phones the second a lead comes in, and auto-dials the lead if no one grabs it in 3 minutes.
2. **Instant "Good Hands" Reply** — texts & emails the lead back within 60 seconds, in their language.
3. **Missed-Call Text-Back** — any missed office call gets an instant "sorry we missed you, tap to book" text.
4. **24/7 AI Intake** — a chat/after-hours voice agent that interviews leads, books consults, and wakes Sam only for emergencies.
5. **Qualification + Deadline Gate** — screens each lead and stamps the legal filing deadline automatically.
6. **No-Show Shield** — consultations confirm, remind, and rebook themselves.
7. **E-Sign Retainer Flow** — turns "yes, take my case" into a signed client in minutes.
8. **Language Router** — the traffic cop that makes every other automation speak EN/ES/Dari/Urdu/Arabic.

*Layer B — Wow every client (reviews & referrals):*
9. **Review Engine** — asks happy clients for a Google review on the perfect day; never lets 18 days pass without one.
10. **"Your Case Right Now" Updates** — proactive status texts so clients never wonder what's happening.
11. **Treatment Nudges** — reminds clients to keep medical appointments (which also protects the case value).
12. **Anniversary & Birthday Touches** — small human touches that keep the firm top-of-mind for referrals.
13. **Referral Thank-You Loop** — automatically thanks (and tracks) anyone who sends a friend.
14. **"How Did You Hear About Us?"** — captures the true lead source on every new client.

*Layer C — Market on autopilot:*
15. **NAP Watchdog** — watches that the firm's name/address/phone stay identical everywhere online.
16. **GBP Post Scheduler** — keeps the Google Business Profile freshly posted every week.
17. **Review-Response Drafter** — writes a tailored reply to every review for one-click approval.
18. **LSA Lead Responder & Dispute Bot** — answers Google Local Services leads fast and disputes bad-charge leads.
19. **Search-Terms Janitor** — trims wasted ad spend on junk search terms automatically.
20. **Creative Fatigue Monitor** — flags ads that are wearing out before they waste money.
21. **Rank + AI-Answer Tracker** — watches where the firm sits on Google and inside AI answers.
22. **Content Decay Radar** — spots pages slipping in rank so they get refreshed.
23. **Blog → Everywhere Repurposer** — turns one article into posts, emails, and clips across channels.
24. **Mention & "Best-Of" Hunter** — finds local "best injury lawyer" lists to get the firm added to.

*Layer D — Protect the firm (back office):*
25. **Medical-Records Chaser** — politely nags hospitals for records until they arrive.
26. **Statute-of-Limitations Sentinel** — the deadline guardian; escalates loudly as any filing date nears.
27. **Lien Tracker** — keeps every medical lien organized for settlement time.
28. **Settlement Disbursement Bot** — runs the payout checklist so clients get paid faster and correctly.
29. **Document Intake OCR** — reads uploaded photos/PDFs and files them into the right case.
30. **Monday Command Dashboard** — emails Sam one clear scoreboard of the whole firm every week.
31. **Intake-Call Quality Coach** — reviews intake calls and coaches the team to sign more cases.
32. **Client Happiness Pulse** — quietly watches for an unhappy client and alerts Sam *before* they leave a bad review.

**Where they run & what they cost:** all of this runs on the **UCL Command Center CRM** (the GoHighLevel-style system we built — $0 license) plus a ~$6/month automation engine (n8n) and pay-as-you-go texting (~$0.008/text). Realistic all-in cost: **≈$137/month**, ceiling **≈$246/month** — full breakdown at the bottom.

**Team-first, always:** every alert routes to the intake team first. Sam is paged **only** for HOT cases (commercial vehicle, catastrophic injury, fatality) and unhappy-client alarms (#32).

---

## GROUP A — Catching leads the moment they appear (the money layer)

### ⚡ 1. Instant Lead Alarm + Auto-Dial Bridge
**What it is:** the moment anyone submits the website form, LSA message, or chat, the intake team's phones light up — and if nobody reacts fast, the system literally dials the lead itself and bridges them to the on-call teammate. Sam is only pulled in when the lead is HOT.
**What happens:** ① Lead submits → ② within 60 seconds: SMS + push to the **intake team** with name, case type, language, phone (HOT flags — commercial vehicle, catastrophic injury, fatality — additionally page Sam) → ③ Case Desk automatically creates the lead record → ④ a 3-minute timer starts → ⑤ if no one has called yet, the system phones the intake line and the lead simultaneously and connects them ("bridge call").
**Why it matters:** this single workflow is the difference between an 80–90% connection rate and losing half of all paid leads. At Sacramento PI lead costs ($100–400 each), it pays for the entire automation program by itself.
**Build:** n8n Webhook trigger (form POST, `responseMode: onReceived`) → Set node (normalize fields: lowercase email, strip phone to digits) → CRM node (create lead) → Twilio SMS node (team alert) → Wait node (3 min) → IF node (CRM status still "new"?) → Twilio Voice call-bridge → Error Trigger workflow texts Sam if anything fails.

### ⚡ 2. Instant "You're in Good Hands" Reply
**What it is:** the lead themselves gets a human-sounding text and email within 60 seconds — in the language they chose on the form.
**What happens:** ① Same webhook as #1 → ② language field routes the message template (EN/ES/Dari/Ur/Ar) → ③ SMS: "Hi {name}, this is the team at United Citizen Law — we have your message about your {case type}. Expect our call within minutes. If you're at the ER, reply ER and we'll come to you." → ④ matching email with what-to-expect and "don't talk to insurance yet" tip.
**Why it matters:** an injured person who gets an instant, warm, in-their-language reply *stops calling other firms*. Silence for even 20 minutes means they kept shopping.
**Build:** shares #1's webhook → Switch node on `language` → Twilio SMS + Gmail/SendGrid nodes per branch.

### ⚡ 3. Missed-Call Text-Back
**What it is:** any call to the office that goes unanswered triggers an automatic apology-plus-action text within 30 seconds.
**What happens:** ① CallRail detects a missed/abandoned call → ② webhook fires to n8n → ③ SMS to the caller: "Sorry we missed you — this is United Citizen Law. Reply 1 and we'll call you right back, or tap here to book a free consult." → ④ intake gets a callback task with the recording link.
**Why it matters:** injury victims rarely leave voicemails; they dial the next Google result. This recovers a third or more of would-be-lost callers.
**Build:** CallRail webhook trigger → IF (call status = missed AND first-time caller) → Twilio SMS → CRM task node.

### 4. 24/7 AI Intake (Chat + After-Hours Voice)
**What it is:** a website chat and after-hours phone agent that interviews the lead like a trained intake specialist, books consultations, and wakes Sam for emergencies.
**What happens:** ① Visitor opens chat (or calls at 2 a.m.) → ② AI asks the intake questions in the visitor's language: what happened, when, injuries, treatment so far, police report, insurance status → ③ answers are written into the CRM as a structured record → ④ qualified leads get offered real calendar slots → ⑤ "hot" signals (commercial truck, fatality, hospitalization) page Sam immediately regardless of hour.
**Why it matters:** accidents peak on nights and weekends — exactly when the current site has zero capture. This is a receptionist who never sleeps and speaks five languages.
**Build:** chat widget (Intaker/Smith.ai or custom) → n8n Webhook per completed conversation → AI Agent node (extraction to JSON) → CRM upsert → IF (hot-case rules) → Twilio call to Sam.

### 5. Qualification + Statute-of-Limitations Gate
**What it is:** every new lead is automatically screened: is this a case the firm takes, and how much legal time is left on the clock?
**What happens:** ① New CRM lead → ② Code node computes the filing deadline from the accident date (California: generally 2 years; only 6 months for claims against government entities) → ③ deadline is stamped on the record → ④ leads outside the firm's practice get a polite, same-day referral-out email (drafted automatically, approved by a human) → ⑤ referral partners are tracked so favors ping back.
**Why it matters:** no dangerous deadline ever hides in a pile; declined leads still leave with a good experience (they refer friends); Sam's time goes only to real cases.
**Build:** CRM "lead created" trigger → Code node (Luxon date math) → CRM update → IF (practice-area match) → AI draft → human-approval step → send.

### 6. No-Show Shield
**What it is:** booked consultations confirm and remind themselves, and rebook themselves when someone doesn't show.
**What happens:** ① Consult booked → ② instant confirmation SMS+email → ③ reminder 24 hours out → ④ reminder 2 hours out with a one-tap reschedule link → ⑤ if marked no-show, a friendly 3-message sequence over 5 days offers new times.
**Why it matters:** intake no-show rates run 25–40%; reminder sequences cut that roughly in half. Every recovered consult is a potential signed case.
**Build:** Calendar/CRM trigger → Wait nodes → Twilio/Gmail → IF (no-show flag) → sequence branch.

### 7. E-Sign Retainer Flow
**What it is:** the paperwork between "yes, take my case" and "you're officially our client" happens in minutes, not days.
**What happens:** ① Consult marked "qualified — wants to proceed" → ② retainer agreement + medical-records release auto-generate with the client's details and go out for e-signature → ③ signed documents file themselves into the matter → ④ signing triggers the client welcome sequence (#10) and the case officially opens.
**Why it matters:** every day between verbal yes and signed retainer is a day competitors, family skeptics, and cold feet can undo the decision. Firms that sign same-day keep measurably more cases.
**Build:** CRM stage trigger → document-template merge → DocuSign/Dropbox Sign node → webhook on completion → CRM stage move + file storage.

### 8. Language Router
**What it is:** the invisible traffic cop that makes every other automation multilingual.
**What happens:** ① Any inbound lead carries a language preference (form field, chat detection, or caller's choice) → ② the record is tagged once → ③ every downstream automation (#2, #6, #9, #10…) reads the tag and sends its Spanish/Dari/Urdu/Arabic template instead of English → ④ reporting splits by language so the firm sees which communities are growing.
**Why it matters:** "we speak your language" is the firm's moat — this makes it true in every text, email, and reminder automatically, not just when a human remembers.
**Build:** Set node standardizing `language` on every entry workflow + Switch nodes in each sender; language column in the weekly dashboard (#30).

---

## GROUP B — Turning clients into five-star reviews and referrals

### ⚡ 9. The Review Engine (the 18-day rule keeper)
**What it is:** a systematic, policy-compliant machine that turns happy case endings into a steady drumbeat of Google/Yelp/BBB reviews — the single strongest input to map rankings AND Google's pay-per-lead ads AND what ChatGPT reads.
**What happens:** ① Case marked "resolved — successful" → ② same-day SMS in the client's language: warm thank-you + direct link to leave a Google review (one tap, no login hunting) → ③ if no review in 3 days, exactly one gentle reminder → ④ every 4th request points to Yelp or BBB instead of Google (those feed AI assistants) → ⑤ a counter watches the calendar: if 14 days pass with no new Google review, the dashboard flags it and suggests recent happy clients to ask personally.
**Why it matters:** review *recency* moves rankings — businesses that go ~3 weeks quiet visibly sag (the "18-day rule"). And per Google/FTC rules we never pre-filter who gets asked ("gating") and never trade anything for reviews — violations carry five-figure fines per incident.
**Build:** CRM stage trigger → Switch (language) → Twilio SMS with place-ID deep link → Wait 3d → IF (review detected via Google Business API poll?) → reminder → Schedule trigger (daily) checks days-since-last-review → alert.

### 10. "Your Case, Right Now" Status Updates
**What it is:** clients automatically hear from the firm at every milestone — before they ever have to wonder.
**What happens:** ① Matter moves stage in the CRM (records requested → demand sent → negotiating → settled) → ② client gets a plain-language, in-their-language text: "Update on your case: we sent your demand letter to the insurance company today. They typically respond in 30–45 days. Nothing needed from you." → ③ every message logs to the matter.
**Why it matters:** "my lawyer never tells me anything" is the #1 complaint against law firms and the top driver of bad reviews and firings. This kills it — and eliminates the daily "any update?" calls that eat staff hours.
**Build:** CRM stage-change trigger → Switch (stage × language template matrix) → Twilio/Gmail → CRM note.

### 11. Treatment-Adherence Nudges
**What it is:** during the medical-treatment phase, clients get a weekly supportive check-in.
**What happens:** weekly SMS while the matter is in "treating" stage: "Hope recovery is going okay, {name}. Keeping every medical appointment protects both your health and your claim's value. Reply here if anything's changed." Replies route to the paralegal.
**Why it matters:** gaps in treatment are the #1 way insurers slash settlement value ("they must not have been that hurt"). A $200/month nudge system protects five- and six-figure outcomes.
**Build:** Schedule trigger (weekly) → CRM query (stage = treating) → SplitInBatches → Twilio → replies via webhook to task queue.

### 12. Anniversary & Birthday Touches
**What it is:** past clients hear from the firm once or twice a year like a human remembered them.
**What happens:** ① Daily schedule scans for birthdays and settlement anniversaries → ② AI drafts a short personal note referencing their case's happy ending → ③ Sam approves in one tap → ④ it sends from his number/inbox.
**Why it matters:** past clients are the cheapest source of new cases — but only if they remember you exist when their cousin gets rear-ended. PI clients hire once; they *refer* forever.
**Build:** Schedule trigger → CRM date-match query → AI draft → approval webhook → send.

### 13. Referral Thank-You Loop
**What it is:** when a new lead names a past client as their source, gratitude fires automatically.
**What happens:** ① Intake source field matches a past client → ② Sam gets an alert → ③ a handwritten-card task (and a bar-rules-compliant thank-you, e.g., a charitable donation in their name where required) is created and tracked to completion.
**Why it matters:** thanked referrers refer again — unthanked ones stop. California bar rules restrict paying for referrals, so the *form* of gratitude is pre-vetted and consistent.
**Build:** CRM trigger → fuzzy match Code node against client table → task + alert nodes.

### 14. "How Did You Hear About Us?" Capture
**What it is:** one mandatory question on every intake, piped into reporting forever.
**What happens:** ① Intake (human or AI) always records the answer verbatim → ② n8n normalizes it into buckets (Google, referral, saw an ad, TikTok, mosque/community event, friend…) → ③ it lands in the weekly dashboard next to what the tracking pixels claim.
**Why it matters:** trackers can't see a friend's recommendation or a community event. This question catches the invisible half of marketing — and it's the tiebreaker when platforms all claim credit for the same client.
**Build:** intake webhook → Code node (keyword bucketing) → data table append → feeds #30.

---

## GROUP C — Marketing that runs itself

### ⚡ 15. NAP Watchdog
**What it is:** a robot that checks every important directory weekly to make sure the firm's Name, Address, and Phone are correct — so the old-address problem that was quietly hurting rankings can never creep back.
**What happens:** ① Weekly crawl of the top ~40 listings (Google, Yelp, BBB, Avvo, Justia, FindLaw, Apple, Bing, chambers…) → ② each is compared against the one true record → ③ any mismatch produces an alert + a fix-it task with the exact wrong field highlighted.
**Why it matters:** the audit found the firm's own website broadcasting its old address — and directories copy each other, so one wrong listing breeds more. Consistency is a core map-ranking trust signal.
**Build:** Schedule trigger → HTTP Request nodes per directory (or DataForSEO business-listings API) → Code node diff vs canonical JSON → IF mismatch → Slack/SMS alert + task.

### 16. GBP Post Scheduler
**What it is:** the Google map listing gets fresh content twice a week without anyone logging in.
**What happens:** ① AI drafts posts from a rotating recipe: anonymized case win → safety tip → FAQ answer → community item → ② human approves in a queue → ③ posts publish via API; a monthly reminder collects fresh office/team photos.
**Why it matters:** active profiles win more clicks, and businesses open-and-posting at search time rank better. Photos alone drive ~45% more direction requests.
**Build:** Schedule trigger → AI node with content-recipe prompt → approval webhook → Google Business Profile API post.

### 17. Review-Response Drafter
**What it is:** every new review, on any platform, gets a ready-to-approve reply in the review's own language within the hour.
**What happens:** ① New review detected → ② AI drafts a reply that thanks them warmly and — critically — **never confirms they were a client** (attorney confidentiality applies even to praise) → ③ one-tap approve/edit → ④ posts.
**Why it matters:** 88% of consumers favor businesses that respond to reviews; response speed also feeds the map algorithm. The confidentiality guardrail is what makes automation safe for a law firm.
**Build:** review-platform webhooks/polling → AI node with compliance-constrained system prompt → approval → API post.

### 18. LSA Lead Responder & Dispute Bot
**What it is:** Google's pay-per-lead ads get answered instantly (which raises the firm's LSA ranking) and junk leads get disputed for refunds before the window closes.
**What happens:** ① LSA lead arrives → ② flows straight into automation #1 (so response time is seconds) → ③ obvious junk (solicitors, wrong service, out-of-area) is auto-flagged with evidence and submitted for credit within Google's dispute window.
**Why it matters:** LSA ranking explicitly rewards >80% answer rates and punishes slow ones; disputes recover 10–20% of spend most firms silently eat.
**Build:** LSA webhook → #1 pipeline + IF (junk heuristics) → dispute API/task with transcript attached.

### 19. Search-Terms Janitor
**What it is:** a weekly robot that reads every actual Google search that triggered the firm's ads and blocks the wasteful ones.
**What happens:** ① Weekly pull of the search-terms report → ② Code node flags known waste patterns ("salary," "free," "how to become," "defense," school names…) → ③ pre-approved patterns auto-apply as negative keywords; borderline ones go to a review list → ④ budget pacing and cost-per-lead anomalies text Sayed.
**Why it matters:** at $100–400 per click, one bad keyword left running for a month is a four-figure leak. Weekly pruning typically saves 20–30% of search budget.
**Build:** Schedule trigger → Google Ads API query → Code node (regex bank) → Ads API negative-keyword mutate → alert thresholds.

### 20. Creative Fatigue Monitor
**What it is:** ads wear out like billboards people stop noticing; this watches the decay curve and queues the next ad before performance collapses.
**What happens:** ① Daily pull of hook rate (how many people stop scrolling) and CTR per ad → ② when either drops 15%+ from its peak, alert + auto-queue the next tested variant from the creative bench.
**Why it matters:** fatigue is the silent killer of ad accounts — most people notice only after cost-per-lead has doubled. Catching the 15% dip catches it weeks early.
**Build:** Schedule trigger → Meta Insights API → static-data peak tracking (`$getWorkflowStaticData`) → IF threshold → alert + campaign-asset swap task.

### 21. Rank + AI-Answer Tracker
**What it is:** a monthly scan answering two questions: "Where do we show on the map across different Sacramento neighborhoods?" and "What does ChatGPT say when asked for an injury lawyer here?"
**What happens:** ① Monthly geo-grid rank check on the money keywords from multiple points around the city → ② scripted queries to ChatGPT/Perplexity ("best personal injury lawyer in Sacramento", in English AND Spanish) with the answers archived → ③ month-over-month delta report.
**Why it matters:** you can't improve what you don't measure — and AI answers are 45% of local discovery now. Watching the actual answers shows whether the Part-6 AEO work is landing.
**Build:** Schedule trigger → DataForSEO/serp API grid → LLM API calls → Code diff vs archive → report to #30.

### 22. Content Decay Radar
**What it is:** pages that are quietly losing Google traffic raise their own hand for a refresh.
**What happens:** ① Quarterly Search Console pull per page → ② any page down 20%+ in clicks vs prior quarter generates a refresh task listing which exact queries slipped → ③ refreshed pages get a new visible "reviewed on" date.
**Why it matters:** content is an orchard, not a statue — rankings decay without maintenance, and substantive updates reliably recover them. This targets effort exactly where traffic is bleeding.
**Build:** Schedule trigger → GSC API → Code compare vs stored baseline → task creation with query deltas.

### 23. Blog → Everywhere Repurposer
**What it is:** every new article automatically becomes a Google post, a Facebook/LinkedIn post, and a Spanish draft.
**What happens:** ① New post published (RSS/webhook) → ② AI produces the platform-sized variants + Spanish translation draft → ③ approval queue → ④ scheduled publishing.
**Why it matters:** one hour of writing becomes five surfaces of presence; the Spanish variant compounds the moat at near-zero marginal cost (human review before publishing keeps quality).
**Build:** RSS trigger → AI multi-output node → approval webhook → platform API nodes.

### 24. Mention & "Best Of" List Hunter
**What it is:** a scout that finds unlinked press mentions and new lawyer rankings the firm should be on.
**What happens:** ① Daily alerts for brand mentions ("United Citizen Law", "Sam Fareed") → ② mentions without a link generate a friendly ask-for-link draft → ③ newly detected "best Sacramento lawyer" listicles create a pitch task with the outlet's contact.
**Why it matters:** "best of" placements are the #1 source AI assistants cite for local recommendations, and brand mentions correlate with AI visibility ~3× more than ordinary links.
**Build:** Schedule trigger → news/serp API queries → Code filter (new vs seen, static data) → AI outreach draft → task.

---

## GROUP D — Back office that runs itself (and protects the firm)

### 25. Medical-Records Chaser
**What it is:** the polite robot that never forgets to follow up with hospitals — the single biggest silent delay in every injury case.
**What happens:** ① Records request logged with provider + date → ② automatic follow-up fax/email/call-task every 10 business days → ③ at 30 days, escalation to the paralegal with the full chase history → ④ arrival stops the clock and files the records to the matter.
**Why it matters:** cases routinely stall 60–90 days waiting on records nobody chased. Faster records = faster demands = faster settlements = happier clients and faster fees.
**Build:** CRM matter-field trigger → Wait loops with business-day Code math → escalating task/notification chain → stop-on-received webhook.

### 26. Statute-of-Limitations Sentinel
**What it is:** an unmissable, escalating alarm on every case's legal filing deadline.
**What happens:** ① Every matter carries its computed deadline (from #5) → ② alerts fire at 12 months, 6, 3, and 1 month out — escalating from dashboard note → email → SMS → daily SMS to Sam personally in the final month until acknowledged.
**Why it matters:** a blown statute of limitations is a destroyed case, a malpractice claim, and a bar complaint. This is malpractice insurance that costs $0.
**Build:** Schedule trigger (daily) → CRM date query → threshold Switch → escalating channel nodes with acknowledgment webhook.

### 27. Lien Tracker
**What it is:** a live board of every medical lien (the "IOUs" doctors and insurers hold against the settlement) and its negotiation status.
**What happens:** ① Liens logged per matter → ② status board (asserted / negotiating / reduced / satisfied) → ③ any settlement approaching disbursement with unresolved liens throws a blocking alert.
**Why it matters:** mishandled liens are how firms accidentally give away client money or trigger post-settlement disputes. Negotiated-down liens literally put more dollars in the client's pocket — the thing five-star reviews are made of.
**Build:** CRM custom objects → Schedule status sweep → IF (settlement stage AND open liens) → blocking alert.

### 28. Settlement Disbursement Checklist Bot
**What it is:** the "landing checklist" that runs itself when a case settles — the most error-sensitive moment in the whole practice.
**What happens:** ① Matter hits "settled" → ② auto-generated closing checklist: release signed → funds received → liens paid (gated by #27) → costs reconciled → client statement generated → e-signed → client paid → ③ each item checks off with proof attached; the client gets a plain-language "here's where your money went" summary and a payment-sent text.
**Why it matters:** trust-account mistakes are the fastest way for a law firm to face bar discipline. And the transparent final statement is the moment clients decide you were worth it — right before #9 asks for a review.
**Build:** CRM stage trigger → templated task chain with dependency gates → document merge → e-sign → final SMS.

### 29. Document Intake OCR
**What it is:** clients photograph any document with their phone; the system reads it and files it.
**What happens:** ① Client texts/uploads a photo (police report, insurance letter, medical bill) → ② OCR extracts the text → ③ AI identifies the document type and pulls key fields (claim number, adjuster name, insurer, dates) → ④ auto-filed to the right matter with fields written to the CRM → ⑤ paralegal sees a one-line summary instead of an attachment pile.
**Why it matters:** hours of manual typing vanish; nothing gets lost in an inbox; adjuster/claim numbers are findable in seconds when the insurer calls.
**Build:** Twilio MMS/portal webhook → OCR (Google Vision) → AI classification+extraction (JSON) → CRM update + file storage.

### 30. Monday Command Dashboard
**What it is:** every Monday 7 a.m., one email that replaces every status meeting.
**What happens:** automatic compile of the week: new leads by source (with the #14 human answers beside the pixel data) · median speed-to-lead · consult-to-retainer rate · new reviews + days-since-last · ad spend vs signed-case value (MER) · case pipeline by stage · any red flags (SOL alerts, stalled records, fatigue warnings).
**Why it matters:** the firm sees its whole business on one screen in 3 minutes — decisions get made from numbers, not vibes, and problems surface Monday instead of month-end.
**Build:** Schedule trigger → parallel API pulls (CRM, CallRail, Ads, Meta, GBP) → Code aggregation → HTML email template → send.

### 31. Intake-Call Quality Coach
**What it is:** every intake call gets transcribed and scored, and the patterns become Friday coaching notes.
**What happens:** ① Call recordings pull nightly → ② transcription → ③ AI scorecard: greeted warmly? empathy shown? all qualification questions asked? consultation offered? language matched? → ④ weekly digest of scores, best-call clips, and the one habit to improve.
**Why it matters:** the most expensive click in America still dies on a cold phone call. Firms that coach intake convert 20–30% more of identical lead flow — this makes coaching automatic instead of "when someone has time."
**Build:** CallRail API nightly → Whisper transcription → AI rubric scoring (JSON) → aggregate → digest email.

### 32. Client Happiness Pulse (save-the-relationship radar)
**What it is:** a one-tap mid-case survey that catches unhappy clients while there's still time to fix it.
**What happens:** ① At set milestones, client gets: "Quick check — how are we doing? 😟 😐 🙂" → ② 🙂 = thank-you (and later feeds the review engine) → ③ 😟 or 😐 = **Sam is paged immediately** with the client's history, and a personal call happens within hours → ④ trends by stage show where the experience sags.
**Why it matters:** unhappy legal clients rarely complain first — they go quiet, then fire the firm or post the one-star story. Catching a frown mid-case converts would-be detractors into the loudest fans (service-recovery paradox: a problem fixed well beats no problem at all).
**Build:** stage-based trigger → Twilio survey → Switch on response → page-Sam branch vs log-and-thank branch → trend table feeding #30.

---

## The price tag: the $100–250/month build (per Sayed's envelope)

Automations get expensive three ways: per-task tools (Zapier charges per step), per-seat software (legal CRMs run $49–200+ *per user per month*), and managed services ($140–300+/month retainers). We avoid all three and spend the budget where it buys reliability instead:

### Recommended configuration ≈ **$137/month**
| What | Tool | Monthly |
|---|---|---|
| CRM (system of record, unlimited users) | **UCL Case Desk** — ours, Twilio + webhooks built in | **$0** |
| CRM hosting + sync (multi-device, backed up) | Vercel free + **Supabase Pro** when the team outgrows one device | **$0–25** |
| Workflow engine, zero-maintenance | **n8n Cloud Starter** (managed, auto-updated — no VPS babysitting) | **$24** |
| SMS + voice + tracking numbers | **Twilio**: 4 numbers (site/GBP/LSA/ads) + realistic volume | **~$35** |
| Professional call tracking + recordings | **CallRail Lite** (feeds automations #18/#31 with zero glue code) | **$45** |
| AI drafting & intake scoring | Budget AI API | **~$15** |
| Form delivery | Formspree Starter (unlimited-ish, spam filtering) | **$10** |
| E-signatures | SignWell/Dropbox Sign starter | **$8–15** |
| **Total** | | **≈ $137–169/mo** |

### Fully-loaded ceiling ≈ **$246/month** (still inside the envelope)
Adds: managed AI voice answering for true 24/7 phone intake (~$50–80 usage-based) and Ahrefs/DataForSEO Lite for rank + citation tracking (~$29). Nothing in the catalog requires this tier — it buys convenience and deeper reporting.

**What the budget explicitly does NOT go to:** Zapier per-task pricing (n8n runs unlimited workflows at flat cost), per-seat CRM licenses (Case Desk is ours — the $200+/mo a Lawmatics seat costs is redirected to call tracking and Twilio, which actually generate cases), Podium-style review retainers (~$300/mo — automation #9 does it on Twilio for pennies), and annual contracts.

**Same catalog bought as SaaS:** Lawmatics (~$200) + CallRail ($45) + Podium (~$300) + Smith.ai chat (~$140) + Zapier Pro (~$50) ≈ **$735+/month** — and the firm would own none of it. At $137–246, everything is either owned outright or month-to-month, and the only cost that grows with success is Twilio usage.

---

## What this all adds up to

| | Without automations | With all 32 |
|---|---|---|
| Lead answered at 2 a.m. Saturday | Voicemail → lost | AI intake, in Dari if needed, consult booked |
| Speed to first response | Hours (business days) | Under 60 seconds, 24/7 |
| Reviews | Sporadic, whenever someone remembers | Weekly drumbeat, never a 3-week gap |
| Wrong address on a directory | Undetected for years | Caught within 7 days |
| Filing deadlines | In someone's head | Four escalating alarms per case |
| Medical records | Chased when remembered | Chased every 10 days automatically |
| Marketing waste | Invisible | Flagged weekly ($-per-keyword, ad fatigue, junk-lead refunds) |
| The team's actual job | Admin + firefighting | **Lawyering and talking to clients. Everything else runs itself.** |

**Build order:** Week 1 → #1, 2, 3, 9, 15, 18 (the ⚡ six — they fund everything else). Weeks 2–4 → rest of Group A + #10. Weeks 5–8 → rest of Group B + C. Weeks 9–12 → Group D. Each is an independent n8n workflow with its own Error Trigger alarm, so one failure never silently breaks another.

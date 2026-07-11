# United Citizen Law — The Growth Plan, Explained in Plain English
**July 10, 2026 · Apex Growth Corp**
*This version is written so anyone — the attorney, the intake team, a new hire — can read it once and understand exactly what we're doing, why, and in what order. Every technical word is explained the moment it appears, and there's a glossary at the end.*

---

## The whole plan in three sentences

1. **Fix the broken foundation** — the website is currently telling Google wrong information and losing visitors, so ads and content poured on top of it leak out the bottom.
2. **Capture the people already searching** — every day, injured people in Sacramento type "car accident lawyer near me" into Google; we make sure United Citizen Law is what they find, click, and call.
3. **Own the two lanes no competitor can copy** — Sam's own accident story, and the five languages the team speaks. The giant firms can outspend us; they cannot out-*story* us or speak Dari.

---

## PART 1 — Where the business is today (and why it's stuck)

Think of the website as the firm's **storefront on Google Street**. Right now that storefront has six serious problems. Here's each one, in plain terms:

### Problem 1: The website hands Google a business card with the OLD address on it
Websites contain a hidden block of text called **schema** (a "business card for robots" — humans never see it, but Google reads it to learn your name, address, and phone number). United Citizen Law's schema still lists the **old office (3400 Watt Ave) and an old phone number**. The real office is 3301 Watt Ave with a different number.
**Why it matters:** Google decides who shows up in the map results by asking, "Am I *sure* this business is where it says it is?" When your own website disagrees with your Google listing and Yelp, Google loses confidence — and quietly shows you less. This is like a store whose sign, receipts, and mail all show different addresses. *Fix cost: one hour. Impact: every single day.*

### Problem 2: The homepage has no headline that Google can read
Every page is supposed to have one main heading (called an **H1** — think of it as the title of a book chapter). Google reads it to understand what the page is about. The current homepage's "headline" lives inside a picture slider, which to Google is just a decoration. The page effectively has **no title**.
**Why it matters:** Imagine handing someone a book report with no title. That's what the firm hands Google every day.

### Problem 3: Every image is invisible to Google — and to blind visitors
Images need a short text label (**alt text**) describing what's in them, because Google can't "see" pictures and screen-reader software for blind users reads those labels aloud. **All 24 homepage images have no labels.** That's zero image search traffic, and — awkward for a law firm — it's the exact kind of accessibility failure that ADA website lawsuits are built on.

### Problem 4: The site can't remember who visited
There are small tracking tools every serious business installs:
- A **pixel** (Meta's "guest book") lets you later show ads to people who visited but didn't call — called **retargeting**. Not installed.
- **Call tracking** shows which ad or page made the phone ring. Not installed — so today, *phone calls, the #1 way injury clients hire lawyers, are invisible in the data.*
- A **chat widget** catches the 2 a.m. visitor who just got rear-ended. Not installed.
**Why it matters:** roughly 97 of every 100 visitors leave without calling. Right now those 97 are gone forever. With these tools, they're an audience we can win back for pennies.

### Problem 5: The site is missing most of its "aisles"
A grocery store with only 4 aisles sells less than one with 12. The site has only **4 practice-area pages** (car, rideshare, dog bite, slip & fall). There is **no page** for truck accidents, motorcycle accidents, pedestrian or bicycle accidents, wrongful death, or brain injuries — so when someone searches "Sacramento truck accident lawyer," Google literally has no United Citizen Law page to show. The big competitor firms have all of these pages. **Dedicated pages per service are the single strongest factor for ranking in local search** (Whitespark's 2026 industry study).

### Problem 6: The firm's biggest superpower is invisible
The team speaks **English, Spanish, Dari/Farsi, Hindi/Urdu, and Arabic**. Sacramento has one of the largest Afghan communities in America, plus huge Spanish-speaking neighborhoods. When someone searches in Spanish ("abogado de accidente en Sacramento") or asks a friend in Dari who to call — **no law firm in this market owns those searches**. The website has zero pages in any of those languages. This is an open lane with no competition in a market where every English keyword is a bidding war.

**Also worth knowing:** the site is slow (built on a heavy page-builder with 53 separate script files — like a car towing three trailers), and Google measures speed with the **Core Web Vitals** stopwatch. Slow sites rank lower and lose impatient visitors. The rebuilt page we delivered is about 87% lighter.

---

## PART 2 — How injured people actually pick a lawyer (the map we're winning)

When someone gets hurt, here's the path nearly all of them walk:

```
Accident happens
   → They Google (usually on a phone, often at night, in the language they think in)
      → They see: ① Ads at the top  ② The MAP with 3 firms  ③ Regular results below
         → They tap 2–3 firms, glance at star ratings and reviews
            → They visit 1–2 websites for maybe 30 seconds
               → They call ONE firm. If it answers well, they usually stop looking.
```

Every move in this plan attacks one specific step of that path:

| Step of the journey | What we do about it |
|---|---|
| The map's top-3 ("local pack") | Fix the address confusion, feed Google consistent info, grow reviews |
| The ads at the very top | Google's pay-per-lead program (LSA) + carefully-managed search ads |
| Star ratings | The review engine (Part 5) |
| The 30-second website visit | The rebuilt black-and-gold site: proof, story, and a giant call button |
| The phone call | Speed-to-lead automation: answer in under 5 minutes, 24/7 |
| Searches in Spanish/Dari/Arabic | The multilingual pages nobody else has |
| People asking ChatGPT for a lawyer | Feeding the sources AI tools trust (details in Part 6) |

---

## PART 3 — Move One: Fix the foundation (Weeks 1–2)

These are unglamorous, one-time repairs. They cost hours, not months, and everything after depends on them:

1. **Correct the robot business card** (schema) — new address, phone, hours, languages, Sam's credentials, star rating. Already written into the rebuilt site.
2. **Give every page a real headline (H1)** and every image a label (alt text).
3. **Install the measurement kit** — Meta pixel + CAPI (CAPI is a direct, server-to-server wire that reports "this ad produced this phone call" even when iPhones block normal tracking), Google call tracking numbers, and a 24/7 chat/intake widget.
4. **Delete the speed bump in robots.txt** — one line (`Crawl-delay: 10`) currently tells Microsoft's search robot to crawl the site absurdly slowly. Why care about Bing? Because **Bing's index is what ChatGPT and Copilot read** when someone asks "who's a good injury lawyer in Sacramento?"
5. **Claim the three free listings most firms forget:** Bing Places, Apple Business Connect (Apple Maps), and the big data distributors (Data Axle, Foursquare, Neustar) that feed hundreds of smaller directories — all with the ONE correct address.
6. **Publish the rebuilt website.**

**How we'll know it worked:** Google Search Console (Google's free report card) shows the pages getting indexed; the firm appears consistently in map searches from different Sacramento neighborhoods; every call and form now shows *where it came from*.

---

## PART 4 — Move Two: Capture existing demand (Weeks 3–6)

### 4a. Google Local Services Ads (LSA) — the smartest dollars in legal marketing
**What it is:** the very top spot on Google — above everything — with a green "Google Verified" badge. Unlike normal ads, **you don't pay per click; you pay only when someone actually calls or messages you.** A click that goes nowhere costs $0.
**How you rank there:** Google's own recipe = review count + how recent your reviews are + how fast you answer (answer over 80% of calls and Google boosts you; ignore calls and it buries you). Notice: *our review engine and our speed-to-lead automation ARE the LSA strategy.* Everything connects.

### 4b. Regular Google Search ads — with a leash
Injury-lawyer clicks in Sacramento cost **$100–$400 each**. That's not a typo; it's the most expensive keyword category in America. So we run this tightly:
- **Small, focused ad groups** ("car accident lawyer sacramento" and its close variants — not a giant keyword soup).
- **Negative keywords** — a blocklist so we never pay $200 for someone searching "car accident lawyer *salary*" or "*free legal aid*" or "how to *become* a lawyer." We build the blocklist before launch and prune weekly. This single habit typically saves 20–30% of the budget.
- **Every ad promise matches the page it lands on.** Ad says "no fee unless we win" → the page's first line says the same. (People bounce instantly when the ad and page don't match.)

### 4c. The Google Business Profile (the map listing)
Weekly posts, monthly photos, correct hours, all five languages listed, review replies within 24 hours. One counterintuitive rule from 2026 testing: **don't link the map listing to the site's strongest page** — Google sometimes then shows only one of the two in results; linking to a different solid page lets both appear.

---

## PART 5 — The review engine (runs forever)

Reviews are the #1 trust signal for both humans and Google — and **recency matters as much as count**: industry tracking shows rankings sag when a business goes ~3 weeks without any new review (the "18-day rule").

The engine (fully automated — see AUTOMATIONS.md #9):
1. Case resolves → client instantly gets a warm thank-you text with a direct "leave a review" link, **in their language**.
2. No review after 3 days → one gentle reminder. That's it — never nagging.
3. Requests rotate between Google (most), then Yelp and BBB (because — see Part 6 — AI assistants read those).
4. Every review gets a reply within 24 hours (drafted by AI, approved by a human, careful never to confirm someone was a client — that's a confidentiality rule for lawyers).
5. A dashboard alarm fires if 14 days pass without a new Google review, so the team can personally ask a happy recent client.
**Never** offered in exchange for anything, and **never** pre-screened ("review gating") — both violate Google policy and FTC rules with five-figure fines.

---

## PART 6 — Getting recommended by ChatGPT (yes, really)

Nearly half of consumers now ask AI assistants for local recommendations, and those referrals convert to customers at ~9× the rate of a regular Google click (15.9% vs 1.76%, Seer Interactive). AI assistants don't read minds — they read **specific sources**:
- **ChatGPT/Copilot** lean on **Bing's index, Yelp, BBB, and Reddit** — which is exactly why we claim Bing Places, keep Yelp/BBB complete and fresh, and (carefully, helpfully, no spam) participate where Sacramento locals ask for lawyer recommendations on Reddit.
- **All AI tools** love pages that answer questions directly. That's why every page we build opens with a plain-English answer, has a real FAQ section, carries FAQ schema (the robot-readable version of those Q&As), and names things clearly ("United Citizen Law is a Sacramento personal injury firm founded by attorney Sam Fareed" — a sentence a machine can quote).
- **"Best lawyer in Sacramento" lists** (Expertise.com and similar) are the #1 source AI cites for local picks. We pitch for inclusion on every credible list.

---

## PART 7 — Move Three: The content & language moat (Weeks 3–12)

**The missing aisles.** We build every missing practice page — truck, motorcycle, pedestrian, bicycle, wrongful death, brain injury, uninsured-motorist — each 2,000+ words, each answering the questions real clients ask, each with its FAQ, Sam's byline, and a visible "reviewed on [date]" stamp. Google rewards demonstrated first-hand expertise (their rubric is called **E-E-A-T**: Experience, Expertise, Authoritativeness, Trustworthiness — and legal content is judged at the strictest level because it affects people's lives). A lawyer who *lived* a crash and publishes under his own name, credentials, and bar number is the strongest E-E-A-T card in the deck.

**Hub-and-spoke linking.** The 30 existing blog posts (genuinely good questions like "should I give a recorded statement?") get three cheap upgrades: Sam's byline, an updated date, and links pointing "up" to the matching practice page. Think of practice pages as the hub of a wheel and blog posts as spokes — Google follows the spokes to learn the hub is important.

**The language pages.** Spanish versions of the money pages first (human-reviewed — machine-translated legal pages destroy trust), then Dari/Farsi, Arabic, and Urdu landing pages. Each tells Google explicitly "this is the Spanish version of that page" via a tag called **hreflang** (a translation signpost for search engines). Then per-language Google posts and per-language review requests. **No Sacramento injury firm is doing this.** First one in owns it for years.

**City pages.** Pages for Elk Grove, Roseville, Folsom, Citrus Heights, Rancho Cordova — each with genuinely local content (local client stories, local roads and hospitals, local FAQ). The test: if you could swap "Elk Grove" for "Folsom" and the page still reads fine, it's a fake ("doorway") page and Google punishes those. Ours must pass the swap test.

---

## PART 8 — Ads that create demand (Weeks 7–12, after capture is running)

Search ads catch people who *already* need a lawyer **right now**. Social ads plant the memory for the day they *will*. Different job, different message (marketing textbooks call these **awareness stages** — you don't propose marriage on a first date, and you don't run "call now!" ads at people who aren't hurt).

- **The founder film.** Sam, to camera, phone-shot and real: *"In 2017 I was the one in the hospital bed…"* That's not an ad — it's a story people remember at the exact moment they need it. We test 3–5 cuts with small budgets, let the data pick the winner, then scale the winner slowly (big sudden budget jumps reset Meta's learning; ~20% steps every few days).
- **Retargeting** (possible only after the pixel from Part 3): visitors who didn't call see, over the following days — first the story, then the objection-killer ("worried you can't afford a lawyer? You pay nothing unless we win"), then the honest deadline (California really does give you only two years to file — that's *real* urgency, not a fake countdown).
- **Bilingual versions** of everything, because the ad auction for Spanish-language Sacramento is a fraction of the English price.

---

## PART 9 — How we measure (so no one argues with feelings)

- **One question on every intake: "How did you first hear about us?"** — catches the word-of-mouth and social buzz no tracker can see.
- **Call tracking** ties every phone call to the ad, page, or listing that produced it.
- **MER** (Marketing Efficiency Ratio) — the honest north star: *all* signed-case revenue ÷ *all* marketing spend, reviewed weekly. Platform dashboards each flatter themselves (Meta and Google will happily both claim the same client); MER can't be gamed.
- Monthly: map-ranking scan from different neighborhoods, plus a manual "ask ChatGPT/Perplexity for a Sacramento injury lawyer" check to track AI visibility.

## PART 10 — The 90-day calendar

| When | What ships |
|---|---|
| **Weeks 1–2** | All Part-3 foundation fixes · rebuilt site live · Bing/Apple/aggregators claimed · review engine ON · speed-to-lead ON |
| **Weeks 3–4** | LSA live · Search ads live with negative blocklist · GBP cadence begins · first 2 new practice pages |
| **Weeks 5–6** | Remaining high-value practice pages · Sam's bio/authority page · case-results page rebuilt as proof engine |
| **Weeks 7–8** | Spanish money pages + hreflang · blog upgrade sweep (bylines, dates, links) · founder film shot |
| **Weeks 9–10** | Meta tests live · first city pages · Dari/Arabic landing pages |
| **Weeks 11–12** | Scale winning ads · "best of" list pitches · first full MER review → reallocate budget to what's working |

**What success looks like by day 90 (conservative):** the firm appears in the map pack across central Sacramento; every lead is answered in under 5 minutes around the clock; reviews arrive weekly instead of sporadically; organic leads run 3–5× the current rate; and every dollar of spend has a receipt.

---

## Glossary (one line each)
- **Schema / structured data** — hidden robot-readable business card on your site.
- **NAP** — Name, Address, Phone; must match everywhere online.
- **H1** — a page's main headline; Google reads it as the page title.
- **Alt text** — the text label on an image for Google and blind users.
- **Local pack** — the 3 businesses Google shows on the map.
- **GBP** — Google Business Profile; your map listing.
- **LSA** — Local Services Ads; top-of-Google, pay-per-lead, "Google Verified" badge.
- **Negative keywords** — search terms you refuse to pay for.
- **Pixel / CAPI** — visitor memory for ads; CAPI is its unblockable server-side wire.
- **Retargeting** — showing ads to people who already visited you.
- **Core Web Vitals** — Google's speed stopwatch for your site.
- **E-E-A-T** — Google's trust rubric: Experience, Expertise, Authoritativeness, Trustworthiness.
- **Hreflang** — tag telling Google "this page is that page, in Spanish."
- **Doorway page** — fake city page with swapped names; punished by Google.
- **Hub-and-spoke** — practice page (hub) fed by related articles (spokes) via links.
- **AEO** — making your business the answer AI assistants give.
- **MER** — total revenue ÷ total marketing spend; the un-gameable scoreboard.
- **Speed-to-lead** — minutes between a lead arriving and a human responding; under 5 = 80–90% connection.
- **Review gating** — pre-filtering who gets asked for reviews; banned, fined, never done.

# United Citizen Law (uclaw.net) — Full SEO / Presentation / Conversion Audit
**Audited:** July 10, 2026 · **Auditor:** Apex Growth Corp (Sayed Sultani) · **Method:** Live-source teardown (raw HTML, sitemaps, robots.txt, schema extraction, citation cross-check) + seo-audit / seo-local / aeo-optimization frameworks

---

## Executive Summary

**Overall SEO Health Score: 42/100** · **Local SEO Score: 48/100**

United Citizen Law is a genuinely strong business wrapped in a website that actively suppresses it. The firm has elite raw material — a founder survivor story, $5M/$2M/$1.75M case results, 4.9-star reputation, BBB A+, Super Lawyers Rising Star 2021–2026, and **five languages (English, Spanish, Dari/Farsi, Hindi/Urdu, Arabic) in a market where nobody else owns the multilingual position** — but the site buries all of it under a slow page-builder stack, broken structured data, and a content footprint one-third the size of what the Sacramento PI market requires.

| Category (weight) | Score | Verdict |
|---|---|---|
| Technical SEO (22%) | 55 | Working basics (Yoast, canonical, sitemap) undermined by bloat + crawl throttle |
| Content Quality (23%) | 40 | Money pages thin (979 words); 8+ missing practice pages; zero multilingual content |
| On-Page SEO (20%) | 45 | **No H1 on homepage**; inconsistent title patterns; builder cruft in visible text |
| Schema (10%) | 35 | LegalService schema exists but contains **wrong address & phone** + invalid formats |
| Performance/CWV (10%) | 30 | 211KB HTML, 53 scripts, Slider Revolution, zero lazy-loading |
| AI Search Readiness (10%) | 35 | FAQPage schema exists (good); no llms.txt, no author entities, no answer-first formatting |
| Images (5%) | 10 | **24 of 24 homepage images missing alt text** (100% failure) |

---

## CRITICAL Findings (fix immediately)

### C1. Schema broadcasts the WRONG address and phone number (NAP poisoning)
The homepage LegalService JSON-LD declares **3400 Watt Ave Ste 200A / (916) 573-0474** while the visible site, Yelp, and GBP say **3301 Watt Ave Suite 100 / (916) 800-8457**. Their own website feeds Google conflicting entity data. The citation ecosystem is already split (TrustAnalytica carries the old address; Yelp the new one). NAP consistency is a foundational local-pack trust factor — this single bug suppresses map rankings every day it lives.
Additional schema defects: empty `{}` nodes in `@graph`, hours as `"8:00 AM "` (must be ISO `08:00`), `dayOfWeek: "Mon"` (must be `Monday`/schema URL), `faxNumber: null`, logo hotlinked from a third-party directory's Cloudinary account, no `aggregateRating`, no `sameAs`, no `priceRange`, no `areaServed`, no founder/attorney `Person` entity, geo coords fine but orphaned. Weekend hours absent entirely (PI clients crash on Saturdays too).

### C2. Homepage has ZERO `<h1>` tags
The single most important on-page element does not exist on the most important page. Google infers topic from a Slider Revolution graphic instead.

### C3. 24/24 homepage images have no alt text
100% failure. Simultaneously an accessibility violation (WCAG 1.1.1), an image-SEO zero, and an ADA lawsuit exposure — a special embarrassment for a law firm.

### C4. No Meta Pixel, no call tracking, no chat, no retargeting infrastructure
GTM + GA4 only. Consequences: (a) cannot retarget the ~97% of visitors who don't convert; (b) phone calls — the primary PI conversion — are invisible in analytics; (c) after-hours visitors (accidents peak nights/weekends) have no engagement path. The firm is paying for traffic it cannot measure, remarket, or capture.

### C5. Content footprint is ~1/3 of market requirement
Only 4 practice pages: car accidents, rideshare, dog bites, slip & fall. **Missing:** truck accidents, motorcycle accidents, pedestrian accidents, bicycle accidents, wrongful death, brain injury (TBI), spinal cord injury, uninsured/hit-and-run motorist. Dedicated service pages are the **#1 local organic ranking factor and #2 AI visibility factor** (Whitespark 2026). Every missing page is a keyword the firm cannot rank for — competitors (Ashton & Price, Demas, Eason & Tambornini, TorkLaw) have all of them.

### C6. The multilingual advantage is invisible to search engines
Five languages is the firm's most defensible differentiator — Sacramento hosts one of the largest Afghan communities in the US, plus large Spanish-speaking and South Asian populations. Yet: no hreflang, no `/es/` pages, no Dari/Farsi content, no "abogado de accidentes en Sacramento" page. **Nobody in the market owns these queries.** This is an open, uncontested lane.

---

## HIGH Findings

- **H1. Performance stack.** Divi + Slider Revolution 6.7 + 53 scripts + 8 stylesheets + 211KB HTML document + zero `loading="lazy"` + render-blocking Google Fonts. WP Rocket is masking, not fixing. CWV thresholds (LCP <2.5s mobile) are near-certainly failed on 4G. (PSI API quota blocked a scored run today; lab signals are unambiguous.)
- **H2. `Crawl-delay: 10` in robots.txt** throttles Bing to ~8,640 pages/day worst-case for no reason — and **Bing powers ChatGPT/Copilot local answers**, which convert at 15.9% vs Google organic 1.76% (Seer). Actively harmful line.
- **H3. Money-page thinness.** Car-accident page: 979 words vs 2,500–4,000 for ranking competitors. Case results page: 313 words with $5M+ of proof buried in it. FAQs page (3,156 words) is the best page on the site and only covers car accidents.
- **H4. Title-tag inconsistency.** Homepage: keyword-first (good). Money page: brand-first ("United Citizen Law | Car Accident…" — backwards). About page: no brand at all.
- **H5. Case results, reviews, credentials scattered and under-leveraged.** $5M / $2M / $1.75M / $1.25M / $1.1M / $915K results live on a 313-word page with 3 images; homepage shows generic slider claims instead. Review count on Google appears modest (Yelp 15; TrustAnalytica 4.9★) vs competitors with 300–1,000+ Google reviews — and review signals are now ~20% of local pack weight with an 18-day recency cliff (Sterling Sky).
- **H6. Visible builder cruft.** "Home administrator 2025-06-26T10:16:52-07:00" and "Choose Language: Off Canvas Toggle" render as visible page text. Unprofessional for a firm selling attention to detail.
- **H7. No embedded Google Map** (the only iframe is GTM noscript) — a missed geographic reinforcement + UX signal for a brick-and-mortar firm.
- **H8. og:image is a generic default banner** — every social/iMessage share shows a bland brand card instead of proof or the founder.

## MEDIUM Findings

- M1. No FAQ schema or FAQ modules on the homepage or practice pages (exists on the FAQ page only — good, extend it).
- M2. No `Person` schema for Sam Fareed (Super Lawyers/Forbes credentials are unmarked E-E-A-T gold; YMYL pages are held to the highest E-E-A-T bar).
- M3. No author bylines, credentials, or visible updated dates on blog posts (30 posts of decent car-accident cluster content wasted on E-E-A-T signals).
- M4. No llms.txt, no answer-first paragraph formatting; AI engines get no structured entity story beyond the (broken) schema.
- M5. No hub-and-spoke internal linking: blog posts don't systematically link up to practice pages with descriptive anchors.
- M6. Dual naming in the wild: "United Citizen Law" vs "United Citizen Law, A Fareed Injury Firm" (BBB, directories) — entity-confusion risk; pick one canonical name + `alternateName`.
- M7. No location pages for Elk Grove, Roseville, Folsom, Citrus Heights, Rancho Cordova, Arden-Arcade (must be non-doorway, ≥60–70% unique).
- M8. Sitemap contains near-zero-value pages (privacy-policy-sms, disclaimer) at equal priority; fine, but the *absence* of the 8 missing money pages is the real sitemap story.

## What's Already GOOD (keep)
- Yoast basics: canonical, meta robots, XML sitemaps, decent homepage title/description
- FAQPage schema present on /faqs/
- HTTPS + Cloudflare, `tel:` links present (4 on homepage), viewport correct
- 30-post blog cluster with genuinely good question-intent topics (the AEO bones already exist)
- BBB A+, Super Lawyers 2021–2026, Forbes mention, 4.9★ third-party ratings, real settlement figures — elite trust inventory awaiting deployment

---

## Competitor Gap Snapshot (Sacramento PI)

| | United Citizen Law | Ashton & Price | Demas Law Group | TorkLaw / Kershaw |
|---|---|---|---|---|
| Practice pages | 4 | 12+ | 10+ | 12+ |
| Positioning | (buried) | $200M+ recovered | 25 yrs, 99% rate | $1B+ verdicts |
| Google review mass | modest | large | large | large |
| Multilingual content | **0 (owns 5 languages!)** | minimal | minimal | minimal |
| Founder story | **unmatched — unused** | generic | generic | generic |

**The play is asymmetric:** don't out-mass the giants on "personal injury lawyer sacramento" day one — own (1) every long-tail accident-type + city combination, (2) the entire multilingual lane uncontested, (3) AI-engine answers via Bing/Yelp/BBB/FAQ surfaces the giants ignore, (4) the human story none of them can copy.

## Limitations
No GSC/GA4 access (no keyword/traffic actuals), PSI quota blocked scored CWV run, GBP interior data (categories, review velocity) not directly visible, backlink profile not pulled (no Ahrefs/Moz key). None of these change any finding above; all would sharpen prioritization in week 1 of engagement.

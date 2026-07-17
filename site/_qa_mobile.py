#!/usr/bin/env python3
"""Mobile regression guard for the UCL site.

Run:  python3 _qa_mobile.py [BASE_URL]
Default BASE is the local site directory (file://). Pass the live URL to
check production, e.g.:
  python3 _qa_mobile.py https://sayedbusiness.github.io/uclaw-website

Checks the exact failure modes seen on real iPhones so they can't silently
come back (headless Chromium can't reproduce iOS font-boosting — that's why
`text-size-adjust` is asserted at the CSS level rather than measured):
  1. html { -webkit-text-size-adjust:100% } present on every page
  2. sticky call bar hidden at top, shows on scroll, pills stay 54px, one line
  3. fixed top scrim (body::before) present on mobile widths
  4. no horizontal overflow at 390px
  5. scroll reveals never leave in-view content hidden
"""
import sys, pathlib
from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else None
PAGES = ["index.html", "car-accident-lawyer-sacramento.html", "team.html",
         "team-sam-fareed.html", "dog-bite-lawyer-sacramento.html"]

def url(page):
    if BASE: return f"{BASE.rstrip('/')}/{page}"
    return pathlib.Path(__file__).parent.joinpath(page).resolve().as_uri()

fails = []
def check(cond, label):
    print(("  ✓ " if cond else "  ✗ ") + label)
    if not cond: fails.append(label)

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 390, "height": 844},
                        device_scale_factor=3, is_mobile=True)
    pg = ctx.new_page()
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    for page in PAGES:
        print(f"[{page}]")
        pg.goto(url(page)); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(500)
        tsa = pg.evaluate("()=>getComputedStyle(document.documentElement).webkitTextSizeAdjust||getComputedStyle(document.documentElement).textSizeAdjust||''")
        check(str(tsa) == "100%", f"text-size-adjust guard = {tsa!r}")
        scrim = pg.evaluate("()=>getComputedStyle(document.body,'::before').position")
        check(scrim == "fixed", "fixed top scrim behind nav")
        over = pg.evaluate("()=>document.documentElement.scrollWidth - innerWidth")
        check(over <= 1, f"no horizontal overflow (delta {over}px)")
        cb0 = pg.evaluate("()=>{const c=document.querySelector('.callbar');return c?getComputedStyle(c).opacity:'none';}")
        check(cb0 in ("0", "none"), f"callbar hidden over hero (opacity {cb0})")
        pg.evaluate("window.scrollTo(0, innerHeight*1.2)"); pg.wait_for_timeout(700)
        bar = pg.evaluate("""()=>{const c=document.querySelector('.callbar'); if(!c) return null;
            return [...c.querySelectorAll('a')].map(a=>{const r=a.getBoundingClientRect();
              const cs=getComputedStyle(a); return {h:Math.round(r.height), wrap:cs.whiteSpace};});}""")
        if bar is not None:
            check(all(x["h"] == 54 for x in bar), f"callbar pills 54px ({[x['h'] for x in bar]})")
            check(all(x["wrap"] == "nowrap" for x in bar), "callbar labels single-line")
        # invariant: anything in view must have been granted its 'in' class —
        # computed opacity would false-fail while the 0.9s blur-in is mid-flight
        stuck = pg.evaluate("""()=>[...document.querySelectorAll('.reveal,.rv')].filter(e=>{
            const r=e.getBoundingClientRect();
            return r.top<innerHeight*0.85 && r.bottom>0 && !e.classList.contains('in');}).length""")
        check(stuck == 0, f"no stuck-hidden reveals in view ({stuck})")
    check(not errs, f"zero JS errors across pages ({errs[:2]})")
    b.close()

print("\n" + ("ALL MOBILE CHECKS PASS" if not fails else f"FAILURES: {len(fails)}"))
sys.exit(1 if fails else 0)

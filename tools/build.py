"""Build gerriscorp.com from src/.

Each file in src/ starts with `key: value` lines, then a line `---`, then the
page body:

    name:        menu and breadcrumb label
    title:       <title>, 50-60 characters, no pipes, dashes or hyphens
    description: meta description, 140-160 characters, same rules
    type:        optional: guide (an article with byline and dates)
    published:   optional ISO date (guides)
    updated:     ISO date the content last changed (shown on the page)

src/about.html becomes /about/, src/guides/glossary.html becomes
/guides/glossary/, and src/<dir>/index.html becomes /<dir>/. `{root}` in a
body is the relative path back to the site root, so links work on
gerriscorp.com and on the github.io preview alike. `{email}`, `{phone}`,
and `{tel}` are replaced with the contact details set below.

Markup the build understands inside a body:
- <section class="faq"> with <h3>question</h3><p>answer</p> pairs becomes
  FAQPage structured data.
- <dl class="glossary"> with <dt id="...">term</dt><dd>definition</dd>
  becomes a DefinedTermSet.

Writes every page plus a Markdown twin (index.md), an HTML site map at
/sitemap/, 404.html, sitemap.xml (with images, styled by sitemap.xsl for
people), robots.txt, feed.xml (guides), llms.txt, llm.txt, llms-full.txt,
.well-known/security.txt, and (when LIVE) CNAME. Then checks the house
rules: titles 50-60 characters, descriptions 140-160, no pipes, dashes or
hyphens in either, unique titles and descriptions, one h1 per page, a
minimum word count, em dashes only closed up, "Chris'" never "Chris's", first person
singular ("I", never "we"), and no links to missing pages.

    python3 tools/build.py
"""
import datetime, html, json, os, re, sys
from html.parser import HTMLParser
from guide_navigation import add_guide_contents

# Set to True at the DNS cutover: drops noindex and writes CNAME (see README).
LIVE = True

SITE = "https://gerriscorp.com/"
PREVIEW_BASE = "/gerriscorp/"
TABS = [("", "Home"), ("services/", "Services"), ("guides/", "Guides"), ("case-studies/", "Case Studies"),
        ("about/", "About"), ("work-with-me/", "Work With Me"), ("contact/", "Contact")]
FILES = ["index",
         "services/index",
         "services/technical-lead", "services/developers", "services/agency-partner", "services/rescue",
         "services/ai-automation", "services/data-cleanup", "services/analytics", "services/advisory",
         "services/technical-seo", "services/seo-engineering", "services/crawler-visibility", "services/large-sites", "services/ecommerce",
         "services/on-page-seo", "services/site-speed", "services/wordpress-care", "services/search-console", "services/migrations",
         "services/ai-search", "services/editorial", "services/podcast-sites", "services/ongoing-support",
         "services/multi-location", "services/reputation", "services/google-business-profile", "services/email-and-dns",
         "guides/index", "guides/fact-check-ai-seo", "guides/measure-ai-search", "guides/citation-gap-analysis", "guides/content-briefs", "guides/readme-ai-source", "guides/speculation-rules", "guides/indexnow-ai-search", "guides/ai-assistants", "guides/javascript-seo", "guides/hydration-errors", "guides/repository-access", "guides/nextjs-seo", "guides/seo-build-checks", "guides/migration-recovery", "guides/migration-tools", "guides/core-web-vitals-mcp", "guides/email-blocklist-recovery", "guides/crawled-not-indexed",
         "guides/migration-checklist", "guides/email-authentication", "guides/personal-information-removal",
         "guides/traffic-drop", "guides/removed-location-pages", "guides/year-end-seo-check", "guides/canonical-tags", "guides/robots-txt", "guides/structured-data",
         "guides/301-redirects", "guides/faceted-navigation", "guides/hreflang", "guides/core-web-vitals",
         "guides/cloudflare-seo", "guides/wordpress-behind-cloudflare", "guides/ga4-consent-mode", "guides/email-deliverability",
         "guides/ai-coding-assistants", "guides/ai-vendor-pitch", "guides/hiring-developers", "guides/hype-or-shift", "guides/seo-superpower", "guides/podcast-website", "guides/search-in-2026", "guides/self-ranking-lists", "guides/seo-101", "guides/podcast-seo", "guides/podcast-for-your-brand", "guides/lynx-qa", "guides/ada-website-compliance", "guides/glossary",
         "case-studies/index", "case-studies/ecommerce-rendering", "case-studies/consent-blocking",
         "case-studies/react-event-platform", "case-studies/netlify-migration", "case-studies/sanity-vercel",
         "case-studies/shopify-migration", "case-studies/app-takeover", "case-studies/programmatic-indexing",
         "case-studies/indexing-recovery", "case-studies/multi-location-entity", "case-studies/seasonal-retailer",
         "case-studies/gbp-reinstatement", "case-studies/umbraco-operations", "case-studies/ai-recruiting",
         "case-studies/data-cleanup", "case-studies/founder-record", "case-studies/four-site-speed-pass", "case-studies/built-with-claude-code",
         "about", "stack", "work-with-me", "faq", "standards", "colophon", "contact", "privacy"]
SERVICE_GROUPS = [
    ("Consulting and technical direction", ["services/technical-lead/", "services/developers/", "services/agency-partner/",
                                            "services/rescue/", "services/ai-automation/", "services/data-cleanup/",
                                            "services/analytics/", "services/advisory/"]),
    ("Search and site performance", ["services/technical-seo/", "services/seo-engineering/", "services/crawler-visibility/", "services/large-sites/",
                                     "services/ecommerce/", "services/on-page-seo/", "services/site-speed/", "services/wordpress-care/",
                                     "services/search-console/", "services/migrations/", "services/ai-search/",
                                     "services/editorial/", "services/podcast-sites/",
                                     "services/ongoing-support/"]),
    ("Local, reputation, and email", ["services/multi-location/", "services/reputation/",
                                      "services/google-business-profile/", "services/email-and-dns/"]),
]
# Additional services and guides, October 15, 2026.
FILES += ['services/internal-linking', 'services/ai-workflow-testing', 'guides/ai-pilot-tests', 'guides/website-handover']
SERVICE_GROUPS[0][1].extend(['services/ai-workflow-testing/'])
SERVICE_GROUPS[1][1].extend(['services/internal-linking/'])

MIN_WORDS = {"guide": 700, "service": 450, "case": 250, "page": 250}
TODAY = datetime.date.today().isoformat()
os.chdir(os.path.join(os.path.dirname(__file__), ".."))
AUTHOR = "https://chrisabraham.com/#person"
# Contact details: the only ones the site publishes. Change EMAIL here to switch every page.
EMAIL = "chris@gerriscorp.com"
PHONE = "+1 202-352-5051"
TEL = "+12023525051"



def close_dashes(h):
    """Chris' rule: "--" becomes an em dash and every em dash is closed up (word—word).
    Code, scripts, styles, and HTML comments keep their text exactly."""
    parts = re.split(r"(<pre\b.*?</pre>|<code\b.*?</code>|<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->|<[^>]+>)", h, flags=re.S)
    return "".join(x if i % 2 else re.sub(r"\s*(?:--|—)\s*", "—", x) for i, x in enumerate(parts))

def text_of(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).replace(" .", ".").strip()


def nice(d):
    return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")


def finish(p):
    """Derived fields shared by source pages and generated pages."""
    p["url"] = SITE + p["path"]
    p["root"] = "../" * p["path"].count("/")
    p.setdefault("name", "Home")
    p.setdefault("updated", TODAY)
    p["h1"] = text_of(re.search(r"<h1>(.*?)</h1>", p["body"], re.S).group(1))
    p["faq"] = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>",
                          "".join(re.findall(r'<section class="faq">(.*?)</section>', p["body"], re.S)), re.S)
    p["terms"] = re.findall(r'<dt id="([^"]+)">(.*?)</dt>\s*<dd>(.*?)</dd>', p["body"], re.S)
    p["words"] = len(text_of(p["body"]).split())
    # sources: "Label | https://url ;; Label | https://url", the primary documentation behind a guide
    p["sources"] = [tuple(x.strip() for x in item.split(" | ", 1)) for item in p.get("sources", "").split(" ;; ") if " | " in item]
    # about: / mentions: "Name | https://en.wikipedia.org/wiki/... ;; ..." (entities the article covers, for AI answer engines)
    for key in ("about", "mentions"):
        p["ent_" + key] = [{"@type": "Thing", "name": n.strip(), "sameAs": u.strip()}
                           for n, u in (item.split(" | ", 1) for item in p.get(key, "").split(" ;; ") if " | " in item)]
    return p


pages = []
for f in FILES:
    head, body = open(f"src/{f}.html", encoding="utf-8").read().split("\n---\n", 1)
    p = dict(line.split(": ", 1) for line in head.strip().splitlines())
    p["src"] = f
    p["path"] = "" if f == "index" else (f[:-5] if f.endswith("/index") else f + "/")
    p["body"] = body.strip().replace("{email}", EMAIL).replace("{phone}", PHONE).replace("{tel}", TEL)
    # Chris' rule (2026-10-13): "--" becomes an em dash, and every em dash is closed up tight.
    p["body"] = close_dashes(p["body"])
    p["tab"] = (p["path"].split("/")[0] + "/") if p["path"] else ""
    if p["tab"] not in dict(TABS):
        p["tab"] = {"privacy/": "privacy/", "standards/": "about/", "colophon/": "about/", "stack/": "about/"}.get(p["path"], "work-with-me/")  # the FAQ lives under Work With Me
    p["kind"] = p.get("type") or ("service" if p["tab"] == "services/" and p["path"] != "services/" else
                                  "case" if p["tab"] == "case-studies/" and p["path"] != "case-studies/" else "page")
    pages.append(finish(p))
by_path = {p["path"]: p for p in pages}


def site_map_body():
    li = lambda q: f'  <li><a href="{{root}}{q["path"]}">{q["h1"]}</a>: {q["description"]}</li>'
    out = ['<h1>Site map</h1>',
           '<p class="lead">Every page on this site, grouped by section, with a one-line summary of each. '
           'Search engines read the same list in <a href="{root}sitemap.xml">sitemap.xml</a>, and AI tools in '
           '<a href="{root}llms.txt">llms.txt</a>.</p>',
           '<h2>Main pages</h2>', '<ul>']
    out += [li(by_path[x]) for x in ["", "services/", "guides/", "case-studies/", "about/", "stack/", "work-with-me/", "faq/", "standards/", "colophon/", "contact/", "privacy/"]]
    out.append('  <li><a href="{root}site-index/">Index</a>: an A to Z list of the people, companies, tools, and problems the site covers, each linked to its pages.</li>')
    out.append('</ul>')
    for title, paths in SERVICE_GROUPS:
        out += [f'<h2>{title}</h2>', '<ul>'] + [li(by_path[x]) for x in paths] + ['</ul>']
    for title, tab in (("Guides", "guides/"), ("Case studies", "case-studies/")):
        out += [f'<h2>{title}</h2>', '<ul>'] + [li(q) for q in pages if q["tab"] == tab and q["path"] != tab] + ['</ul>']
    out += ['<h2>Files for machines</h2>', '<ul>',
            '  <li><a href="{root}sitemap.xml">sitemap.xml</a>: the XML sitemap for search engines.</li>',
            '  <li><a href="{root}llms.txt">llms.txt</a>: a plain summary of the site for language models, linking to Markdown versions of every page.</li>',
            '  <li><a href="{root}llms-full.txt">llms-full.txt</a>: the full text of the site in one file.</li>',
            '  <li><a href="{root}feed.xml">feed.xml</a>: an Atom feed of the guides. RSS is available at <a href="{root}rss.xml">rss.xml</a>.</li>',
            '  <li><a href="{root}robots.txt">robots.txt</a>: crawler rules; every search engine and AI crawler is welcome.</li>',
            '</ul>']
    return "\n".join(out)


pages.append(finish({
    "name": "Site Map", "src": "(generated)", "path": "sitemap/", "tab": "sitemap/", "kind": "page",
    "title": "Site map of gerriscorp.com: every page, with a summary",
    "description": "A complete map of gerriscorp.com: every service, guide, and case study by Chris Abraham at Gerris Corp, grouped by section with a one line summary.",
    "body": site_map_body()}))


# The site index: a back-of-the-book index of every page, written by hand in tools/site_index.json.
# Each heading maps to {kind, pages, main, subs, see}; pages are source paths ("home", "guides/llms-txt"),
# and "main" marks the pages devoted to the subject, shown in bold. "reviewed" lists every page already
# indexed, so a page added later shows up below as not indexed yet until someone reads it and adds its entries.
SITE_INDEX = json.load(open("tools/site_index.json", encoding="utf-8"))
_src_page = {("home" if q["src"] == "index" else q["src"][:-6] if q["src"].endswith("/index") else q["src"]): q for q in pages if q["src"] != "(generated)"}
_order = {k: i for i, k in enumerate(_src_page)}
unindexed = [k for k in _src_page if k not in SITE_INDEX["reviewed"]]


def site_index_body():
    e = html.escape
    sort_key = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower().replace("ʻ", ""))
    slug = lambda s: "ix-" + re.sub(r"[^a-z0-9]+", "-", sort_key(s)).strip("-")
    def locs(keys, main=()):
        keys = sorted((k for k in keys if k in _src_page), key=_order.get)
        out = []
        for k in keys:
            q = _src_page[k]
            a = f'<a href="{{root}}{q["path"]}" title="{e(q["h1"])}">{e(q["name"])}</a>'
            out.append(f"<strong>{a}</strong>" if k in main else a)
        return ", ".join(out)
    def see(targets, also):
        if not targets:
            return ""
        links = "; ".join(f'<a href="#{slug(t)}">{e(t)}</a>' for t in sorted(targets, key=sort_key))
        return (f". <em>See also</em> {links}" if also else f". <em>See</em> {links}")
    entries = sorted(SITE_INDEX["entries"].items(), key=lambda kv: sort_key(kv[0]))
    groups = {}
    for head, v in entries:
        first = sort_key(head)[:1]
        groups.setdefault("0–9" if first.isdigit() else first.upper(), []).append((head, v))
    letters = list(groups)
    out = ['<h1>Index</h1>',
           '<p class="lead">Reference books end with an index, and so does this site. I went through every page, from the services to the '
           f'case studies, and recorded each person, company, tool, standard, and problem it discusses: {len(entries):,} headings drawn from {len(_src_page)} pages. '
           'A locator is a page\'s short name; bold marks the page that treats the subject in full, and hovering shows the page\'s whole title.</p>',
           '<p>Names of people run surname first, and "See also" leads to neighboring headings. Short definitions live in the '
           '<a href="{root}guides/glossary/">glossary</a>, and the <a href="{root}sitemap/">site map</a> lists every page by section.</p>',
           '<nav class="index-letters" id="index-letters" aria-label="Jump to a letter"><p>'
           + " ".join(f'<a href="#ix-letter-{x[0].lower()}">{x}</a>' if x in groups else f'<span class="index-empty" title="No headings under {x}">{x}</span>'
                      for x in ["0–9"] + [chr(c) for c in range(65, 91)]) + '</p></nav>']
    for letter in letters:
        out.append(f'<h2 id="ix-letter-{letter[0].lower()}">{letter}</h2>\n<ul class="site-index">')
        for head, v in groups[letter]:
            line = f'  <li id="{slug(head)}">{e(head)}'
            main_locs = locs(v["pages"], v.get("main", ()))
            if main_locs:
                line += ", " + main_locs
            line += see(v["see"], bool(main_locs or v["subs"]))
            if v["subs"]:
                line += "\n    <ul>" + "".join(
                    f'\n      <li>{e(s)}, {locs(ks)}</li>'
                    for s, ks in sorted(v["subs"].items(), key=lambda kv: sort_key(kv[0])) if locs(ks)) + "\n    </ul>"
            out.append(line + "</li>")
        out.append('</ul>\n<p class="index-top"><a href="#index-letters">Back to the letters</a></p>')
    return "\n".join(out)


pages.append(finish({
    "name": "Index", "src": "(generated)", "path": "site-index/", "tab": "site-index/", "kind": "page",
    "title": "Index of the people, tools, and problems on Gerris Corp",
    "description": "An A to Z index of gerriscorp.com: the people, companies, tools, standards, and technical problems the pages cover, with links to every page on each one.",
    "body": site_index_body()}))
by_path = {p["path"]: p for p in pages}
guides = [p for p in pages if p["kind"] == "guide"]

CSS = """
:root { --orange: #c75000; --blue: #16729e; --teal: #237482; --text: #000; --muted: #333; --link: #284a57; --tab: #8cacbb; --bar: #dee7ec; --rule: #c8d3d8; --bg: #fff; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
body { margin: 0; color: var(--text); background: var(--bg); font: 18px/1.65 Verdana, "Lucida Grande", Lucida, "DejaVu Sans", Helvetica, Arial, sans-serif; }
.wrap { max-width: 46rem; margin: 0 auto; padding: 0 1rem; }
a { color: var(--link); text-decoration: underline; text-underline-offset: .15em; overflow-wrap: anywhere; }
a:hover { text-decoration-thickness: 2px; }
:focus-visible { outline: 3px solid #000; outline-offset: 2px; }
img { max-width: 100%; height: auto; }
.skip { position: absolute; left: -999px; }
.skip:focus { left: 1rem; top: .5rem; background: #fff; padding: .5rem; z-index: 1; }
.top { display: flex; align-items: center; gap: .9rem; padding: 1.25rem 0 .9rem; }
.top > a { flex: none; line-height: 0; }
.top img { width: 64px; height: 64px; max-width: none; }
.brand { font-size: 1.6rem; font-weight: bold; color: var(--orange); text-decoration: none; }
.brand:hover { text-decoration: underline; }
.tag { margin: 0; color: var(--muted); font-size: .95rem; line-height: 1.4; }
nav { border-bottom: 4px solid var(--bar); }
nav ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: .3rem; }
nav li { margin: 0; }
nav a { display: block; padding: .4rem .7rem; border: 1px solid var(--tab); border-bottom: none; text-decoration: none; font-size: .9rem; white-space: nowrap; }
nav a:hover { background: var(--bar); text-decoration: underline; }
nav a[aria-current] { background: var(--bar); color: #000; font-weight: bold; }
.crumbs { font-size: .9rem; margin: 1rem 0 0; color: var(--muted); }
main { padding: 1.25rem 0 2rem; }
h1 { color: var(--blue); font-size: 1.4rem; line-height: 1.25; margin: .25rem 0 1rem; }
h2 { color: var(--teal); font-size: 1.3rem; line-height: 1.3; margin: 2rem 0 .5rem; }
h3 { font-size: 1.08rem; line-height: 1.35; margin: 1.5rem 0 .4rem; }
p, ul, ol, dl, table { margin: 0 0 1rem; }
li { margin-bottom: .4rem; }
.lead { font-size: 1.1rem; }
.byline { color: var(--muted); font-size: .9rem; margin-top: -.5rem; }
.updated { color: var(--muted); font-size: .9rem; margin-top: 2rem; }
code { font-family: Consolas, Menlo, monospace; font-size: .92em; background: #f2f5f7; padding: 0 .2em; }
pre { background: #f2f5f7; padding: .75rem; overflow-x: auto; font-size: .9rem; line-height: 1.45; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; font-size: .95rem; }
th, td { border: 1px solid var(--rule); padding: .4rem .55rem; text-align: left; vertical-align: top; }
th { background: var(--bar); }
dt { font-weight: bold; margin-top: 1rem; }
dd { margin: .2rem 0 0 0; }
.logo-full { margin: 1rem 0 1.5rem; text-align: center; }
.logo-full img { width: 700px; }
.logo-full figcaption { font-size: .85rem; color: var(--muted, #555); margin-top: .5rem; }
.logo-inline { float: right; width: 220px; margin: .25rem 0 1rem 1.25rem; }
.portrait { float: right; width: 160px; height: 160px; margin: .25rem 0 1rem 1.25rem; border: 1px solid var(--rule); }
.button { display: inline-block; margin: 0 .5rem .6rem 0; padding: .6rem 1.1rem; border: 2px solid var(--link); background: var(--bar); color: #000; font-weight: bold; text-decoration: none; }
.button:hover { text-decoration: underline; }
.author-box { display: flex; gap: 1rem; align-items: flex-start; border-top: 1px solid var(--rule); margin-top: 2rem; padding-top: 1rem; font-size: .95rem; }
.author-box img { width: 72px; height: 72px; flex: none; border: 1px solid var(--rule); }
.author-box p { margin: 0; }
.help-box { border: 2px solid var(--rule); margin-top: 2rem; padding: .25rem 1rem 1rem; }
.help-box h2 { margin-top: .75rem; }
.related { border-top: 1px solid var(--rule); margin-top: 2rem; padding-top: .5rem; }
.guide-contents { border: 1px solid var(--rule); margin: 1.5rem 0; padding: .65rem .85rem; font-size: .95rem; }
.guide-contents summary { color: var(--link); cursor: pointer; font-weight: bold; }
.guide-contents ol { margin: .75rem 0 .25rem; padding-left: 1.5rem; }
.guide-contents li { margin-bottom: .35rem; }
h2[id] { scroll-margin-top: 1rem; }
.contact li { margin-bottom: .6rem; }
.index-letters { position: sticky; top: 0; z-index: 1; background: var(--bg); border-bottom: 1px solid var(--rule); margin: 0 0 1rem; }
.index-letters p { margin: 0; padding: .35rem 0; font-size: 1.05rem; display: flex; flex-wrap: wrap; gap: .1rem .2rem; }
.index-letters a, .index-letters span { display: inline-block; min-width: 1.9rem; min-height: 1.9rem; line-height: 1.9rem; text-align: center; }
.index-letters .index-empty { color: #767676; }
.index-top { font-size: .9rem; margin: -.4rem 0 1.25rem; }
[id^="ix-"] { scroll-margin-top: 4.5rem; }
ul.site-index { list-style: none; padding: 0; }
ul.site-index > li { margin-bottom: .35rem; padding-left: 1.5rem; text-indent: -1.5rem; }
ul.site-index ul { list-style: none; padding-left: 1.5rem; margin: .15rem 0 .3rem; }
ul.site-index ul li { margin-bottom: .15rem; text-indent: -1rem; padding-left: 1rem; }
.site-footer { border-top: 1px solid var(--rule); padding: 1rem 0 2.5rem; color: var(--muted); font-size: .9rem; }
.site-footer p { margin: 0 0 .4rem; }
@media (max-width: 34rem) {
  body { font-size: 17px; }
  .top img { width: 52px; height: 52px; }
  nav a { padding: .45rem .55rem; }
  h1 { font-size: 1.25rem; }
  .portrait { width: 112px; height: 112px; margin-left: 1rem; }
}
""".strip()

KNOWS = ["Technical consulting", "Developer specifications", "AI-assisted software development", "OpenAI Codex", "Claude Code", "GitHub Copilot", "Gemini", "Grok", "Perplexity",
         "Git", "Linux server administration", "Technical SEO", "JavaScript SEO", "Indexing",
         "Website migrations", "301 redirects", "Core Web Vitals", "Cloudflare", "Structured data",
         "Answer engine optimization", "Generative engine optimization", "llms.txt",
         "Online reputation management", "Data broker removal", "Google Business Profile", "SPF", "DKIM", "DMARC"]
ENGLISH_SPEAKING = [("Country", "United States", "US"), ("Country", "Canada", "CA"), ("Country", "United Kingdom", "GB"),
                    ("Country", "Ireland", "IE"), ("Country", "Australia", "AU"), ("Country", "New Zealand", "NZ")]
AREA_SERVED = ([{"@type": "AdministrativeArea", "name": "Washington, DC metropolitan area"},
                {"@type": "State", "name": "Virginia", "containedInPlace": {"@type": "Country", "name": "United States"}}]
               + [{"@type": t, "name": n, "identifier": c} for t, n, c in ENGLISH_SPEAKING]
               + ["Worldwide"])
ADDRESS = {"@type": "PostalAddress", "addressLocality": "Arlington", "addressRegion": "VA", "postalCode": "22204",
           "addressCountry": "US"}
HOME = {"@type": "Place", "@id": SITE + "#place", "name": "South Arlington, Arlington, Virginia",
        "alternateName": ["Arlington Heights, Arlington, Virginia", "Arlington, VA 22204"],
        "address": ADDRESS, "geo": {"@type": "GeoCoordinates", "latitude": 38.86, "longitude": -77.10},
        "containedInPlace": {"@type": "AdministrativeArea", "name": "Arlington County, Virginia",
                             "containedInPlace": {"@type": "State", "name": "Virginia"}}}
ORG = {
    "@type": "ProfessionalService", "@id": SITE + "#org", "name": "Gerris Corp",
    "alternateName": ["Gerris"], "url": SITE, "logo": SITE + "logo.png", "image": SITE + "social-card.png",
    "description": "Chris Abraham's consultancy: fractional technical leadership, developer specs and QA, AI tools built with OpenAI Codex and Claude Code, project rescue, technical SEO, site speed, migrations, AI search visibility, and reputation management.",
    "foundingDate": "2012", "founder": {"@id": AUTHOR}, "employee": {"@id": AUTHOR},
    "slogan": "Experienced help for the digital work your business needs done",
    "email": EMAIL, "telephone": "+1-202-352-5051",
    "address": ADDRESS, "location": {"@id": SITE + "#place"},
    "geo": HOME["geo"], "areaServed": AREA_SERVED, "knowsLanguage": "en", "knowsAbout": KNOWS,
    "numberOfEmployees": {"@type": "QuantitativeValue", "value": 1},
    "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": EMAIL, "telephone": "+1-202-352-5051",
                      "areaServed": [c for _, _, c in ENGLISH_SPEAKING], "availableLanguage": "English"},
                     {"@type": "ContactPoint", "contactType": "technical support", "email": EMAIL,
                      "telephone": "+1-202-352-5051", "availableLanguage": "English"}],
    "sameAs": ["https://www.upwork.com/freelancers/chrisjabraham", "https://github.com/chrisabraham/gerriscorp",
               "https://share.google/C5KMu0jYTNz8t2Zpn"],  # verified Google Business Profile "Gerris"
    "publishingPrinciples": SITE + "standards/",
}
PERSON = {
    "@type": "Person", "@id": AUTHOR, "name": "Chris Abraham", "alternateName": "Christopher Abraham",
    "image": {"@type": "ImageObject", "url": SITE + "chris-abraham.jpg", "width": 320, "height": 320,
              "caption": "Chris Abraham, founder of Gerris Corp"},
    "url": "https://chrisabraham.com/", "jobTitle": "Founder and principal consultant",
    "worksFor": {"@id": SITE + "#org"},
    "alumniOf": [{"@type": "CollegeOrUniversity", "name": "The George Washington University",
                  "sameAs": "https://en.wikipedia.org/wiki/George_Washington_University"},
                 {"@type": "CollegeOrUniversity", "name": "University of East Anglia",
                  "sameAs": "https://en.wikipedia.org/wiki/University_of_East_Anglia"}],
    "homeLocation": {"@id": SITE + "#place"}, "workLocation": {"@id": SITE + "#place"},
    "nationality": {"@type": "Country", "name": "United States"}, "knowsLanguage": "en",
    "hasOccupation": {"@type": "Occupation", "name": "Technical consultant and technical SEO specialist",
                      "occupationLocation": {"@type": "Country", "name": "United States"},
                      "skills": "Technical SEO, developer specifications, OpenAI Codex, Claude Code, GitHub Copilot, Git, Linux, Cloudflare, migrations, AI search"},
    "knowsAbout": KNOWS,
    "email": EMAIL, "telephone": "+1-202-352-5051",
    "sameAs": ["https://chrisabraham.com/", "https://www.upwork.com/freelancers/chrisjabraham", "https://hillmole.com/", "https://mastodon.social/@chrisa",
               "https://adage.com/author/chris-abraham/1797"],
}
WEBSITE = {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Gerris Corp",
           "alternateName": "Gerris", "inLanguage": "en-US", "publisher": {"@id": SITE + "#org"},
           "publishingPrinciples": SITE + "standards/"}


ORG["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": "Gerris Corp services", "itemListElement": [
    {"@type": "OfferCatalog", "name": title, "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "@id": SITE + path + "#service", "name": by_path[path]["h1"],
                                           "url": SITE + path}} for path in paths]}
    for title, paths in SERVICE_GROUPS]}


def trail(p):
    out = [by_path[""]]
    if p["tab"] and p["tab"] != p["path"] and p["tab"] in by_path:
        out.append(by_path[p["tab"]])
    if p["path"]:
        out.append(p)
    return out


def schema(p):
    page_type = {"about/": "AboutPage", "contact/": "ContactPage", "faq/": "FAQPage",
                 "guides/": "CollectionPage", "services/": "CollectionPage", "case-studies/": "CollectionPage"}.get(p["path"], "WebPage")
    page = {"@type": page_type, "@id": p["url"] + "#webpage", "url": p["url"], "name": p["title"],
            "description": p["description"], "isPartOf": {"@id": SITE + "#website"},
            "about": {"@id": SITE + "#org"}, "primaryImageOfPage": SITE + "social-card.png",
            "inLanguage": "en-US", "dateModified": p["updated"], "author": {"@id": AUTHOR}}
    graph = [WEBSITE, ORG, PERSON, HOME, page]
    if p["path"]:
        page["breadcrumb"] = {"@id": p["url"] + "#breadcrumb"}
        graph.append({"@type": "BreadcrumbList", "@id": p["url"] + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": q["name"], "item": q["url"]}
            for i, q in enumerate(trail(p))]})
    if p["kind"] == "service":
        graph.append({"@type": "Service", "@id": p["url"] + "#service", "name": p["h1"],
                      "serviceType": p["name"], "description": p["description"],
                      "provider": {"@id": SITE + "#org"}, "areaServed": AREA_SERVED, "url": p["url"],
                      "availableChannel": {"@type": "ServiceChannel", "serviceUrl": SITE + "contact/",
                                           "servicePhone": "+1-202-352-5051", "availableLanguage": "English"}})
        page["mainEntity"] = {"@id": p["url"] + "#service"}
    if p["kind"] == "case":
        graph.append({"@type": "Article", "@id": p["url"] + "#article", "headline": p["h1"], "articleSection": "Case studies",
                      "description": p["description"], "url": p["url"], "mainEntityOfPage": {"@id": p["url"] + "#webpage"},
                      "author": {"@id": AUTHOR}, "publisher": {"@id": SITE + "#org"},
                      "datePublished": p.get("published", p["updated"]), "dateModified": p["updated"],
                      "image": SITE + "social-card.png", "inLanguage": "en-US", "wordCount": p["words"],
                      "citation": [{"@type": "CreativeWork", "name": label, "url": u} for label, u in p["sources"]]})
        page["mainEntity"] = {"@id": p["url"] + "#article"}
    if p["kind"] == "guide":
        graph.append({"@type": "TechArticle", "@id": p["url"] + "#article", "headline": p["h1"],
                      "description": p["description"], "url": p["url"], "mainEntityOfPage": {"@id": p["url"] + "#webpage"},
                      "author": {"@id": AUTHOR}, "publisher": {"@id": SITE + "#org"},
                      "datePublished": p.get("published", p["updated"]), "dateModified": p["updated"],
                      "image": SITE + "social-card.png", "inLanguage": "en-US", "wordCount": p["words"],
                      "citation": [{"@type": "CreativeWork", "name": label, "url": u} for label, u in p["sources"]]})
    if p["kind"] == "guide":
        art = graph[-1]
        if p["ent_about"]: art["about"] = p["ent_about"]
        if p["ent_mentions"]: art["mentions"] = p["ent_mentions"]
        if p.get("keywords"): art["keywords"] = p["keywords"]
    if page_type == "CollectionPage":
        kids = [q for q in pages if q["tab"] == p["path"] and q is not p]
        page["mainEntity"] = {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": q["url"], "name": q["h1"]} for i, q in enumerate(kids)]}
    if p["faq"]:
        node = page if page_type == "FAQPage" else {"@type": "FAQPage", "@id": p["url"] + "#faq"}
        node["mainEntity"] = [{"@type": "Question", "name": text_of(q),
                               "acceptedAnswer": {"@type": "Answer", "text": text_of(a)}} for q, a in p["faq"]]
        if node is not page:
            graph.append(node)
    if p["terms"]:
        graph.append({"@type": "DefinedTermSet", "@id": p["url"] + "#terms", "name": p["h1"], "hasDefinedTerm": [
            {"@type": "DefinedTerm", "@id": f'{p["url"]}#{tid}', "name": text_of(term), "description": text_of(d),
             "url": f'{p["url"]}#{tid}', "inDefinedTermSet": {"@id": p["url"] + "#terms"}} for tid, term, d in p["terms"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)


def body_html(p, *, contents=True):
    r = p["root"] or "./"
    body = p["body"].replace("{root}", r)
    if p["kind"] == "guide" and contents:
        body = add_guide_contents(body, p["words"])
    if p["kind"] == "guide":
        by = (f'<p class="byline">By <a href="{r}about/">Chris Abraham</a> · Published <time datetime="{p.get("published", p["updated"])}">{nice(p.get("published", p["updated"]))}</time>'
              + (f' · Updated <time datetime="{p["updated"]}">{nice(p["updated"])}</time>' if p.get("published", p["updated"]) != p["updated"] else "") + "</p>")
        body = re.sub(r"(</h1>)", r"\1\n" + by, body, count=1)
    if p["kind"] == "guide":
        body += f"""
<aside class="help-box" aria-label="Get help">
  <h2>Want me to handle this for you?</h2>
  <p>This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.</p>
  <p><a class="button" href="https://calendly.com/chrisabraham/30">Book a 30 minute call</a> <a class="button" href="tel:{TEL}">Call {PHONE}</a> <a class="button" href="mailto:{EMAIL}">Email {EMAIL}</a></p>
  <p>If your company hires through Upwork, you'll find me <a href="https://www.upwork.com/freelancers/chrisjabraham">there as well</a>.</p>
</aside>"""
    if p["sources"]:
        body += ('\n<h2>References</h2>\n<ul class="sources">\n'
                 + "".join(f'  <li><a href="{u}">{html.escape(label)}</a></li>\n' for label, u in p["sources"]) + "</ul>")
    if p["kind"] in ("guide", "case"):
        body += f"""
<aside class="author-box" aria-label="About the author">
  <img src="{r}chris-abraham.jpg" width="72" height="72" alt="">
  <p>Written by <a href="{r}about/">Chris Abraham</a>, founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. <a href="{r}standards/">Editorial standards</a> · <a href="https://www.upwork.com/freelancers/chrisjabraham">Upwork profile</a></p>
</aside>"""
    if p["kind"] != "guide":
        body += f'\n<p class="updated">Updated <time datetime="{p["updated"]}">{nice(p["updated"])}</time></p>'
    # Header cells announce their row or column to screen readers.
    body = re.sub(r"<thead>(.*?)</thead>", lambda m: m.group(0).replace("<th>", '<th scope="col">'), body, flags=re.S)
    return body.replace("<th>", '<th scope="row">')


# Google Analytics 4. Consent mode: ads storage denied everywhere; analytics storage
# denied in the UK and EEA (cookieless pings there), granted elsewhere. See /privacy/.
GA_ID = "G-JF2W6ESJZN"
_EEA_UK = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU",
           "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "IS", "LI", "NO", "GB", "CH"]
GA = f"""
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('consent', 'default', {{ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'granted'}});
  gtag('consent', 'default', {{analytics_storage: 'denied', region: {json.dumps(_EEA_UK)}}});
  // Global Privacy Control or Do Not Track turns analytics cookies off anywhere.
  if (navigator.globalPrivacyControl === true || navigator.doNotTrack === '1') gtag('consent', 'default', {{analytics_storage: 'denied'}});
  gtag('js', new Date());
  gtag('config', '{GA_ID}', {{allow_google_signals: false, allow_ad_personalization_signals: false}});
  (function () {{
    // gtag.js loads on the first scroll, tap, or key, or 4 seconds after the page loads,
    // so it never competes with the page itself. The commands above wait in dataLayer.
    var done = false;
    function load() {{
      if (done) return;
      done = true;
      var s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id={GA_ID}';
      document.head.appendChild(s);
    }}
    ['pointerdown', 'keydown', 'scroll', 'touchstart'].forEach(function (e) {{ addEventListener(e, load, {{once: true, passive: true}}); }});
    addEventListener('load', function () {{ setTimeout(load, 4000); }});
  }})();
</script>""" if LIVE else ""

# Chrome prefetches a same-site page when a reader hovers or starts to tap its link,
# so the next page opens at once. Markdown, text, and XML files are left alone.
RELME = '\n<link rel="me" href="https://mastodon.social/@chrisa">'  # Mastodon profile verification
SPECULATION = """
<script type="speculationrules">{"prefetch": [{"where": {"and": [{"href_matches": "/*"}, {"not": {"href_matches": ["/*.md", "/*.txt", "/*.xml"]}}]}, "eagerness": "moderate"}]}</script>"""


# Meta keywords: ignored by Google since 2009 and kept here for old time's sake.
# A few honest terms per page: its topic, its section, and who wrote it.
KEYWORDS_HOME = "technical SEO consultant, technical consulting, AI search, Cloudflare, Google Search Console, Arlington Virginia"
KEYWORDS_SECTION = {"services/": "technical SEO consultant", "guides/": "SEO guide", "case-studies/": "SEO case study"}

def keywords(p):
    if p.get("keywords"):
        return p["keywords"]
    if p["path"] == "":
        return KEYWORDS_HOME + ", Gerris Corp, Chris Abraham"
    own = [p["name"]] if p["kind"] in ("service", "guide", "case") else []
    terms = own + [KEYWORDS_SECTION.get(p["tab"], "technical SEO consultant"), "Gerris Corp", "Chris Abraham"]
    return ", ".join(dict.fromkeys(terms))

def render(p):
    r = p["root"]
    home = r or "./"
    e = lambda s: html.escape(s, quote=True)
    nav = "\n".join(
        f'    <li><a href="{(r + path) or "./"}"{(" aria-current=" + chr(34) + ("page" if path == p["path"] else "true") + chr(34)) if path == p["tab"] else ""}>{label}</a></li>'
        for path, label in TABS)
    crumbs = ""
    if p["path"] and p["tab"] != p["path"] and p["tab"] in by_path:
        crumbs = ('\n<p class="crumbs">' + " › ".join(f'<a href="{(r + q["path"]) or "./"}">{q["name"]}</a>' for q in trail(p)[:-1])
                  + f' › {p["name"]}</p>')
    robots = "" if LIVE else '\n<meta name="robots" content="noindex">'
    og_type = "article" if p["kind"] == "guide" else "website"
    article = ""
    if p["kind"] == "guide":
        article = (f'\n<meta property="article:published_time" content="{p.get("published", p["updated"])}">'
                   f'\n<meta property="article:modified_time" content="{p["updated"]}">'
                   '\n<meta property="article:author" content="https://chrisabraham.com/">')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["description"])}">{robots}
<meta name="keywords" content="{e(keywords(p))}">
<link rel="canonical" href="{p["url"]}">
<meta name="author" content="Chris Abraham">
<meta name="msvalidate.01" content="2E8EA11035C27E2B7C82A165FA698E0C">
<link rel="icon" href="{r}logo.png" type="image/png">
<link rel="apple-touch-icon" href="{r}logo.png">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="alternate" type="text/markdown" title="This page as Markdown" href="index.md">
<link rel="alternate" type="application/rss+xml" title="Gerris guides (RSS)" href="{r}rss.xml">
<link rel="alternate" type="application/atom+xml" title="Gerris guides" href="{r}feed.xml">
<link rel="alternate" type="text/plain" title="llms.txt" href="{r}llms.txt">
<link rel="sitemap" type="application/xml" href="{r}sitemap.xml">
<meta name="theme-color" content="#ffffff">{GA}{SPECULATION}{RELME}
<meta property="og:site_name" content="Gerris Corp">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(p["title"])}">
<meta property="og:description" content="{e(p["description"])}">
<meta property="og:url" content="{p["url"]}">
<meta property="og:image" content="{SITE}social-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The Gerris logo, a sketched water strider">{article}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(p["title"])}">
<meta name="twitter:description" content="{e(p["description"])}">
<meta name="twitter:image" content="{SITE}social-card.png">
<style>
{CSS}
</style>
<script type="application/ld+json">
{schema(p)}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
<header class="top">
  <a href="{home}"><img src="{r}logo-128.png" width="64" height="64" alt="Gerris home" fetchpriority="high"></a>
  <div>
    <a class="brand" href="{home}">Gerris</a>
    <p class="tag">Chris Abraham: technical consulting, AI tools, and technical SEO</p>
  </div>
</header>
<nav aria-label="Site">
  <ul>
{nav}
  </ul>
</nav>{crumbs}
<main id="main">
{body_html(p)}
</main>
<footer class="site-footer">
  <p><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{TEL}">{PHONE}</a> · <a href="https://calendly.com/chrisabraham/30">Book a call</a> · <a href="https://www.upwork.com/freelancers/chrisjabraham">Upwork</a></p>
  <p>© {TODAY[:4]} Gerris Corp, Arlington, Virginia · <a href="{r}faq/">FAQ</a> · <a href="{r}standards/">Standards</a> · <a href="{r}privacy/">Privacy</a> · <a href="{r}sitemap/">Site map</a> · <a href="{r}site-index/">Index</a> · <a href="{r}guides/glossary/">Glossary</a> · <a href="{r}colophon/">Colophon</a> · <a href="{r}llms.txt">llms.txt</a> · <a href="{r}rss.xml">RSS</a> · <a href="https://chrisabraham.com/">chrisabraham.com</a></p>
</footer>
</div>
</body>
</html>
"""


class Markdown(HTMLParser):
    """A page body as Markdown with absolute links, for index.md and llms-full.txt."""
    BLOCK = {"p": "\n\n", "h1": "\n\n# ", "h2": "\n\n## ", "h3": "\n\n### ", "pre": "\n\n```\n",
             "dt": "\n\n**", "dd": "\n", "tr": "\n|", "blockquote": "\n\n> "}

    def __init__(self, base):
        super().__init__(); self.base = base; self.out = []; self.href = None
        self.lists = []; self.pre = False
    def handle_starttag(self, t, a):
        a = dict(a)
        if t in self.BLOCK:
            self.out.append(self.BLOCK[t]); self.pre = self.pre or t == "pre"
        elif t in ("ul", "ol"): self.lists.append([t, 0])
        elif t == "li":
            self.lists[-1][1] += 1
            self.out.append("\n" + "  " * (len(self.lists) - 1) + ("- " if self.lists[-1][0] == "ul" else f"{self.lists[-1][1]}. "))
        elif t in ("strong", "b"): self.out.append("**")
        elif t in ("em", "i"): self.out.append("*")
        elif t == "code" and not self.pre: self.out.append("`")
        elif t in ("td", "th"): self.out.append(" ")
        elif t == "a": self.href = a.get("href"); self.out.append("[")
    def handle_endtag(self, t):
        if t in ("ul", "ol"): self.lists.pop(); self.out.append("\n")
        elif t in ("strong", "b"): self.out.append("**")
        elif t in ("em", "i"): self.out.append("*")
        elif t == "code" and not self.pre: self.out.append("`")
        elif t == "pre": self.out.append("\n```"); self.pre = False
        elif t == "dt": self.out.append("**")
        elif t in ("td", "th"): self.out.append(" |")
        elif t == "thead": self.out.append("\n|" + " --- |" * self._cols())
        elif t == "a" and self.href is not None:
            h = self.href
            if h.startswith("#"): h = self.base + h
            elif not re.match(r"https?:|mailto:|tel:", h): h = SITE + re.sub(r"^(\.\./|\./)+", "", h)
            self.out.append(f"]({h})"); self.href = None
    def _cols(self):
        tail = "".join(self.out)
        return tail[tail.rfind("\n|"):].count("|") - 1
    def handle_data(self, d):
        self.out.append(d if self.pre else re.sub(r"\s+", " ", d))


def markdown(p):
    m = Markdown(p["url"])
    m.feed(body_html(p, contents=False).replace('href="' + (p["root"] or "./"), 'href="'))
    text = re.sub(r"[ \t]+\n", "\n", "".join(m.out))
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# ---- write ----
for p in pages:
    os.makedirs(p["path"] or ".", exist_ok=True)
    open(os.path.join(p["path"], "index.html"), "w", encoding="utf-8").write(render(p))
    # No YAML front matter: Jekyll would convert the file to HTML instead of serving it as Markdown.
    md = (f"> {p['description']}\n>\n> Source: {p['url']} · Updated {p['updated']} · By Chris Abraham, Gerris Corp\n\n"
          + markdown(p) + "\n")
    open(os.path.join(p["path"], "index.md"), "w", encoding="utf-8").write(md)

# Redirects for URLs from the old gerriscorp.com (src/redirects.tsv: old path, target).
# GitHub Pages can't send server 301s, so each old path gets a tiny page with an instant
# meta refresh and a canonical, which Google and Bing treat as a permanent redirect.
redirects = 0
for line in open("src/redirects.tsv", encoding="utf-8"):
    old, target = line.rstrip("\n").split("\t")
    rel = old.strip("/")
    if not rel or rel.rstrip("/") + "/" in by_path:
        continue
    url = target if target.startswith("http") else SITE + target.lstrip("/")
    if not target.startswith("http") and target.lstrip("/") not in by_path:
        print("PROBLEM: redirect target missing:", old, "->", target)
    os.makedirs(rel, exist_ok=True)
    open(os.path.join(rel, "index.html"), "w", encoding="utf-8").write(
        f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>'
        f'<link rel="canonical" href="{url}"><meta http-equiv="refresh" content="0; url={url}">'
        f'<meta name="robots" content="noindex"></head><body><p>This page has moved to <a href="{url}">{url}</a>.</p></body></html>\n')
    redirects += 1
print(f"{redirects} redirect pages written")

base = SITE if LIVE else PREVIEW_BASE
open("404.html", "w", encoding="utf-8").write(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found: Gerris</title>
<meta name="robots" content="noindex">
<style>
{CSS}
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <a href="{base}"><img src="{base}logo-128.png" width="64" height="64" alt="Gerris home"></a>
  <div><a class="brand" href="{base}">Gerris</a></div>
</header>
<main id="main">
<h1>Page not found</h1>
<p>That page isn't here. Try the <a href="{base}">home page</a>, the <a href="{base}services/">services</a>, the <a href="{base}guides/">guides</a>, the <a href="{base}sitemap/">site map</a>, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</main>
</div>
<script>
// Old Squarespace blog and podcast URLs not listed in src/redirects.tsv (tags, archives) go to their new homes.
(function () {{
  var p = location.pathname;
  var t = /^\\/blog(\\/|$)/.test(p) ? "https://chrisabraham.com/blog" :
          /^\\/podcast(\\/|$)/.test(p) ? "https://chrisabraham.com/thechrisabrahamshow" : "";
  if (t) location.replace(t);
}})();
</script>
</body>
</html>
""")


def sitemap_entry(p):
    img = ""
    if p["path"] == "":
        img = (f"\n    <image:image><image:loc>{SITE}logo.png</image:loc></image:image>"
               f"\n    <image:image><image:loc>{SITE}social-card.png</image:loc></image:image>")
    if p["path"] == "about/":
        img = f"\n    <image:image><image:loc>{SITE}chris-abraham.jpg</image:loc></image:image>"
    return f"  <url>\n    <loc>{p['url']}</loc>\n    <lastmod>{p['updated']}</lastmod>{img}\n  </url>\n"


open("sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="sitemap.xsl"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    + "".join(sitemap_entry(p) for p in pages) + "</urlset>\n")
open("sitemap.xsl", "w", encoding="utf-8").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="robots" content="noindex"/>
<title>XML sitemap: Gerris Corp</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<main id="main">
<h1>XML sitemap</h1>
<p class="lead">This is the sitemap search engines read for gerriscorp.com: <xsl:value-of select="count(s:urlset/s:url)"/> pages, each with the date it last changed. People may prefer the <a href="sitemap/">site map with summaries</a>.</p>
<table>
<thead><tr><th>Page</th><th>Last changed</th></tr></thead>
<tbody>
<xsl:for-each select="s:urlset/s:url">
<tr><td><a href="{{s:loc}}"><xsl:value-of select="s:loc"/></a></td><td><xsl:value-of select="s:lastmod"/></td></tr>
</xsl:for-each>
</tbody>
</table>
</main>
</div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
""")

open("robots.txt", "w", encoding="utf-8").write("""# Search engines and AI assistants are welcome to read and cite everything here.
#
# Search engines get the HTML pages only. The Markdown twins (index.md),
# llm.txt, and llms-full.txt repeat the HTML word for word, so search
# indexes skip them to avoid duplicate-content reports. AI assistants,
# which read them in place of HTML, get everything.
User-agent: *
Allow: /

User-agent: Googlebot
User-agent: Bingbot
User-agent: Applebot
User-agent: DuckDuckBot
User-agent: YandexBot
Allow: /
Disallow: /*.md$
Disallow: /llm.txt
Disallow: /llms-full.txt

User-agent: GPTBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: Amazonbot
User-agent: DuckAssistBot
User-agent: MistralAI-User
User-agent: CCBot
User-agent: GoogleOther
User-agent: Google-CloudVertexBot
User-agent: Google-Agent
User-agent: Google-GeminiNotebook
User-agent: meta-webindexer
User-agent: meta-externalagent
User-agent: meta-externalfetcher
User-agent: Amzn-SearchBot
User-agent: Amzn-User
Allow: /

Sitemap: https://gerriscorp.com/sitemap.xml
""")

# Feed bodies travel outside the site, so every local resource needs an absolute URL.
from urllib.parse import urljoin

def feed_body(p):
    body = body_html(p, contents=False)
    return re.sub(r'(href|src)="([^"]+)"',
                  lambda m: m[1] + '="' + html.escape(urljoin(p["url"], html.unescape(m[2])), quote=True) + '"', body)

guides = sorted(guides, key=lambda p: (p["updated"], p.get("published", p["updated"]), p["url"]), reverse=True)

esc = lambda s: html.escape(s, quote=False)
newest = max(p["updated"] for p in guides)
open("feed.xml", "w", encoding="utf-8").write(
    f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Gerris guides</title>
  <subtitle>Technical SEO, AI search, migration, email, and privacy guides by Chris Abraham</subtitle>
  <link href="{SITE}feed.xml" rel="self"/>
  <link href="{SITE}guides/"/>
  <id>{SITE}guides/</id>
  <updated>{newest}T12:00:00Z</updated>
  <author><name>Chris Abraham</name><uri>https://chrisabraham.com/</uri></author>
""" + "".join(f"""  <entry>
    <title>{esc(p["h1"])}</title>
    <link href="{p["url"]}"/>
    <id>{p["url"]}</id>
    <published>{p.get("published", p["updated"])}T12:00:00Z</published>
    <updated>{p["updated"]}T12:00:00Z</updated>
    <summary>{esc(p["description"])}</summary>
    <content type="html">{esc(feed_body(p))}</content>
  </entry>
""" for p in guides) + "</feed>\n")

rfc822 = lambda d: datetime.date.fromisoformat(d).strftime("%a, %d %b %Y 12:00:00 +0000")
open("rss.xml", "w", encoding="utf-8").write(
    f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/">
<channel>
  <title>Gerris guides</title>
  <link>{SITE}guides/</link>
  <description>Technical SEO, AI search, migration, email, and privacy guides by Chris Abraham</description>
  <language>en-us</language>
  <lastBuildDate>{rfc822(newest)}</lastBuildDate>
  <atom:link href="{SITE}rss.xml" rel="self" type="application/rss+xml"/>
""" + "".join(f"""  <item>
    <title>{esc(p["h1"])}</title>
    <link>{p["url"]}</link>
    <guid isPermaLink="true">{p["url"]}</guid>
    <pubDate>{rfc822(p.get("published", p["updated"]))}</pubDate>
    <description>{esc(p["description"])}</description>
    <content:encoded>{esc(feed_body(p))}</content:encoded>
  </item>
""" for p in guides) + "</channel>\n</rss>\n")

os.makedirs(".well-known", exist_ok=True)
expires = (datetime.date.today() + datetime.timedelta(days=365)).isoformat()
open(".well-known/security.txt", "w", encoding="utf-8").write(
    f"Contact: mailto:{EMAIL}\nExpires: {expires}T00:00:00Z\nPreferred-Languages: en\n"
    f"Canonical: {SITE}.well-known/security.txt\n")

sections = [(title, [by_path[x] for x in paths]) for title, paths in SERVICE_GROUPS] + [
    ("Guides", [p for p in pages if p["tab"] == "guides/"]),
    ("About and working together", [p for p in pages if p["tab"] in ("", "case-studies/", "about/", "work-with-me/", "contact/", "sitemap/", "site-index/")])]
llms = f"""# Gerris Corp

> {ORG["description"]} Run by Chris Abraham in Arlington, Virginia. Chris has built websites since 1994; Gerris Corp was founded in 2012.

Every engagement starts with a prepaid diagnostic. Contact: {EMAIL}, {PHONE}, https://calendly.com/chrisabraham/30, or https://www.upwork.com/freelancers/chrisjabraham. Each link below goes to the Markdown version of a page; the HTML version is the same URL without index.md.
""" + "".join(f"\n## {title}\n\n" + "".join(f"- [{p['h1']}]({p['url']}index.md): {p['description']}\n" for p in group)
              for title, group in sections) + f"""
## Optional

- [Full text of this site]({SITE}llms-full.txt)
- [Chris Abraham's personal site](https://chrisabraham.com/)
"""
open("llms.txt", "w", encoding="utf-8").write(llms)
open("llm.txt", "w", encoding="utf-8").write(llms)
full = (f"# Gerris Corp: full text of gerriscorp.com\n\n> {ORG['description']}\n> Built {TODAY}. "
        "Quote freely with attribution and a link to the source page.\n")
for p in pages:
    full += f"\n\n---\n\nSource: {p['url']}\nUpdated: {p['updated']}\n\n" + markdown(p) + "\n"
open("llms-full.txt", "w", encoding="utf-8").write(full)

if LIVE:
    open("CNAME", "w").write("gerriscorp.com\n")
elif os.path.exists("CNAME"):
    os.remove("CNAME")

# ---- check ----
problems = []
for p in pages:
    where, t, d, b = p["path"] or "/", p["title"], p["description"], text_of(p["body"])
    if not 50 <= len(t) <= 60: problems.append(f"{where}: title is {len(t)} chars: {t}")
    if not 140 <= len(d) <= 160: problems.append(f"{where}: description is {len(d)} chars: {d}")
    for label, s in (("title", t), ("description", d)):
        # Chris' rule: no pipes or dashes as separators; hyphens inside words (back-of-the-book) are fine.
        if re.search(r"\||[–—]|(?<!\w)-|-(?!\w)", s): problems.append(f"{where}: pipe or separator dash in {label}: {s}")
    if p["body"].count("<h1>") != 1: problems.append(f"{where}: needs exactly one h1")
    if p["words"] < MIN_WORDS[p["kind"]]: problems.append(f"{where}: only {p['words']} words (min {MIN_WORDS[p['kind']]})")
    if re.search(r"\s—|—\s| – ", text_of(re.sub(r"<pre\b.*?</pre>|<code\b.*?</code>", "", p["body"], flags=re.S))): problems.append(f"{where}: spaced em or en dash in the copy (close it up: word—word)")
    if "Chris's" in b + t + d: problems.append(f"{where}: write Chris' not Chris's")
    plain = re.sub(r"<code>.*?</code>|<pre>.*?</pre>|<blockquote>.*?</blockquote>", "", p["body"], flags=re.S)  # quoted words aren't the site's voice
    for m in re.finditer(r"\b(we|We|our|Our|us)\b", text_of(plain)):
        problems.append(f"{where}: first person plural: {m.group(0)}")
    for target in re.findall(r'href="\{root\}([^"#]*)', p["body"]):
        if target and target not in by_path and not os.path.exists(target):
            problems.append(f"{where}: link to missing page {target}")
    # Anchor text: every link names its destination on its own.
    for m in re.finditer(r"<a [^>]*>(.*?)</a>", p["body"], re.S):
        label = text_of(m.group(1)).strip().rstrip(".!:").lower()
        if re.fullmatch(r"(read|click|tap|go|see|view|learn|find out|continue|continue reading)?( (more|here|this|it|on))*|here|more|this|link|this page|this post|details|read (the )?(full )?(case( study)?|guide|post|article|story)|the case study|this (case study|guide)", label) or re.match(r"https?://", label):
            problems.append(f"/{p['path']}: link text says nothing on its own: {text_of(m.group(1)).strip() or '(empty)'}")
# Distinct content: no two pages may share more than 15% of their six-word phrases,
# and no sentence of ten or more words may appear on more than one page.
# Keeps Search Console from treating pages as duplicates or near-duplicates.
def _words(p):
    t = text_of(re.sub(r"<pre>.*?</pre>", "", p["body"], flags=re.S))
    return t, re.findall(r"[a-z0-9']+", t.lower())
_sh, _sent = {}, {}
for p in pages:
    if p["path"] in ("sitemap/", "site-index/"):
        continue  # the site map lists every page's description by design, and the index every page's name
    t, w = _words(p)
    _sh[p["path"]] = {" ".join(w[i:i + 6]) for i in range(len(w) - 5)}
    for sentence in re.split(r"(?<=[.!?])\s+", t):
        if len(sentence.split()) >= 10:
            _sent.setdefault(sentence.strip(), []).append(p["path"] or "/")
_paths = list(_sh)
for i, a in enumerate(_paths):
    for c in _paths[i + 1:]:
        small = min(len(_sh[a]), len(_sh[c])) or 1
        share = len(_sh[a] & _sh[c]) / small
        if share > 0.15:
            problems.append(f"/{a} and /{c} share {share:.0%} of their phrasing")
for sentence, where in _sent.items():
    if len(where) > 1:
        problems.append(f"sentence repeated on {', '.join(where)}: {sentence[:80]}")
if "Gerris" not in pages[0]["title"]: problems.append("home title should carry the name")
for key in ("title", "description", "h1"):
    seen = [p[key] for p in pages]
    for s in set(seen):
        if seen.count(s) > 1: problems.append(f"duplicate {key}: {s}")

total = sum(p["words"] for p in pages)
print(f"built {len(pages)} pages ({total} words), 404, sitemap.xml and .xsl, robots, feed, security.txt, "
      f"llms.txt, llms-full.txt; " + ("LIVE" if LIVE else "preview (noindex, no CNAME)"))
for p in pages:
    print(f"  {p['words']:5d}  {p['kind']:7s} /{p['path']}")
if unindexed:
    print(f"site index: {len(unindexed)} page(s) not indexed yet: {', '.join(unindexed)} (read each one and add its entries to tools/site_index.json)")
for x in problems: print("PROBLEM:", x)
sys.exit(1 if problems else 0)

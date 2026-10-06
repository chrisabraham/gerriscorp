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
minimum word count, no em dashes, "Chris'" never "Chris's", first person
singular ("I", never "we"), and no links to missing pages.

    python3 tools/build.py
"""
import datetime, html, json, os, re, sys
from html.parser import HTMLParser

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
         "services/technical-seo", "services/crawler-visibility", "services/large-sites", "services/ecommerce",
         "services/on-page-seo", "services/site-speed", "services/search-console", "services/migrations",
         "services/ai-search", "services/ongoing-support",
         "services/multi-location", "services/reputation", "services/google-business-profile", "services/email-and-dns",
         "guides/index", "guides/ai-assistants", "guides/javascript-seo", "guides/crawled-not-indexed",
         "guides/migration-checklist", "guides/email-authentication", "guides/personal-information-removal",
         "guides/glossary",
         "case-studies/index", "case-studies/ecommerce-rendering", "case-studies/consent-blocking",
         "case-studies/react-event-platform", "case-studies/netlify-migration", "case-studies/sanity-vercel",
         "case-studies/shopify-migration", "case-studies/app-takeover", "case-studies/programmatic-indexing",
         "case-studies/indexing-recovery", "case-studies/multi-location-entity", "case-studies/seasonal-retailer",
         "case-studies/gbp-reinstatement", "case-studies/umbraco-operations", "case-studies/ai-recruiting",
         "case-studies/data-cleanup", "case-studies/built-with-claude-code",
         "about", "work-with-me", "faq", "contact", "privacy"]
SERVICE_GROUPS = [
    ("Consulting and technical direction", ["services/technical-lead/", "services/developers/", "services/agency-partner/",
                                            "services/rescue/", "services/ai-automation/", "services/data-cleanup/",
                                            "services/analytics/", "services/advisory/"]),
    ("Search and site performance", ["services/technical-seo/", "services/crawler-visibility/", "services/large-sites/",
                                     "services/ecommerce/", "services/on-page-seo/", "services/site-speed/",
                                     "services/search-console/", "services/migrations/", "services/ai-search/",
                                     "services/ongoing-support/"]),
    ("Local, reputation, and email", ["services/multi-location/", "services/reputation/",
                                      "services/google-business-profile/", "services/email-and-dns/"]),
]
MIN_WORDS = {"guide": 700, "service": 450, "case": 250, "page": 250}
TODAY = datetime.date.today().isoformat()
os.chdir(os.path.join(os.path.dirname(__file__), ".."))
AUTHOR = "https://chrisabraham.com/#person"
# Contact details: the only ones the site publishes. Change EMAIL here to switch every page.
EMAIL = "chris@gerriscorp.com"
PHONE = "+1 202-352-5051"
TEL = "+12023525051"


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
    return p


pages = []
for f in FILES:
    head, body = open(f"src/{f}.html", encoding="utf-8").read().split("\n---\n", 1)
    p = dict(line.split(": ", 1) for line in head.strip().splitlines())
    p["src"] = f
    p["path"] = "" if f == "index" else (f[:-5] if f.endswith("/index") else f + "/")
    p["body"] = body.strip().replace("{email}", EMAIL).replace("{phone}", PHONE).replace("{tel}", TEL)
    p["tab"] = (p["path"].split("/")[0] + "/") if p["path"] else ""
    if p["tab"] not in dict(TABS):
        p["tab"] = {"privacy/": "privacy/"}.get(p["path"], "work-with-me/")  # the FAQ lives under Work With Me
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
    out += [li(by_path[x]) for x in ["", "services/", "guides/", "case-studies/", "about/", "work-with-me/", "faq/", "contact/", "privacy/"]]
    out.append('</ul>')
    for title, paths in SERVICE_GROUPS:
        out += [f'<h2>{title}</h2>', '<ul>'] + [li(by_path[x]) for x in paths] + ['</ul>']
    for title, tab in (("Guides", "guides/"), ("Case studies", "case-studies/")):
        out += [f'<h2>{title}</h2>', '<ul>'] + [li(q) for q in pages if q["tab"] == tab and q["path"] != tab] + ['</ul>']
    out += ['<h2>Files for machines</h2>', '<ul>',
            '  <li><a href="{root}sitemap.xml">sitemap.xml</a>: the XML sitemap for search engines.</li>',
            '  <li><a href="{root}llms.txt">llms.txt</a>: a plain summary of the site for language models, linking to Markdown versions of every page.</li>',
            '  <li><a href="{root}llms-full.txt">llms-full.txt</a>: the full text of the site in one file.</li>',
            '  <li><a href="{root}feed.xml">feed.xml</a>: an Atom feed of the guides.</li>',
            '  <li><a href="{root}robots.txt">robots.txt</a>: crawler rules; every search engine and AI crawler is welcome.</li>',
            '</ul>']
    return "\n".join(out)


pages.append(finish({
    "name": "Site Map", "src": "(generated)", "path": "sitemap/", "tab": "sitemap/", "kind": "page",
    "title": "Site map of gerriscorp.com: every page, with a summary",
    "description": "A complete map of gerriscorp.com: every service, guide, and case study by Chris Abraham at Gerris Corp, grouped by section with a one line summary.",
    "body": site_map_body()}))
by_path = {p["path"]: p for p in pages}
guides = [p for p in pages if p["kind"] == "guide"]

CSS = """
:root { --text: #000; --muted: #333; --link: #284a57; --tab: #8cacbb; --bar: #dee7ec; --rule: #c8d3d8; --bg: #fff; }
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
.brand { font-size: 1.6rem; font-weight: bold; color: #000; text-decoration: none; }
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
h1 { font-size: 1.75rem; line-height: 1.25; margin: .25rem 0 1rem; }
h2 { font-size: 1.3rem; line-height: 1.3; margin: 2rem 0 .5rem; }
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
.portrait { float: right; width: 160px; height: 160px; margin: .25rem 0 1rem 1.25rem; border: 1px solid var(--rule); }
.button { display: inline-block; margin: 0 .5rem .6rem 0; padding: .6rem 1.1rem; border: 2px solid var(--link); background: var(--bar); color: #000; font-weight: bold; text-decoration: none; }
.button:hover { text-decoration: underline; }
.related { border-top: 1px solid var(--rule); margin-top: 2rem; padding-top: .5rem; }
.contact li { margin-bottom: .6rem; }
.site-footer { border-top: 1px solid var(--rule); padding: 1rem 0 2.5rem; color: var(--muted); font-size: .9rem; }
.site-footer p { margin: 0 0 .4rem; }
@media (max-width: 34rem) {
  body { font-size: 17px; }
  .top img { width: 52px; height: 52px; }
  nav a { padding: .45rem .55rem; }
  h1 { font-size: 1.5rem; }
  .portrait { width: 112px; height: 112px; margin-left: 1rem; }
}
""".strip()

KNOWS = ["Technical consulting", "Developer specifications", "AI-assisted software development", "Claude Code",
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
    "description": "Chris Abraham's consultancy: fractional technical leadership, developer specs and QA, AI tools built with Claude Code, project rescue, technical SEO, site speed, migrations, AI search visibility, and reputation management.",
    "foundingDate": "2007", "founder": {"@id": AUTHOR}, "employee": {"@id": AUTHOR},
    "slogan": "Experienced help for the digital work your business needs done",
    "email": EMAIL, "telephone": "+1-202-352-5051",
    "address": ADDRESS, "location": {"@id": SITE + "#place"},
    "geo": HOME["geo"], "areaServed": AREA_SERVED, "knowsLanguage": "en", "knowsAbout": KNOWS,
    "numberOfEmployees": {"@type": "QuantitativeValue", "value": 1},
    "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": EMAIL, "telephone": "+1-202-352-5051",
                      "areaServed": [c for _, _, c in ENGLISH_SPEAKING], "availableLanguage": "English"},
                     {"@type": "ContactPoint", "contactType": "technical support", "email": EMAIL,
                      "telephone": "+1-202-352-5051", "availableLanguage": "English"}],
    "sameAs": ["https://www.upwork.com/freelancers/chrisjabraham", "https://github.com/chrisabraham/gerriscorp"],
}
PERSON = {
    "@type": "Person", "@id": AUTHOR, "name": "Chris Abraham", "alternateName": "Christopher Abraham",
    "image": {"@type": "ImageObject", "url": SITE + "chris-abraham.jpg", "width": 225, "height": 225,
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
                      "skills": "Technical SEO, developer specifications, Claude Code, Git, Linux, Cloudflare, migrations, AI search"},
    "knowsAbout": KNOWS,
    "email": EMAIL, "telephone": "+1-202-352-5051",
    "sameAs": ["https://chrisabraham.com/", "https://www.upwork.com/freelancers/chrisjabraham", "https://hillmole.com/"],
}
WEBSITE = {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Gerris Corp",
           "alternateName": "Gerris", "inLanguage": "en-US", "publisher": {"@id": SITE + "#org"}}


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
                      "image": SITE + "social-card.png", "inLanguage": "en-US", "wordCount": p["words"]})
        page["mainEntity"] = {"@id": p["url"] + "#article"}
    if p["kind"] == "guide":
        graph.append({"@type": "TechArticle", "@id": p["url"] + "#article", "headline": p["h1"],
                      "description": p["description"], "url": p["url"], "mainEntityOfPage": {"@id": p["url"] + "#webpage"},
                      "author": {"@id": AUTHOR}, "publisher": {"@id": SITE + "#org"},
                      "datePublished": p.get("published", p["updated"]), "dateModified": p["updated"],
                      "image": SITE + "social-card.png", "inLanguage": "en-US", "wordCount": p["words"]})
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


def body_html(p):
    r = p["root"] or "./"
    body = p["body"].replace("{root}", r)
    if p["kind"] == "guide":
        by = (f'<p class="byline">By <a href="{r}about/">Chris Abraham</a> · Published {nice(p.get("published", p["updated"]))}'
              + (f' · Updated {nice(p["updated"])}' if p.get("published", p["updated"]) != p["updated"] else "") + "</p>")
        body = re.sub(r"(</h1>)", r"\1\n" + by, body, count=1)
    else:
        body += f'\n<p class="updated">Updated {nice(p["updated"])}</p>'
    return body


# Google Analytics 4. Consent mode: ads storage denied everywhere; analytics storage
# denied in the UK and EEA (cookieless pings there), granted elsewhere. See /privacy/.
GA_ID = "G-JF2W6ESJZN"
_EEA_UK = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU",
           "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "IS", "LI", "NO", "GB", "CH"]
GA = f"""
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('consent', 'default', {{ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'granted'}});
  gtag('consent', 'default', {{analytics_storage: 'denied', region: {json.dumps(_EEA_UK)}}});
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>""" if LIVE else ""


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
<link rel="canonical" href="{p["url"]}">
<meta name="author" content="Chris Abraham">
<meta name="msvalidate.01" content="2E8EA11035C27E2B7C82A165FA698E0C">
<link rel="icon" href="{r}logo.png" type="image/png">
<link rel="apple-touch-icon" href="{r}logo.png">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="alternate" type="text/markdown" title="This page as Markdown" href="index.md">
<link rel="alternate" type="application/atom+xml" title="Gerris guides" href="{r}feed.xml">
<link rel="alternate" type="text/plain" title="llms.txt" href="{r}llms.txt">
<link rel="sitemap" type="application/xml" href="{r}sitemap.xml">
<meta name="theme-color" content="#ffffff">{GA}
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
  <a href="{home}"><img src="{r}logo-128.png" width="64" height="64" alt="Gerris home"></a>
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
  <p>© {TODAY[:4]} Gerris Corp, Arlington, Virginia · <a href="{r}faq/">FAQ</a> · <a href="{r}privacy/">Privacy</a> · <a href="{r}sitemap/">Site map</a> · <a href="{r}guides/glossary/">Glossary</a> · <a href="{r}llms.txt">llms.txt</a> · <a href="{r}feed.xml">Feed</a> · <a href="https://chrisabraham.com/">chrisabraham.com</a></p>
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
    m.feed(body_html(p).replace('href="' + (p["root"] or "./"), 'href="'))
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
Allow: /

Sitemap: https://gerriscorp.com/sitemap.xml
""")

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
  </entry>
""" for p in guides) + "</feed>\n")

os.makedirs(".well-known", exist_ok=True)
expires = (datetime.date.today() + datetime.timedelta(days=365)).isoformat()
open(".well-known/security.txt", "w", encoding="utf-8").write(
    f"Contact: mailto:{EMAIL}\nExpires: {expires}T00:00:00Z\nPreferred-Languages: en\n"
    f"Canonical: {SITE}.well-known/security.txt\n")

sections = [(title, [by_path[x] for x in paths]) for title, paths in SERVICE_GROUPS] + [
    ("Guides", [p for p in pages if p["tab"] == "guides/"]),
    ("About and working together", [p for p in pages if p["tab"] in ("", "case-studies/", "about/", "work-with-me/", "contact/", "sitemap/")])]
llms = f"""# Gerris Corp

> {ORG["description"]} Run by Chris Abraham in Arlington, Virginia. Chris has built websites since 1994; Gerris Corp was founded in 2007.

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
        if re.search(r"[|\-–—]", s): problems.append(f"{where}: pipe, dash or hyphen in {label}: {s}")
    if p["body"].count("<h1>") != 1: problems.append(f"{where}: needs exactly one h1")
    if p["words"] < MIN_WORDS[p["kind"]]: problems.append(f"{where}: only {p['words']} words (min {MIN_WORDS[p['kind']]})")
    if "—" in b or " – " in b: problems.append(f"{where}: em or en dash in the copy")
    if "Chris's" in b + t + d: problems.append(f"{where}: write Chris' not Chris's")
    plain = re.sub(r"<code>.*?</code>|<pre>.*?</pre>", "", p["body"], flags=re.S)
    for m in re.finditer(r"\b(we|We|our|Our|us)\b", text_of(plain)):
        problems.append(f"{where}: first person plural: {m.group(0)}")
    for target in re.findall(r'href="\{root\}([^"#]*)', p["body"]):
        if target and target not in by_path and not os.path.exists(target):
            problems.append(f"{where}: link to missing page {target}")
# Distinct content: no two pages may share more than 15% of their six-word phrases,
# and no sentence of ten or more words may appear on more than one page.
# Keeps Search Console from treating pages as duplicates or near-duplicates.
def _words(p):
    t = text_of(re.sub(r"<pre>.*?</pre>", "", p["body"], flags=re.S))
    return t, re.findall(r"[a-z0-9']+", t.lower())
_sh, _sent = {}, {}
for p in pages:
    if p["path"] == "sitemap/":
        continue  # the site map lists every page's description by design
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
for x in problems: print("PROBLEM:", x)
sys.exit(1 if problems else 0)

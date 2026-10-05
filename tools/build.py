"""Build gerriscorp.com from src/.

Each file in src/ starts with `key: value` lines (title, description, and
`name` for the menu and breadcrumbs), then a line `---`, then the page body.
src/about.html becomes /about/, src/services/migrations.html becomes
/services/migrations/, and src/index.html files become their folder's index.
`{root}` in a body is the relative path back to the site root, so links work
on gerriscorp.com and on the github.io preview alike.

Writes every page, 404.html, sitemap.xml, robots.txt, llms.txt, llm.txt,
llms-full.txt, and (when LIVE) CNAME, then checks the house rules:
titles 50-60 characters, descriptions 140-160, no pipes, dashes or
hyphens in either, unique titles and descriptions, one h1 per page, no em
dashes, "Chris'" never "Chris's", and first person singular ("I", never
"we").

    python3 tools/build.py
"""
import datetime, html, json, os, re, sys
from html.parser import HTMLParser

# Set to True at the DNS cutover: drops noindex and writes CNAME (see README).
LIVE = False

SITE = "https://gerriscorp.com/"
PREVIEW_BASE = "/gerriscorp/"
TABS = [("", "Home"), ("services/", "Services"), ("case-studies/", "Case Studies"), ("about/", "About"), ("work-with-me/", "Work With Me"), ("contact/", "Contact")]
FILES = ["index", "services/index", "services/technical-seo", "services/migrations", "services/ai-search",
         "services/developers", "services/ongoing-support", "services/reputation",
         "services/google-business-profile", "services/email-and-dns", "case-studies", "about",
         "work-with-me", "contact"]
TODAY = datetime.date.today().isoformat()
os.chdir(os.path.join(os.path.dirname(__file__), ".."))

pages = []
for f in FILES:
    head, body = open(f"src/{f}.html", encoding="utf-8").read().split("\n---\n", 1)
    p = dict(line.split(": ", 1) for line in head.strip().splitlines())
    p["src"] = f
    p["path"] = "" if f == "index" else (f[:-5] if f.endswith("/index") else f + "/")
    p["body"] = body.strip()
    p["url"] = SITE + p["path"]
    p["root"] = "../" * p["path"].count("/")
    p["tab"] = (p["path"].split("/")[0] + "/") if p["path"] else ""
    p.setdefault("name", "Home")
    pages.append(p)
by_path = {p["path"]: p for p in pages}

CSS = """
:root { --text: #000; --muted: #333; --link: #284a57; --tab: #8cacbb; --bar: #dee7ec; --rule: #c8d3d8; --bg: #fff; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
body { margin: 0; color: var(--text); background: var(--bg); font: 18px/1.65 Verdana, "Lucida Grande", Lucida, "DejaVu Sans", Helvetica, Arial, sans-serif; }
.wrap { max-width: 44rem; margin: 0 auto; padding: 0 1rem; }
a { color: var(--link); text-decoration: underline; text-underline-offset: .15em; overflow-wrap: anywhere; }
a:hover { text-decoration-thickness: 2px; }
:focus-visible { outline: 3px solid #000; outline-offset: 2px; }
img { max-width: 100%; height: auto; }
.skip { position: absolute; left: -999px; }
.skip:focus { left: 1rem; top: .5rem; background: #fff; padding: .5rem; z-index: 1; }
.top { display: flex; align-items: center; gap: .9rem; padding: 1.25rem 0 .9rem; }
.top img { width: 64px; height: 64px; flex: none; }
.brand { font-size: 1.6rem; font-weight: bold; color: #000; text-decoration: none; }
.brand:hover { text-decoration: underline; }
.tag { margin: 0; color: var(--muted); font-size: .95rem; line-height: 1.4; }
nav { border-bottom: 4px solid var(--bar); }
nav ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: .35rem; }
nav li { margin: 0; }
nav a { display: block; padding: .4rem .8rem; border: 1px solid var(--tab); border-bottom: none; text-decoration: none; font-size: .95rem; }
nav a:hover { background: var(--bar); text-decoration: underline; }
nav a[aria-current] { background: var(--bar); color: #000; font-weight: bold; }
.crumbs { font-size: .9rem; margin: 1rem 0 0; color: var(--muted); }
main { padding: 1.25rem 0 2rem; }
h1 { font-size: 1.75rem; line-height: 1.25; margin: .25rem 0 1rem; }
h2 { font-size: 1.3rem; line-height: 1.3; margin: 2rem 0 .5rem; }
p, ul { margin: 0 0 1rem; }
li { margin-bottom: .4rem; }
.lead { font-size: 1.1rem; }
code { font-family: Consolas, Menlo, monospace; font-size: .95em; }
.button { display: inline-block; margin: 0 .5rem .6rem 0; padding: .6rem 1.1rem; border: 2px solid var(--link); background: var(--bar); color: #000; font-weight: bold; text-decoration: none; }
.button:hover { text-decoration: underline; }
.contact li { margin-bottom: .6rem; }
.site-footer { border-top: 1px solid var(--rule); padding: 1rem 0 2.5rem; color: var(--muted); font-size: .9rem; }
.site-footer p { margin: 0 0 .4rem; }
@media (max-width: 34rem) {
  body { font-size: 17px; }
  .top img { width: 52px; height: 52px; }
  nav a { padding: .45rem .6rem; font-size: .9rem; }
  h1 { font-size: 1.5rem; }
}
""".strip()

ORG = {
    "@type": "ProfessionalService", "@id": SITE + "#org", "name": "Gerris Corp",
    "alternateName": ["Gerris"], "url": SITE, "logo": SITE + "logo.png", "image": SITE + "social-card.png",
    "description": "Chris Abraham's consultancy: technical SEO forensics, website migrations, AI search visibility (SEO, AEO, GEO), work alongside client developers, and reputation and perception management.",
    "email": "chris@gerriscorp.com", "telephone": "+1-202-352-5051",
    "address": {"@type": "PostalAddress", "addressLocality": "Arlington", "addressRegion": "VA", "addressCountry": "US"},
    "areaServed": "Worldwide", "founder": {"@id": "https://chrisabraham.com/#person"},
    "employee": {"@id": "https://chrisabraham.com/#person"},
    "knowsAbout": ["Technical SEO", "JavaScript rendering and indexing", "Website migrations", "301 redirects",
                   "Answer engine optimization", "Generative engine optimization", "Structured data",
                   "Online reputation management", "Google Business Profile", "SPF, DKIM, and DMARC"],
    "sameAs": ["https://www.upwork.com/freelancers/chrisjabraham", "https://github.com/chrisabraham/gerriscorp"],
}
PERSON = {
    "@type": "Person", "@id": "https://chrisabraham.com/#person", "name": "Chris Abraham",
    "alternateName": "Christopher Abraham", "url": "https://chrisabraham.com/", "jobTitle": "Founder",
    "worksFor": {"@id": SITE + "#org"}, "alumniOf": "The George Washington University",
    "homeLocation": {"@type": "Place", "name": "Arlington, Virginia"},
    "sameAs": ["https://chrisabraham.com/", "https://www.linkedin.com/in/chrisabraham",
               "https://twitter.com/chrisabraham",
               "https://www.instagram.com/chrisabraham", "https://www.facebook.com/chrisabraham",
               "https://www.upwork.com/freelancers/chrisjabraham", "https://github.com/chrisabraham",
               "https://hillmole.com/"],
}
WEBSITE = {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Gerris Corp",
           "alternateName": "Gerris", "inLanguage": "en-US", "publisher": {"@id": SITE + "#org"}}


def text_of(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()


def trail(p):
    """Breadcrumb pages from Home down to p."""
    out = [by_path[""]]
    if p["tab"] and p["tab"] != p["path"]:
        out.append(by_path[p["tab"]])
    if p["path"]:
        out.append(p)
    return out


def schema(p):
    page_type = "AboutPage" if p["path"] == "about/" else "ContactPage" if p["path"] == "contact/" else "WebPage"
    page = {"@type": page_type, "@id": p["url"] + "#webpage", "url": p["url"], "name": p["title"],
            "description": p["description"], "isPartOf": {"@id": SITE + "#website"},
            "about": {"@id": SITE + "#org"}, "primaryImageOfPage": SITE + "social-card.png",
            "inLanguage": "en-US", "dateModified": TODAY}
    graph = [WEBSITE, ORG, PERSON, page]
    if p["path"]:
        page["breadcrumb"] = {"@id": p["url"] + "#breadcrumb"}
        graph.append({"@type": "BreadcrumbList", "@id": p["url"] + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": q["name"], "item": q["url"]}
            for i, q in enumerate(trail(p))]})
    if p["tab"] == "services/" and p["path"] != "services/":
        graph.append({"@type": "Service", "@id": p["url"] + "#service", "name": text_of(
            re.search(r"<h1>(.*?)</h1>", p["body"]).group(1)), "description": p["description"],
            "provider": {"@id": SITE + "#org"}, "areaServed": "Worldwide", "url": p["url"]})
        page["mainEntity"] = {"@id": p["url"] + "#service"}
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)


def render(p):
    r = p["root"]
    home = r or "./"
    e = lambda s: html.escape(s, quote=True)
    nav = "\n".join(
        f'    <li><a href="{(r + path) or "./"}"{(" aria-current=" + chr(34) + ("page" if path == p["path"] else "true") + chr(34)) if path == p["tab"] else ""}>{label}</a></li>'
        for path, label in TABS)
    crumbs = ""
    if p["path"] and p["tab"] != p["path"]:
        crumbs = ('\n<p class="crumbs">' + " › ".join(f'<a href="{r}{q["path"]}">{q["name"]}</a>' for q in trail(p)[:-1])
                  + f' › {p["name"]}</p>')
    robots = "" if LIVE else '\n<meta name="robots" content="noindex">'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["description"])}">{robots}
<link rel="canonical" href="{p["url"]}">
<meta name="author" content="Chris Abraham">
<link rel="icon" href="{r}logo.png" type="image/png">
<link rel="apple-touch-icon" href="{r}logo.png">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="alternate" type="text/plain" title="llms.txt" href="{r}llms.txt">
<meta name="theme-color" content="#ffffff">
<meta property="og:site_name" content="Gerris Corp">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(p["title"])}">
<meta property="og:description" content="{e(p["description"])}">
<meta property="og:url" content="{p["url"]}">
<meta property="og:image" content="{SITE}social-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The Gerris logo, a sketched water strider">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@chrisabraham">
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
  <a href="{home}"><img src="{r}logo.png" width="64" height="64" alt="Gerris home"></a>
  <div>
    <a class="brand" href="{home}">Gerris</a>
    <p class="tag">Chris Abraham: technical SEO, AI search, and reputation</p>
  </div>
</header>
<nav aria-label="Site">
  <ul>
{nav}
  </ul>
</nav>{crumbs}
<main id="main">
{p["body"].replace("{root}", home if r == "" else r)}
</main>
<footer class="site-footer">
  <p><a href="mailto:chris@gerriscorp.com">chris@gerriscorp.com</a> · <a href="tel:+12023525051">202-352-5051</a> · <a href="https://calendly.com/chrisabraham/30">Book a call</a> · <a href="https://www.upwork.com/freelancers/chrisjabraham">Upwork</a></p>
  <p>© {TODAY[:4]} Gerris Corp, Arlington, Virginia · <a href="https://chrisabraham.com/">chrisabraham.com</a> · <a href="{r}llms.txt">llms.txt</a></p>
</footer>
</div>
</body>
</html>
"""


class Text(HTMLParser):
    """A page body as Markdown-ish text with absolute links, for llms-full.txt."""
    def __init__(self):
        super().__init__(); self.out = []; self.href = None; self.start = 0
    def handle_starttag(self, t, a):
        a = dict(a)
        if t in ("h1", "h2", "h3"): self.out.append("\n\n" + "#" * int(t[1]) + " ")
        elif t == "p": self.out.append("\n\n")
        elif t == "li": self.out.append("\n- ")
        elif t == "a": self.href = a.get("href"); self.start = len(self.out)
    def handle_endtag(self, t):
        if t == "a" and self.href:
            h = self.href.split("?")[0].replace("mailto:", "").replace("tel:", "")
            if not re.match(r"https?:|[\w.+-]+@|\+\d", h):
                h = SITE + re.sub(r"^(\.\./|\./)+", "", h)
            label = "".join(self.out[self.start:]).strip()
            if h.rstrip("/") not in label and label not in h:
                self.out.append(f" ({h})")
            self.href = None
    def handle_data(self, d): self.out.append(re.sub(r"\s+", " ", d))


def as_text(p):
    t = Text(); t.feed(p["body"].replace("{root}", ""))
    return re.sub(r"[ \t]+\n", "\n", re.sub(r"\n{3,}", "\n\n", "".join(t.out))).strip()


# ---- write ----
for p in pages:
    os.makedirs(p["path"] or ".", exist_ok=True)
    open(os.path.join(p["path"], "index.html"), "w", encoding="utf-8").write(render(p))

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
  <a href="{base}"><img src="{base}logo.png" width="64" height="64" alt="Gerris home"></a>
  <div><a class="brand" href="{base}">Gerris</a></div>
</header>
<main id="main">
<h1>Page not found</h1>
<p>That page isn't here. Try the <a href="{base}">home page</a>, the <a href="{base}services/">services</a>, or email <a href="mailto:chris@gerriscorp.com">chris@gerriscorp.com</a>.</p>
</main>
</div>
</body>
</html>
""")

open("sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{p['url']}</loc><lastmod>{TODAY}</lastmod></url>\n" for p in pages)
    + "</urlset>\n")

open("robots.txt", "w", encoding="utf-8").write("""# Search engines and AI assistants are welcome to read and cite everything here.
User-agent: *
Allow: /

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
User-agent: CCBot
Allow: /

Sitemap: https://gerriscorp.com/sitemap.xml
""")

llms = f"""# Gerris Corp

> {ORG["description"]} Based in Arlington, Virginia. Chris Abraham has built websites since 1994.

Every engagement starts with a prepaid diagnostic. Contact: chris@gerriscorp.com, +1 202-352-5051, https://calendly.com/chrisabraham/30, or https://www.upwork.com/freelancers/chrisjabraham.

## Pages

""" + "".join(f"- [{p['name']}]({p['url']}): {p['description']}\n" for p in pages) + f"""
## Optional

- [Full text of this site]({SITE}llms-full.txt)
- [Chris Abraham's personal site and blog](https://chrisabraham.com/)
"""
open("llms.txt", "w", encoding="utf-8").write(llms)
open("llm.txt", "w", encoding="utf-8").write(llms)
full = (f"# Gerris Corp: full text of gerriscorp.com\n\n> {ORG['description']}\n> Updated {TODAY}. "
        "Quote freely with attribution and a link.\n")
for p in pages:
    full += f"\n\n---\n\nSource: {p['url']}\n\n" + as_text(p) + "\n"
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
    if "—" in b or " – " in b: problems.append(f"{where}: em or en dash in the copy")
    if "Chris's" in b + t + d: problems.append(f"{where}: write Chris' not Chris's")
    for m in re.finditer(r"\b(we|We|our|Our|us)\b", b):
        problems.append(f"{where}: first person plural: …{b[max(0, m.start() - 30):m.end() + 30]}…")
if "Gerris" not in pages[0]["title"]: problems.append("home title should carry the name")
for key in ("title", "description"):
    seen = [p[key] for p in pages]
    for s in set(seen):
        if seen.count(s) > 1: problems.append(f"duplicate {key}: {s}")

print(f"built {len(pages)} pages, 404, sitemap, robots, llms.txt, llms-full.txt; "
      + ("LIVE" if LIVE else "preview (noindex, no CNAME)"))
for x in problems: print("PROBLEM:", x)
sys.exit(1 if problems else 0)

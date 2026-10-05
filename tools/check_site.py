"""Regenerate llms-full.txt from index.html and check the page against the
rules used on Hill Mole: title 50-60 characters, description 140-160, no
pipes, dashes or hyphens in either, the name on the main page, matching
og/twitter copies, valid JSON-LD, every FAQ question visible on the page,
and a warning while the preview noindex is still in place.

Run from the repo root before each commit:  python3 tools/check_site.py
"""
import html, json, re, sys
from html.parser import HTMLParser

page = open("index.html", encoding="utf-8").read()
problems = []

def meta(attr, name):
    m = re.search(rf'<meta {attr}="{re.escape(name)}" content="([^"]*)"', page)
    return html.unescape(m.group(1)) if m else None

title = html.unescape(re.search(r"<title>(.*?)</title>", page, re.S).group(1))
desc = meta("name", "description")
if not 50 <= len(title) <= 60: problems.append(f"title is {len(title)} chars: {title}")
if not desc or not 140 <= len(desc) <= 160: problems.append(f"description is {len(desc or '')} chars")
for label, s in (("title", title), ("description", desc or "")):
    if re.search(r"[|\-–—]", s): problems.append(f"pipe, dash or hyphen in {label}: {s}")
if "Gerris Corp" not in title: problems.append("main page title should carry the name")
for attr, name, want in (("property", "og:title", title), ("name", "twitter:title", title),
                         ("property", "og:description", desc), ("name", "twitter:description", desc)):
    if meta(attr, name) != want: problems.append(f"{name} doesn't match")

blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', page, re.S)
graph = []
for b in blocks:
    try: graph += json.loads(b).get("@graph", [])
    except json.JSONDecodeError as e: problems.append(f"JSON-LD: {e}")
for node in graph:
    if node.get("@type") == "WebPage":
        if node.get("name") != title: problems.append("WebPage name doesn't match <title>")
        if node.get("description") != desc: problems.append("WebPage description doesn't match")
    if node.get("@type") == "FAQPage":
        for q in node["mainEntity"]:
            if f"<h3>{html.escape(q['name'], quote=False)}</h3>" not in page:
                problems.append(f"FAQ question not on the page: {q['name']}")

class Text(HTMLParser):
    """index.html as Markdown-ish plain text, for llms-full.txt."""
    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0; self.href = None
    def handle_starttag(self, t, a):
        a = dict(a)
        if t in ("head", "nav", "script", "style"): self.skip += 1
        elif t in ("h1", "h2", "h3"): self.out.append("\n\n" + "#" * int(t[1]) + " ")
        elif t in ("p", "blockquote"): self.out.append("\n\n")
        elif t == "li": self.out.append("\n- ")
        elif t == "footer": self.out.append("\n\n— ")
        elif t == "a": self.href = a.get("href")
    def handle_endtag(self, t):
        if t in ("head", "nav", "script", "style"): self.skip -= 1
        elif t == "a" and self.href and not self.skip:
            h = self.href
            if not h.startswith(("http", "mailto", "tel")): h = "https://gerriscorp.com/" + h.lstrip("./")
            self.out.append(f" ({h.replace('mailto:', '').replace('tel:', '')})"); self.href = None
    def handle_data(self, d):
        if not self.skip: self.out.append(re.sub(r"\s+", " ", d))

t = Text(); t.feed(page)
body = re.sub(r"[ \t]+\n", "\n", re.sub(r"\n{3,}", "\n\n", "".join(t.out))).strip()
body = re.sub(r"^# Gerris Corp", "# Gerris Corp\n\n> " + desc + "\n> Source: https://gerriscorp.com/ · Last updated: "
              + next(n["dateModified"] for n in graph if n.get("@type") == "WebPage"), body)
open("llms-full.txt", "w", encoding="utf-8").write(body + "\n")

if 'name="robots" content="noindex"' in page:
    print("NOTE: preview noindex is still on; delete it at cutover (see README).")
print(f"title {len(title)}, description {len(desc)}, {len(graph)} JSON-LD nodes; llms-full.txt rewritten")
for p in problems: print("PROBLEM:", p)
sys.exit(1 if problems else 0)

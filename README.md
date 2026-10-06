# gerriscorp.com

Gerris Corp, Chris Abraham's consultancy. Static pages on GitHub Pages: plain HTML with inline CSS, no JavaScript except the Google Analytics tag (GA4 with consent mode: analytics cookies off in the UK and EEA, ads storage off everywhere; see /privacy/), Plone classic look (tabs, slate-blue links), built for legibility (black Verdana at 18px, AAA link contrast, visible focus, skip link).

## Editing

1. Edit the page sources in `src/`. Each file starts with `title:`, `description:`, `name:` (menu and breadcrumb label), and `updated:`; guides add `type: guide` and `published:`. Then `---`, then the HTML body. Write `{root}` before internal links, and `{email}`, `{phone}`, `{tel}` for contact details (set once at the top of `tools/build.py`).
2. Run `python3 tools/build.py`. It writes every page, a Markdown twin of each (`index.md`), the HTML site map at `/sitemap/`, `404.html`, `sitemap.xml` with its browser stylesheet `sitemap.xsl`, `robots.txt`, `feed.xml`, `llms.txt`, `llm.txt`, `llms-full.txt`, and `.well-known/security.txt`. Then it checks the house rules: titles 50–60 characters, descriptions 140–160, no pipes, dashes, or hyphens in either, unique titles and descriptions, one h1 per page, minimum word counts (guides 700, services 450, other pages 250), no em dashes, `Chris'`, first person singular, and no links to missing pages.
3. Commit the sources and the generated files together, and push.

To add a page, create its source file and add it to `FILES` in `tools/build.py` (and to `SERVICE_GROUPS` for a service). Marking up a `<section class="faq">` or a `<dl class="glossary">` produces FAQPage or DefinedTermSet structured data automatically.

Preview locally: `python3 -m http.server`, then open http://localhost:8000

## Search and AI

- Per-page title, description, canonical, Open Graph, and Twitter card; 1200×630 `social-card.png`. Visible "Updated" dates on every page, bylines on guides.
- JSON-LD on every page: WebSite, ProfessionalService, Person, the page, breadcrumbs, plus `Service` on service pages, `TechArticle` on guides, `FAQPage` wherever there are questions, `DefinedTermSet` on the glossary, and `ItemList` on section pages.
- `sitemap.xml` with image entries and a stylesheet that renders it as a table in a browser; an HTML site map at `/sitemap/`.
- `robots.txt` welcomes every crawler and names the AI crawlers explicitly. `llms.txt` links to Markdown versions of every page; `llms-full.txt` holds the full text. Atom feed of guides at `feed.xml`.
- IndexNow: the `<key>.txt` file, `tools/indexnow.py`, and `.github/workflows/indexnow.yml` ping Bing and the other IndexNow engines after each push, once gerriscorp.com really serves this site.
- `_config.yml` keeps `src/` and `tools/` off the public site and publishes `.well-known/`.

## DNS (Cloudflare, since 2026-10-05)

Registrar: Squarespace Domains (registered 2012-05-07, expires 2027-05-07). Nameservers: adam.ns.cloudflare.com and cruz.ns.cloudflare.com. DNSSEC off.

| Record | Value | Notes |
|---|---|---|
| A @ | 185.199.108.153, .109.153, .110.153, .111.153 | GitHub Pages, DNS only |
| AAAA @ | 2606:50c0:8000::153, 8001::153, 8002::153, 8003::153 | GitHub Pages, DNS only |
| CNAME www | chrisabraham.github.io | GitHub redirects www to the apex |
| MX @ | aspmx.l.google.com (1), alt1/alt2 (5), alt3/alt4 (10) | Google Workspace mail |
| TXT @ | v=spf1 include:_spf.google.com ~all | SPF |
| TXT @ | google-site-verification=… | Search Console |
| TXT _dmarc | v=DMARC1; p=quarantine; rua=mailto:dmarc@gerriscorp.com; pct=100 | DMARC |
| TXT google._domainkey | DKIM public key | Google Workspace DKIM |
| CNAME docs, mail | ghs.googlehosted.com | legacy Google custom URLs |

Keep the website records DNS only until GitHub's certificate is issued; after that they can be proxied with SSL/TLS set to Full (strict). Keep Cloudflare's "Block AI bots" off so AI crawlers can read the site.

## Live

The site went live on gerriscorp.com on 2026-10-05 (`LIVE = True` in `tools/build.py`, custom domain set in the repo's Pages settings). The github.io address redirects to it.

After going live: submit `https://gerriscorp.com/sitemap.xml` in Google Search Console and Bing Webmaster Tools, and run the IndexNow workflow by hand once.

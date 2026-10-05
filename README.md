# gerriscorp.com

Gerris Corp, Chris Abraham's consultancy. Static pages on GitHub Pages: plain HTML with inline CSS, no JavaScript, Plone classic look (tabs, slate-blue links), built for legibility (black Verdana at 18px, AAA link contrast, visible focus, skip link).

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

## DNS inventory (read on 2026-10-05, before any change)

Registrar: Squarespace Domains (registered 2012-05-07, expires 2027-05-07). Nameservers: ns-cloud-e1…e4.googledomains.com.

| Record | Value | At cutover |
|---|---|---|
| A @ | 198.49.23.144, 198.49.23.145, 198.185.159.144, 198.185.159.145 (Squarespace redirect) | **Replace** with GitHub Pages |
| CNAME www | ext-cust.squarespace.com | **Replace** with chrisabraham.github.io |
| MX @ | aspmx.l.google.com and alt1–alt4 (Google Workspace) | Keep |
| TXT @ | v=spf1 include:_spf.google.com ~all | Keep |
| TXT @ | google-site-verification=… (Search Console) | Keep |
| TXT _dmarc | v=DMARC1; p=quarantine; rua=mailto:dmarc@gerriscorp.com; pct=100 | Keep |
| TXT google._domainkey | DKIM public key | Keep |

## Going live on gerriscorp.com

The site is a noindexed preview at https://chrisabraham.github.io/gerriscorp/ until these steps are done. Canonical host: `gerriscorp.com`; GitHub Pages redirects `www` to it.

1. Set `LIVE = True` in `tools/build.py`, run it (this removes `noindex` and writes `CNAME`), commit, and push.
2. In the repo's Settings → Pages, set the custom domain to `gerriscorp.com`.
3. In Squarespace DNS, replace only the apex A records with 185.199.108.153, 185.199.109.153, 185.199.110.153, and 185.199.111.153 (optionally AAAA 2606:50c0:8000::153, 8001::153, 8002::153, 8003::153), and point `www` at `chrisabraham.github.io`. Leave MX and every TXT record alone, and turn off Squarespace's domain forwarding.
4. Once GitHub issues the certificate, tick Enforce HTTPS. Check `https://gerriscorp.com/`, `https://www.gerriscorp.com/`, and that mail still arrives.
5. Run the IndexNow workflow by hand, and submit `https://gerriscorp.com/sitemap.xml` in Google Search Console (already verified by DNS) and Bing Webmaster Tools.

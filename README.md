# gerriscorp.com

Gerris Corp, Chris Abraham's consultancy. Static pages on GitHub Pages: plain HTML with inline CSS, no JavaScript, Plone classic look (tabs, slate-blue links), built for legibility (black Verdana at 18px, AAA link contrast, visible focus, skip link).

## Editing

1. Edit the page sources in `src/`. Each file starts with `title:`, `description:`, and `name:` (the menu and breadcrumb label), then `---`, then the HTML body. Write `{root}` before internal links, e.g. `<a href="{root}services/">`.
2. Run `python3 tools/build.py`. It writes every page, `404.html`, `sitemap.xml`, `robots.txt`, `llms.txt`, `llm.txt`, and `llms-full.txt`, then checks the house rules: titles 50–60 characters, descriptions 140–160, no pipes, dashes, or hyphens in either, unique titles and descriptions, one h1 per page, no em dashes in the copy, `Chris'` (never `Chris's`), and first person singular.
3. Commit the sources and the generated files together, and push.

To add a page, create its source file and add it to `FILES` in `tools/build.py` (and to `TABS` if it gets its own tab).

Preview locally: `python3 -m http.server`, then open http://localhost:8000

## Search and AI

- Per-page title, description, canonical, Open Graph, and Twitter card; 1200×630 `social-card.png`.
- JSON-LD on every page: WebSite, ProfessionalService (Gerris Corp), Person (Chris, with `sameAs` to his profiles), the page itself, breadcrumbs, a `Service` on each service page, and `PodcastSeries` on The Show.
- `robots.txt` welcomes every crawler and names the AI crawlers explicitly. `llms.txt` lists every page; `llms-full.txt` holds the full text.
- IndexNow: the `<key>.txt` file, `tools/indexnow.py`, and `.github/workflows/indexnow.yml` ping Bing and the other IndexNow engines after each push, once gerriscorp.com really serves this site.
- `_config.yml` keeps `src/` and `tools/` off the public site.

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

# gerriscorp.com

Brochure site for Gerris Corp, served by GitHub Pages. Plain hand-written HTML: no build step, no framework, no JavaScript. The whole page weighs about 45 KB.

## Files

- `index.html`: the whole site, CSS inline. Paths are relative so the github.io preview works too.
- `logo.png` (400×400) and `social-card.png` (1200×630, for link previews)
- `404.html`, `manifest.webmanifest`, `.nojekyll` (serve files as-is)
- Search and AI: `robots.txt`, `sitemap.xml`, `llms.txt` (same as `llm.txt`), `llms-full.txt` (the full page as text), schema.org JSON-LD in `index.html` (WebSite, WebPage, ProfessionalService with priced offers, Person, FAQPage)
- IndexNow: the `<key>.txt` file at the root, `tools/indexnow.py`, `.github/workflows/indexnow.yml`. Pings Bing and the other IndexNow engines after each push, but only once gerriscorp.com is really serving this site.

## Editing

1. Edit `index.html`. If you change the title or description, change them everywhere they appear in the head and the JSON-LD (the checker catches mismatches). If you add a question to the visible FAQ, add it to the FAQPage JSON-LD too.
2. Bump `dateModified` in the JSON-LD and `<lastmod>` in `sitemap.xml`.
3. Run `python3 tools/check_site.py`. It rewrites `llms-full.txt` and checks: title 50–60 characters, description 140–160, no pipes, dashes or hyphens in either, matching og/twitter/schema copies, valid JSON-LD, FAQ questions present on the page.
4. Commit and push.

Preview locally: `python3 -m http.server`, then open http://localhost:8000

## Going live on gerriscorp.com

The site is a noindexed preview at https://chrisabraham.github.io/gerriscorp/ until these steps are done:

1. Remove the redirect from gerriscorp.com to chrisabraham.com at your DNS host. Point the apex at GitHub Pages with four A records: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (and optionally AAAA records 2606:50c0:8000::153, 8001::153, 8002::153, 8003::153). Add `www` as a CNAME to `chrisabraham.github.io`.
2. Add a `CNAME` file containing `gerriscorp.com`, and in the repo's Settings → Pages set the custom domain to `gerriscorp.com`. Once the certificate is issued, tick Enforce HTTPS.
3. Delete the `<meta name="robots" content="noindex">` line in `index.html`, run the checker, commit and push. The IndexNow workflow then submits the site.
4. Verify gerriscorp.com in Google Search Console (DNS TXT record) and Bing Webmaster Tools, and submit `https://gerriscorp.com/sitemap.xml` to both.

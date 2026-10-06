> A step by step website migration SEO checklist: URL inventory, 301 redirect map, template review, launch day checks, and the weeks of monitoring after.
>
> Source: https://gerriscorp.com/guides/migration-checklist/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# The website migration SEO checklist

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 5, 2026

Migrations lose traffic for predictable reasons: URLs that weren't mapped, redirects that weren't tested, templates that changed what crawlers see, and nobody watching afterward. This checklist covers each stage.

## Before you start
- Record a baseline: organic sessions and conversions by landing page from analytics, and clicks, impressions, and indexed pages from Search Console. Export them, because you'll compare against them for months.
- Decide the launch window. Avoid your busiest season.
- Make sure Search Console and Bing Webmaster Tools are verified for both the old and new sites, and that you'll keep access to the old domain if it's changing.

## Build the URL inventory

Combine every source, because each one misses something:
- A full crawl of the current site.
- Every URL in the XML sitemaps.
- Pages with clicks or impressions in Search Console over the last 16 months.
- Landing pages with traffic in analytics.
- URLs with external backlinks, from Ahrefs, Semrush, or Search Console's Links report.
- Images, PDFs, and other files that rank or receive links.

## Build the redirect map
- Map every old URL to its closest equivalent on the new site with a 301 or 308 permanent redirect.
- Redirect to the most relevant page, never to the home page in bulk. Google treats mass redirects to the home page like soft 404s.
- Make deliberate decisions about pages you're retiring: redirect them to a close substitute, or let them return 404 or 410 if nothing fits.
- Avoid chains. Every old URL should reach its final destination in one hop, including URLs that were already redirecting.
- Keep the map in a spreadsheet: old URL, new URL, status, reason. It's the document every later question goes back to.

## Review the new site before launch
- Crawl staging and compare titles, descriptions, headings, canonicals, and word counts with the old site, template by template.
- Check that the main content is in the server's HTML, so it doesn't depend on JavaScript.
- Check structured data, internal links, image alt text, and hreflang if you have more than one language.
- Test Core Web Vitals on the new templates.
- Keep staging blocked from search with authentication or noindex, and write down exactly how, so it can be removed at launch.

## Launch day
- Remove the staging block, and confirm production robots.txt and meta robots tags allow crawling.
- Test the redirect map in bulk against the live site: status codes, single hops, correct destinations.
- Submit the new XML sitemaps. Keep a sitemap of the old URLs available for a few weeks so Google recrawls them and discovers the redirects faster.
- For a domain change, use Google's Change of Address tool in Search Console and Bing's Site Move tool.
- Confirm analytics and tag tracking work on every template.
- If DNS changes, confirm that mail records were left untouched and email still arrives.

## The weeks after
- Watch Search Console daily for the first two weeks: page indexing, crawl stats, and 404s.
- Compare organic landing pages with the baseline, and investigate every important page that lost traffic.
- Fix redirect gaps as they appear in 404 reports and server logs.
- Update internal links that still point at old URLs.
- Ask the most valuable sites linking to you to update their links.
- Keep the redirects in place for at least a year, and ideally indefinitely.

## Special cases

### HTTP to HTTPS and www changes

Pick one canonical host and protocol, redirect every other combination to it in a single hop, and update canonicals, sitemaps, and internal links to match.

### Merging several sites into one

Map each old site's pages to their best home on the new one, and keep every old domain registered and redirecting. Old domains carry links for years.

### Moving to a JavaScript framework

Check that the new templates render their content on the server. A migration from a traditional CMS to a client-rendered app is a common way to lose content from Google and AI crawlers. See the [JavaScript SEO guide](https://gerriscorp.com/guides/javascript-seo/).

## What to expect

A well-run migration often shows some fluctuation for a few weeks while Google reprocesses the site, then settles. Domain changes take longer than platform changes on the same domain. A drop that deepens after the first month, or that's concentrated in one template, means something specific went wrong, and it's worth diagnosing rather than waiting out.

I run this process as [website migration support](https://gerriscorp.com/services/migrations/), before launch or after it.

## References
- [Google Search Central: Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)
- [Google Search Central: Redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

> What Google Search Console's Crawled, currently not indexed status means, how it differs from Discovered, and a step by step method to find the real cause.
>
> Source: https://gerriscorp.com/guides/crawled-not-indexed/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# "Crawled, currently not indexed": what it means and how to fix it

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 5, 2026

Google visited the page, read it, and decided not to put it in the index, at least for now. It's the most misunderstood status in Search Console, and the fix depends entirely on why Google made that call.

## Where you see it

In Google Search Console, open Indexing, then Pages. The "Why pages aren't indexed" table lists every reason Google has for leaving URLs out. "Crawled, currently not indexed" means Googlebot fetched the URL successfully and chose not to index it. Google gives no specific reason, and the status alone isn't an error. Every large site has some URLs here, and many of them deserve to be.

## How it differs from "Discovered, currently not indexed"

"Discovered, currently not indexed" means Google knows the URL exists and hasn't crawled it yet. That usually points to crawl priority: too many URLs, weak internal linking, a slow server, or a site Google doesn't consider worth crawling quickly. "Crawled, currently not indexed" means Google did crawl the page and judged it not worth indexing. One is about getting Google to look; the other is about what Google saw when it looked.

## Common causes
- **Thin or duplicate content.** Pages that say little, or say nearly the same thing as other pages: tag archives, near-identical location pages, product variants, and boilerplate-heavy templates.
- **Content hidden from the renderer.** The page looks rich to visitors, but Google's rendered HTML holds only the template, because the substance loads on scroll or click. The [JavaScript SEO guide](https://gerriscorp.com/guides/javascript-seo/) shows how to check.
- **Weak signals of importance.** Few internal links, no external links, buried deep in the site.
- **Low-value URL patterns.** Filter and sort parameters, internal search results, and session URLs that multiply without adding anything.
- **Soft 404s and empty states.** Out-of-stock or "no results" pages that return a 200 status.
- **A new or recently changed site.** Google is still deciding, and many URLs move into the index over the following weeks.

## A method that finds the real cause
1. **Export the examples.** Click the status in the report and export the URL list. Search Console shows a sample of up to 1,000 URLs.
2. **Group them by template.** Sort the URLs into page types: product, category, article, location, tag, parameter. A status spread evenly across the site tells a different story than a cluster in one template.
3. **Ask whether each group deserves indexing.** Parameter URLs, tag pages, and near-duplicates are often correctly excluded. Handle those with canonicals, noindex, or by removing the links that create them, and move on.
4. **Inspect the important ones.** For pages that should rank, run URL Inspection, test the live URL, and read the rendered HTML. Is the main content there? Is the canonical the URL you expect? Is the page returning 200?
5. **Compare with pages that are indexed.** Crawl both groups and compare word counts, internal links, duplication, and load time. The difference usually points at the cause.
6. **Check the dates.** Line up when the count started rising with deployments, template changes, migrations, and plugin updates.
7. **Keep other problems separate.** A backlink spike or a redirect error at the same time may be a coincidence. Investigate each on its own track until the data connects them.

## Fixes, by cause
- Thin or duplicate pages: merge them, expand them with real substance, or canonicalize them to the strongest version.
- Hidden content: render it in the server's HTML.
- Weak signals: link to the pages from relevant, indexed pages and from navigation where it makes sense.
- Low-value patterns: stop generating crawlable links to them, and keep them out with canonicals or noindex.
- Soft 404s: return a real 404 or 410, or give the page useful content.

After the fix ships, click "Validate fix" in the report. Validation takes days to weeks, and Google reprocesses pages at its own pace. Request indexing through URL Inspection for a handful of the most important pages.

## When it's a crisis

A sudden rise concentrated in your most valuable template, with a matching traffic drop, is a technical emergency, and it's usually a rendering or template change. A slow, even scatter across low-value pages is housekeeping. Telling the two apart is the first job.

I diagnose indexing problems as part of [technical SEO forensics](https://gerriscorp.com/services/technical-seo/) and [Search Console cleanup](https://gerriscorp.com/services/search-console/).

## References
- [Search Console Help: Page indexing report](https://support.google.com/webmasters/answer/7440203)
- [Google Search Central: JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

> Chris Abraham sets up Google Search Console and Bing Webmaster Tools properly, reads the indexing reports, and fixes the problems they reveal, page by page.
>
> Source: https://gerriscorp.com/services/search-console/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Google Search Console setup, cleanup, and indexing fixes

Search Console is the closest thing to a direct line into how Google sees your site. Most businesses have it set up badly or never look at it. I set it up properly and act on what it says.

## Setup done right
- A Domain property verified by DNS, so every subdomain and protocol is covered, plus URL-prefix properties where they help.
- The right people with the right permission levels, and former agencies and staff removed.
- XML sitemaps submitted and checked against what's actually indexable.
- Bing Webmaster Tools set up as well, because Bing's index feeds Microsoft Copilot and other AI assistants. It imports directly from Search Console.
- Search Console linked to GA4 where it's useful.

## Reading the reports

### Page indexing

The report that explains why pages aren't in Google: "Crawled, currently not indexed," "Discovered, currently not indexed," "Duplicate without user-selected canonical," "Alternate page with proper canonical tag," "Page with redirect," "Not found (404)," "Soft 404," and "Blocked by robots.txt." Each status has different causes and different fixes. The guide to ["Crawled, currently not indexed"](https://gerriscorp.com/guides/crawled-not-indexed/) covers the most misunderstood one.

### Performance

Clicks, impressions, and positions by query and page, which show what you rank for, what's slipping, and which pages earn impressions without clicks because their titles undersell them.

### URL Inspection

The live test shows the HTML Google rendered for a page, which is how I prove whether content is visible to Googlebot.

### Core Web Vitals, HTTPS, and enhancements

Field speed data by URL group, security problems, and structured data errors and warnings.

### Crawl stats

Found under Settings: how often Googlebot visits, what it fetches, and how fast your server responds. It's essential after migrations and server changes.

## Cleanup and fixes

I turn the reports into a list of real problems, ignore the noise, and fix the causes: redirects, canonicals, thin or duplicate pages, sitemap errors, blocked resources, and soft 404s. Then I request reindexing where it's worth it and watch the reports as Google recrawls.

## Common findings

The same problems turn up again and again: a property verified by an agency that no longer works with you, sitemaps listing redirected or noindexed URLs, parameter URLs multiplying in the index, staging sites indexed by accident, and important templates quietly dropping out of the index after a release.

## Common questions

### Should every page on my site be indexed?

No site needs every URL indexed. Filter pages, internal search results, tag archives, and near-duplicates are better left out. The goal is to get every page that deserves to rank into the index, and keep the rest out deliberately.

### Is a Search Console cleanup a one-time job?

The setup and first cleanup are a project. Monitoring fits naturally into [ongoing support](https://gerriscorp.com/services/ongoing-support/), since new problems appear whenever the site changes.

**Related:** ["Crawled, currently not indexed" explained](https://gerriscorp.com/guides/crawled-not-indexed/) · [Technical SEO](https://gerriscorp.com/services/technical-seo/) · [Website migrations](https://gerriscorp.com/services/migrations/)

[Ask me to read your Search Console](https://gerriscorp.com/contact/)

Updated October 5, 2026

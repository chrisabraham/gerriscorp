> The tools that carry a website migration safely: crawlers, Search Console, redirect testing, crawl comparison, and analytics, with the job each one does.
>
> Source: https://gerriscorp.com/guides/migration-tools/ · Updated 2026-10-13 · By Chris Abraham, Gerris Corp

# The SEO tools for a website migration, and the job each one does

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 13, 2026

No single product migrates a website for you. A migration is a handful of jobs, and each has a tool that does it well: an inventory, a redirect map, a pre-launch comparison, a launch day test, and weeks of watching. Here is the kit I use, matched to the job, with the free options where they exist.

## Job 1: list every URL that matters

The inventory is the foundation, and it comes from several tools at once, since no single source sees everything.
- **A crawler.** Screaming Frog SEO Spider, Sitebulb, or a similar desktop crawler finds every URL linked from the site. Screaming Frog's free version stops at 500 URLs; a licence removes the limit.
- **Google Search Console.** The Performance report, exported by page over the last twelve to sixteen months, lists the URLs that actually earn impressions, including ones no longer linked from anywhere.
- **Analytics.** Landing pages from GA4 or whatever you run, for the URLs people arrive on from every channel.
- **A backlink tool.** Ahrefs, Semrush, or Majestic for the URLs other sites link to, which carry value even if they earn no traffic.
- **The XML sitemaps** and, if you can get them, **server logs.**

Merge them into one spreadsheet with a row per URL and columns for clicks, links, and sessions. That's the list everything else is tested against.

## Job 2: build and store the redirect map

The map pairs each old URL with its closest new equivalent. A spreadsheet is fine for drafting. The finished map belongs wherever the new site serves redirects: the server configuration, the host's redirect rules file on Netlify, Vercel, or Cloudflare, or the framework's own configuration. In Next.js, for example, redirects live in `next.config.js`, and each rule's `permanent` flag decides between a 308 and a 307. Keeping the map in version control means it gets reviewed, and nobody loses it.

For large sites, pattern rules cover whole sections in one line, and exceptions handle the pages that don't fit the pattern. Test the patterns before launch, because one bad regex can redirect thousands of pages to the wrong place.

## Job 3: compare staging with the live site

Before launch, crawl both the live site and the staging site with the same settings, then compare them. Screaming Frog's crawl comparison does this with URL Mapping, which uses a regex to pair the staging hostname's URLs with the live ones. You see, template by template, which titles, descriptions, headings, canonicals, structured data, and internal links changed. It needs a licence and database storage mode.

Check the staging site's robots.txt and meta robots tags at the same time. Staging is supposed to be blocked from search. Production isn't, and the block coming across at launch is one of the most common migration disasters.

## Job 4: test every redirect on launch day

Once the redirects are live, crawl the old URL list in Screaming Frog's list mode with Always Follow Redirects switched on, as Screaming Frog's migration guide describes. The All Redirects report shows each old URL, where it finally lands, and every hop in between, so you can spot 404s, chains, loops, and temporary redirects in minutes. Run it again a day later, after caches have cleared.

For a quick spot check without a crawler, `curl -sI` on the command line shows the status code and the Location header for any single URL.

## Job 5: tell Google, then watch
- **Search Console sitemaps.** Google's site move guidance is to submit the sitemaps for both the old and new URLs, then watch the indexed count move from one to the other. Warnings that the old URLs redirect are expected.
- **The Change of Address tool,** for moves from one domain or subdomain to another, used after the redirects are in place. It doesn't apply to HTTP to HTTPS, www changes, or path changes within one site.
- **URL Inspection,** on a sample of important old and new URLs, to see Google's chosen canonical and indexing status.
- **The Performance report with a date comparison,** by page, to catch any section that loses more than the expected dip.
- **Bing Webmaster Tools,** the equivalent for Bing, which also supplies results to other search and AI products.
- **Server logs,** which Google also recommends checking during a move, to confirm Googlebot is crawling the new URLs and to catch error codes your crawler missed.

## Job 6: prove the move held

A few weeks after launch, crawl the new site again and compare it with the pre-launch staging crawl, and rerun the old URL list. Anything that drifted, such as a redirect someone edited or a template change that dropped schema, shows up as a difference. If the numbers have fallen and stayed down, the [migration recovery guide](https://gerriscorp.com/guides/migration-recovery/) covers what to do next.

## What a tool can't do

Every tool above reports facts. None of them decides which new page is the right home for an old one, whether a thin page should be merged or kept, or which redirect rule is safe on a site with forty thousand URLs. That judgment is the migration work itself, and it's why the inventory and the map deserve the most time.

I run migrations with this kit as [website migration SEO](https://gerriscorp.com/services/migrations/). For the full sequence, follow the [website migration checklist](https://gerriscorp.com/guides/migration-checklist/), and for redirect rules in depth, see [301 redirects explained](https://gerriscorp.com/guides/301-redirects/).

## References
- [Google Search Central: Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)
- [Search Console Help: Change of Address tool](https://support.google.com/webmasters/answer/9370220)
- [Screaming Frog: How to use the SEO Spider in a site migration](https://www.screamingfrog.co.uk/seo-spider/tutorials/how-to-use-the-seo-spider-in-a-site-migration/)
- [Screaming Frog: How to compare crawls](https://www.screamingfrog.co.uk/seo-spider/tutorials/how-to-compare-crawls/)
- [Next.js: redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

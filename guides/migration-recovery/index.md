> A recovery plan for a website migration that lost search traffic: rebuild the old URL list, test every redirect, compare old and new pages, and fix in order.
>
> Source: https://gerriscorp.com/guides/migration-recovery/ · Updated 2026-10-13 · By Chris Abraham, Gerris Corp

# Traffic fell after a site migration: how to find what broke and get it back

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 13, 2026

The new site launched, and organic traffic dropped and stayed down. Some dip is normal while Google recrawls. A drop that's still there after a month has a cause, and it's almost always one of a short list. Here is the recovery routine I run, in the order that finds the money fastest.

## First, separate normal turbulence from real loss

Google says to expect ranking fluctuations during any significant move, and that for a medium sized site it can take a few weeks or more before the new URLs gradually replace the old ones in results, longer for large sites. So the first question is shape. A dip that's recovering week over week is the move settling. A cliff that hasn't moved, or losses concentrated in one section, is a fault.

In Search Console, compare the four weeks after launch with the four weeks before, and look at pages rather than totals. Sort by lost clicks. The top twenty URLs usually account for most of the loss, and they tell you where to dig.

## Rebuild the list of old URLs

Every recovery starts with the URL inventory the migration should have started with. If nobody kept one, rebuild it from every source you can reach:
- The Search Console Performance report for the months before launch, exported by page.
- Analytics landing pages for the same period.
- The old XML sitemaps, from a backup or from the Wayback Machine.
- A backlink tool's list of linked URLs on your domain.
- Server logs, if the old host kept them.

Merge them and remove duplicates. This list, weighted by the traffic and links each URL carried, is what you'll test.

## Test every old URL's redirect

Screaming Frog's own migration guide describes the method. Switch to list mode, turn on Always Follow Redirects under Config > Spider > Advanced, upload the old URLs, and crawl them. The All Redirects export then shows each old address, the final address it lands on, the type of each hop, and whether a chain or a loop is involved.

Read the export for these failures, in this order:
1. **404s and soft 404s.** Old URLs with no redirect at all. On a big site these are usually whole patterns, such as an old category path or a dropped file extension.
2. **Redirects to the home page or a generic category.** Google treats a redirect to an unrelated page much like a missing page, and the old URL's value doesn't carry over.
3. **Temporary redirects.** Google's documentation says a permanent redirect shows the new target in results, while a temporary one keeps showing the source. A migration built on 302s or 307s is telling Google to keep the old URLs.
4. **Chains and loops.** Each extra hop slows crawling, and loops never resolve.
5. **JavaScript and meta refresh redirects.** Google ranks server side redirects as the most reliable way to signal a move. Anything else should be replaced with one.

## Compare old pages with their new versions

A redirect that lands on the right URL still loses traffic if the new page is weaker. If you have a crawl from before launch, compare it with a crawl of the new site in Screaming Frog's comparison mode, using URL Mapping to pair old and new addresses. Without one, archived copies of the top pages will do. Check each pair for:
- Titles, descriptions, and H1s that were rewritten, shortened, or replaced with a template default.
- Body copy cut down, split across tabs, or moved behind a script.
- Structured data that existed before and doesn't now.
- Internal links that used to point at the page and no longer do, which shows up as greater crawl depth.
- Canonical tags pointing at staging, at the old domain, or at the wrong page.
- A noindex or a robots.txt rule carried over from the staging site.

## Check that Google can see the new site the way you think

Use URL Inspection on a sample of the top lost URLs and their new equivalents. Look at Google's chosen canonical, the indexing status, and the rendered page. Check the old sitemap and the new one in the Sitemaps report: Google's guidance is to submit both during a move, and to expect the indexed count on the old one to fall as the new one rises. If the old URLs still show as indexed weeks later, Google isn't following your redirects as you intended.

For a move to a new domain, confirm the Change of Address request went in from the old property. Google's help is specific about when it applies: a move between domains or subdomains. HTTP to HTTPS, www to non-www, and path changes within one site don't use it.

## Fix in order of value

Recovery work goes fastest when it follows the money. Fix the redirects for the twenty URLs that lost the most first, then the patterns that cover hundreds of URLs at once, then content and template gaps on the pages that matter, then the long tail. Keep every redirect in place: Google recommends at least a year, and longer is better for people following old links.

After each round of fixes, run the list crawl again and confirm the failures are gone, then watch the affected pages in Search Console. Recovered pages usually come back over weeks, as Google recrawls them. I make no promise about full recovery, because rankings also move for reasons unrelated to the migration, but a site whose old URLs all resolve cleanly to equal or better pages has removed every cause it controls.

## Keep the evidence

Write down what you found, what you fixed, and when, with the before and after crawl exports. If traffic doesn't come back in the expected window, that record is what lets the next person separate a migration fault from an algorithm update or a seasonal dip.

I handle this as part of [website migration SEO](https://gerriscorp.com/services/migrations/), and for inherited projects that went badly, [project rescue](https://gerriscorp.com/services/rescue/). To prevent the next one, use the [website migration checklist](https://gerriscorp.com/guides/migration-checklist/) and the [tools I use for a website migration](https://gerriscorp.com/guides/migration-tools/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Google Search Central: Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)
- [Google Search Central: Redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
- [Search Console Help: Change of Address tool](https://support.google.com/webmasters/answer/9370220)
- [Screaming Frog: How to use the SEO Spider in a site migration](https://www.screamingfrog.co.uk/seo-spider/tutorials/how-to-use-the-seo-spider-in-a-site-migration/)
- [Screaming Frog: How to compare crawls](https://www.screamingfrog.co.uk/seo-spider/tutorials/how-to-compare-crawls/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

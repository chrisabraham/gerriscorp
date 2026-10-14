> Four static sites I own, measured with mobile Lighthouse, fixed in one afternoon, and measured again: analytics deferred, images resized, robots rules verified.
>
> Source: https://gerriscorp.com/case-studies/four-site-speed-pass/ · Updated 2026-10-14 · By Chris Abraham, Gerris Corp

# Four static sites: a speed and AI crawler pass in one afternoon

In October 2026 I ran a full speed and AI crawler review across four sites I own: this one, a second consulting site, Hill Mole, and a feed-driven archive of 465 pages. They were already fast by most standards. The review found one cause behind most of the remaining slowness, fixed it with a trade-off I could state in a sentence, and moved every page I measured to 89 or better on mobile, most of them to 97 or above.

## My role

Everything: measurement, diagnosis, the code changes in each site's build, verification, and deployment. The sites are mine, so every number here can be checked on the live pages.

## Method

I measured a home page and a typical inner page on each site with Lighthouse 12 in mobile mode, using the same throttling PageSpeed Insights applies. I tested each fix on a local build of the same code before shipping it. Separately, I crawled 41 pages per site with my own audit script, checking headings, structured data, canonicals, image dimensions and alt text, dates, robots directives, and whether every sitemap URL returned a 200 and was indexable.

## What I found
- **The analytics tag.** On three of the sites, gtag.js produced most of the main-thread blocking time, 575 to 1,291 milliseconds per page. The sites' own code was small.
- **Image weight on the archive.** Cover images were 800-pixel JPEGs. WebP at three sizes cut the image weight on an episode page by about 300 KB.
- **A render-blocking stylesheet on Hill Mole.** A 2 KB stylesheet held the first paint, and the 700-pixel banner was a GIF shown at 412 pixels on phones.
- **Small tap targets.** A dark-mode button 22 pixels tall, below the 24-pixel minimum.
- **An incomplete AI crawler list.** robots.txt named 14 AI agents and missed 9 newer ones. Every token I added came from the vendor's own documentation that day, which also showed that one Google fetcher had been renamed two months earlier.

The crawl found no structural problems: one H1 per page, valid structured data everywhere, clean canonicals, complete alt text, and no noindexed URL in any sitemap.

## What I changed

Analytics now loads on the visitor's first scroll, tap, or key press, or four seconds after the page loads, with every command queued until the script arrives. The archive serves WebP covers at 400, 600, and 800 pixels with the JPEG as the fallback. Hill Mole's stylesheet is inlined and its banner is served as WebP. The dark-mode button grew to 48 by 28 pixels. robots.txt on all four sites names the newer agents. And every site now carries a speculation rule that prefetches a same-site page when a reader hovers over or starts to tap its link.

## Results
| Page | Before | After |
| --- | --- | --- |
| This site, home | 65 | 100 |
| This site, service page | 79 | 97 |
| Second consulting site, home | 83 | 98 |
| Second consulting site, service page | 84 | 100 |
| Hill Mole, home | 98 | 100 |
| Hill Mole, entry | 98 | 100 |
| Archive, home | 75 | 89 |
| Archive, episode page | 70 | 97 |

Scores are mobile Lighthouse performance. Accessibility reached 100 on all eight pages.

## The trade-off

Deferring analytics means a visitor who leaves within about four seconds without touching the page is never counted. Every other pageview is recorded. I made that choice for my own sites and would put the same choice to a client in writing before shipping it.

## What it shows

A fast site can still carry one expensive habit, and the fix is often a single decision once the measurement names it. The audit took an afternoon because the sites are generated from code I control: each change went into a build script once and reached every page. See [site speed](https://gerriscorp.com/services/site-speed/) for the same review on your site.

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

Updated October 14, 2026

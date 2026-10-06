> A step by step method for finding why organic traffic fell: confirm the drop is real, isolate pages and queries, check updates and indexing, and name the cause.
>
> Source: https://gerriscorp.com/guides/traffic-drop/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# How to diagnose a Google traffic drop in Search Console

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Organic traffic fell and everyone wants an answer by Friday. The answer is almost always findable, and it comes from narrowing the drop down until only one explanation fits. This is the order I work in.

## 1. Confirm the drop is real

Start by ruling out measurement. Analytics can fall while search traffic is fine.
- Compare Google Analytics with Search Console clicks over the same dates. If Search Console is flat and analytics fell, the problem is tracking: a broken tag, a new consent banner, a site redesign that dropped the snippet from some templates.
- Check that the date ranges match in length and in days of the week. A Monday-to-Sunday week compared with a Thursday-to-Wednesday week shows a false drop on a business site.
- Compare with the same period last year. Many businesses fall every summer or every January, and that's seasonality.

One reporting change to know about: in September 2025 Google stopped supporting a parameter that rank-tracking tools used to load a hundred results at a time. Desktop impressions fell sharply for many sites and average position appeared to improve, with no change in clicks. A drop in impressions alone from that month is usually that.

## 2. Read clicks, impressions, CTR, and position together
| Pattern | Likely meaning |
| --- | --- |
| Impressions and clicks both fell, position fell | Rankings dropped: an algorithm update, a technical problem, or stronger competition |
| Impressions steady, clicks and CTR fell | The results page changed: an AI Overview, more ads, a new feature above you, or a rewritten title |
| Impressions fell, position steady | Fewer people are searching: seasonality, a news cycle ending, or a product falling out of fashion |
| Everything fell to near zero | The site is blocked, deindexed, or under a manual action |

## 3. Find where the loss is

Use the Compare option in the Performance report, then sort each tab by the change in clicks.
- **Pages.** Is the loss spread across the site, or concentrated in one section or template? A drop in one template points to something technical about that template.
- **Queries.** Separate branded searches from everything else with a regular expression filter on the brand name. Branded loss means fewer people are looking for the business; unbranded loss means rankings.
- **Countries and devices.** A drop on mobile alone suggests a mobile rendering or speed problem. A drop in one country suggests hreflang, a local competitor, or a regional update.
- **Search appearance and search type.** Lost rich results, or lost image and video traffic, show up here.

## 4. Line it up with dates

Find the first day of the decline as precisely as the daily data allows, then check what happened that week.
- **Google's Search Status Dashboard** lists confirmed core updates, spam updates, and incidents with start and end dates.
- **Your own changes.** Deploys, plugin and theme updates, CMS upgrades, migrations, CDN or security changes, new consent tools, and changes to robots.txt or redirects. Ask the developers for the deploy log.
- **Outside events.** A competitor's launch, a press story, a product recall.

## 5. Check the technical reports
- **Security and Manual actions.** One look, and either there's a notice or there isn't.
- **Page indexing.** A rise in "Crawled, currently not indexed," "Excluded by noindex," "Blocked by robots.txt," or "Duplicate, Google chose different canonical" that starts on the same date is a strong lead.
- **Crawl stats.** Under Settings: host status problems, a spike in server errors, slower response times, or a sudden change in crawl volume.
- **URL Inspection.** Run a live test on a page that lost traffic and read the rendered HTML. Content missing from Google's render is a common, invisible cause. The [JavaScript SEO guide](https://gerriscorp.com/guides/javascript-seo/) has the tests.

## 6. Separate the problems

Drops often have more than one cause at once: a core update lands the same month a redesign broke a template, or a backlink spam spike shows up beside a redirect error. Treat each candidate as its own hypothesis and test it against the data separately. When the evidence for each one points to different pages or different dates, they're different problems, and each gets its own fix.

## 7. Write it down

The deliverable is a short document: the size and start date of the drop, where it is concentrated, the cause, the evidence for it, the explanations that were ruled out and why, and the fix with tickets the developers can act on. Then mark the fix's ship date and watch the same report, filtered the same way, over the following weeks.

## Questions about traffic drops

### How fast does traffic recover after a fix?

A technical fix such as an unblocked template often recovers within weeks, as Google recrawls. Losses from a core update usually move only when Google runs a later update, after the content has improved.

### How far back does Search Console go?

Sixteen months. For longer history, set up the bulk export to BigQuery now, because it only collects data from the day it starts.

Finding the cause of lost traffic is the core of [technical SEO forensics](https://gerriscorp.com/services/technical-seo/). See also the [indexing recovery case study](https://gerriscorp.com/case-studies/indexing-recovery/).

## References
- [Google Search Central: Debugging drops in Google Search traffic](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
- [Google Search Status Dashboard](https://status.search.google.com/)
- [Search Console Help: Page indexing report](https://support.google.com/webmasters/answer/7440203)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

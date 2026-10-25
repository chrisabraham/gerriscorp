> When a traffic loss has two causes, one blended story produces the wrong fix. How to split the evidence, test each cause alone, and join them only on proof.
>
> Source: https://gerriscorp.com/guides/two-problems-at-once/ · Updated 2026-10-24 · By Chris Abraham, Gerris Corp

# When two problems hit at once, keep them on separate tracks

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 24, 2026

The hardest traffic losses to fix are the ones with two causes. Everyone wants one story, so the evidence for both gets poured into the same bucket, a single explanation forms, and the fix that follows repairs half the damage or none of it. I run every overlapping cause as its own investigation, with its own evidence and its own test, and I connect them only when the data does.

## Why one story feels right and fails

A single explanation is satisfying. It fits on one slide, it gives the team one thing to do, and it lets everyone stop worrying. When a site loses traffic in the same season that a spam link spike shows up in a backlink tool, the spike becomes the villain within a day, because it is visible, dated, and blamable on strangers.

The trouble is what happens next. The team ships the fix for the story it chose, waits six weeks, and reads the result. If the other cause was the bigger one, traffic keeps sliding and the fix looks like it failed, so a good fix gets abandoned. If both causes ease at the same time, the fix gets credit for a recovery it didn't produce, and the real cause returns with the next release. Either way the business pays for weeks of waiting and learns the wrong lesson.

## Signs you have more than one problem

Nobody announces that a drop has two causes. These are the patterns that tell me to split the work before anyone writes a ticket:
- **The decline has two shapes.** A slow slope across months plus a sudden step on one date is almost never one cause.
- **The losing pages don't share a template.** When product pages and the homepage both fall, one mechanism rarely explains both.
- **The dates don't line up.** If one page group started falling in February and another in April, an April event can't explain February.
- **Brand and nonbrand queries move differently.** Branded searches respond to reputation, links, and redirects; product and category searches respond to content, rendering, and indexing.
- **The first fix moved one metric and not the others.** That is the clearest sign of all, and the most often ignored.

## Open a track for each candidate cause

A track is a written hypothesis with four parts: what I think is happening, the evidence that supports it, the test that would prove it wrong, and the person who can fix it. Writing the disproof test first matters most. A hypothesis with no way to fail is a belief, and beliefs are how one story swallows two problems.

Each track gets its own page in the working document and its own heading in the report. Findings get filed under the track they support. A finding that seems to support both goes in a third place, marked as unassigned, until something decides it.

## Give each track its own evidence

Different causes leave fingerprints in different places, so each track gets the evidence that can actually speak to it:
- **Template problems** show up in a crawl. I compare what a crawler extracts from each page type with what a person sees in the browser. A product page that weighs over a megabyte but yields three hundred words of text to the crawler is a template problem, whatever else is going on.
- **Indexing problems** show up in Search Console's Page indexing report and in URL Inspection, grouped by template rather than read one URL at a time.
- **Date driven problems** show up when the Performance report is segmented by page group and query type and laid against a calendar of releases, migrations, confirmed Google updates, and changes to redirects or hosting.
- **Link and reputation problems** show up in the Links report and in third party backlink data, read for timing and pattern rather than for alarming totals.

Segmentation is where most blended stories fall apart. A sitewide traffic line hides everything. The same data split into homepage, category, product, and editorial pages, and then into branded and unbranded queries, usually shows two or three distinct curves, each with its own start date.

## Join the tracks only on proof

Two problems can be connected, and sometimes one causes the other. A redirect error can send link equity to the wrong place and depress branded rankings. A rendering failure can strip internal links and starve deeper pages of crawl attention. When that happens, I merge the tracks. What I need before merging is a shared mechanism, the same affected URLs, or the same date with a plausible path from one to the other. Coincidence in the same month is not enough, and neither is the fact that both problems are bad.

## A worked example

An ecommerce client lost a large share of organic sessions over several months. Two things were visibly wrong. Product templates mounted their specifications, FAQs, and reviews only when a shopper scrolled them into view, so crawlers received a heading, an image, a few bullets, and a price. Separately, in April, the backlink tools showed several hundred new spam links against a baseline of a few dozen, around the same weeks that homepage traffic and branded searches fell.

The tempting story was the spam. It was dated, it was dramatic, and it blamed someone outside the building. Split into tracks, the evidence told a different and more useful story. The rendering track was confirmed by crawl extraction on every major product page, by the template code itself, and by a cluster of clean product URLs sitting in "Crawled, currently not indexed." The April track explained the homepage and the brand queries, and it pointed at a redirect and URL handling issue as much as at the links. Neither track explained the other's pages. They went to different people as different tickets: server rendering to the developers, the redirect handling and the link review to me.

## Sequence the fixes so you can read the result

When two fixes ship in the same week, nobody can say afterward which one worked. Where the business can afford it, I ship them apart, with the larger or better proven fix first, and I annotate every release date in the reporting. Where both have to ship at once, I measure each against the page group and query segment it was meant to move, so a recovery in product pages counts for the rendering fix and a recovery in branded queries counts for the redirect fix.

Each fix gets an acceptance check on the live site before anyone waits for traffic: a plain fetch of a product page that returns the specifications, a redirect test that returns one hop to the right destination. Traffic takes weeks to respond. Whether the fix shipped correctly takes minutes to verify, and there is no reason to spend six weeks waiting on a fix that never deployed.

## What the owner hears

The written report keeps the tracks separate all the way to the summary. Leadership gets one paragraph per problem: what it is, what it costs, who fixes it, and how anyone will know it worked. Engineers get the technical evidence, also by track. Nobody gets a single blended villain, because a single villain is the most expensive thing a diagnosis can produce.

## How I handle this for clients

This is the core of my [technical SEO forensics](https://gerriscorp.com/services/technical-seo/) work. Every engagement starts with a paid diagnostic that ends in a cause per track, the evidence behind each, and a prioritized plan with an owner for every item. When the cause turns out to be content the crawler never sees, that track becomes [crawler visibility](https://gerriscorp.com/services/crawler-visibility/) work; when it becomes a ticket for your team, it gets a [developer spec with acceptance criteria](https://gerriscorp.com/services/developers/). For the single cause version of the method, start with [diagnosing a traffic drop in Search Console](https://gerriscorp.com/guides/traffic-drop/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Google Search Central: Debugging drops in Google Search traffic](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
- [Search Console Help: Performance report](https://support.google.com/webmasters/answer/7576553)
- [Search Console Help: URL Inspection tool](https://support.google.com/webmasters/answer/9012289)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

> Chris Abraham diagnoses traffic drops, indexing problems, slow pages, and redirect errors with evidence, then works with your developers until the fixes ship.
>
> Source: https://gerriscorp.com/services/technical-seo/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Technical SEO forensics and fixes

A site lost traffic and nobody knows why. My job is to find the mechanism, prove it, and get it fixed.

Technical SEO is the work that decides whether search engines and AI systems can find, render, understand, and trust your pages. It's the part of SEO I love most: on-page structure, site speed, 301 redirects, canonical tags, indexing, and Google Search Console. Most sites that underperform have a technical cause hiding in plain sight, and most of those causes leave evidence.

## When to call me
- Organic traffic fell after a redesign, a platform change, a template update, a hosting move, or for no visible reason.
- Search Console shows a growing pile of pages marked "Crawled, currently not indexed" or "Discovered, currently not indexed."
- Important pages rank below thin ones, or Google picks a different URL than the one you want.
- The site looks complete to people and nearly empty to crawlers.
- Pages are slow on phones, or Core Web Vitals are failing.
- Redirects have piled up over the years and nobody trusts them.

## What I check

### Rendering

What crawlers actually receive, compared with what a visitor sees. JavaScript frameworks and lazy-loading patterns can leave product details, reviews, and FAQs out of the HTML a crawler reads. I compare the raw HTML, the rendered DOM, and a crawler's extraction for the same page. The [JavaScript SEO guide](https://gerriscorp.com/guides/javascript-seo/) explains the method.

### Crawling and indexing

Robots rules, XML sitemaps, canonical tags, status codes, parameters, pagination, duplicate URLs, and how Google's chosen canonical compares with yours. I read the Search Console page indexing report as a set of clues, then confirm each with URL Inspection and a crawl.

### Redirects and broken links

Chains, loops, temporary redirects that should be permanent, redirects to irrelevant pages, and internal links that still point at old URLs.

### On-page structure

Titles, meta descriptions, heading order, internal linking, image alt text, and whether each page says plainly what it's about.

### Site speed and Core Web Vitals

Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift, measured from real users where data exists and from lab tests where it doesn't. The usual culprits are oversized images, render-blocking CSS and JavaScript, third-party scripts, web fonts, and slow servers or missing caching.

### Structured data

Schema.org JSON-LD for your organization, people, products, services, articles, and breadcrumbs, and whether it matches the visible page.

### Off-site signals

Backlink anomalies such as a sudden spike in spam links, and whether they matter at all.

## One cause at a time

Two problems often arrive together: a template change and a spam link spike, or a redirect error and a seasonal dip. I keep each on its own track until the data connects them, so every fix targets a proven cause and nobody spends a quarter fixing the wrong thing.

## What you get
- Findings with evidence: crawl data, Search Console reports, rendered HTML comparisons, and example URLs.
- The mechanism, explained in plain language for owners and in technical detail for developers.
- A prioritized list of fixes, each with an owner and an expected effect.
- Developer tickets with affected URLs, observed behavior, the fix, and acceptance criteria.
- A check of the live site once the fixes ship, and a follow-up read of Search Console as Google recrawls.

I make the changes I have access to myself, in the CMS or the repository, and work with your developers on the rest. See [working with your developers](https://gerriscorp.com/services/developers/).

## Tools

Google Search Console, GA4, Screaming Frog, Semrush, Ahrefs, PageSpeed Insights and the Chrome UX Report, Cloudflare, browser developer tools, and the command line.

## Common questions

### How long does a technical SEO diagnostic take?

Usually one to three weeks, depending on the size of the site, the access I have, and how many separate problems turn up. I agree the questions and the timeline in writing before I start.

### What access do you need?

Search Console and analytics access, a staging or production URL I can crawl, and ideally read access to the CMS or repository so I can find the template behind a problem.

### Do you fix things or only report them?

Both. I fix what I have access to and write developer-ready tickets for changes that belong in the codebase, then check the result once it's live.

### How soon will traffic recover after the fixes?

Google has to recrawl and reprocess the affected pages first, which takes days for important pages and weeks or months for large sites. I track the recovery in Search Console and report what changes.

**Related:** ["Crawled, currently not indexed" explained](https://gerriscorp.com/guides/crawled-not-indexed/) · [JavaScript SEO](https://gerriscorp.com/guides/javascript-seo/) · [Website migrations](https://gerriscorp.com/services/migrations/)

[Tell me what happened to your traffic](https://gerriscorp.com/contact/)

Updated October 5, 2026

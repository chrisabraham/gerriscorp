> How Chris Abraham traced a Magento and Hyvä store's falling traffic to Alpine.js sections that never rendered for Googlebot, and kept two problems apart.
>
> Source: https://gerriscorp.com/case-studies/ecommerce-rendering/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Magento store: product content Googlebot never saw

An equipment retailer on Magento 2 with the Hyvä theme had been losing organic traffic for months. Brand searches and the home page were down while non-brand category traffic was growing, a pattern that didn't fit any single explanation.

## My role

Forensic diagnosis and technical direction, working alongside the client's contractor, who owns implementation.

## What I found

### Track one: rendering

The product templates used Alpine.js to mount the specifications, FAQs, and reviews only when a visitor scrolled them into view, with `x-intersect` wrapped around `x-if`. Googlebot never scrolls the way a person does, so those sections never mounted. A Screaming Frog crawl extracted thousands of words from category pages but only 250 to 400 words from flagship product pages that weighed more than 1.2 MB. Search Console showed a selective cluster of product URLs in "Crawled, currently not indexed," while the rest of the site indexed normally.

### Track two: backlinks and redirects

In the same period, a spike of spam, adult, and warez backlinks arrived, mostly from cloud-hosting address ranges, alongside a 301 redirect problem. I kept this on its own track, collected the evidence, and asked for upgraded Search Console access to examine it properly, without folding it into the rendering story.

## What I recommended
- Render the product sections in the server's HTML and keep the scroll animation as progressive enhancement.
- An A/B test that removes the scroll gates from a group of product pages first, so the effect can be measured before a full rollout.
- A separate investigation and cleanup plan for the backlink spike and the redirect problem.

## How it was checked

Raw HTML, rendered DOM, and crawler extraction compared on the same URLs, Search Console's live test used to see what Google rendered, and the indexing cluster matched to the affected template.

## Status

Diagnosis delivered and the test scoped; implementation sits with the client's contractor. The method is written up in the [JavaScript SEO guide](https://gerriscorp.com/guides/javascript-seo/) and on [content the crawler never sees](https://gerriscorp.com/services/crawler-visibility/).

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

Updated October 5, 2026

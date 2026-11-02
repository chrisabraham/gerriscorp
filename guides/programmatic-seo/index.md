> What programmatic SEO is, where database driven pages earn their place, why Google leaves them unindexed, and the playbook that fixes a set at scale.
>
> Source: https://gerriscorp.com/guides/programmatic-seo/ · Updated 2026-11-02 · By Chris Abraham, Gerris Corp

# Programmatic SEO: what it is, where it works, and why Google ignores it

By [Chris Abraham](https://gerriscorp.com/about/) · Published November 2, 2026

Programmatic SEO publishes pages from a database instead of an editor: one template, thousands of rows of structured data, and a page for every row, each aimed at a long-tail search. Built on real data, it produces some of the most useful pages on the web. Built on swapped variables and nothing else, it produces pages Google crawls once and refuses to index.

## What is programmatic SEO?

Programmatic SEO is a publishing method with two working parts. The first is a data layer: a structured table of entities, such as products, properties, places, routes, or practitioners, where every row carries that entity's attributes. The second is a template layer: page designs that render one row each, under a predictable URL pattern. Point the templates at the table and the site gains a page for every row, each one matched to a query pattern such as {product} price, {service} in {city}, or {city} to {city} flights.

Every content management system renders templates, so templating alone is not the method. Programmatic SEO begins when the database decides how many pages exist and which searches each page targets. A single build can create a few hundred pages or a few million, and nothing in the build checks whether each page deserves to exist. That check is the whole job, and it belongs to the people publishing, because Google performs its own version of it later and publishes the verdict in Search Console.

## Where does programmatic SEO work?

It works where every row holds facts that are true of that entity alone, facts a rival cannot reproduce by renaming a variable. The durable examples share that property:
- **Property listings.** Price, beds, baths, photographs, floor area, days on market, and sale status. Two listings on the same street differ in ways a buyer acts on.
- **Product databases.** Specifications, price, stock, compatibility, manuals, and owner reviews. A parts catalog page answers questions no article could answer as well.
- **Location pages carrying genuine local data.** The address, the hours, the staff, the services that branch actually offers, local inventory, and reviews of that branch. A location page earns its URL with the branch's real record.
- **Pages computed from live data.** Prices, comparisons, schedules, and conversions drawn from feeds that change, so the page a visitor reads today differs from last month's because the facts moved.

The test takes ten seconds. Hide the names, read two pages from the set side by side, and ask whether a visitor could tell them apart and learn something different from each. If the answer is yes, the set is publishing. If the pages collapse into one page wearing different nouns, Google reaches the same conclusion.

## Why do programmatic pages fail to get indexed?

Indexing is a selection, and a template set that differs only in swapped variables gives Google nothing to select. The failure modes stack:
- **Near duplication.** Google crawls a sample of the set, compares the pages, and finds the same text arranged around different names and numbers. The rest of the set waits in "Discovered, currently not indexed" or falls into "Crawled, currently not indexed," the status the [guide to Crawled, currently not indexed](https://gerriscorp.com/guides/crawled-not-indexed/) takes apart.
- **No unique value per URL.** An indexed page has to be a good answer to something. A page whose only unique tokens are a city and a product name answers nothing its siblings fail to answer.
- **Weak internal linking.** Generated sets often sit deep in the site, reachable only through paginated archives or a sitemap file. Pages that nothing links to read as pages nobody values, and crawlers budget their visits accordingly.
- **Crawl waste.** Combinations, parameters, and sort orders multiply URLs far beyond the entity count, and Googlebot spends visits on variants while new or changed real pages wait. The [faceted navigation guide](https://gerriscorp.com/guides/faceted-navigation/) covers the catalog version of this trap.
- **Site-level drag.** Thousands of weak URLs feed the quality signals Google computes for the whole domain and the crawl rate it grants. A flood in one template can slow indexing for pages that were never part of the flood.

## What does Google's scaled content abuse policy say?

In March 2024, Google added scaled content abuse to its [spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies). The policy names the practice plainly: generating many pages primarily to manipulate search rankings, with little or no value added for the people who land on them, is spam. The method of production makes no difference. Automation, human writers, and a mixture of the two all fall under the same rule, and the examples Google gives include bulk-generated pages published without added value, material scraped or stitched from other sources, and many sites used to hide a scaled operation.

The policy judges the output and its purpose, never the technique. A database behind a page is ordinary publishing, and has been since the first catalog went online. A database behind ten thousand pages that exist to catch queries, carrying nothing a visitor could use, is the abuse. Sites that cross the line risk demotion or removal under the spam policies, and the cleanup takes far longer than the publishing did. Any programmatic project should be planned against that standard from the first template, because retrofitting value into a published flood is the expensive direction.

## How do you fix a programmatic site Google will not index?

Work at the level of the template and the dataset, never page by page. A set of fifty thousand URLs has perhaps six problems, one per template, and fixing templates fixes the set.
1. **Audit each template against demand and data.** For every page type, write down the searches it targets and the facts unique to each row. A type with no real demand and no unique data is a removal candidate, however many pages it has already published.
2. **Feed the survivors real data.** Live prices and availability, local facts, photographs, reviews, computed comparisons: material a competitor cannot produce by renaming a variable. Where the data cannot be obtained, the honest move is to shrink the set until it matches the data on hand.
3. **Chunk the content.** Break each template into blocks that each answer one question: the specification table, the price block, the local details, the questions buyers actually ask, each under a descriptive heading. Readers scan blocks, and answer engines extract from blocks. A wall of prose with variables poured in defeats both.
4. **Match schema to the page type.** Product pages carry Product data, listings carry the listing type, locations carry LocalBusiness, and hubs carry ItemList, always describing content the visitor can see. The [structured data guide](https://gerriscorp.com/guides/structured-data/) sorts the types worth using from the ones Google retired.
5. **Rebuild internal linking as hub and spoke.** A hub for each category or region links down to every spoke beneath it; spokes link back to the hub and across to true siblings. Keep the set a few clicks from the home page, keep the sitemap limited to pages meant for the index, and treat [internal linking architecture](https://gerriscorp.com/services/internal-linking/) as part of the publishing system rather than decoration added later.
6. **Prune what cannot justify itself.** Delete the combinations nobody searches for, consolidate near-duplicates into the strongest URL with redirects, and noindex the variants visitors need but engines do not, such as sort orders and filter states. Pages nothing links to and nobody needs can go with a 410. A smaller set in which every page carries real facts recrawls faster and indexes better than a large set diluted by filler.
7. **Earn real links.** Publish the interesting edges of the dataset: rankings, research, tools, and local data that journalists, partners, and customers cite. Links into the hubs lift the whole set, while a large inventory with no links pointing at it asks Google to take the site's word for its importance.

Measure the result by template in Search Console's Page indexing report. Movement shows over weeks as Google recrawls the set, and on a pruned site the strongest pages usually get picked up first.

## Questions about programmatic SEO

### Is programmatic SEO against Google's rules?

No. The spam policies ban scaled content abuse: many pages produced to manipulate rankings with little value added. A database-driven page carrying real facts about a real entity is ordinary publishing, and some of the most heavily indexed pages on the web are built exactly that way.

### How many pages is it safe to generate?

The policies set no number. Safety scales with data: a million listings backed by live records index well, while a thousand city pages carrying swapped names struggle. Count the unique facts on each page rather than counting pages.

### Why does Google crawl my pages and still refuse to index them?

Crawling is cheap and indexing is a judgment. Google samples the set, finds pages that differ mainly in variables, and declines to spend index space on the rest. The [guide to Crawled, currently not indexed](https://gerriscorp.com/guides/crawled-not-indexed/) gives the full method for confirming the cause on a specific site.

### Should thin pages be noindexed or deleted?

Delete pages nobody needs and nothing links to; a 410 tells Google the removal was deliberate. Noindex pages visitors still need, such as filtered views, so they stay reachable while leaving the index. Consolidate pages that split one topic into near copies into the strongest URL and redirect the rest.

### Does adding schema get programmatic pages indexed?

No. Schema describes a page; it cannot give a page value. Accurate, type-matched structured data helps engines understand and display a page that already deserves indexing, and wasted schema on thin pages changes nothing.

### How long does recovery take after a prune?

Expect the first movement in weeks and the full picture across a quarter. Google recrawls at its own pace, strongest pages first. Track the Page indexing report template by template and resist republishing the pruned set while the recrawl is under way.

I run this diagnosis as a fixed-fee [indexing audit](https://gerriscorp.com/services/indexing-audit/). See also [the programmatic indexing case study](https://gerriscorp.com/case-studies/programmatic-indexing/) and the [faceted navigation guide](https://gerriscorp.com/guides/faceted-navigation/) for the catalog version of the crawl problem.

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Google Search Central: Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google Search Central: Managing crawl budget for large sites](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget)
- [Google Search Central: Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

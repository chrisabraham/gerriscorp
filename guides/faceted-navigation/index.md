> How product filters create millions of crawlable URLs, when crawl budget becomes a real problem, and how to decide which filter pages deserve to be indexed.
>
> Source: https://gerriscorp.com/guides/faceted-navigation/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Faceted navigation SEO: filters, parameters, and crawl budget

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Filters are how shoppers narrow a catalog: size, color, brand, price, rating. Every combination can become its own URL, and a store with a few thousand products can produce millions of them. Google spends its time crawling those combinations instead of the pages that sell.

## How the problem grows

A category with ten colors, eight sizes, twelve brands, and five price bands has 4,800 single combinations before sort order, page number, and the order the parameters appear in. Multiply by every category and the site has far more filter URLs than products. Most of them show the same handful of items, many show none, and almost nobody searches for them.

Google's documentation names faceted navigation as the most common cause of crawling problems it sees, and its December 2024 guidance on the subject is the clearest statement of what it wants.

## When crawl budget actually matters

Google says crawl budget is a concern mainly for sites with more than a million unique pages that change weekly, or more than ten thousand pages that change daily. Smaller sites rarely need to think about it. The signs that a site has crossed the line:
- New products take weeks to appear in Google.
- Search Console's Page indexing report shows a large and growing count of "Discovered, currently not indexed."
- Crawl stats show most of Googlebot's requests going to parameter URLs.
- Server logs show Googlebot fetching filter combinations far more often than product pages.

Server logs are the definitive source. Search Console shows a sample; the logs show every request Googlebot made and where its time went.

## Decide which filters deserve pages

Some filtered views match real searches. "Women's trail running shoes," "red sofa," and "Makita cordless drills" are all a category plus one filter, and each can be a strong landing page. Use keyword research to find the combinations with search demand, usually one filter deep and occasionally two. Give each one a clean, permanent URL such as `/shoes/womens/trail/`, a unique title and heading, some introductory text, and links from the category navigation. Everything else stays a convenience for shoppers and stays out of the crawl.

## Keep the rest away from crawlers

Google's guidance offers two approaches for filter URLs that shouldn't be indexed.
- **Block them in robots.txt.** Disallow the parameters that create combinations, such as `Disallow: /*?*color=`. This stops crawling immediately and saves the most budget. The [robots.txt guide](https://gerriscorp.com/guides/robots-txt/) covers the syntax.
- **Use URL fragments.** Filters applied after a `#`, handled by JavaScript, never create new crawlable URLs, because Google ignores fragments.

Other tools are weaker for this job:
- **Canonical tags** pointing filter pages at the category consolidate signals over time, and Google still has to crawl every URL to read them, so they save no crawl budget.
- **noindex** keeps pages out of results and also has to be crawled to work. Over time Google crawls noindexed pages less often.
- **nofollow on filter links** discourages crawling and is a hint Google may disregard.

Search Console's URL Parameters tool, which used to handle this, was retired in 2022.

## If filter pages must be crawlable
- Use the standard `&` separator and the same parameter order every time, so one combination has one URL.
- Return a 404 for combinations with no products, and for nonsense values. A "no results" page with a 200 status becomes a soft 404 and wastes crawls.
- Keep sort order and items-per-page out of the URL, or block them, since they reshuffle the same products.
- Limit how many filters can be stacked into one crawlable URL.

## Pagination

Paginated category pages are different from filters: they list different products, and they're how crawlers reach products deep in a catalog. Keep them crawlable with plain links, let each page declare itself as canonical, and keep pages from going on forever by giving categories sensible sizes.

## Measure the change

Before changing anything, record the share of Googlebot requests going to parameter URLs, the count of discovered and unindexed pages, and how long new products take to be indexed. After the change, watch the same numbers. On large catalogs the shift in crawl toward products shows up within weeks, and the indexing of new products speeds up soon after.

Crawl control for big catalogs is the focus of [large-site SEO](https://gerriscorp.com/services/large-sites/) and [ecommerce SEO](https://gerriscorp.com/services/ecommerce/). See also the [programmatic indexing case study](https://gerriscorp.com/case-studies/programmatic-indexing/).

## References
- [Google Search Central: Managing crawling of faceted navigation URLs](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation)
- [Google Search Central: How to specify a canonical URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

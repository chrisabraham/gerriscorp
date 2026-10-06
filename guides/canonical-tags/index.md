> How rel canonical works, why Google sometimes overrides it, the Search Console statuses that reveal canonical problems, and the mistakes that misdirect signals.
>
> Source: https://gerriscorp.com/guides/canonical-tags/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Canonical tags: how Google chooses which URL to index

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Most sites publish the same content at more than one address: with and without tracking parameters, sorted and filtered, printed, paginated, or copied across domains. Google picks one address from each group to show in results. The canonical tag is how you tell Google which one you prefer.

## What the tag does

A canonical tag is a line in the page's head:

```
<link rel="canonical" href="https://example.com/shoes/trail-runner/">
```

It says: this page is a copy, or the original, of the content at that address, and that address is the one to index. Google consolidates ranking signals such as links onto the chosen URL and shows it in results. The duplicates stay reachable for visitors.

For files without a head, such as PDFs, the same instruction can go in an HTTP header: `Link: <https://example.com/guide.pdf>; rel="canonical"`.

## A hint, weighed against other signals

Google treats the canonical tag as a strong hint. It weighs the tag together with redirects, internal links, the URLs listed in the XML sitemap, hreflang annotations, and a preference for HTTPS and for shorter, cleaner URLs. When the signals agree, Google follows the tag almost every time. When they disagree, Google decides for itself.

A typical conflict: every product page declares a clean canonical URL, while the navigation, the sitemap, and the breadcrumbs all link to a version with a parameter. Three signals point one way and one points the other, and Google may side with the majority.

## The Search Console statuses

The Page indexing report shows canonical decisions in three statuses.
- **Alternate page with proper canonical tag.** The page points elsewhere, and Google agreed. This is working as intended.
- **Duplicate without user-selected canonical.** Google found duplicates with no canonical tag and picked one itself. Add tags so the choice is yours.
- **Duplicate, Google chose different canonical than user.** You named one URL and Google picked another. Look for conflicting signals, or for pages that are more different than you think.

URL Inspection shows both the user-declared canonical and the Google-selected canonical for any page, which settles individual cases.

## The rules I apply
- **Every indexable page declares itself.** A self-referencing canonical guards against parameter copies that other sites and ad platforms create.
- **Absolute URLs.** Include the protocol and host. Relative canonicals are valid, and they break the moment a page is served from a staging host or a second domain.
- **The target returns a 200.** A canonical pointing at a redirect, a 404, or a noindexed page sends contradictory instructions.
- **One tag per page, in the head.** Two different canonicals cancel each other, and Google ignores canonical tags in the body. Plugins and themes that each add their own tag are the usual cause.
- **In the server's HTML.** A canonical inserted or changed by JavaScript may be read late or not at all. If the raw HTML and the rendered HTML disagree, fix the template.
- **Internal links match.** Navigation, breadcrumbs, and sitemaps link to the canonical version.

## Common mistakes
- **Pagination pointing to page one.** Page two of a category holds different products from page one. Each paginated page should declare itself. Google stopped using rel prev and next as an indexing signal in 2019, so plain crawlable links between the pages do that job.
- **Canonical and noindex together.** One says "index that other page instead," the other says "index nothing." Pick one.
- **Every page pointing at the home page.** A template bug that copies the home URL into every canonical can remove most of a site from results within weeks.
- **Canonicals to the HTTP version, or to the old domain.** Leftovers from a migration that nobody updated.
- **Product variants.** Color and size variants that differ only by a parameter usually canonicalize to the main product. Variants that people search for by name, such as a specific model, may deserve their own indexable pages.

## Across domains

A canonical can point to another domain, which is how a business that runs two sites with overlapping content can concentrate signals on one. For syndicated articles republished by partners, Google's current advice is that the partner should block indexing of its copy with noindex, because a cross-domain canonical on a large partner site doesn't always win against that site's own authority.

## Canonical or redirect

When visitors never need the duplicate URL, redirect it. A 301 is a stronger signal, and nobody lands on the copy. Use a canonical when the duplicate has to keep working, such as a filtered view, a tracking link, or a print version.

Canonical audits are part of [technical SEO forensics](https://gerriscorp.com/services/technical-seo/) and [large-site SEO](https://gerriscorp.com/services/large-sites/). For the related indexing status, see [Crawled, currently not indexed](https://gerriscorp.com/guides/crawled-not-indexed/).

## References
- [Google Search Central: What is canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization)
- [Google Search Central: How to specify a canonical URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

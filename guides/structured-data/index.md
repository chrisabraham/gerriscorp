> Which schema.org markup still earns rich results in Google, which types were retired, how JSON LD helps search engines and AI understand entities, and testing.
>
> Source: https://gerriscorp.com/guides/structured-data/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Structured data in 2026: which schema markup is worth adding

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Structured data is a machine-readable description of what a page is about: this is a product with this price, this is a business at this address, this article was written by this person. It can earn enhanced listings in Google, and it helps every system that reads the page, including AI assistants, understand the facts without guessing.

## The format

Use JSON-LD: a block of JSON in a `script` tag with the type `application/ld+json`, using the vocabulary from schema.org. Google supports Microdata and RDFa too, and recommends JSON-LD because it sits apart from the visible HTML and is easy to generate from a template. A minimal example for a business:

```
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://example.com/#business",
  "name": "Example Consulting",
  "url": "https://example.com/",
  "telephone": "+1 555 0100",
  "address": {"@type": "PostalAddress", "addressLocality": "Arlington",
              "addressRegion": "VA", "postalCode": "22204", "addressCountry": "US"}
}
</script>
```

## What still earns rich results

Google has narrowed the list of types that change how a result looks. In 2023 it limited FAQ rich results to well-known government and health sites and dropped How-to rich results. In 2025 it retired several more, including Claim Review, Estimated Salary, and Vehicle Listing, and stopped showing breadcrumb trails on mobile results. The types that still produce visible features include:
- **Product**, with offers, price, availability, shipping, and return policy, for product snippets and merchant listings.
- **Review snippets and aggregate ratings** on products, recipes, books, software, and other eligible types. Reviews of your own business on your own site are excluded.
- **Organization and LocalBusiness**, for the logo and business details Google uses in knowledge panels.
- **Article**, for headline, image, dates, and author.
- **Event, JobPosting, Recipe, VideoObject, and Course list**, each tied to its own search feature.
- **BreadcrumbList**, still shown on desktop and still useful for understanding site structure.

Google's search gallery in its developer documentation is the current list, and it changes, so check it before building anything around a feature.

## Markup without a rich result still helps

A retired rich result doesn't make the markup useless. FAQPage markup no longer produces dropdowns for most sites, and it still states plainly which question each answer belongs to. Search engines use structured data to understand entities: who the business is, who wrote the page, which person is which, and how they relate. Microsoft's Bing team has said that schema markup helps its language models understand content. When an assistant has to decide whether two mentions refer to the same business, consistent structured data across the web removes doubt.

## Build a connected graph

The strongest pattern is one graph per page, where each thing has an `@id` and refers to the others by it. The WebSite is published by the Organization. The Organization is founded by the Person. The Article is written by the Person and is about the Service. Every page on this site carries a graph like that, built from one template, so the facts never contradict each other.
- **sameAs** links an entity to its profiles elsewhere: a Wikipedia article, Wikidata, a professional profile, a Google Business Profile. Those links are how systems confirm identity.
- **Stable identifiers.** Use the same `@id` for the same entity on every page.
- **The same facts everywhere.** Name, address, phone, founding date, and founder should match the visible page, the business profile, and the directories.

## Rules that keep markup safe
- **Mark up only what visitors can see.** Reviews, prices, and FAQs in the markup must appear on the page. Hidden or invented markup can earn a manual action for spammy structured data, which removes rich results for the whole site.
- **Keep it current.** A price or an event date in the markup that disagrees with the page is a quality problem. Generate the markup from the same data as the page.
- **Server-rendered.** Google can read JSON-LD injected by JavaScript, and many other crawlers can't. Put it in the HTML.

## How to validate it
- **Google's Rich Results Test** shows which rich results a page is eligible for and flags missing required properties.
- **The Schema Markup Validator** at validator.schema.org checks any schema.org markup against the full vocabulary, including types Google ignores.
- **Search Console** lists each detected rich result type under Enhancements, with valid and invalid counts across the site and alerts when a template breaks.

## Questions about structured data

### Is structured data a ranking factor?

Google says it isn't a direct ranking factor. It affects how results look and how well Google understands the page, and both of those affect clicks.

### Can a plugin handle it?

Yoast, Rank Math, and Shopify themes add sensible defaults for common types. For a connected graph, custom business types, or multiple plugins that each add their own markup, it usually needs a hand-built template.

I build schema and entity markup as part of [on-page SEO](https://gerriscorp.com/services/on-page-seo/) and [AI search visibility](https://gerriscorp.com/services/ai-search/) work.

## References
- [Google Search Central: Introduction to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Google Search Central: Local business structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

> When an English language business needs hreflang for the US, UK, Canada, Australia, Ireland, and New Zealand, how to write the tags, and errors that void it.
>
> Source: https://gerriscorp.com/guides/hreflang/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# hreflang for English-language sites serving the US, UK, Canada, and Australia

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

A business that sells in several English-speaking countries often ends up with near-identical pages for each one. hreflang tells Google which version belongs to which audience, so a shopper in Leeds sees prices in pounds and a shopper in Toronto sees Canadian dollars. Written wrong, it does nothing at all.

## Do you need it?

hreflang is for sites with separate versions of a page for different languages or regions. One English site that serves everyone the same content needs none. The tags start paying off when the versions differ in ways that matter to the visitor:
- Prices and currency
- Shipping, taxes, returns, and delivery times
- Legal terms, regulated claims, and contact details
- Spelling and vocabulary: color and colour, sneakers and trainers, apartment and flat

Without hreflang, Google sees several pages saying almost the same thing, may pick one as canonical for every country, and shows the American page in Australia. With it, Google treats the pages as a set and swaps in the right member for each searcher.

## The codes

Each value is an ISO 639-1 language code, optionally followed by an ISO 3166-1 country code:
| Audience | Code |
| --- | --- |
| United States | `en-US` |
| United Kingdom | `en-GB` (never en-UK, which isn't a valid code) |
| Canada, English | `en-CA` |
| Canada, French | `fr-CA` |
| Australia | `en-AU` |
| New Zealand | `en-NZ` |
| Ireland | `en-IE` |
| English speakers anywhere else | `en` |
| Fallback for everyone unmatched | `x-default` |

The language is required. A country on its own, such as `gb`, is read as a language code, and since there's no language with that code, the annotation is ignored.

## Writing the tags

Every version in the set lists every version, including itself:

```
<link rel="alternate" hreflang="en-US" href="https://example.com/us/boots/">
<link rel="alternate" hreflang="en-GB" href="https://example.com/uk/boots/">
<link rel="alternate" hreflang="en-AU" href="https://example.com/au/boots/">
<link rel="alternate" hreflang="x-default" href="https://example.com/boots/">
```

The same block goes on the US, UK, and Australian pages. The annotations can also live in the XML sitemap, which is easier to maintain on large sites, or in HTTP headers for files such as PDFs. Pick one method. Mixing them invites the two copies to drift apart, and a set that disagrees with itself is ignored.

## The rules that void it
- **Missing return links.** If the UK page names the US page and the US page doesn't name the UK page back, Google ignores the pair. This is the most common failure.
- **Pointing at non-canonical URLs.** Every URL in the set should return a 200 and declare itself as canonical. A UK page whose canonical points at the US page tells Google to drop the UK page, and hreflang can't override that.
- **Relative or mixed URLs.** Use full absolute URLs, with the same protocol and host style used everywhere else.
- **Tags only in JavaScript.** Put them in the server's HTML or in the sitemap.

## How to structure the versions
- **Subfolders** such as `/uk/` and `/au/` on one domain share all its authority and are the simplest to run. This is my default recommendation.
- **Country domains** such as `.co.uk` and `.com.au` send the strongest local signal and build trust with local buyers, and each domain has to earn its own links.
- **Subdomains** such as `uk.example.com` work, with more setup and no real advantage over subfolders.

## Don't redirect by location

Redirecting visitors automatically by IP address hides versions from Google, because Googlebot crawls mostly from the United States and would only ever see the American pages. Let every URL load for everyone, and offer a banner that suggests the local version. hreflang handles search; the banner handles direct visitors.

## Bing

Bing gives hreflang less weight and looks more at the `content-language` meta tag and the page's `lang` attribute. Set `<html lang="en-GB">` on UK pages, and so on, so both engines get a clear signal.

## Checking it

Search Console retired its International Targeting report in 2022, so checking falls to crawlers. Screaming Frog and Sitebulb both validate hreflang sets, flag missing return links and non-canonical targets, and export the errors by page. After that, search from each country with a VPN or with Google's country settings and confirm the right page appears. Spot check a few sets by hand as well: open the source of each version and confirm the block of annotations is identical on every page in the set.

I sort out international setups as part of [technical SEO](https://gerriscorp.com/services/technical-seo/) and [ecommerce SEO](https://gerriscorp.com/services/ecommerce/) engagements, for clients across the English-speaking world.

## References
- [Google Search Central: Tell Google about localized versions of your page](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google Search Central: Managing multi-regional and multilingual sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

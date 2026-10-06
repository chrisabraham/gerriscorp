> How robots.txt rules are matched, why a Disallow rule still lets pages be indexed, how to handle AI crawlers, and how to test robots.txt changes before launch.
>
> Source: https://gerriscorp.com/guides/robots-txt/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# How robots.txt works, and the mistakes that cost traffic

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

robots.txt is a plain text file at the root of a site that tells crawlers which paths they may fetch. It's small, it's public, and a single wrong line in it can take a site out of Google. Here's how it actually behaves.

## Where it lives and what it covers

The file must sit at the root of the host, such as `https://example.com/robots.txt`. It applies only to that exact protocol and host: `www.example.com`, `shop.example.com`, and the HTTP version each need their own. Google reads up to 500 kibibytes of it and generally caches it for up to a day, so changes take effect within about 24 hours.

## The syntax

```
User-agent: *
Disallow: /cart/
Disallow: /search
Allow: /search/help

User-agent: GPTBot
Disallow: /

Sitemap: https://example.com/sitemap.xml
```
- **User-agent** starts a group of rules for a named crawler. `*` means every crawler that has no group of its own. A crawler obeys only the most specific group that names it and ignores the rest, so a bot with its own group skips everything under `*`.
- **Disallow** and **Allow** take a path prefix. `Disallow: /search` blocks `/search`, `/search?q=shoes`, and `/searching`.
- **Wildcards.** `*` matches any characters, and `$` anchors the end. `Disallow: /*.pdf$` blocks every URL ending in .pdf.
- **Conflicts.** When an Allow and a Disallow both match, Google uses the longer, more specific rule, and Allow wins a tie.
- **Sitemap** lines can appear anywhere and apply to every crawler.

Google ignores `Crawl-delay`; Bing honors it. Google also stopped supporting `Noindex` lines in robots.txt in 2019.

## Blocking crawling is different from blocking indexing

This is the most expensive misunderstanding. Disallow stops a crawler from fetching a page. It doesn't stop the URL from being indexed. If other pages link to a blocked URL, Google can index the address alone, with no content, and Search Console reports it as "Indexed, though blocked by robots.txt."

To keep a page out of results, let it be crawled and give it a `noindex` robots meta tag or an `X-Robots-Tag: noindex` header. Google has to fetch the page to see that instruction, so a page that's both disallowed and noindexed stays in the index, because the noindex is never read. For content that must stay private, use a login. robots.txt is public, and listing secret paths in it advertises them.

## Status codes matter
- **200**: Google follows the rules in the file.
- **404 or another 4xx**: Google treats the site as having no restrictions and crawls everything.
- **500 or another 5xx, or a timeout**: Google treats the whole site as disallowed and pauses crawling. If the error lasts, Google falls back to its last good copy, and after about a month without one it treats the site as unrestricted.

A server or firewall that errors only on robots.txt can quietly stop all crawling, which is why it's one of the first URLs I check on a site that lost traffic.

## AI crawlers

Each AI company publishes the user agents it uses, and each honors robots.txt. They split into crawlers that gather training data, such as GPTBot, ClaudeBot, and CCBot, and crawlers that fetch pages for live answers, such as OAI-SearchBot, Claude-SearchBot, and PerplexityBot. Google-Extended and Applebot-Extended are tokens rather than separate crawlers: they control whether content fetched by Googlebot and Applebot may be used for AI models, and blocking them leaves ordinary search crawling alone. The [AI assistants guide](https://gerriscorp.com/guides/ai-assistants/) lists which crawler feeds which product.

This site lets every AI crawler read everything, and keeps the Markdown copies of its pages out of traditional search engines, so they never compete with the HTML pages. Because a crawler follows only its own group, naming the search engines in one group and the AI crawlers in another gives each its own rules:

```
User-agent: Googlebot
User-agent: Bingbot
Allow: /
Disallow: /*.md$

User-agent: GPTBot
User-agent: ClaudeBot
User-agent: PerplexityBot
Allow: /
```

## Mistakes I find most often
- **The staging file goes live.** `Disallow: /` protects a staging site, gets copied to production at launch, and blocks everything. Check robots.txt on launch day before anything else.
- **Blocking CSS and JavaScript.** Google renders pages, and a disallowed script folder can leave it looking at a broken layout with missing content.
- **Blocking parameters that carry real pages.** A broad rule like `Disallow: /*?` also blocks paginated categories and filtered pages that rank.
- **A bot's own group dropping the general rules.** Adding a group for one crawler without repeating the shared rules gives that crawler free run of everything else.

## Testing changes

Search Console's robots.txt report shows the version Google last fetched, when it fetched it, and any parsing errors. Before changing a live file, test the proposed rules against a list of important URLs with a parser that follows Google's rules, such as Google's open-source robots.txt library or a crawler like Screaming Frog with a custom robots.txt. Then confirm the change in Search Console after Google picks it up.

robots.txt is part of every [crawler visibility audit](https://gerriscorp.com/services/crawler-visibility/) and every [technical SEO](https://gerriscorp.com/services/technical-seo/) engagement I run.

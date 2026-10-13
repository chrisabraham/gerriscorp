> A Next.js App Router SEO checklist: metadata, canonicals, title templates, streamed metadata, sitemap.ts, robots.ts, 308 redirects, real 404s, and schema.
>
> Source: https://gerriscorp.com/guides/nextjs-seo/ · Updated 2026-10-13 · By Chris Abraham, Gerris Corp

# A Next.js SEO checklist for the App Router

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 13, 2026

Next.js gives you everything a search engine needs, as code: metadata, sitemaps, robots rules, redirects, and status codes. Every one of them can also be left at a default that quietly hurts you. This is the list I work through on every Next.js site, in the order I check it.

## 1. Every route sets its own title and description

In the App Router, metadata comes from a `metadata` object or a `generateMetadata` function exported from a layout or page. Static pages can use the object. Pages built from data, such as products, posts, and locations, need `generateMetadata` so each URL gets its own title and description from its own record.

Both exports work only in Server Components, which keeps the tags in the server's HTML. If a page needs client side features, keep `page.tsx` as a Server Component and move the interactive parts into a child component.

## 2. The title template does what you meant

A `title.template` in the root layout, such as `'%s | Brand'`, adds a suffix to every child page's title, and `title.default` fills in for pages that set none. That's convenient, and it's also how a site ends up with 2,000 pages titled with the brand name alone. Crawl the site and sort titles by frequency: any title used more than a few times is a page that fell through to the default.

## 3. Canonicals are set per route, with a metadataBase

Set `metadataBase` once in the root layout, then give each route `alternates.canonical`. Next.js combines the two into a full URL. Check the output on routes with query strings and on paginated lists, where a template canonical copied from the parent layout can point every page at page one.

## 4. You know what crawlers receive when metadata streams

When `generateMetadata` waits on request time data, Next.js can stream the page first and append the metadata tags to the body once they resolve. It does that for crawlers it expects to run JavaScript, such as Googlebot, and blocks rendering to put the tags in the head for a list of HTML limited bots, including Bingbot, social preview bots, and several others. GPTBot, ClaudeBot, and PerplexityBot are absent from the default list in the Next.js source. If AI crawler visibility matters to you, fetch your key pages with those user agents and check where the title and canonical land. The `htmlLimitedBots` option in the Next.js config lets you add them, at some cost in response time.

## 5. The sitemap is generated, complete, and honest

An `app/sitemap.ts` file that returns an array of URLs produces `/sitemap.xml`. Generate it from the same data source as the routes, include only canonical, indexable URLs that return 200, and set `lastModified` from the content's real update date rather than the build time. Large sites can split into several sitemaps. Compare the sitemap with a crawl: every URL in one should be in the other.

## 6. robots.ts says what you mean, for each crawler

An `app/robots.ts` file generates `/robots.txt`, with rules per user agent and a sitemap line. Decide deliberately about AI crawlers, and make sure preview and staging deployments disallow everything while production allows what you intend. A single environment variable deciding which robots file ships is a common source of a production site that tells every crawler to stay out.

## 7. Redirects are permanent where you mean permanent

Redirects in `next.config.js` take a `source`, a `destination`, and a `permanent` flag. With `permanent: true` Next.js returns a 308, the permanent status that tells browsers and search engines to remember the move. With `false` it returns a 307, a temporary redirect that nothing caches. A migration map written with `permanent: false` tells search engines to keep the old URLs. Check every rule's flag, and test the map against a crawl of the old site.

## 8. Missing pages return a real 404

Calling `notFound()` renders the not-found page, returns a 404, and adds a noindex tag. One catch: if the check runs inside a Suspense boundary after the response has started streaming, the status is already sent, so the page keeps its 200 and relies on the noindex tag. Run the existence check before streaming begins on routes where a real 404 matters, such as products and posts that get deleted. Then crawl a list of deliberately broken URLs and confirm the status codes.

## 9. JSON-LD is rendered in the component

The Next.js recommendation is a plain `<script type="application/ld+json">` in the layout or page, built from the same data as the visible content. Escape the `<` character in the JSON, as the Next.js guide shows, so content from a CMS can't inject script. Validate a sample from each template with the Rich Results Test or the Schema Markup Validator.

## 10. Navigation uses real links

The `Link` component extends the HTML anchor element, so it produces an `<a href>` that crawlers can follow. Navigation built from buttons with `router.push` in a click handler produces no link at all. Search the codebase for click handlers that navigate, and crawl with JavaScript rendering off to see which pages are reachable from plain HTML.

## 11. The rendered page matches the server page

Finally, compare the raw HTML with the rendered DOM on each template, and run the pages in headless Chrome to collect console errors. Hydration mismatches, content that loads only after interaction, and client side redirects all show up here. The [guide to React hydration errors](https://gerriscorp.com/guides/hydration-errors/) covers the most common fault.

## Make the checklist permanent

Every item above can become an automated check in the build, so a future change can't undo it. That's the subject of [adding SEO tests to your website's build](https://gerriscorp.com/guides/seo-build-checks/).

I work through this list, and fix what it finds, as part of [SEO engineering](https://gerriscorp.com/services/seo-engineering/) for Next.js and React sites. If you're bringing me into your repository, start with [how to give an outside SEO safe access](https://gerriscorp.com/guides/repository-access/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Next.js: generateMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)
- [Next.js: sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
- [Next.js: robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)
- [Next.js: redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
- [Next.js: notFound](https://nextjs.org/docs/app/api-reference/functions/not-found)
- [Next.js: JSON-LD](https://nextjs.org/docs/app/guides/json-ld)
- [Next.js: Link component](https://nextjs.org/docs/app/api-reference/components/link)
- [Next.js source: HTML limited bot list](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

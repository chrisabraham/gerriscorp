> A practical test for JavaScript SEO: compare raw and rendered HTML, check Search Console, find content that needs a scroll or click, and fix it on the server.
>
> Source: https://gerriscorp.com/guides/javascript-seo/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# How to tell if JavaScript is hiding your content from Google and AI

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 5, 2026

A page can look complete in a browser and nearly empty to a crawler. When the important content depends on JavaScript, search engines may see less of it, later, and AI crawlers may not see it at all.

## How crawlers handle JavaScript

Googlebot renders pages with an up-to-date version of Chromium, so it can run JavaScript. Rendering happens in a queue after the initial crawl, though, and the renderer behaves like a very patient visitor who never clicks, never types, and never scrolls the way a person does. It loads the page with a tall viewport and takes a snapshot. Content that waits for a click, a real scroll event, or a user action can be missing from that snapshot.

Most AI crawlers are simpler. GPTBot, ClaudeBot, PerplexityBot, and similar crawlers generally fetch the HTML the server sends and read it without running JavaScript. If your product details, prices, reviews, or answers exist only after scripts run, those crawlers see a shell.

## Five tests that settle it

### 1. Compare view-source with the rendered page

Open the page, then open view-source. View-source shows the HTML your server sent; the Elements panel in developer tools shows the DOM after JavaScript ran. Search view-source for a sentence from the content you care about. If it's missing, crawlers that don't render can't see it.

### 2. Fetch it from the command line

```
curl -sL https://example.com/products/widget-200 | grep -c "Specifications"
```

A count of zero means the text isn't in the server's HTML.

### 3. Disable JavaScript

Turn off JavaScript in your browser's developer tools and reload. What remains is roughly what a non-rendering crawler gets.

### 4. Ask Google directly

In Search Console, run URL Inspection on the page, click "Test live URL," then "View tested page" and the HTML tab. That's the HTML Google rendered. If your content is missing there, Google doesn't have it.

### 5. Crawl both ways

Crawl a sample of pages in Screaming Frog with JavaScript rendering off, then on, and compare word counts by template. In one diagnosis I ran, category pages yielded thousands of words while flagship product pages yielded 250 to 400 words despite weighing more than a megabyte, which pointed straight at the product template.

## Common causes
- **Client-side rendering.** Single-page apps that send an empty HTML shell and build the page in the browser.
- **Content that loads on scroll or interaction.** Sections rendered only when they enter the viewport after a real scroll, such as Alpine.js `x-if` combined with `x-intersect`, or reviews fetched when a visitor scrolls near them.
- **Content that loads on click.** Tabs and accordions that fetch their content when opened. Tabs that merely hide content already in the HTML are fine.
- **Links without real URLs.** Navigation built with click handlers instead of `<a href>` links, which crawlers can't follow.
- **Infinite scroll without paginated URLs.** Products beyond the first batch never get a crawlable link.
- **Metadata changed by JavaScript.** Titles, canonical tags, or robots directives rewritten after load, so the raw HTML and the rendered page disagree.
- **Blocked resources.** JavaScript or CSS files disallowed in robots.txt, which prevents Google from rendering the page properly.

## Fixes
- **Render on the server.** Server-side rendering or static generation puts the content in the initial HTML. Next.js, Nuxt, SvelteKit, Astro, and similar frameworks do this well when pages are configured for it.
- **Keep content in the HTML and hide it with CSS.** In Alpine.js, `x-show` keeps an element in the DOM and only toggles visibility, while `x-if` removes it entirely until the condition is true. Use animation as progressive enhancement on content that's already present.
- **Use real links and paginated URLs** for navigation and long lists.
- **Put titles, canonicals, and structured data in the server's HTML**, and keep them unchanged after load.
- **Avoid dynamic rendering** as a long-term answer. Google describes serving crawlers a separately rendered version as a workaround, and server rendering is the durable fix.

## Writing the ticket

Developers fix these problems fastest with evidence: the affected template, example URLs, the word count with and without rendering, the Search Console live test result, and a testable definition of done, such as "a curl of the product URL returns the specification table." There's a [sample ticket on the developers page](https://gerriscorp.com/services/developers/).

I diagnose rendering problems as part of [technical SEO forensics](https://gerriscorp.com/services/technical-seo/).

## References
- [Google Search Central: JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [OpenAI: Overview of OpenAI crawlers](https://platform.openai.com/docs/bots)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

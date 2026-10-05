> Pages that look complete to visitors and empty to Google and AI crawlers: how Chris Abraham finds the cause on Magento, WordPress, and React sites.
>
> Source: https://gerriscorp.com/services/crawler-visibility/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Content the crawler never sees

The page looks complete in a browser. Googlebot and the AI crawlers get a shell. There are no crawl errors anywhere, only a growing pile of pages marked "Crawled, currently not indexed" and traffic that won't come back. This is the diagnosis I'm best known for.

## One failure, many stacks

The same class of failure keeps turning up on completely different technology. In a single year I found it on three different stacks:

### Magento with Hyvä: content mounted on scroll

Product specifications, FAQs, and reviews were wrapped in Alpine.js directives that only rendered them once a shopper scrolled down. Crawler extraction on the store's most valuable product pages fell to a few hundred words, and exactly those pages piled up in Search Console's not-indexed report. [Read the Magento case study](https://gerriscorp.com/case-studies/ecommerce-rendering/).

### WordPress media site: consent management blocking the page

The cookie consent platform held back scripts until a visitor accepted, including the script that opened the tabs holding every article. A crawler never accepts cookies, so it met empty tabs everywhere. [Read the consent case study](https://gerriscorp.com/case-studies/consent-blocking/).

### React event platform: links crawlers couldn't follow

Server-side rendering was already in place, yet event pages stayed undiscovered because the cards navigated with JavaScript click handlers instead of anchor links. [Read the React case study](https://gerriscorp.com/case-studies/react-event-platform/).

## The pattern behind all three

In each case the page was technically "there." Visitors saw it, the CMS showed it, and no tool reported an error. The failure only appears when you look at the page the way a crawler does: no scrolling, no clicking, no cookie consent, and often no JavaScript at all. That's why it survives for months, and why ordinary SEO audits miss it.

## How I find it
1. **Compare three views of the same page:** the raw HTML the server sends, the DOM after JavaScript runs, and what a crawler extracts.
2. **Crawl with and without rendering,** and compare word counts and links by template. A template that loses most of its text without JavaScript stands out at once.
3. **Ask Google directly** with Search Console's live URL test, and read the rendered HTML it returns.
4. **Read the code** for the template responsible, often with an AI coding assistant searching the repository alongside the crawl evidence, until the exact mechanism is clear.
5. **Keep other problems separate.** A backlink spike or redirect error in the same month gets its own investigation.

## What you get
- The mechanism, proven with side-by-side evidence.
- A developer spec with the affected templates, example URLs, the fix, and acceptance criteria, such as "a plain fetch of a product URL returns the specification table."
- Verification once the fix ships, in the raw HTML and in Search Console.

## Why it matters more every year

Google renders JavaScript, slowly and imperfectly. Most AI crawlers don't render it at all. As more buyers ask ChatGPT, Perplexity, Claude, and Gemini instead of searching, content that exists only after scripts run is invisible to a growing share of the people looking for you. The [JavaScript SEO guide](https://gerriscorp.com/guides/javascript-seo/) shows how to run the first tests yourself.

## Common questions

### How do I know if my site has this problem?

Search view-source for a sentence from your most important content. If it's missing, crawlers that don't run JavaScript can't see it. A growing "Crawled, currently not indexed" count in one template is another strong sign.

### Does the fix require a rebuild?

Rarely. Most fixes change how one template renders a few sections, such as rendering on the server, keeping content in the HTML and toggling visibility with CSS, or using real links.

**Related:** [JavaScript SEO guide](https://gerriscorp.com/guides/javascript-seo/) · ["Crawled, currently not indexed"](https://gerriscorp.com/guides/crawled-not-indexed/) · [Technical SEO forensics](https://gerriscorp.com/services/technical-seo/)

[Ask me what Google actually sees](https://gerriscorp.com/contact/)

Updated October 5, 2026

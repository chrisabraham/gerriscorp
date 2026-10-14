> One script tag tells Chrome to fetch a page while the reader decides to click. How prefetch and prerender differ, which eagerness to pick, and what to exclude.
>
> Source: https://gerriscorp.com/guides/speculation-rules/ · Updated 2026-10-14 · By Chris Abraham, Gerris Corp

# Speculation rules: make the next page open instantly in Chrome

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 14, 2026

Speculation rules are a short block of JSON in a script tag that tells Chrome and Edge which links to load before the reader clicks them. When the reader does click, the page is already in memory and opens at once. I added one rule to every site I run in October 2026. It costs nothing in browsers that don't support it, and on a static site it takes about five minutes.

## Prefetch or prerender

A prefetch downloads the next page's HTML and holds it in memory without rendering it. A prerender goes further: Chrome's documentation says the page behaves as if it had been opened in an invisible background tab, then is shown when the reader arrives. Prerender is faster still and uses more memory and bandwidth, and it runs the page's scripts before anyone sees the page.

I use prefetch. It removes the network wait, which is most of the delay on a static site, and it runs no scripts early, so analytics, consent tools, and anything else that should only run for a real visit behave exactly as before. Prerender suits sites whose pages are heavy to render and whose scripts are built to handle it. Chrome also caps how much it will speculate: its documentation allows up to 50 immediate prefetches and 10 immediate prerenders per page, so a rule that matches every link on a long page cannot flood the network.

## Choose the eagerness

Eagerness sets how early Chrome acts on a rule. The four levels, from Chrome's documentation:
- **immediate:** as soon as the rule is seen.
- **eager:** on desktop, when the pointer rests on a link for 10 milliseconds; on mobile, shortly after a link enters the viewport.
- **moderate:** on desktop, when the pointer rests on a link for 200 milliseconds, or on pointer down if that comes first; on mobile, using viewport heuristics after the reader stops scrolling.
- **conservative:** on pointer or touch down, the default for rules that match links on the page.

Moderate is the setting I use. A 200-millisecond hover is a good signal of intent, and it fetches few pages the reader never opens.

## The rule I use

```
<script type="speculationrules">
{"prefetch": [{"where": {"and": [
  {"href_matches": "/*"},
  {"not": {"href_matches": ["/*.md", "/*.txt", "/*.xml"]}}
]}, "eagerness": "moderate"}]}
</script>
```

It matches every same-site link and excludes the files no reader opens in a browser: Markdown copies, llms.txt, and XML feeds and sitemaps. Exclude anything with side effects as well. A logout link, an "add to cart" URL, or any GET request that changes state must never be prefetched. On a static site there are none; on an application, list them.

## Check that it works

Open the site in Chrome, open DevTools, and go to the Application panel. Under background services, the speculative loads view lists the rules Chrome found on the page and the status of each speculation: not triggered, running, ready, or failed, with the reason for any failure. Hover over a link for a moment and watch its entry change. The Network panel shows the prefetch request itself.

Chrome marks speculative requests with a Sec-Purpose request header, set to prefetch for a prefetch. That gives servers and log analysis a way to separate speculative fetches from real visits. A static host serves the page either way. A site that counts visits on the server side should exclude requests carrying that header, so prefetches never inflate the numbers.

## Browser support

Chrome and Edge support speculation rules, with eagerness settings since version 121. Firefox does not support them, and Safari has them behind a flag. Unsupported browsers ignore the script tag, so the rule degrades to an ordinary link.

## What it changes

Lighthouse measures a single page load, so speculation rules leave its scores where they were. What changes is the second page: the reader clicks and the page is already there. That is the part of speed a visitor notices most. In field data, the prefetched page's Largest Contentful Paint starts from a page already in memory, so real-user loading times improve once enough visits have been recorded.

## Where I fit

I add speculation rules as part of a [site speed](https://gerriscorp.com/services/site-speed/) engagement, along with the work Lighthouse does measure: render-blocking resources, image sizes, and third-party scripts. For the measurement side, start with my guide to [Core Web Vitals](https://gerriscorp.com/guides/core-web-vitals/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Chrome for Developers: Prerender pages in Chrome for instant page navigations (updated January 23, 2026)](https://developer.chrome.com/docs/web-platform/prerender-pages)
- [MDN: Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
- [web.dev: Largest Contentful Paint](https://web.dev/articles/lcp)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

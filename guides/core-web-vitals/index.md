> What Google measures with Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift, how to read field data, and the fixes for each one.
>
> Source: https://gerriscorp.com/guides/core-web-vitals/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Core Web Vitals explained: LCP, INP, CLS, and the fixes that work

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Core Web Vitals are three measurements of how a page feels to real visitors: how fast the main content appears, how quickly the page responds, and how much it jumps around. Google uses them in ranking as part of page experience. They matter more to visitors than to rankings, and that alone makes them worth fixing.

## The three measurements
| Metric | What it measures | Good | Poor |
| --- | --- | --- | --- |
| LCP, Largest Contentful Paint | Time until the biggest image or text block in view finishes rendering | 2.5 seconds or less | Over 4 seconds |
| INP, Interaction to Next Paint | Delay between a tap, click, or key press and the screen visibly responding, across the whole visit | 200 milliseconds or less | Over 500 milliseconds |
| CLS, Cumulative Layout Shift | How much visible content moves unexpectedly while the page is in use | 0.1 or less | Over 0.25 |

INP replaced First Input Delay in March 2024. FID only measured the first interaction; INP watches every interaction and reports one of the slowest, which is why many sites that passed under FID fail under INP.

## Field data and lab data

Google's assessment uses field data: measurements from real Chrome users, collected in the Chrome User Experience Report over a rolling 28 days. A page passes when the 75th percentile of visits meets the good threshold for all three metrics. Mobile and desktop are judged separately.

Lab data comes from a single simulated load, such as a Lighthouse run. It's useful for debugging and for testing a fix before it ships, and it can't measure INP at all, because nobody clicks anything during a lab test. Lighthouse reports Total Blocking Time as a stand-in. A perfect Lighthouse score with failing field data is common, and the field data is the one that counts.

## Where to read it
- **PageSpeed Insights** shows field data for the URL and for the whole origin at the top, and a Lighthouse lab run below it.
- **Search Console's Core Web Vitals report** groups URLs with similar problems, usually by template, and tracks them over time. Fixing one template often fixes thousands of URLs.
- **Chrome DevTools**, in the Performance panel, records a real session on your own machine, shows each interaction's timing, and highlights layout shifts.
- **Real user monitoring**, through Google's web-vitals JavaScript library or a commercial tool, collects the metrics from your own visitors, with the element and script responsible attached.

## Fixing LCP

Break LCP into its parts: time to first byte, the delay before the browser discovers the LCP resource, the time to download it, and the time to render it. Fix whichever part is largest.
- **Slow server response.** Cache HTML at a CDN, speed up database queries, and remove redirects in front of the page.
- **Late discovery.** Put the hero image in the HTML as an ordinary `img` tag with `fetchpriority="high"`. A background image set in CSS, or an image inserted by JavaScript, is found late.
- **Lazy loading the hero.** `loading="lazy"` belongs on images below the fold. On the LCP image it delays the most important download on the page.
- **Heavy files.** Serve images at the size they're displayed, in WebP or AVIF, with `srcset` for different screens.
- **Render blocking.** Large stylesheets and synchronous scripts in the head hold back the first paint. Inline the critical CSS and defer the rest.

## Fixing INP

Poor INP almost always means the browser's main thread was busy when the visitor interacted. The culprits are long JavaScript tasks.
- **Third-party scripts.** Chat widgets, heatmaps, tag managers full of old tags, and ad scripts. Audit them, remove the ones nobody uses, and load the rest after the page is interactive.
- **Heavy event handlers.** A click that triggers a large re-render or a synchronous calculation blocks the next paint. Show visual feedback first, then do the work, and break long tasks up so the browser can paint in between.
- **Hydration.** Frameworks such as React and Vue attach their behavior after load, and interactions during that window wait. Smaller bundles, partial hydration, and server components shorten it.

## Fixing CLS
- Give every image and video `width` and `height` attributes, or a CSS `aspect-ratio`, so the browser reserves the space.
- Reserve fixed space for ads, embeds, and cookie banners, or show banners as overlays that cover content instead of pushing it.
- Load web fonts with `font-display: swap` and a fallback font sized to match, or use system fonts, as this site does.
- Never insert content above what the visitor is already reading, unless they asked for it.

## How much it matters

Page experience is one ranking signal among hundreds, and relevance wins. A slow page with the best answer still outranks a fast page with a weak one. The business case is visitors: faster pages convert better, and slow mobile pages lose people before they ever see the offer. I treat Core Web Vitals as a quality bar every template should clear, and I fix the templates in order of the traffic and revenue they carry.

Speed work is its own service: [site speed, Core Web Vitals, and Cloudflare](https://gerriscorp.com/services/site-speed/). For the CDN side, see [Cloudflare settings for SEO](https://gerriscorp.com/guides/cloudflare-seo/).

## References
- [Google Search Central: Understanding Core Web Vitals and Google search results](https://developers.google.com/search/docs/appearance/core-web-vitals)
- [web.dev: Web Vitals](https://web.dev/articles/vitals)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

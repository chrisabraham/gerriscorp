> Chris Abraham makes sites fast on real phones: Core Web Vitals, image and script optimization, caching, and Cloudflare CDN setup, rules, and redirects.
>
> Source: https://gerriscorp.com/services/site-speed/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Site speed, Core Web Vitals, and Cloudflare

Fast pages rank better, convert better, and get crawled more. I find what's actually slowing your site on real phones and fix it.

## Core Web Vitals

Google measures page experience with three Core Web Vitals, scored from real Chrome users at the 75th percentile:
| Metric | Measures | Good |
| --- | --- | --- |
| Largest Contentful Paint (LCP) | How fast the main content appears | 2.5 seconds or less |
| Interaction to Next Paint (INP) | How fast the page responds to taps and clicks | 200 milliseconds or less |
| Cumulative Layout Shift (CLS) | How much the layout jumps while loading | 0.1 or less |

INP replaced First Input Delay in March 2024, and many sites that passed before now fail on it, usually because of heavy JavaScript and third-party scripts.

## What I fix
- **Images:** right-sized, modern formats such as WebP and AVIF, explicit dimensions, lazy loading below the fold, and priority loading for the main image.
- **CSS and JavaScript:** render-blocking files, unused code, oversized bundles, and long tasks that block interaction.
- **Third-party scripts:** tag managers, chat widgets, ad and analytics scripts, and what each one actually costs.
- **Fonts:** fewer files, preloading, and font-display settings that avoid invisible text and layout shifts.
- **Servers and caching:** slow time to first byte, missing page caching, and cache headers that make browsers download the same files again.

## Cloudflare and CDNs

A CDN puts copies of your site close to every visitor and absorbs load and attacks. I've used Cloudflare for years and set it up properly:
- DNS moved without downtime and without disturbing email records.
- Caching configured with Cache Rules, including full-page caching where it's safe, and Tiered Cache for sites with global traffic.
- Automatic Platform Optimization for WordPress sites that benefit from it.
- Compression, HTTP/3, and Early Hints switched on, and image optimization through Polish or Cloudflare Images.
- Redirects moved to Redirect Rules and Bulk Redirects, so they run at the edge and survive CMS changes. Cloudflare is retiring the older Page Rules, and I migrate them.
- Crawler Hints turned on, which notifies search engines of changes through IndexNow.
- Bot and AI crawler settings checked. Cloudflare now blocks many AI crawlers by default on newer setups, which can quietly keep you out of AI search. I set them deliberately.

I also work with Netlify, GitHub Pages, and other hosts' built-in CDNs.

## What you get
- A speed diagnosis from field data and lab tests, with the causes ranked by impact.
- The fixes I can make directly, and developer tickets for the rest.
- A before and after comparison on the pages that matter.

## Common questions

### Will Cloudflare make my site faster by itself?

It helps immediately with static files and distance. The large gains come from configuring caching, compression, images, and redirects for your specific site, which is the work I do.

### How long until Core Web Vitals improve in Search Console?

The Chrome UX Report uses a rolling 28 days of real-user data, so improvements show up gradually over about a month after the fixes ship.

**Related:** [Technical SEO](https://gerriscorp.com/services/technical-seo/) · [Email and DNS](https://gerriscorp.com/services/email-and-dns/) · [JavaScript SEO](https://gerriscorp.com/guides/javascript-seo/)

[Ask me why your site is slow](https://gerriscorp.com/contact/)

Updated October 5, 2026

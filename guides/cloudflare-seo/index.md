> The Cloudflare settings that decide whether Googlebot, Bingbot, and AI crawlers can reach your site, plus the caching, HTTPS, and redirect choices that help.
>
> Source: https://gerriscorp.com/guides/cloudflare-seo/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Cloudflare settings that help or hurt SEO and AI crawlers

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Cloudflare sits in front of millions of websites, and a handful of its switches decide whether search engines and AI assistants can read yours. I set it up for clients often, and I audit it every time a site's crawling looks strange. These are the settings I check first.

## Proxied or DNS only

Every DNS record in Cloudflare has a cloud icon. Orange means proxied: visitors and crawlers reach Cloudflare's network, which applies caching, security, and rules before passing the request to your server. Grey means DNS only: Cloudflare answers the DNS lookup and then steps aside. Only proxied records get Cloudflare's speed and protection, and only proxied records can be blocked by its security features. When a crawling problem appears, the cloud color is the first thing to confirm.

Mail records always stay grey. MX targets and the hostnames used by mail services must resolve to the real servers.

## AI crawler controls

In July 2025 Cloudflare began blocking known AI crawlers by default on newly added domains, and it offers a one-click switch to block them on existing ones. The current controls live under AI Crawl Control, where each crawler can be allowed or blocked by name, and Cloudflare can also manage robots.txt for you with its own content signals added.

This matters because the crawlers are different jobs. GPTBot and ClaudeBot gather training data. OAI-SearchBot, Claude-SearchBot, and PerplexityBot build the indexes that assistants search when they answer questions live. Blocking the search crawlers keeps you out of those answers entirely. Decide crawler by crawler, then confirm the setting matches the decision. The [AI assistants guide](https://gerriscorp.com/guides/ai-assistants/) explains which crawler feeds which product.

## Bot protection and challenges
- **Bot Fight Mode** on the free plan challenges traffic that looks automated. Cloudflare exempts its list of verified bots, which includes Googlebot and Bingbot, and the WAF can't override this mode, so a misfire is hard to work around.
- **Super Bot Fight Mode** on paid plans has a separate setting for verified bots. Set it to allow.
- **Under Attack Mode** puts a challenge page in front of every visitor, and crawlers can't pass it. Use it during an actual attack and turn it off when the attack ends.
- **Custom WAF rules** that block by country, by user agent, or by request rate catch crawlers too. Googlebot crawls mostly from the United States, so a rule that challenges American traffic hits it directly.

The proof is in Security, then Events. Filter by user agent for Googlebot or Bingbot and look for blocks or managed challenges. In Search Console, the Crawl stats report under Settings shows host status and response codes from Google's side, and a URL Inspection live test shows exactly what Googlebot received.

## Caching HTML

By default Cloudflare caches static files such as images, CSS, and JavaScript, and passes HTML requests through to your server. For a site whose pages are the same for every visitor, a Cache Rule that marks HTML as eligible for cache can cut time to first byte to a few dozen milliseconds worldwide. Exclude anything personal: carts, checkouts, account pages, admin paths, and any request carrying a login cookie. Set an edge cache time you can live with, and purge the cache on deploy.

## HTTPS settings
- **SSL mode Full (strict).** Cloudflare connects to your server over HTTPS and checks its certificate. Flexible mode connects over plain HTTP, and when the server also redirects to HTTPS, the result is an endless redirect loop.
- **Always Use HTTPS.** Sends every HTTP request to HTTPS with a 301 at the edge, so the server needs no rule of its own.
- **HSTS.** Tells browsers to refuse plain HTTP for a period you choose. Start with a short max age, and add preload only when every subdomain serves HTTPS, because preload is slow to undo.

## Features that change your HTML

Several Cloudflare features rewrite pages on the way out, and each deserves a deliberate decision.
- **Rocket Loader** defers JavaScript by rewriting script tags. It can speed up simple sites and break complex ones, including analytics and consent banners. Test with it off before blaming anything else.
- **Email Address Obfuscation** replaces email addresses in the HTML with a script. Visitors see the address, and crawlers that read raw HTML see a placeholder.
- **Auto Minify** was retired in 2024. If a build still depends on it, move minification into the build.

## Redirects at the edge

Redirect Rules handle patterns, such as moving a whole folder or forcing the www or bare domain. Bulk Redirects handle long lists of one-to-one moves from a file. Both answer at the edge with a true 301, which makes Cloudflare a good home for a migration's redirect map. Keep all the redirects in one layer; rules split between Cloudflare and the origin server are where chains and loops come from. The [redirects guide](https://gerriscorp.com/guides/301-redirects/) covers mapping and testing.

## Crawler Hints

Crawler Hints notifies search engines that support IndexNow, including Bing and Yandex, when your content changes, based on what Cloudflare sees passing through its cache. It's a free switch under Caching and worth turning on for any site that changes regularly. Google doesn't use IndexNow, so it does nothing for Google.

## Questions about Cloudflare and search

### Does Cloudflare's shared IP address hurt rankings?

No. Millions of sites share Cloudflare's addresses, and Google judges sites by their content and links, not by who else is on the IP.

### Should a small site use Cloudflare at all?

Yes, at least for DNS. Cloudflare's free DNS is fast and well documented, and proxying can be added record by record later. This site uses Cloudflare for DNS only, because GitHub Pages already provides HTTPS and a CDN.

I configure and audit Cloudflare as part of [site speed and Cloudflare work](https://gerriscorp.com/services/site-speed/) and [crawler visibility audits](https://gerriscorp.com/services/crawler-visibility/).

## References
- [Cloudflare Docs: Verified bots](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/)
- [Cloudflare Docs: Cache](https://developers.cloudflare.com/cache/)
- [Google Search Central: Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

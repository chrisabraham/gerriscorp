> Full-page caching keeps most visitors away from WordPress and MySQL. Here is the traffic that still reaches your server, and how to harden each path it takes.
>
> Source: https://gerriscorp.com/guides/wordpress-behind-cloudflare/ · Updated 2026-10-14 · By Chris Abraham, Gerris Corp

# What Cloudflare's cache leaves exposed on a WordPress site

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 14, 2026

Putting WordPress behind Cloudflare with full-page caching is the best single change I know for a slow WordPress site. Visitors get a saved copy of each page from a data center near them, and your server, PHP, and MySQL sit idle for most of the traffic. I think of it as a plate carrier: it covers the vital organs, where most of the hits land. The traffic it lets through goes straight to the parts of WordPress attackers aim at, so those parts need their own protection.

## How the cache decides

Cloudflare doesn't cache HTML by default. You turn page caching on with Automatic Platform Optimization, which Cloudflare built for WordPress, or with a cache rule that tells Cloudflare to cache everything on chosen paths. APO comes with its own logic for what to skip. Cloudflare's documentation says it bypasses the cache for logged-in and administrator users so private content isn't cached, and that a request skips the cache when bypass cookies are present, naming logged-in, session, and WooCommerce cookies. With the Cloudflare WordPress plugin installed, the edge copy updates when you change content.

A hand-written cache rule has none of that logic until you add it. A rule that caches everything and forgets the login cookie will serve one editor's view of the site to the public. If you write your own rules, add a bypass for requests carrying the WordPress login cookie, and test logged in and logged out before trusting it.

## Traffic that still reaches your server
- **Logins.** Every request to `wp-login.php` and the dashboard runs PHP and queries the database. Password-guessing bots aim here first.
- **XML-RPC.** `xmlrpc.php` is an older remote-publishing interface that WordPress still ships. It accepts logins too, and bots use it for password guessing. Jetpack depends on it, so check before closing it.
- **Logged-in sessions.** Editors, members, and customers with a session cookie get uncached pages, by design.
- **Forms, comments, and search.** Every submission and search query goes to the origin.
- **Carts and checkout** on WooCommerce, which carry session cookies.
- **Anything requested by IP address**, if the server answers requests that skip Cloudflare entirely.

## Hardening the paths that remain

WordPress's own hardening guide, in the Advanced Administration Handbook, covers most of this, and I follow it:
1. **Update core, plugins, and themes.** The handbook's first advice is to keep WordPress current, and it says the same of plugins.
2. **Delete plugins you don't use.** The handbook says to remove an unused plugin from the system entirely. A deactivated plugin still sits on disk.
3. **Use strong passwords and two-step login** for every account that can publish, and close accounts that belong to people who've left.
4. **Turn off the dashboard file editor** with `define( 'DISALLOW_FILE_EDIT', true );` in `wp-config.php`, so a stolen administrator login can't rewrite your theme's code from the browser.
5. **Protect the login.** The handbook suggests server-side password protection for the admin area as a second layer. At Cloudflare, a rate limiting rule on `wp-login.php` stops bulk guessing before it reaches the server.
6. **Close XML-RPC** when nothing needs it, with a Cloudflare rule that blocks the path or a plugin that disables it.
7. **Back up the files and the database**, which the handbook names explicitly, and store the copies away from the server. Restore one to a test site once, so you know the backups work.
8. **Accept only Cloudflare's traffic** at the origin, through your host's firewall or Cloudflare Tunnel, so nobody can go around the proxy.

## The maintenance never stops

Caching removes the speed problem and most of the load. It leaves the upkeep: updates every week, plugin audits, backup checks, and an eye on login attempts. That is the standing cost of running WordPress, and for stores, membership sites, and newsrooms it's worth paying.

For a company site that changes a few times a year, it often isn't. A static site has no login page, no database, and no plugins, so the whole list above disappears. I covered that trade in [WordPress care: caching, hardening, or a static move](https://gerriscorp.com/services/wordpress-care/). For the Cloudflare settings that affect search engines and AI crawlers, see [Cloudflare settings that help or hurt SEO and AI crawlers](https://gerriscorp.com/guides/cloudflare-seo/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Cloudflare Docs: About Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/about/)
- [WordPress Advanced Administration Handbook: Hardening WordPress](https://developer.wordpress.org/advanced-administration/security/hardening/)
- [Cloudflare Docs: Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)
- [Cloudflare Docs: Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

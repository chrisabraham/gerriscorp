> For WordPress sites that are slow, exposed, or costly to keep: Cloudflare page caching, hardening for what the cache can't shield, or a move to static pages.
>
> Source: https://gerriscorp.com/services/wordpress-care/ · Updated 2026-10-14 · By Chris Abraham, Gerris Corp

# WordPress care: caching, hardening, or moving off

A WordPress site carries running costs that never show up on an invoice: a MySQL database, PHP on every uncached request, and a stack of plugins that each need updates and each open a door. I bring those costs down in one of two ways. I put the site behind Cloudflare and harden what's left exposed, or I move it to static pages when it never needed WordPress in the first place.

## Option one: cache it and harden it

Cloudflare can serve whole WordPress pages from its edge, through Automatic Platform Optimization or a cache rule, so most visitors never reach your server or your database. I set that up and test it: cached pages carry the right canonical, logged-in views never get cached for the public, and the cache clears when you publish.

The cache shields most of the site and leaves gaps by design. Cloudflare's documentation says APO sends logged-in users, and requests carrying session or WooCommerce cookies, straight to the origin. Login attempts, comment and form posts, search, and the XML-RPC endpoint all reach WordPress. Those gaps are where the hardening goes:
- Core, plugins, and themes updated on a schedule, with a staging check first when the site is complex.
- Plugins nobody uses removed outright, which WordPress's own hardening guide recommends.
- Strong passwords and two-step login for every administrator, and old accounts closed.
- The dashboard file editor disabled in wp-config.php.
- XML-RPC switched off unless Jetpack or another tool depends on it, and login attempts rate limited at Cloudflare.
- Backups that include the database, kept off the server, and a restore tested at least once.

The reasoning, with sources, is in my guide to [what Cloudflare's cache doesn't protect on WordPress](https://gerriscorp.com/guides/wordpress-behind-cloudflare/).

## Option two: leave WordPress

A company site that changes a few times a year pays all of those costs to serve pages that hardly change. I move sites like that to static HTML on GitHub Pages behind Cloudflare: every URL kept or redirected, titles and descriptions carried over, structured data added, and rankings watched through the launch. I did the same for my own serialized novel, moving it off a broken Movable Type install with every original address intact, as described under [project rescue](https://gerriscorp.com/services/rescue/). My own sites run this way; the [colophon](https://gerriscorp.com/colophon/) shows how this one is built.

WordPress stays the right tool for stores, membership sites, and teams that publish daily through its editor. For those, option one is the plan.

## How I decide which

A short diagnostic answers it: how often the site changes, who edits it, what plugins it runs and why, what the hosting costs, and what it has already suffered. You get the recommendation in writing with the reasons, and the choice stays yours.

## Engagement

A prepaid diagnostic, then a fixed-scope setup or migration. Monthly care is available under [ongoing support](https://gerriscorp.com/services/ongoing-support/). Terms are on [Work With Me](https://gerriscorp.com/work-with-me/).

Updated October 14, 2026

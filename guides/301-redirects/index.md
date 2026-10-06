> Which redirect to use, how to map old URLs to new ones, where to implement redirects on common platforms, how to test them, and how long to keep them live.
>
> Source: https://gerriscorp.com/guides/301-redirects/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# How to plan 301 redirects that keep your rankings and links

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

A redirect tells browsers and search engines that a page has moved. Done well, it carries the old page's links, bookmarks, and search history to the new address. Done badly, it quietly throws all of that away. Here's how I plan them.

## Which redirect to use
| Type | Meaning | Use it for |
| --- | --- | --- |
| 301 | Moved permanently | Almost every move: renamed pages, merged pages, domain changes, HTTP to HTTPS |
| 308 | Moved permanently, and the request method stays the same | The same jobs as a 301; some servers and APIs prefer it |
| 302 or 307 | Moved temporarily | A page that will come back: a short promotion, maintenance, a geographic or login handoff |
| Meta refresh at zero seconds | An HTML instruction to load another page | Hosts that can't send server redirects, such as GitHub Pages |
| JavaScript redirect | A script that changes the location | A last resort; it only works once the page renders |

Google treats 301 and 308 as strong signals that the new URL should replace the old one in its index. A temporary redirect is a weaker signal, though Google may eventually treat a 302 that never goes away as permanent. An instant meta refresh is read as a permanent move too, which is how this site handles the hundreds of old gerriscorp.com addresses it inherited: GitHub Pages can't send a real 301, so each old path holds a tiny page that forwards immediately and names the new page as its canonical.

## Map every old URL to its closest equivalent

The redirect map is a two-column list: old URL, new URL. The work is in the second column. Each old page goes to the page that answers the same question its visitors arrived with.
- **One to one when you can.** A product, article, or service that still exists goes to its new address.
- **Merged pages go to the survivor.** Three thin pages folded into one strong page all point at it.
- **Retired pages go to the nearest parent.** A discontinued product goes to its category, and a retired service goes to the services overview.
- **Junk can stay gone.** Spam URLs, old tag archives, and test pages with no links and no traffic can return a 404 or 410.

Send old pages to relevant pages, and keep the home page for the home page. Google treats a mass redirect to an unrelated page as a soft 404, so the old page's signals are dropped anyway, and visitors land somewhere that doesn't answer what they came for.

## Where the old URLs come from

Build the list from every source you have, because no single one is complete. Crawl the current site with a tool such as Screaming Frog. Export pages from Search Console's Performance report and from analytics landing pages. Pull linked pages from a backlink tool. For an old site that's already gone, the Internet Archive's Wayback Machine keeps a record of URLs it captured, which is how I recovered more than six hundred old paths for this domain.

## Where to implement them
- **At the edge.** Cloudflare's Redirect Rules and Bulk Redirects answer before the request ever reaches your server, which is fast and survives a change of host or platform.
- **On the web server.** Apache uses `Redirect 301` or `RewriteRule` in the configuration or `.htaccess`; Nginx uses `return 301` inside a `location` block.
- **In the platform.** WordPress handles them with a plugin such as Redirection or the redirect manager in Rank Math. Shopify has a URL redirects screen in the admin, and it only applies a redirect when the old path would otherwise return a 404. Squarespace, Wix, and Webflow each have a redirects panel in their settings.
- **In the framework.** Next.js, Netlify, and Vercel take redirects in a configuration file that ships with the code, which keeps them under version control.

Pick one layer and keep all the redirects there. Rules split across Cloudflare, the server, and a plugin are how loops and chains happen.

## Chains and loops

A chain is a redirect that lands on another redirect: A goes to B, and B goes to C. Googlebot follows up to ten hops, but each hop costs time for visitors and makes the signal weaker. When a site has been redesigned more than once, old redirects often point at URLs that are themselves redirected now. Update the old rules so every one points straight at the final address.

A loop is A to B and B back to A. Browsers give up with an error. Loops usually come from two layers fighting, such as an HTTPS rule in Cloudflare and a different HTTPS rule on the server.

## How to test them

From a terminal, `curl -sIL https://example.com/old-page` prints every hop with its status code, so you can see a 301 followed by a 200 and nothing in between. For the full map, feed the old URL list to a crawler in list mode and check three things for each row: the first response is a 301 or 308, the final response is a 200, and the final URL matches the target in the map. Then spot check the same URLs in a private browser window, since your own browser caches permanent redirects aggressively.

## How long to keep them

Google's advice is at least a year. I keep them indefinitely. Backlinks from other sites never get updated, and a redirect costs almost nothing to keep. Removing redirects after a year is how a business loses links it earned a decade ago.

## Questions about redirects

### Do 301 redirects lose PageRank?

No. Google has said for years that 301, 302, and 308 redirects pass link value without a penalty. The losses people see come from redirecting to the wrong page, from chains, or from removing redirects too soon.

### Should I redirect a page I deleted on purpose?

Only if something on the site now answers the same need. Otherwise a 410 tells search engines the removal was deliberate, and they drop the URL a little faster than with a 404.

### How many redirects is too many?

There's no practical limit on the number of rules. Tens of thousands are normal on large sites. What matters is that each one is a single hop to a relevant page.

Redirect mapping is part of every [website migration](https://gerriscorp.com/services/migrations/) I run. For the whole process, see the [migration checklist](https://gerriscorp.com/guides/migration-checklist/).

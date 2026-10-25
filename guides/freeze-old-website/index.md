> Retire a website stuck on a dead CMS without losing its links: count every URL, keep addresses exactly, handle feeds and query strings, and cut over safely.
>
> Source: https://gerriscorp.com/guides/freeze-old-website/ · Updated 2026-10-24 · By Chris Abraham, Gerris Corp

# How to freeze an old website as static HTML without losing a single link

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 24, 2026

Plenty of good websites are running on software nobody maintains anymore: Drupal 7 after its January 2025 end of life, Movable Type installs from the 2000s, PHP portals that only run on a host's oldest PHP version. The content still matters, people still link to it, and search engines still send visitors. The owner usually doesn't need a redesign. They need the site to stop being a security liability and a monthly hosting bill, and to keep working. Freezing it as static HTML does both. I did exactly this with my own serialized novel, which ran on Movable Type from 2005 to 2022, and here is the method.

## When freezing is the right call

A frozen site is a set of plain files: no database, no login, no plugins, nothing to patch. It loads quickly, it's close to free to host, and it can sit untouched for years. That makes it right for archives, finished projects, publications that stopped publishing, a business's old site after a rebrand, and documentation for a retired product.

It's the wrong call if people still edit the site every week, or if it depends on logins, shopping carts, or bookings. Those need a real [migration](https://gerriscorp.com/services/migrations/) to a maintained platform. And there's a middle path: a site can be frozen and still be edited occasionally, if the static pages are generated from source files kept in Git. My novel works that way. Corrections still happen; they just go through a build instead of an admin panel.

## Count every address the old site ever published

The single biggest risk is underestimating how many URLs exist. Old blogging and portal software publishes far more than its articles. Movable Type, for example, writes individual entry pages plus monthly, weekly, daily, and category archives, separate feed files, and TrackBack endpoints for every entry. My novel had 309 chapters, and the full count of public addresses came to 953.

Build the list from several sources and merge them, because each one misses something:
- **The database or export.** The most complete list of content, if you can still get a dump. Entry IDs, slugs, and dates let you reconstruct every permalink the software would have generated.
- **The old web root.** If the software published static files, as Movable Type did, the server's folder is a literal inventory of what it served.
- **A crawl of the live site.** Run it before anything changes, and save the export. This also captures what each page looked like, which you'll want for comparison.
- **The Wayback Machine.** The Internet Archive's CDX API returns every URL it has ever captured on a domain, including pages deleted years ago that other sites still link to. When I rebuilt the redirect map for a site that had lived on three platforms, this was where most of the forgotten addresses came from.
- **Search Console and server logs.** Pages with impressions or real visits in the last year or two are the ones you can least afford to lose.

Deduplicate, normalize the protocol and host, and you have the master list. Everything after this point is checked against it.

## Keep the address exactly, redirect only what you must

A redirect works, but the same URL serving the same content works better: no chain, no lost signal, nothing for anyone to maintain. So the goal for each URL on the list is to publish a file at exactly that path. Most static generators let you set the output path per page, so a chapter that lived at `/archives/2005/03/chapter_one.html` can be written back to that exact spot.

For the rest, decide in this order:
1. **Same path, same content.** Entries, main pages, and anything with outside links.
2. **Same path, lighter content.** Date and category archives that only list entries can become small generated listing pages. Mark them noindex, follow so they pass visitors along without competing with the entries they repeat.
3. **Redirect.** Leftovers from moved or merged entries, and dynamic URLs that can't exist as files.
4. **Let it go.** Spam-filled endpoints and admin paths that were never meant to be public can return 404 or 410. Decide this on purpose, with the list in front of you, not by accident.

## The URLs a static host can't serve as files

Some old addresses don't map onto a file at all. Watch for these:
- **Query strings.** Addresses like `/index.php?p=123` or `/node?id=45` are a script plus a parameter. A static host serves the same file no matter what comes after the question mark, so every one of those URLs would collapse into one page. They need redirect rules that match the query string, at the host or at a CDN in front of it.
- **Script extensions.** Paths ending in `.php`, `.cgi`, or `.asp` can be written as files on some hosts but may be served with the wrong content type. Test each one, or redirect them.
- **Feeds.** Feed readers and aggregators subscribed years ago and never updated. If the old site published RSS 1.0, RSS 2.0, and Atom at three different addresses, publish all three again, in their original formats. My novel still serves all three.

Where the redirect lives matters. GitHub Pages can't send a real 301 from a list of rules; it can only serve a page with an instant meta refresh, which Google says it treats as a permanent redirect but other crawlers and tools may not. If a site needs more than a handful of true redirects, put a CDN such as Cloudflare in front and use its bulk redirect lists, or choose a static host that reads a redirects file. I compare the options in my guide to [planning 301 redirects](https://gerriscorp.com/guides/301-redirects/).

## Replace the dynamic parts, or retire them out loud

Every feature that needed the server has to be replaced or retired deliberately:
- **Comments.** Keep the historical comments as part of each page's HTML, since they're often half the value of an old post, and close new ones.
- **Contact forms.** Replace them with a plain email address or a hosted form service. Then send a test message, because a form that silently drops inquiries is worse than no form.
- **Site search.** A static search index, such as Pagefind, builds at publish time and runs in the browser. For a small archive, a good index page by date and topic may be enough.
- **Analytics.** Carry over the same property, so the before and after are comparable.

## Clean up while you're in there, and log it

A freeze is a rare chance to fix things that have bothered search engines for years: give every page a real title and description, make archive pages noindex, generate a sitemap that lists only the pages meant for search, and add a canonical to each page. On my novel, every chapter got a handwritten title and description, and a script checked them. Typos and broken typography got fixed too, each one recorded in a log with the original text, so any correction can be reversed. If you're tempted to "improve" the content more than that, stop. A frozen archive should read like itself.

## Cut over in the right order

The step that most often goes wrong is the last one, because old hosting packages tend to bundle more than the website. Check before you cancel anything:
1. **Find out who runs DNS.** If the old host is also the DNS provider, canceling the account takes the domain's records down with it, including email. Move DNS first, copying every record exactly, especially mail and verification records. My guide to [email authentication](https://gerriscorp.com/guides/email-authentication/) explains which ones keep mail flowing.
2. **Publish the frozen site on a test address** and check it against the master list: every URL answers, the content matches, redirects land on the right page in one hop.
3. **Switch the website records** to the new host, and confirm https and the www and non-www versions behave.
4. **Run the master list again on the real domain.** For the novel, a script checked all 953 addresses, the redirects, and the canonicals before I told Google and Bing anything.
5. **Submit the new sitemap,** then watch Search Console for a few weeks. Expect a quiet transition. Anything else means something on the list was missed.
6. **Only then cancel the old hosting,** after downloading a final copy of the files and the database.

## What it costs, and what it saves

For a small site, the work is mostly the inventory and the checking, not the conversion. A blog of a few hundred posts is a few days of careful work. The savings are ongoing: no security patches for software that no longer gets any, no emergency when a host retires an old PHP version, and hosting that's often free. The site also tends to get faster, which matters to visitors more than the owner usually expects.

## Questions about freezing a website

### Will I lose my search rankings?

Not if the URLs and content stay the same. Search engines see the same pages at the same addresses, served faster. Rankings drop when addresses change without redirects or when content disappears.

### Can I just use a website copier?

Tools that mirror a site, like wget or HTTrack, are a useful starting point and a good backup. On their own they miss feeds, unlinked pages, and query string URLs, and they copy the old site's problems along with its content. Check their output against the master list.

### Can a frozen site still be updated?

Yes, if it's generated from source files kept in Git. Edit the source, rebuild, publish. No server or database involved.

If you have a site stranded on old software and want it preserved rather than rebuilt, that's [site rescue](https://gerriscorp.com/services/rescue/) work, and I'm happy to look at it. Send me the address on the [contact page](https://gerriscorp.com/contact/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Drupal.org: Drupal 7 end of life](https://www.drupal.org/about/drupal-7/d7eol/partners)
- [Google Search Central: Redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
- [Internet Archive: Wayback CDX Server API](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server)
- [Cloudflare Docs: Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

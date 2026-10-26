> A backup is only proven when you have restored from it. How I run a website restore drill, what to time and record, and the gaps it usually uncovers.
>
> Source: https://gerriscorp.com/guides/restore-drills/ · Updated 2026-10-26 · By Chris Abraham, Gerris Corp

# Website restore drills

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 26, 2026

Every hosting plan and every WordPress backup plugin promises backups. Few owners have ever restored one. The first restore usually happens during an emergency: the site is hacked, a plugin update breaks the checkout, a developer deletes the wrong folder. That's when people find out the backup excluded the uploads folder, the database export is from March, or the only person with the hosting password is on a plane. A restore drill finds all of that on a quiet afternoon instead.

## What the agencies say

CISA's #StopRansomware Guide tells organizations to maintain offline, encrypted backups of critical data and to regularly test the availability and integrity of those backups in a disaster recovery scenario. It separately advises testing backup procedures on a regular basis. NIST's contingency planning guide for federal systems treats testing and exercises as part of the plan itself. Neither document is written for a small business website, but the principle carries over without change: an untested backup is a hope.

## Decide what you're protecting

List what the site is made of. For a typical WordPress site that's the database, the uploads folder, the theme and plugins, the configuration file, and the DNS records. For a static site in a Git repository, it's the repository, the build settings, the hosting configuration, and DNS. For a store, add product data, orders, customer accounts, and the payment and shipping integrations.

Then set two numbers with the owner. The first is how much recent work you can afford to lose: a day of orders, an hour, none. The second is how long the site can be down before it costs real money. Those two answers decide how often backups run and how fast a restore has to be.

## Restore somewhere safe

Never drill on the live site. Restore to a staging server, a local machine, or a fresh hosting account, on a temporary address blocked from search engines. The point is to rebuild the site from nothing but the backup and the written instructions, the way you would if the original server were gone.

Use the most recent backup, not a specially prepared one. Have someone other than the person who set up the backups run the drill, following only what's written down. Every question they have to ask is a gap in the instructions.

## What to check on the restored copy
- **Completeness.** Every page loads, images appear, downloads work, and the newest content is there.
- **Freshness.** The latest post, product, or order in the restored copy matches what the backup schedule promises.
- **Function.** Forms submit, search works, logins work, a test order goes through in the store's test mode.
- **Settings.** Redirects, robots rules, canonical tags, and the analytics tag are all present, since these live in places backups often skip.
- **Secrets.** API keys, mail settings, and payment credentials can be found and re-entered from a secure store.

## Time it and write it down

Record when the drill started, when the site was usable, and every step in between. Note each problem: a missing file, a version mismatch, a password nobody had, a step that took an hour because nobody had done it before. The record becomes the runbook for the real event and shows how close you are to the downtime the owner agreed to.

## Gaps a drill usually uncovers
- The backup lives on the same server as the site, so it would be lost with it.
- The plugin backs up the database but not the uploads, or the reverse.
- The backup is encrypted, and the key is stored only on the server being protected.
- Backups stopped months ago when a card expired or a storage quota filled, and nobody was told.
- DNS records were never saved, so pointing a new server at the domain means rebuilding them from memory.
- The hosting account, registrar, and DNS host logins belong to someone who has left.

Each of those is easy to fix once seen. CISA's offline-copy advice addresses the first and third: keep at least one copy somewhere an attacker on the server can't reach or erase.

## How often

Run a full drill once a year and after any major change: a new host, a redesign, a new backup tool, a platform migration. Check every month that the latest backup exists and has a sensible size. A backup file that's suddenly much smaller than last month's is often the first sign something has stopped being included.

## The static site advantage

A static site kept in a Git repository carries its own history. Every version of every page is in the repository, and a copy of the repository on any laptop is a full backup. Restoring means pointing a new host at the repository and rebuilding. The drill still matters, because DNS, hosting settings, and form handlers live outside the repository, but the hardest part of the problem is already solved.

When a site needs a fast rebuild after an incident, the record-keeping side is in my guide to [the website incident timeline](https://gerriscorp.com/guides/website-incident-timeline/). Backups and restore drills are part of [WordPress care](https://gerriscorp.com/services/wordpress-care/), and when an old site needs saving outright, see [freezing an old website as static HTML](https://gerriscorp.com/guides/freeze-old-website/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [CISA: #StopRansomware Guide (September 2023)](https://www.cisa.gov/stopransomware/ransomware-guide)
- [NIST: Contingency Planning Guide for Federal Information Systems, SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

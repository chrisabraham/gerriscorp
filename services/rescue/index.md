> Chris Abraham takes over stalled or inherited web projects: inventories code, servers, accounts, and DNS, stabilizes them, and moves sites off dead software.
>
> Source: https://gerriscorp.com/services/rescue/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Project rescue, takeovers, and legacy migrations

A developer disappeared. An agency handed over a zip file. The site is down, or running on software nobody can update. I find out what you actually have and get it working again.

## Takeover and handover review

The first job in any rescue is finding out what exists. I inventory:
- The source code: where it lives, whether it matches what's running, and whether it builds.
- The environments: hosting, servers, databases, build pipelines, and process managers.
- The accounts and credentials: registrar, DNS, hosting, CDN, email, analytics, payment and third-party services, and who controls each one.
- The outstanding work: what was promised, what was half-finished, and what's broken.

You get a written handover review and a credible plan, whether that's resuming development, stabilizing what exists, or transferring responsibility to a new developer.

## Hands-on stabilization

I work directly on Linux servers over SSH: reading logs, editing application and environment configuration, managing Node applications with process managers, and resolving the port conflicts, failed services, and expired certificates that take sites down. When I provision a server, it's hardened from the start: key-only SSH, root and password login disabled, a firewall that allows only what's needed, and unattended security updates.

## Legacy CMS migrations

Old sites on dead software still hold years of content and links. I move them to something maintainable without losing a word or a URL. I moved my own serialized novel, 309 entries from 2005 to 2022, off a broken Movable Type install onto static pages on GitHub Pages, keeping every original URL and the feel of the old site. The same approach works for abandoned WordPress installs, old Drupal and Joomla sites, and hand-built sites nobody can edit.

## Platform migrations

Squarespace to Shopify, WordPress rebuilds, moves to static or headless builds, and hosting changes, with content, rankings, and email preserved. That includes DNS planning that leaves mail records untouched, 301 redirects for every changed URL, and post-launch 404 and redirect cleanup. See [website migrations](https://gerriscorp.com/services/migrations/) and the [migration checklist](https://gerriscorp.com/guides/migration-checklist/).

## Restoring self-service

Sometimes the rescue is simply getting the client able to edit their own site again: a broken visual editor, lost admin access, or a publishing workflow that stopped working. Restoring that is often worth more than any new feature.

## What a handover review covers

A good review answers a handful of plain questions in writing: Do you have the real source code? Can it be built and deployed by someone new? Who holds the domain, the DNS, and the hosting? Are there credentials only the departed developer knows? What would it cost to keep going versus starting over? The answers decide the next step, and they're useful even if someone else does the work.

## Common questions

### Where does a rescue start?

With a paid diagnostic: access gathered, the inventory done, and a written plan. Recovery work follows under its own agreed scope.

### Do you host the rescued site?

The site goes back onto hosting you own and control, set up properly and documented, so you never depend on one person's server.

**Related:** [Fractional technical lead](https://gerriscorp.com/services/technical-lead/) · [Website migrations](https://gerriscorp.com/services/migrations/) · [Email and DNS](https://gerriscorp.com/services/email-and-dns/)

[Tell me what you inherited](https://gerriscorp.com/contact/)

Updated October 5, 2026

> Chris Abraham inventories every domain a company holds, moves each into a company-owned account, locks it down, and documents renewals, DNS, and access.
>
> Source: https://gerriscorp.com/services/domain-portfolio/ · Updated 2026-10-26 · By Chris Abraham, Gerris Corp

# Domain portfolio audit

A full accounting of the domains your company depends on: where each one is registered, whose account it sits in, who can log in, when it renews, and what it does.

Companies collect domains the way they collect software subscriptions. A founder registers the first one on a personal card. A marketing agency buys three for a campaign. A product launch adds two more, a rebrand adds five, and someone buys the typo versions to keep them from squatters. Ten years later the domains are spread across four registrars and six accounts, some owned by people who've left, and nobody can say which ones still matter. I sort that out, and then I make sure it stays sorted.

## What the audit covers
- **Every domain the company uses or owns**, found from registrar accounts, DNS zones, certificate transparency logs, redirects on the main site, and the memories of long-serving staff.
- **The registrar, account, and account holder** for each, with the email address that receives renewal and transfer notices.
- **Lock status**: transfer, update, and delete locks, and whether Registry Lock is available for the main domain.
- **Renewal dates and payment**, with the domains closest to expiry flagged first.
- **DNS host and records**, including stale records pointing at services the company no longer uses.
- **Purpose**: live site, redirect, email only, defensive, or unused, so each domain gets the right treatment.

## What I fix

Each domain moves into a company-owned account under a shared role address, with two named people holding access and two-factor authentication on every login. Transfer locks go on everywhere. Auto-renew goes on with a card someone watches. Domains that only exist to stop squatters get records that reject all email, so they can't be used for phishing in your name. Domains with visitors or links get permanent redirects to the right page on the main site. Domains nobody needs are allowed to lapse on purpose, after checking that nothing points at them.

Consolidating onto fewer registrars makes all of this easier to keep. I move domains between registrars with the DNS left untouched, so websites and email keep running through the transfer. The step-by-step reasoning is in my guide to [domain security and registrar locks](https://gerriscorp.com/guides/domain-account-security/).

## What you get
- A domain register: one spreadsheet listing every domain with its registrar, account, purpose, renewal date, lock status, and DNS host.
- A written record of what changed, with dates.
- A short procedure for adding, renewing, and retiring domains, so the register stays current.
- A list of anything I couldn't resolve, such as a domain held by a former contractor who must release it, with the steps to recover it.

## When companies call me

After a scare: a renewal notice that went to a departed employee, a phishing email sent from a lookalike domain, a website that vanished because a card expired. Before a sale or an investment, when buyers ask for a list of digital assets. After a rebrand, when the old domains need redirects that keep their search value. And when a new IT or marketing lead discovers nobody can log into the registrar.

## Common questions

### Will moving registrars take the site or email offline?

A registrar transfer leaves DNS where it is. I confirm the nameservers and every record before and after the move, and plan transfers away from busy periods.

### Do you need the account passwords?

I prefer delegated access where the registrar supports it. Where it doesn't, I arrange temporary access and change the credentials when the work is done.

### How is it billed?

A fixed-scope audit, paid in advance and quoted from the number of domains and accounts. Fixes can be included or billed by the hour.

**Related:** [Email authentication and DNS](https://gerriscorp.com/services/email-and-dns/) · [Domain security guide](https://gerriscorp.com/guides/domain-account-security/) · [Website migrations](https://gerriscorp.com/services/migrations/)

## Start a conversation

Scope and fees are settled in conversation, once I understand the problem. Choose the route that fits how your company works.

[Schedule a call](https://calendly.com/chrisabraham/30) [Work with me through Upwork](https://www.upwork.com/freelancers/chrisjabraham)

Updated October 26, 2026

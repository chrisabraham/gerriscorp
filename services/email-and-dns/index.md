> Chris Abraham sets up SPF, DKIM, and DMARC, fixes deliverability, consolidates domains, and moves DNS and hosting without breaking email or search.
>
> Source: https://gerriscorp.com/services/email-and-dns/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Email authentication and DNS

Unglamorous plumbing that decides whether your email arrives and whether your domains keep their value.

Since February 2024, Gmail and Yahoo have required authenticated email, and Microsoft's Outlook.com followed in May 2025 for high-volume senders. Mail that fails authentication lands in spam or bounces. At the same time, DNS is where websites, email, and verification records all live, so a careless change for a website move can quietly break email. I handle both with an inventory first and a change list second.

## Email authentication
- **SPF** listing every service allowed to send as your domain, within the ten-lookup limit.
- **DKIM** signing for your mailbox provider and every sending service: newsletters, CRM, invoicing, help desk.
- **DMARC** starting at monitoring, reading the aggregate reports to find every legitimate sender, then tightening to quarantine and reject.
- Alignment, one-click unsubscribe headers for bulk mail, and spam-rate monitoring in Google Postmaster Tools.

The [SPF, DKIM, and DMARC guide](https://gerriscorp.com/guides/email-authentication/) explains each record and the current requirements.

## Deliverability

When mail goes missing, I trace it: authentication results in message headers, DMARC reports, blocklists, sending reputation, and content. Then I fix the cause.

## DNS and domains
- A complete DNS inventory before any change, so nothing breaks by accident.
- Moves between DNS providers, such as Cloudflare, Squarespace, GoDaddy, and Route 53, without downtime.
- Website moves that change only the web records and leave mail exactly where it is.
- Domain consolidation, including internationalized domains, with 301 redirects that carry search equity to the right place.
- Verification records for Google, Microsoft, and other services kept intact and documented.

## How an engagement runs
1. A complete export of every DNS record, and a list of every service that sends mail as your domain.
2. A written change plan: what changes, what stays, and in what order.
3. The changes, made in a quiet period with time-to-live values lowered first.
4. Verification with test messages, header analysis, and DMARC reports.
5. A record of the final configuration, so the next person who touches DNS knows what everything does.

## Domains you own but don't use

Old brand names, typo domains, and defensive registrations need attention too. Parked domains get spoofed for phishing, so they need SPF and DMARC records that reject all mail, and any that still attract visitors or links should redirect to the right place on your main site.

## Common questions

### How long does DMARC take to set up?

The records take minutes. Moving safely from monitoring to enforcement usually takes a few weeks of reading reports, because every legitimate sender has to be found and authenticated first.

### Will changing DNS take my site or email offline?

Not when it's planned. I copy every record, lower time-to-live values ahead of the change, and verify mail and web after the switch.

**Related:** [SPF, DKIM, and DMARC explained](https://gerriscorp.com/guides/email-authentication/) · [Site speed and Cloudflare](https://gerriscorp.com/services/site-speed/) · [Website migrations](https://gerriscorp.com/services/migrations/)

[Get your email and domains in order](https://gerriscorp.com/contact/)

Updated October 5, 2026

> How to find out why legitimate business email lands in spam or bounces: authentication results, reputation, blocklists, content, list hygiene, and tools.
>
> Source: https://gerriscorp.com/guides/email-deliverability/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Why business email lands in spam, and how to find the cause

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Invoices disappear, proposals land in junk folders, and customers say they never got the reset link. Deliverability failures look random from the outside. They have specific causes, and the evidence for each one is sitting in the message headers and a few free tools.

## Start with one message's headers

Send a message to a Gmail address you control, open it, and choose Show original. Gmail prints three verdicts at the top: SPF, DKIM, and DMARC, each with pass or fail, and the domain each one checked. In Outlook, the same information sits in the message properties under the `Authentication-Results` header. Read it before changing anything; it tells you which of the following sections applies.

## Authentication failures

A failing result usually has one of four causes.
- **A sender left out of SPF.** The CRM, the invoicing tool, or the website's contact form sends as your domain and isn't listed in the SPF record.
- **SPF over its lookup limit.** SPF allows ten DNS lookups. Every `include` costs at least one, and a record that exceeds the limit fails for every message, including the ones from legitimate senders.
- **DKIM never switched on.** Many services sign with their own domain until you publish their DKIM records and enable signing in their dashboard.
- **No alignment.** DMARC needs SPF or DKIM to pass for the same domain shown in the From line. A service that passes SPF for its own bounce domain still fails DMARC for yours.

The [SPF, DKIM, and DMARC guide](https://gerriscorp.com/guides/email-authentication/) covers the records themselves. DMARC aggregate reports, sent daily by the big mailbox providers to the address in your DMARC record, list every source sending as your domain and whether it passed. They're the fastest way to find a sender you forgot.

## Reputation

When authentication passes and mail still lands in spam, the problem is reputation: how the mailbox providers judge mail from your domain and your sending servers, based on how recipients treat it.
- **Google Postmaster Tools** shows Gmail's view of a domain that sends in volume: spam complaint rate, authentication rates, and delivery errors. Gmail expects bulk senders to keep reported spam below 0.3 percent, and recommends staying under 0.1.
- **Microsoft's Smart Network Data Services** shows how Outlook.com sees the IP addresses you send from, if you control them.
- **Blocklists.** Check the domain and the sending IPs against Spamhaus and the other major lists with a lookup tool such as MXToolbox. A listing usually comes with a reason and a removal process.

Shared sending services put many customers on the same IP addresses, so a neighbor's bad behavior can affect you. That's one reason marketing email and everyday business email belong on separate services, and often on separate subdomains, such as `news.example.com` for newsletters. A newsletter complaint spike then can't drag down invoices.

## The sending practices that cause it
- **Old or purchased lists.** Addresses that bounce, and spam traps hidden on old lists, damage reputation quickly. Mail only people who asked for it, and remove addresses that bounce.
- **No easy unsubscribe.** Since 2024 Gmail and Yahoo require bulk senders to support one-click unsubscribe. People who can't leave a list mark it as spam instead.
- **Sudden volume.** A domain that sends fifty messages a day and then ten thousand looks compromised. Increase volume over weeks.
- **Mail nobody opens.** Providers watch engagement. Stop mailing people who haven't opened anything in months.

## Content and links

Content matters less than authentication and reputation, and it still matters. Link shorteners, links to domains with poor reputations, a single large image with no text, and attachments that commonly carry malware all raise suspicion. Every link in a message is judged by its domain, so a tracking domain shared with spammers hurts every message that uses it.

## Bounces tell you exactly what happened

A bounce message carries a status code and usually a sentence from the receiving server. A `550 5.7.26` from Gmail means the message failed authentication. Codes starting with 4 are temporary and the sending server retries. Codes starting with 5 are permanent. Search the exact code and text; the major providers document what each one means.

## Testing

Services such as mail-tester.com score a single message against authentication, blocklists, and content rules. Seed tests, which send to test mailboxes at each major provider, show whether a campaign lands in the inbox, the promotions tab, or spam. Run one after every change to DNS or sending services.

I fix deliverability as part of [email authentication and DNS work](https://gerriscorp.com/services/email-and-dns/), usually alongside the domain cleanup that caused the problem.

## References
- [Google Workspace Admin Help: Email sender guidelines](https://support.google.com/a/answer/81126)
- [Yahoo Sender Hub: Best practices](https://senders.yahooinc.com/best-practices/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

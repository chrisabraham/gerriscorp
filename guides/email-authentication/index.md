> What SPF, DKIM, and DMARC records do, example records, the Gmail, Yahoo, and Microsoft sender requirements, and how to reach DMARC enforcement safely.
>
> Source: https://gerriscorp.com/guides/email-authentication/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# SPF, DKIM, and DMARC for every domain that sends email

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 5, 2026

Three DNS records decide whether mail from your domain is trusted. Since 2024, the largest mailbox providers require them, and mail without them increasingly lands in spam or bounces.

## The current requirements

Since February 2024, Gmail and Yahoo require every sender to authenticate mail with SPF or DKIM, to have valid forward and reverse DNS for sending servers, and to keep spam complaint rates low. Bulk senders, those sending around 5,000 or more messages a day to Gmail accounts, must also have SPF, DKIM, and a DMARC policy, align the visible From domain with SPF or DKIM, offer one-click unsubscribe on marketing mail, and keep the spam rate reported in Google Postmaster Tools below 0.3%. Since May 2025, Microsoft's Outlook.com has required SPF, DKIM, and DMARC from senders of more than 5,000 messages a day to its consumer addresses.

Even small businesses are affected, because a newsletter tool, CRM, invoicing system, or help desk sending as your domain counts as a sender.

## SPF: who may send

SPF (Sender Policy Framework) is a TXT record on your domain listing the servers and services allowed to send mail as you.

```
example.com.  TXT  "v=spf1 include:_spf.google.com include:sendgrid.net ~all"
```
- Publish exactly one SPF record per domain. Two records break SPF.
- SPF allows at most ten DNS lookups. Each `include` counts, and nested includes count too. Too many services can push you over.
- `~all` (soft fail) is the common ending; `-all` (fail) is stricter. With DMARC in place, either works.

## DKIM: a signature on every message

DKIM (DomainKeys Identified Mail) signs each message with a private key; receivers check the signature against a public key published in DNS under a selector.

```
google._domainkey.example.com.  TXT  "v=DKIM1; k=rsa; p=MIIBIjANBgkq..."
```
- Every service that sends as your domain needs its own DKIM setup, usually a TXT or CNAME record the service provides.
- Use 2048-bit keys where the service offers them.
- DKIM survives forwarding better than SPF, which makes it the more reliable of the two for DMARC alignment.

## DMARC: the policy that ties them together

DMARC (Domain-based Message Authentication, Reporting, and Conformance) tells receivers what to do when a message claiming to be from your domain fails authentication, and asks them to send you reports.

```
_dmarc.example.com.  TXT  "v=DMARC1; p=none; rua=mailto:dmarc@example.com"
```
- A message passes DMARC when SPF or DKIM passes and the domain it passed for aligns with the visible From address.
- `p=none` monitors only, `p=quarantine` sends failures to spam, and `p=reject` refuses them.
- `rua` sets where daily aggregate reports go. They're XML files listing every source that sent mail as your domain and whether it passed.

## Reaching enforcement safely
1. Inventory every service that sends mail as your domain.
2. Set up SPF and DKIM for each.
3. Publish DMARC at `p=none` with reporting, and read the reports for two to four weeks, using a report viewer to make them readable.
4. Fix every legitimate source that fails.
5. Move to `p=quarantine`, optionally with `pct` below 100 to phase it in, and keep reading reports.
6. Move to `p=reject` once failures are only spoofing.

Enforcement is what stops criminals sending invoices and password resets in your name. It also unlocks BIMI, which can show your logo next to your mail in supporting inboxes when combined with a verified mark certificate.

## Common mistakes
- Two SPF records after a new service is added, which invalidates both.
- A sending service set up without DKIM, so its mail fails DMARC once enforcement begins.
- DMARC reports sent to a mailbox nobody reads.
- Jumping straight to `p=reject` and blocking legitimate invoices or password resets.
- Mail records lost during a DNS provider change because only the web records were copied.

## Domains that don't send mail

Parked and secondary domains get spoofed too. Protect them with an SPF record of `v=spf1 -all`, a DMARC record at `p=reject`, and no MX records if they receive no mail.

## Changing DNS without breaking mail

Website moves, CDN setups, and DNS provider changes are when mail records get lost. Export every record first, recreate them exactly, keep MX, SPF, DKIM, and DMARC untouched unless they're the point of the change, and send test messages afterward. Header analyzers show exactly which checks passed.

I set this up and troubleshoot deliverability as [email authentication and DNS](https://gerriscorp.com/services/email-and-dns/) work.

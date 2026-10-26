> Who holds the login to your domain decides who controls your website and email. Registrar locks, Registry Lock, two-factor access, and DNSSEC, in order.
>
> Source: https://gerriscorp.com/guides/domain-account-security/ · Updated 2026-10-26 · By Chris Abraham, Gerris Corp

# Domain security: the registrar account comes first

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 26, 2026

Every website and every company email address depends on one login at a domain registrar. Whoever controls that account can point the website anywhere, read the mail by changing the MX records, and issue new security certificates in the company's name. In practice that account often belongs to a founder's personal email, a departed employee, or a web designer from years ago, protected by a password and nothing else. This guide covers the protections in the order I put them in place.

## Find out who holds the account

Start with an inventory. For every domain the company uses, record the registrar, the account it sits in, the email address on that account, who can log in, and when the domain renews. Include the domains nobody thinks about: the old brand name that still redirects, the product site from a past campaign, the domain that only sends email. Then check where DNS is hosted, since that can be a different company with a different login.

The account should belong to the company, registered to a shared role address such as domains@ on the company's own domain, with at least two named people able to log in. A domain in a personal account belongs, in every practical sense, to that person.

## Turn on two-factor authentication everywhere

In January 2019, after a wave of DNS hijacking against government domains, the US Cybersecurity and Infrastructure Security Agency issued Emergency Directive 19-01. It required federal agencies to audit their DNS records, change the passwords on every account that could alter them, including registrar accounts, add multi-factor authentication to those accounts, and watch certificate transparency logs for certificates they hadn't requested. CISA recommended phishing-resistant factors and advised against text-message codes.

That list was written for agencies and fits any company. Use a hardware key or an authenticator app on the registrar and the DNS host. Store recovery codes where the company, not one person, can find them.

## Registrar lock

A registrar lock sets status codes at the registry that refuse certain requests. ICANN's explanation of these EPP status codes describes clientTransferProhibited, which tells the registry to reject transfers to another registrar; clientDeleteProhibited, which rejects deletion; and clientUpdateProhibited, which rejects changes. Most registrars switch on the transfer lock by default and show it as a single toggle. Check that it's on for every domain.

You can look up any domain's status codes with a public lookup tool. If clientTransferProhibited is missing on a domain that matters, fix that before anything else on this list.

## Registry Lock for the domains that matter most

A registrar lock can be removed by anyone who gets into the registrar account. Registry Lock goes a level higher. Some registry operators offer it through participating registrars, and it sets server status codes that only the registry can lift, usually after a manual, out-of-band confirmation from named contacts. ICANN notes that server statuses take precedence over client statuses and take longer to remove. That delay is the point. Registry Lock costs money and makes legitimate changes slower, so I recommend it for the primary domain of a company whose revenue or reputation depends on it.

## Auto-renew and a payment card that works

More domains are lost to expired cards than to attackers. Turn on auto-renew, attach a company card that someone watches, and set a renewal of several years for the main domain. Make sure renewal notices go to the shared role address, not to someone who left.

## DNSSEC

DNSSEC adds digital signatures to DNS records so that resolvers can detect forged answers. ICANN describes it as protection against attackers redirecting users to a fake site by tampering with DNS responses. Many DNS hosts now enable it with one setting, and the registrar then publishes the matching record at the registry. It's worth turning on where your DNS host supports it, with one warning: if you move DNS providers later, disable DNSSEC or move the keys first, or the domain can stop resolving.

## Watch for changes

Set registrar notifications for any change to contacts, nameservers, or lock status. Subscribe to certificate transparency alerts for your domains through a free monitoring service, so a certificate you didn't request shows up as an email. Review the DNS records once a quarter against a saved copy, and remove records for services you no longer use, since a stale record pointing at an abandoned service can be taken over.

## The short version
- Every domain in a company-owned account, with two people who can log in.
- Two-factor authentication on the registrar and the DNS host, without text messages.
- Transfer lock on for every domain; Registry Lock on the main one.
- Auto-renew with a monitored card and notices to a shared address.
- DNSSEC on where the DNS host supports it.
- Alerts for changes and for new certificates.

Mail records are covered in my guide to [email authentication](https://gerriscorp.com/guides/email-authentication/). If a company has dozens of domains spread across accounts, I run the inventory and consolidation as a [domain portfolio audit](https://gerriscorp.com/services/domain-portfolio/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [ICANN: EPP status codes, what do they mean](https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en)
- [CISA: Emergency Directive 19-01, Mitigate DNS infrastructure tampering (Jan 22, 2019)](https://www.cisa.gov/news-events/directives/ed-19-01-mitigate-dns-infrastructure-tampering)
- [ICANN: DNSSEC, what is it and why is it important](https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

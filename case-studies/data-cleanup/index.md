> Python pipelines that cleaned an 88,900 contact list, merged two 28,800 record exports at 94% email coverage, and caught an AI tracker inventing its data.
>
> Source: https://gerriscorp.com/case-studies/data-cleanup/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Contact data: three cleanups and an AI audit

Messy contact data costs money: bounced campaigns, damaged sender reputation, embarrassing wrong-name emails, and decisions made from lists nobody trusts. These projects turned unusable lists into reliable ones.

## An 88,900-contact master list

For a communications agency, a Python pipeline built one master list from a large accumulated set of contacts. It normalized names, removed bad email addresses, validated names against a global names database, flagged contradictions between a contact's name and email address, recovered missing names from email prefixes, and deduplicated across domains. The result was about 88,900 unique contacts.

## Two 28,800-record exports merged

For a reconnection campaign, I consolidated former clients and colleagues into one clean record per person, with company, first name, last name, and best email address, preferring personal addresses. The sources were a working spreadsheet and two contact-manager exports of about 28,800 records each, with shifted columns and broken field mappings that had to be repaired first. Tighter deduplication rules followed. The output reached about 94% email coverage, and every record carries a tag showing how it was resolved.

## An AI-generated tracker audited

An outreach tracker built with an AI tool claimed messages had been sent to contacts who had bounced or didn't exist, with uniform timestamps that couldn't be real, and duplicates throughout. I rebuilt it against the actual sending records: 452 rows became 392 real contacts, each with a status the evidence supported.

## Lessons
- Scripts beat hand-cleaning: the work is repeatable, and every change can be traced.
- Every record needs a resolution status, so nothing disappears silently.
- AI-produced data needs checking against source records before anyone relies on it.
- Sending volume matters as much as list quality: a mail-merge blast at high daily volume can get a sending account shut down, even with a clean list.

See [data cleanup and AI-output audits](https://gerriscorp.com/services/data-cleanup/).

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

Updated October 5, 2026

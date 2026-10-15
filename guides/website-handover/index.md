> A website handover checklist for owners: account control, reproducible builds, hosting, DNS, data, backups, renewals, and proof a new maintainer can operate it.
>
> Source: https://gerriscorp.com/guides/website-handover/ · Updated 2026-10-15 · By Chris Abraham, Gerris Corp

# A website handover needs more than a zip file and a password

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 15, 2026

The contractor says the website is yours. Can someone new rebuild it, publish a correction, renew the domain, and restore the data without calling that contractor? Those are practical handover questions, and they can be answered while everyone is still available to help. Here is the inventory I would want before accepting responsibility for an inherited site.

## Start with the account that controls each layer

A domain registration, a DNS zone, a hosting subscription, and a code repository can belong to four different accounts. List them separately. For each, record the business owner, the people with administrative access, the billing contact, and the recovery route. The person who can edit a page is not necessarily the person who can recover the account.

The [website handover inventory worksheet](https://gerriscorp.com/downloads/website-handover-inventory.csv) provides rows for these layers and room to record evidence. Put account identifiers in the private working copy, but keep passwords, recovery codes, tokens, and private keys in an approved secrets manager. The worksheet should say where access is managed, not become another loose credentials file.

## Prove the source matches the site

Ask which repository and revision produced the current deployment. Keep the build instructions, runtime requirements, dependency files, and a list of required configuration variable names with the project. A useful handover lets a new maintainer start from the recorded revision in a fresh workspace and reproduce the intended result.

Try that build before treating the instructions as complete. If it needs a file that exists only on somebody's laptop, an unrecorded account, or a package that cannot be retrieved, the trial has found an unresolved dependency. Record the dependency and its owner rather than quietly borrowing the departing developer's working directory.

## Separate a repository transfer from an access review

GitHub documents that secrets, deploy keys, and webhooks can remain associated with a transferred repository. Receiving ownership therefore does not by itself settle who can still act on the project. Review the actual connections, collaborators, automation accounts, and deployment credentials as part of the handover.

Agree the timing of access changes with the people responsible for the live service. An old key may still be powering the production build. Replace and test necessary connections before withdrawing the previous ones, then record that the old access has been removed. This sequence keeps an ownership improvement from becoming an accidental outage.

## Inventory the things outside Git

A working site may depend on a database, uploaded media, scheduled jobs, a mail provider, search indexes, an external form service, or storage controlled by a different account. Include the dependencies the visitor never sees. A nightly import that stops running can make the site wrong for weeks before anybody notices that a background job was missed.
- **Content and files:** where editable content, original artwork, and visitor uploads live.
- **Recurring jobs:** what runs, on whose service, and who receives a failure alert.
- **Forms and notifications:** where submissions are stored and how delivery is verified.
- **Analytics:** which properties and accounts contain the business's reporting history.
- **Licenses:** which commercial components need renewal or a new owner.

## Restore something before calling it a backup

List what each backup includes, its schedule, where it is stored, and who can retrieve it. Then restore the necessary components into a separate test environment. A repository backup is useful, but the application may also need data and media stored elsewhere. GitHub's backup documentation explains repository backup methods; the running service needs its own inventory around them.

Choose a small, recognizable check after the restore: a particular article, a known uploaded file, or a test record that should exist. Record the backup date and the result. Keep test notifications and outbound integrations disabled while checking the restored copy so a rehearsal does not contact real customers.

## Write down the domain and email dependencies

A website move often shares a DNS zone with the company's email. Save the current records and identify which serve the site, which serve mail, and which verify ownership for other services. A new maintainer needs to know why a record exists before deciding that an unfamiliar entry is obsolete.

Record domain renewal responsibility, certificate handling, redirects, and any old hostnames that still serve files or forward visitors. The domain is not fully handed over if its renewal notice goes only to an address nobody in the business can read. The [email and DNS service](https://gerriscorp.com/services/email-and-dns/) covers that layer when it needs hands on work.

## Ask the receiving person to do one routine job

Have the new maintainer make an agreed harmless change on a preview, inspect the result, and explain the release and rollback process. It is a much better test of the documentation than asking whether the folder of instructions looks complete. The exercise also reveals which decisions still depend on knowledge the departing contractor has never written down.

Record unresolved items, their owners, and the next date to review them. A handover can be accepted with clearly identified followup work, but a missing recovery route should not disappear inside a general statement that everything is finished.

## Keep the inventory useful after handover

Review it when hosting changes, a new supplier joins, or an integration is added. It becomes the starting point for the next contractor and a much calmer starting point for an outage. My [application takeover case](https://gerriscorp.com/case-studies/app-takeover/) shows the kind of configuration and operational work that an inherited project can require.

If the documentation is incomplete or nobody knows what is running, [project rescue and takeover review](https://gerriscorp.com/services/rescue/) is an existing way to hire me for the inventory and a practical next plan. A second opinion before you accept a supplier's handover also fits [strategic advisory](https://gerriscorp.com/services/advisory/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [GitHub Docs: Transferring a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)
- [GitHub Docs: Backing up a repository](https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

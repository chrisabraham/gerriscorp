> Chris Abraham cleans and dedupes contact lists and CRMs with Python, and audits AI generated spreadsheets for fabricated or wrong data before you rely on them.
>
> Source: https://gerriscorp.com/services/data-cleanup/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Data cleanup and AI-output audits

Contact lists with thousands of duplicates. CRMs nobody trusts. Confident-looking spreadsheets an AI produced that turn out to be partly invented. I turn messy data into something you can rely on.

## Contact list and CRM cleanup

I build Python pipelines for the job instead of cleaning by hand, so the work is repeatable and every change can be traced. On a recent project with more than 28,000 exported records, the pipeline:
- Remapped broken export formats into consistent columns.
- Validated first and last names by country against a large names dataset, ranking how plausible each name is.
- Rescued missing names from email address prefixes, and detected surnames entered in the wrong field.
- Deduplicated contacts across domains and spelling variants.
- Assigned every record a resolution status, so nothing was silently dropped.

The same approach works for CRM exports, newsletter lists, event registrations, and merged lists after an acquisition.

## Auditing AI output

AI tools now produce trackers, reports, and spreadsheets that look finished. Some of them contain fabricated values. In one audit, an AI-generated outreach tracker marked bounced and nonexistent contacts as sent, carried uniform timestamps that couldn't be real, and repeated contacts. I rebuilt it against the actual sending records into a verified master list: 452 rows became 392 real contacts, each with a status the evidence supported.

I check AI output the way I check anything else: against the source records, looking for patterns that are too neat, and separating what was verified from what was assumed.

## Measurement sanity checks

Dashboards mislead, too. A sudden drop in a metric can be a vendor changing its methodology rather than a real decline. I once traced an industry-wide drop in AI visibility scores to exactly that. Before you react to a number, I find out what it actually measures.

## What you get
- A cleaned, deduplicated dataset with a status for every record.
- The script that did the work, so the cleanup can be rerun on the next export.
- A short report: what was wrong, what changed, and what still needs a human decision.

## When to call me

Before a big campaign goes out to a merged list, after an acquisition or CRM migration, when a newsletter's bounce rate starts climbing, or when a report built with AI is about to go to leadership.

## Common questions

### Is client data kept private?

Yes. Data stays in your accounts or on encrypted storage I control for the duration of the project, it's never pasted into public AI tools, and it's deleted at the end unless you ask otherwise.

### Can you clean data directly inside a CRM?

Usually I export, clean, and re-import with your approval at each step, which keeps a record of every change. Direct in-CRM cleanup is possible when the CRM supports it safely.

**Related:** [AI agents and automation](https://gerriscorp.com/services/ai-automation/) · [Built with Claude Code](https://gerriscorp.com/case-studies/built-with-claude-code/)

[Send me the messy spreadsheet](https://gerriscorp.com/contact/)

Updated October 5, 2026

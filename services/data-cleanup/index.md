> Chris Abraham cleans and dedupes contact lists and CRMs with Python, and audits AI generated spreadsheets for fabricated or wrong data before you rely on them.
>
> Source: https://gerriscorp.com/services/data-cleanup/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Data cleanup and AI-output audits

Contact lists with thousands of duplicates. CRMs nobody trusts. Confident-looking spreadsheets an AI produced that turn out to be partly invented. I turn messy data into something you can rely on.

## Contact list and CRM cleanup

I build Python pipelines for the job instead of cleaning by hand, so the work is repeatable and every change can be traced. A typical pipeline repairs broken export columns, checks names for plausibility by country, recovers missing names from email addresses, catches surnames in the wrong field, merges duplicates across domains and spellings, and gives every record a status explaining what happened to it. I've run this on lists from a few thousand records to nearly ninety thousand. The details are in the [data cleanup case study](https://gerriscorp.com/case-studies/data-cleanup/).

The same approach works for CRM exports, newsletter lists, event registrations, and lists merged after an acquisition.

## Auditing AI output

AI tools now produce trackers, reports, and spreadsheets that look finished, and some contain values that were never real: actions logged that never happened, timestamps too regular to be genuine, records counted twice. I check AI output the way I check anything else: against the source records, looking for patterns that are too neat, and separating what was verified from what was assumed. Then I rebuild the file so every row is backed by evidence.

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

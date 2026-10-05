> Chris Abraham builds small, safe AI tools with Claude Code: human confirmation on every action, tests, secrets kept out of Git, and encrypted backups.
>
> Source: https://gerriscorp.com/services/ai-automation/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# AI agents and automation, built safely

Small AI tools and automations for real workflows, built with Claude Code and engineered so they can't send, spend, or delete anything without a person saying yes.

## Why I can build these

I built my own. Blackbox is a command-line chief of staff that runs on a Debian server I administer. It manages my tasks in Todoist, reads and writes my Google Calendar through my own Google Cloud OAuth project, triages work opportunities through Upwork's official MCP server, keeps state in SQLite, and drafts writing with whichever model does the job best. I directed the build with Claude Code from a 1,500-line script to about 9,600 lines in four days: 17 Python modules, an installer, a backup tool, and 106 end-to-end tests. Claude Code wrote the implementation; I specified the behavior, made the design decisions, tested every stage, and accepted or rejected the work. The full story is on [Built with Claude Code](https://gerriscorp.com/case-studies/built-with-claude-code/).

## Safety by design

Companies are discovering that AI agents need guardrails. These are the ones I build in from the start:
- **A human confirms every external action.** Each action has one unambiguous target, and nothing sends, submits, spends, or deletes on its own.
- **Deterministic first.** Everything that can be handled by ordinary code is, and models are reserved for writing and judgment. That makes the tool faster, predictable, and cheap: Blackbox's total model spend at launch was under three dollars.
- **Untrusted content is data.** Emails, web pages, and documents the tool reads are treated as data and never as instructions, which defends against prompt injection.
- **Secrets stay out of Git.** API keys and tokens live outside the repository.
- **Tests and a real deploy loop.** Work happens on a branch, tests run, the database is backed up, the change is merged and pushed, and a live smoke test confirms it.
- **Encrypted backups with tested restores.** Nightly AES-256 encrypted backups, and a restore actually performed, not assumed.
- **Model choice by evidence.** I test models from OpenAI, Anthropic, and open-weight providers against each other on the real task before choosing.

## What I build for clients

Focused tools with a clear job: a morning briefing assembled from your tasks, calendar, and inbox; triage of incoming requests into your project tool; a research assistant that gathers sources and drafts a reviewable summary; integrations between systems that don't talk to each other; command-line tools for repetitive website and data chores; and audits of AI output before anyone relies on it.

## How a pilot works

Every build starts as a pilot, defined in writing before work begins:
- **Inputs:** what goes in, from where.
- **Permissions:** which accounts and data it touches, and nothing more.
- **Outputs:** what it produces, where it's saved, and how a person reviews it.
- **Acceptance:** the tests that prove it works, run in front of you.
- **Handover:** the code in your repository, documentation, ownership of every account, and what to do when it fails.

## The questions I ask

What's the actual job? What happens after this step? Where is the result saved? Can you recover it if something goes wrong? What does this error mean? Does the system remember what it needs to remember? Those questions decide whether an AI tool saves time or creates a new mess.

## Advice before building

Not every team needs a custom tool. Often the right first step is advice: which tasks are worth automating, which off-the-shelf tools fit, what your team's working practices should be, and what should never be pasted into a public AI service. That's available on its own as part of [strategic advisory](https://gerriscorp.com/services/advisory/).

## Common questions

### Who owns what you build?

You do. Pilots run on your accounts, and the code, prompts, tests, and documentation are handed over at the end.

### Do you build large AI applications?

I build small, focused tools that prove value quickly. When a pilot needs to grow into a larger system, I specify it and work with developers who build at that scale.

**Related:** [Built with Claude Code](https://gerriscorp.com/case-studies/built-with-claude-code/) · [Data cleanup and AI-output audits](https://gerriscorp.com/services/data-cleanup/) · [Strategic advisory](https://gerriscorp.com/services/advisory/)

[Tell me the workflow you'd automate](https://gerriscorp.com/contact/)

Updated October 5, 2026

> A working method for using Claude Code and other AI coding assistants on real websites: specs, project memory, automated checks, review, and secrets.
>
> Source: https://gerriscorp.com/guides/ai-coding-assistants/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# How to use AI coding assistants on a business website safely

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

AI coding assistants such as Claude Code, Cursor, and GitHub Copilot can now do real work on real websites: migrations, redirect maps, templates, structured data, content checks across hundreds of pages. They work fast and they work confidently, including when they're wrong. The method below is how I get the speed without the damage.

## Start with a written spec

An assistant does exactly what it understands you to want, at full speed. Before any code, write down the goal, the constraints, and what done looks like. "Move the blog to the new platform" is a wish. A spec says: every old URL keeps working or redirects to its closest match, titles and dates carry over, images are copied and not hotlinked, the build fails if any internal link points to a missing page, and nothing ships until the redirect list has been checked. The assistant can help draft this, and a person decides it.

## Give the project a memory

Claude Code reads a `CLAUDE.md` file at the start of every session, and other tools have their own equivalents. Put the things that must never be forgotten there: the build command, the deploy process, the voice rules for copy, the files that must never be committed, the decisions already made and why. This site's project file holds its style rules and a list of names that must never appear on the site. The assistant reads it every time; a new contractor would need the same briefing.

## Turn the rules into checks

Instructions get forgotten. Automated checks don't. Every rule that can be tested by a script should be. The build for this site refuses to finish if a page title falls outside 50 to 60 characters, if a meta description is the wrong length, if two pages share a title, if any page links to one that doesn't exist, or if two pages share too much of their wording. When the assistant writes a new page, the build tells it what's wrong before I ever see the draft. The same approach works for any site: link checkers, HTML validators, accessibility tests, and unit tests for anything with logic in it.

## Small changes, reviewed
- **Use version control.** Every change goes through Git, on a branch, so anything can be undone and every change can be read as a diff.
- **Keep each change small enough to read.** A change that touches three files gets reviewed properly. One that touches three hundred gets skimmed.
- **Read the diff, not the summary.** An assistant's description of what it changed is a claim. The diff is the evidence.
- **Watch for scope creep.** Assistants like to tidy things nobody asked them to touch. Reject unrelated changes and ask again.

## Keep secrets and production out of reach

Never paste passwords, API keys, or customer data into a conversation, and never commit them to a repository. Give the assistant access to a copy of the site, a staging environment, or a local build, and keep deploys to production a deliberate human step, or an automated pipeline that runs only after the checks pass. For anything destructive, such as deleting files, rewriting history, or changing DNS, require explicit confirmation every time. Inventory the DNS records before touching any of them; a careless change can stop a company's email.

## Verify against the real world

Assistants are well read and out of date in places. They'll describe a platform setting that moved last year, or a search feature Google retired, with total confidence. For anything that depends on a third party's current behavior, check the vendor's documentation or test it directly. After deploying, check the live result: fetch the pages, test the redirects with `curl`, run PageSpeed Insights, and look at the page in a browser. "The code looks right" isn't the same as "the site works."

## Where assistants are strongest
- **Bulk, rule-based work.** Building a redirect map from hundreds of old URLs, rewriting templates across a site, generating structured data from page content, converting content between platforms.
- **Audits at scale.** Checking every page for missing titles, broken links, duplicate descriptions, or images without alt text, then fixing them.
- **Small internal tools.** Scripts that pull reports, clean exports, or automate a weekly chore.
- **Explaining unfamiliar code.** Reading an inherited theme or plugin and describing what it actually does.

## Where to slow down
- **Judgment calls.** Which pages to merge, which claims a page should make, what a client would or wouldn't want public. The assistant can propose; a person decides.
- **Security and payments.** Authentication, checkout, and anything handling personal data needs an expert review regardless of who wrote it.
- **Long sessions.** As a conversation grows, early instructions carry less weight. Restate the important rules, or keep them in the project memory file where they're read fresh.

## Someone has to be accountable

The assistant writes code; a person owns the outcome. For a business site that means someone who can read the diff, understands search and infrastructure, and will notice when a confident change is wrong. That's the role I play for clients: I write the spec, set up the checks, direct the assistant or the developers, and verify what ships.

See how this site and other projects were built in the [Claude Code case study](https://gerriscorp.com/case-studies/built-with-claude-code/), and what I build for clients under [AI tools and automation](https://gerriscorp.com/services/ai-automation/) and [fractional technical lead](https://gerriscorp.com/services/technical-lead/).

## References
- [Anthropic: Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

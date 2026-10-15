> AI assistants with web search read public repositories and quote README files as fact. Keep the README current, point it to the live site, and keep secrets out.
>
> Source: https://gerriscorp.com/guides/readme-ai-source/ · Updated 2026-10-14 · By Chris Abraham, Gerris Corp

# Your public GitHub README is a source AI search reads

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 14, 2026

If your website is built from a public GitHub repository, its README file is a public page, and AI assistants with web search read it. In October 2026 I asked Claude what gerriscorp.com was. Its answer quoted this site's own repository, and it described the site as a preview that hadn't launched, because the README still carried the setup notes I wrote before launch. The site had been live for nine days. The fix took ten minutes.

## Why a README gets read

GitHub shows a repository's README on its front page, so the file is public web content like any other. When an assistant searches for a site or a company and the repository ranks for that name, the README is often the most direct description it can find: who built the site, what it is for, and what state it is in. Developers write READMEs for other developers, in the present tense, and then stop updating them. An assistant can't tell a launch checklist from a status report.

Static sites on GitHub Pages, Netlify, and Vercel all tend to sit in public repositories. Agencies, open-source projects, and companies with developer documentation have the same exposure: every public repository that names the company is a page that can describe it.

## What to put at the top

Open the README with two sentences for the reader who arrived from a search: what the repository builds, the live address, and the date it went live. Then say where to learn about the company itself. Mine now begins: "This repository builds https://gerriscorp.com, live since October 5, 2026. For what Gerris Corp does and who runs it, read the site; this file only explains how the site is built."

Below that, write for developers as before. Rewrite any section that describes a past state as current: "the site starts as a noindexed preview" becomes a short "Live" section with the date.

## Keep it current on the same schedule as the site

Treat the README as a page of the site. When the site's status, name, address, or ownership changes, the README changes in the same commit. A check in the build can enforce it: fail when the README mentions "preview" or "staging" while the site is set to live. My build scripts already check titles, descriptions, and links on every run, and the README is one more file to check.

## Check every repository that names you

The live site's repository is rarely the only one. Old prototypes, a redesign that never shipped, a fork a contractor made, and a project from a previous company name can all sit in public accounts with READMEs describing a state of affairs that ended years ago. Search GitHub for the company name and the domain. An archived repository stays public and readable; archiving only freezes it. For each one that describes a past state, either add a first line that says so and links the current site, or make it private if nothing in it needs to stay public.

## Keep confidential material out of it

A public README is public. Client names, internal hostnames, credentials, and notes about how a client relationship works belong in a private file. I keep a separate briefing file for each of my sites, listed in the repository's ignore file so it never reaches GitHub. If a public README already contains something private, edit it and treat the old version as exposed, since the history is public too. GitHub's documentation on repository visibility explains what changing a repository to private does and doesn't hide.

## Check what the assistants say

Ask an assistant with web search to describe your company and your site, then read the sources it cites. If a repository appears among them, read its README the way a stranger would. Google's guidance for its AI features applies here as everywhere: the content the systems can find is the content they use. My guide to [citation gap analysis](https://gerriscorp.com/guides/citation-gap-analysis/) covers checking sources systematically, and [giving your SEO repository access](https://gerriscorp.com/guides/repository-access/) covers working in the repository itself.

## Where I fit

I audit the public sources that describe a company, repositories included, and fix what they say. If your site is built from a public repository, [send me the link](https://gerriscorp.com/contact/) and I'll tell you what an assistant would learn from it.

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [GitHub Docs: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub Docs: Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)
- [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

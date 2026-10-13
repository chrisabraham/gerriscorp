> A safe setup for letting an SEO consultant into your GitHub or GitLab repository: one repo, the Read role first, reviewed pull requests, and no secrets.
>
> Source: https://gerriscorp.com/guides/repository-access/ · Updated 2026-10-13 · By Chris Abraham, Gerris Corp

# How to give an outside SEO safe access to your code repository

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 13, 2026

On a site built with Next.js, React, or a headless CMS, the search problems live in the code, so the person fixing them needs to see it. Granting that access is a small, routine job when you set it up in the right order. Here is the order I ask clients to follow, and the reasons behind each step.

## Why an SEO asks for the repository at all

A crawl tells me that 900 pages share a title. The repository tells me which component writes it, which data it reads, and whether a fix will reach every route that uses it. Without the code, I write a ticket describing the symptom and your developer goes looking for the cause. With it, the ticket names the file, or arrives as a pull request ready for review. Read access alone usually cuts the time from finding to fix by a wide margin.

## Invite them to one repository, as an outside collaborator

On GitHub, a consultant belongs outside your organization's membership. Add them as an outside collaborator on the one repository that builds the website, rather than as an organization member who inherits base permissions across everything you own. Your other repositories, your internal tools, and your infrastructure code stay out of view. If the site is split across a frontend and a content repository, add them to both and nothing else.

## Start with the Read role

GitHub's repository roles, from least access to most, are Read, Triage, Write, Maintain, and Admin. GitHub's own guidance is to pick the role that fits each person's function without giving them more access than they need.
- **Read** is GitHub's role for people who view or discuss a project without changing it. That covers the whole diagnostic phase.
- **Triage** adds managing issues and pull requests without write access, which suits a consultant who files tickets in your tracker.
- **Write** is for contributors who push to the project, which an SEO needs only once they start making changes themselves.
- **Maintain** and **Admin** are for your own team. An outside SEO never needs either.

GitLab has its own set: Guest, Reporter, Developer, Maintainer, and Owner, ordered from fewest permissions to most, plus specialized Planner and Security Manager roles. Reporter is the usual starting point for an outside reviewer there, and Developer is roughly the equivalent of GitHub's Write.

## Grant Write only after main is protected

Before anyone outside your team can push, make sure nobody can push straight to your main branch. On GitHub, a ruleset or a branch protection rule controls who can push to a branch and can require reviews on pull requests before they merge. GitHub's documentation notes that when both a ruleset and a protection rule apply to the same branch, all the rules apply, and the most restrictive version of each wins.

With that in place, Write access becomes safe: the consultant can create branches and open pull requests, and every change still waits for one of your people to approve it. Nothing they write reaches production without your review.

## Use deploy previews to see each change before merge

Netlify builds a Deploy Preview for pull requests in a connected GitHub, GitLab, Bitbucket, or Azure DevOps repository, and Vercel creates a preview deployment for every push to a non-production branch and every pull request. Each preview gets its own URL. Your team can click through the change, and I can check what a crawler will see on it: titles, canonicals, structured data, status codes, and rendered content. Netlify adds an `X-Robots-Tag: noindex` header to its previews, which asks search engines to leave them out of results. For anything sensitive, Netlify recommends password protection on top.

## Keep secrets out of the repository

API keys, database passwords, and tokens belong in your host's environment variables, never in a committed file. Anyone you give read access can read every file and its history, so a key committed two years ago and deleted since is still visible to them. Two habits protect you:
- **Turn on push protection.** GitHub's push protection is a secret scanning feature that blocks pushes containing recognized credentials before they reach the repository, from the command line, the web interface, and the API.
- **Rotate anything that ever leaked.** If secret scanning finds an old key in the history, revoke it and issue a new one before you invite anyone in.

An SEO needs no production credentials to do this work. If someone asks for them, ask why.

## The CMS only option

Some teams can't open the codebase, for contractual or security reasons. That still leaves plenty of room. Give the consultant an editor role in the CMS for content, titles, and descriptions, Search Console access, and the preview URLs. They write tickets with the evidence and the acceptance criteria, and your developer makes the code changes. It's slower, and it works.

## Remove access when the engagement ends

Put the end date in your own calendar on the day you grant access. When the work finishes, remove the outside collaborator from the repository, take them out of Search Console and the hosting dashboard, and revoke any deploy keys or tokens created for the engagement.

## A checklist for the day you say yes
1. Invite the consultant as an outside collaborator on the website repository only.
2. Assign Read on GitHub, or Reporter on GitLab.
3. Confirm deploy previews are switched on for pull requests.
4. Check that push protection or secret scanning is enabled and the history is clean.
5. Add a ruleset or branch protection requiring a reviewed pull request on main.
6. Move to Write, or Developer, only once that rule is in place.
7. Set a reminder to remove every grant at the end date.

This is the setup I ask for at the start of an [SEO engineering](https://gerriscorp.com/services/seo-engineering/) engagement. For how I work once I'm in, see [developer specs and QA](https://gerriscorp.com/services/developers/) and the guide to [working safely with AI coding assistants](https://gerriscorp.com/guides/ai-coding-assistants/).

## References
- [GitHub Docs: Repository roles for an organization](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)
- [GitHub Docs: About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [GitHub Docs: About push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)
- [GitLab Docs: Roles and permissions](https://docs.gitlab.com/user/permissions/)
- [Netlify Docs: Deploy Previews](https://docs.netlify.com/site-deploys/deploy-previews/)
- [Vercel Docs: Preview deployments](https://vercel.com/docs/deployments/preview-deployments)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

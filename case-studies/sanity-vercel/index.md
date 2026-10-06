> A local service business on Sanity and Vercel: Chris Abraham set SEO priorities, merged metadata changes through GitHub, and verified the prerendering.
>
> Source: https://gerriscorp.com/case-studies/sanity-vercel/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Local service business on Sanity and Vercel: SEO in the repository

A junk removal company's website ran on a modern stack: Sanity for content, Vercel for hosting, and GitHub for code. It had the classic problems of a client-rendered site, and the fixes had to go through code.

## The problems
- Client-side rendering, so crawlers received thin HTML.
- Duplicate titles and meta descriptions across many pages.
- Heading structure problems.
- Soft 404s: missing pages returning a success status.
- Missing or inconsistent canonical and structured data signals.

## Who did what

The developer implemented the substantial infrastructure changes, including prerendered HTML and deployment improvements. I handled the SEO side: setting priorities, specifying what each page needed, reviewing the developer's changes, and verifying the live result independently. I also made code-level metadata changes myself through GitHub, in a pull request that was reviewed and merged.

## Why it matters

Many businesses now run on headless CMSs and JavaScript frameworks where there's no SEO plugin to configure. The work happens in templates, routes, and build settings. I can read that code, propose and make changes through the team's normal review process, and check what crawlers actually receive after deployment.

It also means changes are reviewable: every edit has a commit, a reviewer, and a way back.

## How it was checked

Crawls before and after the prerendering change, raw HTML fetched from production, Search Console's live test, and a review of titles, descriptions, canonicals, and status codes across the site.

## Status

Core fixes deployed and verified; a final audit is under way. See [developer specs and implementation QA](https://gerriscorp.com/services/developers/).

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

Updated October 5, 2026

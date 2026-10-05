> Chris Abraham turns a diagnosis into a prioritized developer spec with evidence and acceptance criteria, then verifies on the live site that the fix shipped.
>
> Source: https://gerriscorp.com/services/developers/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Developer specs and implementation QA

Your developers are good. What they need is someone to tell them exactly what to build, why, and how to know it's done, and then to check that it was. That's this service.

## The spec

I turn a diagnosis into a developer-ready specification. A recent one ran to 13 pages of prioritized items from P0 to P3, each with:
- **Confirmed evidence:** affected URLs, crawl data, screenshots, and the observed behavior.
- **Consequence:** what the problem costs, in plain terms, which sets the priority.
- **Build steps:** exactly what to change, in which template, file, or setting.
- **Acceptance criteria:** a testable definition of done.

I generate specs programmatically from the evidence, so they stay consistent and can be regenerated as findings change. The owner gets a separate plain-English summary, so the engineer gets precision and the CEO gets clarity, and neither has to wade through the other's document.

## A sample ticket

```
P0: Product specs, FAQs, and reviews missing from initial HTML

Affected: all /products/* templates (example: /products/widget-200)
Evidence: spec table, FAQ, and reviews render only after an
  x-intersect scroll trigger; crawler extraction shows 250 to 400
  words per product page versus 2,000+ for category pages.
Consequence: product pages clustered in "Crawled, currently not
  indexed"; organic product traffic falling.
Build: render these sections in the server HTML; keep the
  scroll animation as progressive enhancement only.
Acceptance: a plain fetch of the product URL returns the spec
  table, FAQ, and review text; Search Console live test shows
  them in the rendered HTML.
```

## Implementation QA

When the developer says it's done, I check, against the acceptance criteria, on the live site, in the page source. CMS panels and staging environments say one thing; the live HTML says what crawlers and visitors actually get. I check for side effects too, such as a fix applied too broadly or a cache that never purged, and I follow up on anything still open.

## Working with your team
- Direct work with client developers and IT on cache purges, template constraints, CMS publish behavior, and access.
- Content changes separated from template, routing, infrastructure, CDN, and rendering changes, so each goes to the person who can fix it.
- Plain explanations in both directions.
- Specialist subcontractors brought in and managed when a job needs one, with a clear handoff and a regular status cadence.
- A blame-free working relationship. Developers are usually solving five problems at once; my job is to make one of them easy.

## In your repository

I work in GitHub repositories through branches and pull requests, and I've made metadata changes directly in React and TypeScript codebases under review. I use AI coding assistants to search a codebase alongside crawl evidence, which finds the file responsible for a problem in minutes instead of days.

## Fractional SEO and AI search lead

For teams shipping continuously, I join as the embedded, part-time person who writes the SEO and AEO acceptance criteria for new work, reviews templates and releases before they ship, and catches the change that's about to hide your content from Google.

## Common questions

### Can you change the code directly?

When you want me to and access is set up for it, I work through branches and pull requests so your team reviews every change. Many teams prefer that I write the specs and verify the result, which works just as well.

### Which ticket systems do you use?

Whatever your team uses, such as Jira, Linear, GitHub Issues, or Basecamp.

**Related:** [Fractional technical lead](https://gerriscorp.com/services/technical-lead/) · [Content the crawler never sees](https://gerriscorp.com/services/crawler-visibility/) · [JavaScript SEO](https://gerriscorp.com/guides/javascript-seo/)

[Get your developers a real spec](https://gerriscorp.com/contact/)

Updated October 5, 2026

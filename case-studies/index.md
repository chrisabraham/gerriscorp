> Anonymized case studies from Chris Abraham: JavaScript rendering failures on three stacks, a Next.js migration plan, an app takeover, and data cleanup.
>
> Source: https://gerriscorp.com/case-studies/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Case studies

Each case describes the problem, what I did, who did what, and how the work was checked. Clients are described by industry; I name them only with their permission.

## E-commerce on Magento and Hyvä: product content Googlebot never saw

**Problem.** Organic traffic was falling and the client's team had no explanation.

**What I found.** Product templates used Alpine.js to mount specifications, FAQs, and reviews only when a visitor scrolled them into view, with `x-intersect` wrapped around `x-if`. A crawl showed category pages with thousands of words and flagship product pages with 250 to 400 words, despite page weights above 1.2 MB. Search Console showed a selective cluster of product pages marked "Crawled, currently not indexed." A spam backlink spike and a redirect problem in the same period were investigated on separate tracks.

**Deliverable.** The mechanism, the evidence, and a developer spec with acceptance criteria. See [content the crawler never sees](https://gerriscorp.com/services/crawler-visibility/).

## WordPress media site: consent management hiding every article

**Problem.** Large numbers of articles sat in "Crawled, currently not indexed," with no crawl errors anywhere.

**What I found.** The site's consent-management platform blocked scripts for visitors who hadn't accepted cookies, including the script that initialized the jQuery UI tabs holding each article's content. Googlebot never accepts cookies, so it saw empty tabs on every page.

**How it was checked.** Rendered HTML from Search Console's live test compared with a consenting browser session.

## React event platform: links crawlers couldn't follow

**Problem.** Server-side rendering had been added, yet pages still weren't being discovered.

**What I found.** Navigation used the router's click handlers without real anchor links, so crawlers had no paths to the pages rendering had already fixed. The fix was real `<a href>` links.

## Clinical practice: migration investigation and technical direction

**Problem.** A practice moving from WordPress to a Next.js site on Netlify needed to know what the new site still depended on from the old one.

**What I did.** Combined crawls and exports with a read-only, AI-assisted analysis of the Next.js repository using Claude Code. The analysis identified thousands of references to media still hosted on the old WordPress site and the handful of central files responsible. I turned that into a developer-ready plan, and worked on sequencing, media and redirect requirements, DNS review, and launch verification. The site's developer carried out the implementation.

## Consumer skincare brand: application takeover and operations

**Problem.** A React application changed hands after an outage, with project files, credentials, hosting, DNS, and repository arrangements spread across several parties.

**What I did.** Assessed the handoff and inventoried what existed. Then, hands-on, I worked on the DigitalOcean Linux server over SSH: edited environment and application configuration, managed the application with PM2, and diagnosed a port conflict that was keeping it down.

## Seasonal multi-site retailer: business-aware technical planning

**Problem.** A retailer with several sites and its own staff needed technical problems fixed without disrupting its peak season.

**What I did.** Brought in as the accountable lead working with the client's existing people, I proposed the investigation, the access needed, a migration review, and a staged plan that put risky changes after the peak.

## Shopify: duplicate and broken product schema

**What I did.** Working in a duplicated theme so the live store was never at risk, I edited the Liquid templates, found an HTML-encoding bug corrupting the structured data output, and consolidated duplicate Product schema into a single valid block.

## Contact data: a 28,000-record cleanup and an AI tracker audit

**What I did.** Built Python pipelines to clean and deduplicate more than 28,000 exported contact records, with name validation by country, name recovery from email addresses, and a resolution status on every record. Separately, I audited an AI-generated outreach tracker that marked bounced and nonexistent contacts as sent, with fabricated timestamps, and rebuilt it into a verified list: 452 rows became 392 real contacts. See [data cleanup](https://gerriscorp.com/services/data-cleanup/).

## Measurement: a drop that wasn't a decline

**What I did.** Traced an industry-wide drop in AI visibility scores to a change in the vendor's methodology, which kept a client from reacting to a decline that hadn't happened.

## Long-term perception management for a founder

**What I do.** An eight-year retainer shaping search results and the public record for a high-net-worth founder, removing personal information from data brokers, and reporting monthly, now alongside a security firm's open-source intelligence program.

## My own builds

Blackbox, my command-line assistant, Hill Mole's move off Movable Type, and this site are covered on [Built with Claude Code](https://gerriscorp.com/case-studies/built-with-claude-code/).

[Tell me about your problem](https://gerriscorp.com/contact/)

Updated October 5, 2026

> A Create React App event platform with 2,000 pages Google never found: Chris Abraham wrote a 13 page developer spec ranked P0 to P3 and verified the fixes.
>
> Source: https://gerriscorp.com/case-studies/react-event-platform/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# React event platform: 2,000 pages Google couldn't reach

An event and nightlife discovery app built with Create React App needed about 2,000 event pages indexed. Three months of Search Console data showed impressions on the home page and almost nothing else.

## My role

Strategist and QA. I diagnosed the problems, wrote the specification, and verify the results; the founder's developer implements.

## What I found
- **An empty home page.** The home page served an empty root element; everything appeared only after JavaScript ran.
- **No crawlable links.** Event cards navigated with click handlers instead of real `<a href>` links, so crawlers had no path to the event pages.
- **Orphaned pages.** The event pages themselves already had server-side rendering, so their HTML was fine, but nothing linked to them.
- **Wrong canonicals.** The canonical tags on the events and community sections pointed to the home page, telling Google those pages were duplicates of it.

## What I delivered

Two documents. For the founder, a plain-language summary of what was wrong and what it would take. For the developer, a 13-page specification of 12 items ranked P0 to P3, each with the evidence, the consequence, exact build steps, and acceptance criteria. The P0 items were real anchor links on event cards, server-side rendering for the home page and feed, and manual indexing requests for priority pages.

## How it is checked

Each item has a testable acceptance criterion, such as event links present in the server's HTML and self-referencing canonicals on each section. I verify the developer's changes against those criteria with a crawl and Search Console's live test, with remaining checks on how page heads are generated and whether the canonicals were corrected.

## Status

Reports delivered and acknowledged; verification of the developer's fixes in progress. See [developer specs and implementation QA](https://gerriscorp.com/services/developers/).

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

Updated October 5, 2026

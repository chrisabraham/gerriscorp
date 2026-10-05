> A bilingual WordPress review site indexed on Bing but barely in Google: Chris Abraham traced it to consent blocking that left article tabs empty.
>
> Source: https://gerriscorp.com/case-studies/consent-blocking/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# WordPress media site: a consent banner hiding every article

A bilingual English and Italian site of film reviews was almost absent from Google, while Bing indexed it normally. There were no crawl errors anywhere, just page after page in "Crawled, currently not indexed."

## My role

Paid diagnosis for the site's owner, with a call to walk through the findings.

## What I found

Every review's content lived inside jQuery UI tabs. The site's consent-management platform used prior-consent blocking: scripts were held back until a visitor accepted cookies. One of the held-back scripts was the one that initialized the tabs. Googlebot never accepts cookies, so it crawls every page as a permanent non-consenting visitor, and it rendered each page with the structure intact and the content empty. That explains the gap between Google and Bing, which handled the pages differently.

Two secondary problems made things worse: 97% of pages shared the same hardcoded H2 headings, and 95% of internal links had no anchor text, so even the visible structure told search engines almost nothing about each page.

## What I recommended
- Exempt the scripts that build the page's content from consent blocking, or render the tab content in the HTML so it doesn't depend on scripts at all. Consent rules should govern tracking and advertising scripts, never the article itself.
- Replace the hardcoded H2s with headings drawn from each review.
- Give internal links descriptive anchor text.

## How it was checked

Pages compared in a consenting browser session and a non-consenting one, the blocked scripts identified in the consent platform's configuration, and the empty tabs matched to the indexing pattern. Confirmation in Search Console's rendered HTML was the next step once access was granted.

## Why it matters

Consent platforms are now on almost every site, and their default settings can hide content from every crawler that never clicks "accept." It's one of three examples of the same failure on [content the crawler never sees](https://gerriscorp.com/services/crawler-visibility/).

Updated October 5, 2026

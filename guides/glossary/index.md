> Plain definitions of technical SEO, AI search, site speed, and email terms: AEO, GEO, canonical tags, Core Web Vitals, DMARC, IndexNow, llms.txt, and many more.
>
> Source: https://gerriscorp.com/guides/glossary/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Glossary of SEO, AI search, and technical website terms

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 5, 2026

Plain definitions of the terms that come up in my work, written so each one makes sense on its own.

**301 redirect**
A permanent redirect from one URL to another. Search engines transfer the old URL's ranking signals to the new one. The 308 status code is also permanent; 302 and 307 are temporary.

**AEO (answer engine optimization)**
Shaping content so it directly answers the questions people ask, in a form that search features and AI assistants can quote.

**AI Mode**
Google Search's conversational, AI-generated search experience, which answers questions with a written response and links, built on Google's search index.

**AI Overviews**
The AI-generated summaries that appear at the top of many Google search results, with links to the pages they draw on.

**Alt text**
A text description of an image in the HTML alt attribute, read aloud by screen readers and used by search engines to understand the image.

**BIMI**
Brand Indicators for Message Identification: a DNS record that lets supporting inboxes show a brand's logo beside authenticated email. It requires DMARC enforcement.

**Bing Webmaster Tools**
Microsoft's free service for monitoring a site in Bing, whose index also feeds Microsoft Copilot and other AI assistants.

**Canonical tag**
A link element that tells search engines which URL is the preferred version of a page when several URLs show the same or similar content. Google treats it as a strong hint.

**CDN (content delivery network)**
A network of servers around the world that stores copies of a site's files close to visitors, making pages faster and absorbing traffic spikes and attacks. Cloudflare is the best-known example.

**Core Web Vitals**
Google's three page experience metrics: Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift, measured from real Chrome users.

**Crawl budget**
How many URLs a search engine is willing and able to crawl on a site in a given period. It matters mostly for large sites and sites with many low-value URLs.

**Crawled, currently not indexed**
A Google Search Console status meaning Google fetched a page and chose not to index it. See the [full guide](https://gerriscorp.com/guides/crawled-not-indexed/).

**CLS (Cumulative Layout Shift)**
A Core Web Vital measuring how much visible content moves unexpectedly while a page loads. Good is 0.1 or less.

**Discovered, currently not indexed**
A Search Console status meaning Google knows a URL exists and hasn't crawled it yet, usually a sign of crawl priority problems.

**DKIM**
DomainKeys Identified Mail: a cryptographic signature on outgoing email, verified against a public key published in DNS.

**DMARC**
A DNS policy telling receiving mail servers what to do with mail that fails SPF and DKIM alignment, and where to send reports. Policies are none, quarantine, and reject.

**E-E-A-T**
Experience, expertise, authoritativeness, and trustworthiness: the qualities Google's quality rater guidelines ask raters to assess, and a useful description of what makes content credible.

**GEO (generative engine optimization)**
Making a business and its content easy for AI systems to find, understand, and cite in generated answers.

**Google Search Console**
Google's free service for monitoring how a site appears in Google Search: indexing, queries, clicks, Core Web Vitals, and errors.

**hreflang**
An annotation that tells search engines which language or regional version of a page to show to which users.

**IndexNow**
An open protocol that lets a site notify Bing, Yandex, and other participating search engines immediately when pages are added, changed, or removed.

**INP (Interaction to Next Paint)**
A Core Web Vital measuring how quickly a page responds to taps, clicks, and key presses. Good is 200 milliseconds or less. It replaced First Input Delay in March 2024.

**JSON-LD**
A format for adding structured data to a page in a script block, recommended by Google for schema.org markup.

**LCP (Largest Contentful Paint)**
A Core Web Vital measuring how long the largest visible element, usually a hero image or headline, takes to appear. Good is 2.5 seconds or less.

**llms.txt**
A proposed convention, introduced in 2024, for a plain Markdown file at a site's root that summarizes the site and links to its key pages for language models. Adoption by AI companies is still emerging. This site publishes [one](https://gerriscorp.com/llms.txt).

**Meta description**
A short summary of a page in its HTML head, often shown under the title in search results. Usually 140 to 160 characters.

**robots.txt**
A file at a site's root that tells crawlers which paths they may fetch. It controls crawling, not indexing; a blocked page can still appear in results if other sites link to it.

**Schema.org**
The shared vocabulary search engines use for structured data, describing organizations, people, products, services, articles, events, and much more.

**Server-side rendering**
Generating a page's full HTML on the server before sending it, so browsers and crawlers receive the content without running JavaScript. Static generation does the same at build time.

**Soft 404**
A page that tells visitors it doesn't exist or has nothing to show, while returning a 200 success status. Google treats it as an error.

**SPF**
Sender Policy Framework: a DNS record listing the servers allowed to send email for a domain. It allows at most ten DNS lookups.

**Structured data**
Machine-readable information about a page, usually schema.org in JSON-LD, describing what the page is about and how it relates to people, organizations, and other pages.

**Title tag**
The HTML title of a page, shown in browser tabs and usually as the headline of a search result. Usually 50 to 60 characters.

**TTFB (time to first byte)**
How long a browser waits for the first byte of a server's response. Slow TTFB delays everything else, and caching and CDNs reduce it.

**XML sitemap**
A file listing the URLs a site wants search engines to crawl, with optional last-modified dates.

Want these applied to your site? See [services](https://gerriscorp.com/services/).

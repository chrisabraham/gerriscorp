> Plain definitions of technical SEO, AI search, site speed, and email terms: AEO, GEO, canonical tags, Core Web Vitals, DMARC, IndexNow, llms.txt, and many more.
>
> Source: https://gerriscorp.com/guides/glossary/ · Updated 2026-10-15 · By Chris Abraham, Gerris Corp

# Glossary of SEO, AI search, and technical website terms

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 5, 2026 · Updated October 15, 2026

Plain definitions of the terms that come up in my work, written so each one makes sense on its own. The [index](https://gerriscorp.com/site-index/) lists every page where a term comes up.

**301 redirect**
A permanent redirect from one URL to another. Search engines transfer the old URL's ranking signals to the new one. The 308 status code is also permanent; 302 and 307 are temporary.

**Acceptance criteria**
The plain statements a finished change has to satisfy before anyone calls it done, written before the work starts. They turn a request into something a developer can build and a reviewer can check.

**AEO (answer engine optimization)**
Shaping content so it directly answers the questions people ask, in a form that search features and AI assistants can quote.

**AI Mode**
Google Search's conversational, AI-generated search experience, which answers questions with a written response and links, built on Google's search index.

**AI Overviews**
The AI-generated summaries that appear at the top of many Google search results, with links to the pages they draw on.

**AI washing**
Claiming artificial intelligence a product doesn't really use, or overstating what its AI does. The SEC brought its first AI washing cases in March 2024; see [how to vet an AI vendor's pitch](https://gerriscorp.com/guides/ai-vendor-pitch/).

**Alt text**
A text description of an image in the HTML alt attribute, read aloud by screen readers and used by search engines to understand the image.

**Amara's law**
Roy Amara's observation that people overestimate a technology's effect in the short run and underestimate it in the long run. It's the first test in [hype or real shift](https://gerriscorp.com/guides/hype-or-shift/).

**BIMI**
Brand Indicators for Message Identification: a DNS record that lets supporting inboxes show a brand's logo beside authenticated email. It requires DMARC enforcement.

**Bing Webmaster Tools**
Microsoft's free service for monitoring a site in Bing, whose index also feeds Microsoft Copilot and other AI assistants.

**Canonical tag**
A link element that tells search engines which URL is the preferred version of a page when several URLs show the same or similar content. Google treats it as a strong hint.

**CDN (content delivery network)**
A network of servers around the world that stores copies of a site's files close to visitors, making pages faster and absorbing traffic spikes and attacks. Cloudflare is the best-known example.

**Citation gap**
A page AI assistants cite when answering your buyers' questions that names your competitors and leaves you out. Finding them is the job of a [citation gap analysis](https://gerriscorp.com/guides/citation-gap-analysis/).

**CLS (Cumulative Layout Shift)**
A Core Web Vital measuring how much visible content moves unexpectedly while a page loads. Good is 0.1 or less.

**Content brief**
A one-page instruction that settles a page's question, answer, evidence, and limits before anyone writes. See [writing a content brief](https://gerriscorp.com/guides/content-briefs/).

**Core update**
A broad recalibration of Google's ranking systems, announced a few times a year and logged on the Search Status Dashboard. Losses after one reflect being outranked, and Google says recovery can take months.

**Core Web Vitals**
Google's three page experience metrics: Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift, measured from real Chrome users.

**Crawl budget**
How many URLs a search engine is willing and able to crawl on a site in a given period. It matters mostly for large sites and sites with many low-value URLs.

**Crawled, currently not indexed**
A Google Search Console status meaning Google fetched a page and chose not to index it. See the [full guide](https://gerriscorp.com/guides/crawled-not-indexed/).

**Crawler Hints**
A free Cloudflare feature that watches content change as it passes through Cloudflare's cache and notifies IndexNow engines such as Bing. Google doesn't take part.

**Discovered, currently not indexed**
A Search Console status meaning Google knows a URL exists and hasn't crawled it yet, usually a sign of crawl priority problems.

**DKIM**
DomainKeys Identified Mail: a cryptographic signature on outgoing email, verified against a public key published in DNS.

**DMARC**
A DNS policy telling receiving mail servers what to do with mail that fails SPF and DKIM alignment, and where to send reports. Policies are none, quarantine, and reject.

**E-E-A-T**
Experience, expertise, authoritativeness, and trustworthiness: the qualities Google's quality rater guidelines ask raters to assess, and a useful description of what makes content credible.

**Email blocklist**
A list of IP addresses and domains that spam filters consult to reject or junk mail, also called a DNSBL. Getting off one starts with fixing the cause; see [blocklist recovery](https://gerriscorp.com/guides/email-blocklist-recovery/).

**GEO (generative engine optimization)**
Making a business and its content easy for AI systems to find, understand, and cite in generated answers.

**Git**
The version control system almost every software team uses. It records each change to a set of files, who made it, and why, so any version can be restored.

**Google Search Console**
Google's free service for monitoring how a site appears in Google Search: indexing, queries, clicks, Core Web Vitals, and errors.

**hreflang**
An annotation that tells search engines which language or regional version of a page to show to which users.

**HSTS (HTTP Strict Transport Security)**
A response header that commits browsers to HTTPS for a site for a chosen length of time. Add preload only once every subdomain serves HTTPS, because preload is slow to reverse.

**Hype cycle**
Gartner's curve for a new technology's reputation: a trigger, a peak of inflated expectations, a trough of disillusionment, a slope of enlightenment, and a plateau of productivity.

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

**OAI-SearchBot**
OpenAI's crawler for ChatGPT search. It's controlled separately from GPTBot, the training crawler, so a site can appear in ChatGPT answers while declining to be used for training.

**Orange cloud (proxied)**
A Cloudflare DNS record whose traffic runs through Cloudflare's network, gaining caching, compression, and attack protection. Gray means Cloudflare answers DNS and steps aside.

**Pull request**
A proposed set of changes to a repository, presented for review and comment before it's merged. Requiring one for every change gives an owner a complete history; see [hiring developers](https://gerriscorp.com/guides/hiring-developers/).

**README**
The introductory file at the top of a code repository. On a public GitHub repository it's a public page that AI assistants with web search read, so it should describe the live site; see [your README is a source AI reads](https://gerriscorp.com/guides/readme-ai-source/).

**Repository**
The folder of code and content Git tracks, along with its full history. Owning the repository, in an account the business controls, is owning the website.

**robots.txt**
A file at a site's root that tells crawlers which paths they may fetch. It controls crawling, not indexing; a blocked page can still appear in results if other sites link to it.

**Scaled content abuse**
The spam policy covering mass-produced pages made mainly to rank, by any method, human or machine. Google's 2026 spam updates focused on it.

**Schema.org**
The shared vocabulary search engines use for structured data, describing organizations, people, products, services, articles, events, and much more.

**Server-side rendering**
Generating a page's full HTML on the server before sending it, so browsers and crawlers receive the content without running JavaScript. Static generation does the same at build time.

**Site reputation abuse**
Hosting third-party pages on an established site so they ride its reputation in search. Google introduced the policy in 2024 and updated it in August 2026.

**Soft 404**
A page that tells visitors it doesn't exist or has nothing to show, while returning a 200 success status. Google treats it as an error.

**Spam update**
An upgrade to the systems that detect violations of Google's spam policies. Unlike a core update, it targets specific behavior, and the sites it catches tend to fall fast.

**Speculation rules**
A JSON block in a script tag that tells Chrome and Edge which links to prefetch or prerender before the reader clicks, so the next page opens at once. See [speculation rules](https://gerriscorp.com/guides/speculation-rules/).

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

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

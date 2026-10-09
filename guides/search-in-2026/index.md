> Every 2026 Google core and spam update with dates, the new spam rule against manipulating AI answers, what Bing and ChatGPT now report, and what to do now.
>
> Source: https://gerriscorp.com/guides/search-in-2026/ · Updated 2026-10-09 · By Chris Abraham, Gerris Corp

# The state of search in 2026: every Google update so far, and the AI shift behind them

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 9, 2026

2026 has been the busiest year for Google's ranking systems in a long time: two core updates, four spam updates, and a rule change that brings AI Overviews and AI Mode under the spam policies. Here is what happened, in order, from Google's own records, along with what Bing and OpenAI now let site owners see, and what all of it means for anyone who publishes on the web.

## The 2026 updates, from Google's dashboard

Google logs every confirmed ranking update on its Search Status Dashboard. Through early October, 2026 has seven:
- **February Discover update:** began February 5, ran about 22 days. It changed what appears in the Discover feed, separately from Search.
- **March spam update:** began March 24, finished in under a day.
- **March core update:** began March 27, ran about 12 days.
- **May core update:** began May 21, ran about 12 days, finishing June 2.
- **June spam update:** began June 24, ran about two days.
- **August spam update:** began August 18, ran under three days.
- **September spam update:** began September 24 and ran nearly two weeks, far longer than the year's earlier spam updates.

Core updates reassess how every page ranks against everything else, and pages can rise or fall. Spam updates improve the automated systems that detect policy violations, and the sites they hit tend to drop hard and fast.

## The big rule change: AI answers are now inside the spam policies

In May, Google revised the opening of its spam policies. Spam now explicitly includes "attempting to manipulate generative AI responses in Google Search," which covers AI Overviews and AI Mode. The June spam update was widely reported as the first to enforce it. In practice, the tactics now in scope include:
- Hidden text or instructions aimed at AI systems: white-on-white copy, zero-size fonts, or prompts tucked into markup that try to make an assistant favor a brand.
- Structured data that claims things the visible page doesn't say.
- Networks of near-identical "best of" pages built to seed the answers an AI assembles.

Security researchers have shown for two years that hidden page text can steer AI search tools. Search engines are now treating those tricks the way they treated keyword stuffing in 2005.

## Scaled content abuse is the year's main target

Google's policy defines scaled content abuse by intent and outcome: many pages made primarily to manipulate rankings, written by automation, by people, or by both. Automation alone is never the violation; the purpose is. Reporting on the August and September updates centered on sites that mass-published AI-written pages with no review and nothing original in them. Two older policies stayed in the news alongside it:
- **Site reputation abuse:** renting a trusted site's subfolder or subdomain to third-party content, coupons, gambling, or affiliate pages, to borrow its rankings.
- **Expired domain abuse:** buying a dead domain with history and filling it with low-value pages to exploit its old reputation.

## What Google says about optimizing for AI Overviews

Google's own documentation is blunt: there are no additional requirements to appear in AI Overviews or AI Mode, and no special optimizations, files, or schema are needed. A page has to be indexed and eligible to show a snippet. The recommended practices are the ordinary ones: allow crawling, link pages internally, keep important content in text, and make structured data match the visible page. Traffic from both features is counted in Search Console's Performance report under the Web search type. Every vendor selling a secret AI Overview formula is selling something Google says doesn't exist.

## Bing and ChatGPT now show their work

Bing Webmaster Tools added an AI Performance report, in public preview since February. It counts how often Copilot, Bing's AI summaries, and some partner integrations cite your pages, and it lists the grounding queries that led to those citations. It counts citations only, no clicks, and it is a rare first-party view of how an AI search product uses a site.

OpenAI documents its crawlers separately. `OAI-SearchBot` decides whether a site can appear in ChatGPT search; `GPTBot` collects training data. Each is controlled independently in robots.txt, so a site can welcome search and decline training. A site that blocks OAI-SearchBot, often by accident through a firewall or CDN bot setting, simply drops out of ChatGPT's answers.

## A measurement change that still confuses reports

In September 2025, Google stopped honoring the `num=100` parameter that let rank trackers load a hundred results at once. Desktop impressions in Search Console fell for most sites and average position jumped, because bots had been inflating the counts. Any year-over-year report that spans September 2025 needs that footnote, or it will show a decline that never happened to real visitors.

## What wins in this environment
- **Evidence of real work.** Original data, photos, tests, case details, and first-hand experience: material an assistant can't produce by summarizing other pages.
- **Fewer, better pages.** Consolidate thin and overlapping pages into ones that fully answer a question.
- **Clean access.** Check robots.txt, CDN, and firewall settings for every crawler you want: Googlebot, Bingbot, OAI-SearchBot, and the rest.
- **Honest markup.** Structured data that matches the page, and nothing hidden.
- **A clear entity.** Consistent names, addresses, and profiles across the web, so every engine and assistant knows exactly who you are.

For the crawler side, see [how AI assistants decide what to say about your business](https://gerriscorp.com/guides/ai-assistants/) and [my robots.txt guide](https://gerriscorp.com/guides/robots-txt/). If a 2026 update has already hit you, start with [how to diagnose a traffic drop](https://gerriscorp.com/guides/traffic-drop/), or [send me the dates and the domain](https://gerriscorp.com/contact/).

## References
- [Google Search Status Dashboard: Ranking incident history](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history)
- [Google Search Central: Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google Search Central: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Search Engine Journal: Google spam update rolls out, AI manipulation in scope](https://www.searchenginejournal.com/seo-pulse-google-spam-update-rolls-out-ai-manipulation-in-scope/580565/)
- [Bing Webmaster Tools](https://www.bing.com/webmasters/)
- [OpenAI: Overview of OpenAI crawlers](https://developers.openai.com/docs/bots)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

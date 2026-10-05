> Where ChatGPT, Claude, Gemini, Perplexity, and Google AI Overviews get their answers about a business, which crawlers feed them, and what you can do about it.
>
> Source: https://gerriscorp.com/guides/ai-assistants/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# How AI assistants decide what to say about your business

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 5, 2026

When someone asks ChatGPT, Claude, Gemini, Perplexity, or Google's AI Overviews about your company, the answer comes from two places: what the model learned in training, and what it finds by searching the web right then. You can influence both, and the second is where most of the action is.

## Two sources of knowledge

### Training data

Every large language model is trained on a huge snapshot of text, much of it crawled from the public web, and that knowledge stops at a training cutoff. What a model "knows" about you from training reflects whatever was public and widely repeated before that date. It changes only when the company trains a new model, so it lags reality by months or years. Older press coverage, Wikipedia, directories, and anything that was repeated often all weigh heavily here.

### Live retrieval

Most assistants now search the web before answering questions about specific businesses, products, and recent events. The assistant turns the question into one or more searches, reads the top results, and writes an answer grounded in those pages, often with citations. This is called retrieval or grounding, and it means a page that ranks well and answers the question clearly can shape the answer within days of being published.

## Which search indexes feed which assistants
- **Google AI Overviews and AI Mode** are built on Google Search's own index, crawled by Googlebot.
- **Gemini** grounds its answers with Google Search.
- **Microsoft Copilot** uses Bing's index.
- **ChatGPT search** uses OpenAI's own crawler, OAI-SearchBot, alongside third-party search providers.
- **Perplexity** runs its own crawler, PerplexityBot, and its own index.
- **Claude** searches the web through a search provider and fetches pages with Anthropic's crawlers.

The practical lesson: being well indexed in both Google and Bing covers most of the AI landscape. Bing Webmaster Tools and IndexNow, which tells Bing and other engines about changed pages within minutes, matter more than they used to.

## The crawlers, and what each one is for
| Company | Training | Search index | Fetches for a user |
| --- | --- | --- | --- |
| OpenAI | GPTBot | OAI-SearchBot | ChatGPT-User |
| Anthropic | ClaudeBot | Claude-SearchBot | Claude-User |
| Perplexity | (none listed) | PerplexityBot | Perplexity-User |
| Google | Google-Extended (a robots.txt token) | Googlebot | Google's user-triggered fetchers |

You can allow or block each in robots.txt. Blocking a training crawler keeps your future pages out of future models; blocking a search crawler keeps you out of that assistant's live answers. Google-Extended controls whether your content is used for Gemini, and it doesn't affect Google Search or AI Overviews, which follow Googlebot. Check your CDN, too: Cloudflare began blocking many AI crawlers by default on new setups in 2025, which can keep a business out of AI answers without anyone deciding that on purpose.

## What assistants favor when they write an answer
- **Direct answers.** Pages that state the answer plainly near the top, in a sentence that still makes sense when quoted on its own.
- **Self-contained context.** Definitions, dates, locations, and names on the page itself, so the assistant doesn't have to guess.
- **Consistency.** The same facts about you on your site, your profiles, directories, and press. Conflicting facts produce hedged or wrong answers.
- **Third-party confirmation.** Reviews, news coverage, industry directories, and community discussions. Assistants treat what others say about you as evidence.
- **Freshness.** Visible "updated" dates and current information, especially for anything that changes.
- **Readable HTML.** Most AI crawlers fetch the HTML without running JavaScript, so content that appears only after scripts run is invisible to them. The [JavaScript SEO guide](https://gerriscorp.com/guides/javascript-seo/) shows how to check.

## What you can do this quarter
1. Ask the major assistants the ten questions your buyers ask, and write down the answers and the sources cited.
2. Fix your own pages first: one clear page per service or product, with the facts stated plainly and an FAQ section with real answers.
3. Make your facts consistent everywhere: name, description, location, founding date, leadership, services, prices where public.
4. Add schema.org structured data for your organization, people, products, and services, matching the visible page.
5. Check robots.txt and your CDN's bot settings for the AI crawlers you want.
6. Submit your sitemap to Google Search Console and Bing Webmaster Tools, and turn on IndexNow.
7. Consider an [llms.txt](https://gerriscorp.com/guides/glossary/#llms-txt) file. It's a proposed convention from 2024 that gives language models a plain summary of your site; adoption by AI companies is still uncertain, and it costs almost nothing.
8. Repeat the same questions in a month and compare.

## Measuring it

AI answers vary with phrasing, location, account history, and time, so a single test proves little. Use a fixed set of prompts, run them on a schedule, and record the answers and citations. Add referral traffic from chatgpt.com, perplexity.ai, gemini.google.com, and copilot.microsoft.com in analytics, and watch which pages they land on.

I do this work as [AI search visibility](https://gerriscorp.com/services/ai-search/), starting with an AI search readiness audit.

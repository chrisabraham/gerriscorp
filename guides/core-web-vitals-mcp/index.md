> How to diagnose LCP, INP, and CLS with an AI coding assistant through MCP: Chrome DevTools traces, real user CrUX data, and Screaming Frog at scale.
>
> Source: https://gerriscorp.com/guides/core-web-vitals-mcp/ · Updated 2026-10-13 · By Chris Abraham, Gerris Corp

# Diagnosing Core Web Vitals with MCP and an AI coding assistant

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 13, 2026

Fixing a slow page used to mean running a test, reading a waterfall, opening the code, and going back and forth between the three. With the Model Context Protocol, an AI coding assistant such as Claude Code can drive Chrome, record a performance trace, read the result, and open the component responsible, all in one session. Here is how I set it up, what each piece does, and where a person still has to check the work.

## The three numbers you're chasing

Core Web Vitals measure loading, responsiveness, and visual stability. Google's web.dev thresholds for a good experience are a Largest Contentful Paint within 2.5 seconds, an Interaction to Next Paint of 200 milliseconds or less, and a Cumulative Layout Shift of 0.1 or less, measured at the 75th percentile of page loads on mobile and desktop separately. A page passes when it meets all three. The [Core Web Vitals guide](https://gerriscorp.com/guides/core-web-vitals/) explains each metric and its usual causes; this guide is about the tooling.

## What MCP adds

MCP is a standard way for an AI assistant to call outside tools. An MCP server wraps a tool, such as a browser or a crawler, and the assistant can ask it to do things and read back the results. In Claude Code, you register a server with `claude mcp add`, and its tools become available in the session. The assistant still needs you to tell it what to look at and to check its conclusions, but the tedious loop of test, read, and search the code collapses into one conversation.

## Chrome DevTools MCP: lab traces on demand

Google's Chrome DevTools MCP server gives an assistant control of a real Chrome browser and the DevTools performance panel. Its documented setup for Claude Code is a single command:

```
claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```

The tools that matter for Core Web Vitals:
- **performance_start_trace** and **performance_stop_trace** record a trace, optionally reloading the page and bypassing the cache to measure a cold load. The tool is described as finding frontend performance issues and Core Web Vitals.
- **performance_analyze_insight** opens a specific finding from the trace, such as the LCP breakdown, which shows where the time before the largest element appeared actually went.
- **emulate** throttles the CPU and network, with presets from Slow 3G to Fast 4G, and sets a mobile viewport, so a fast desktop doesn't hide a slow phone experience.
- **list_console_messages** and **list_network_requests** show errors and the heaviest resources.
- **lighthouse_audit** runs Lighthouse for accessibility, SEO, and best practices. Its documentation notes that it excludes performance, which is what the trace tools are for.

Two settings are worth knowing. The performance tools can send the traced URL to Google's CrUX API to show real user data beside the lab result; the `--no-performance-crux` flag turns that off. And Google collects usage statistics from the server by default, which `--no-usage-statistics` disables.

## Real user data: CrUX, and a change to PageSpeed Insights

A lab trace shows one load on one machine. Search uses field data from real Chrome users, collected in the Chrome UX Report. The CrUX API returns that data for a page or a whole origin, with a Google Cloud API key set up for it.

One change to plan around: Google's PageSpeed Insights API documentation says Google plans to stop including CrUX real user data in that API, and recommends the CrUX API or the CrUX History API instead. Any script or dashboard that pulls field data from PageSpeed Insights should move now.

## Screaming Frog: every template, not one page

Traces are for depth. For breadth, Screaming Frog's PageSpeed Insights integration, under Configuration > API Access > PageSpeed Insights, pulls Lighthouse metrics and opportunities for every URL during a crawl. It can also run Lighthouse locally, which avoids the API's daily query limit but has no CrUX data.

Screaming Frog version 24 also runs as an MCP server, so an assistant can start crawls and read reports and bulk exports directly. It's a paid licence feature and needs database storage mode. Optional tools let the assistant run Node.js scripts, and they're off until you enable them in the MCP server settings.

The combination is where the time savings live: crawl every URL, group the slow ones by template, trace one representative page per template, and fix the template once.

## A working session, step by step
1. **Start from field data.** Check the Core Web Vitals report in Search Console or the CrUX API to see which metric fails and on which group of pages.
2. **Pick representative URLs,** one per failing template.
3. **Trace each on emulated mobile.** Ask the assistant to throttle to a mid-range phone and record a cold load.
4. **Read the insight, then the code.** For a slow LCP, the breakdown shows whether the time goes to the server, to fetching the hero image, or to rendering. With the repository open, the assistant can find the component that loads the image and propose a change, such as preloading it or removing its lazy loading.
5. **Test on a preview.** Trace the same page on the branch's preview deployment and compare.
6. **Confirm in the field.** CrUX data is a rolling 28 day window, so real user numbers improve gradually after release.

## Where to keep a hand on the wheel
- **Lab is not field.** A trace on a developer's machine, even throttled, is one sample. Treat it as a diagnosis and judge the outcome by field data.
- **Check every proposed fix.** An assistant can suggest deferring a script that the page needs, or a preload that competes with the real LCP image. Measure before and after.
- **Mind what the browser can see.** The DevTools server's own documentation warns that it exposes the browser's content to the assistant. Use a separate browser profile, never one signed in to anything sensitive.
- **INP needs interaction.** A page load trace says little about responsiveness. Have the assistant click, type, and open menus during a trace, and compare with field INP.

This is how I run speed work on code based sites as part of [site speed and Core Web Vitals](https://gerriscorp.com/services/site-speed/) and [SEO engineering](https://gerriscorp.com/services/seo-engineering/). For the habits that keep an AI assistant safe in a client codebase, see [using AI coding assistants on a business website](https://gerriscorp.com/guides/ai-coding-assistants/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Chrome DevTools MCP (README)](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [Chrome DevTools MCP tool reference](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md)
- [Anthropic: Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)
- [web.dev: Web Vitals](https://web.dev/articles/vitals)
- [Google: PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/get-started)
- [Chrome for Developers: CrUX API](https://developer.chrome.com/docs/crux/api)
- [Screaming Frog: SEO Spider configuration (MCP server and PageSpeed Insights)](https://www.screamingfrog.co.uk/seo-spider/user-guide/configuration/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

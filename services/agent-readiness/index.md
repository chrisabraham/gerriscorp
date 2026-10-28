> Chris Abraham runs ChatGPT, Gemini, and other AI agents through your key tasks, then fixes the firewall rules, forms, and markup that stop them before the sale.
>
> Source: https://gerriscorp.com/services/agent-readiness/ · Updated 2026-10-28 · By Chris Abraham, Gerris Corp

# Agent readiness review for your website

Your customers have started sending software to do their errands. An AI agent will open your site, read it, fill in your form, and try to finish the job. I find out whether it can, where it stops, and what to change so it gets through.

## Who this is for

This review suits companies whose website does something, rather than only describing something: a quote request, a booking, a store, a portal, a demo request, a dealer locator. If a customer could plausibly ask an assistant to do that task for them, the task needs testing with an agent. It also suits marketing and IT teams who were told to block bots and now suspect they blocked customers along with them.

## What I test

I choose your three to five most valuable tasks with you, then run each one with the agents your customers actually use, including the ChatGPT agent and Google's agents, and with a screen reader and a text browser as controls. For every run I record whether the agent reached the page, whether it understood the page, where it hesitated, and where it stopped. I keep the transcripts, screenshots, and server log lines together so each finding can be checked by your team rather than taken on trust.

## What I usually find

The most common failure is the firewall. Bot protection, challenge pages, CAPTCHA on routine forms, and blocks on data center addresses turn away signed agents without leaving a trace anyone reads. The second is the page itself: unlabeled fields, icon buttons without names, prices and stock loaded by script after the page renders, and steps that only respond to a mouse. The third is content risk. User reviews, comments, and uploads can carry text aimed at the agent rather than the reader, and some sites have planted that kind of text themselves on a vendor's advice.

## What I fix, or specify for your developers

For Cloudflare, Akamai, and similar platforms I write the allow rules for verified agents, using the signature checks the AI companies publish, and I confirm your proxies pass the signature headers through. On the page I fix labels, button names, server rendering of the facts an agent needs, and confirmation steps for anything that spends money or changes an account. Where your developers own the code, I deliver tickets with acceptance tests, in the same format I describe in my guide on [turning audits into developer tickets](https://gerriscorp.com/guides/seo-developer-tickets/). Then I rerun every agent against the fixed version and report the difference.

## What you receive

You get a written report with each task, each agent, and the result, the evidence behind every finding, the firewall rules and code changes made or specified, and a short policy note on what agents may and may not do on your site. I also leave you a repeatable test list, so the next redesign or security change can be checked against the same tasks before it ships.

## How this connects to the rest of my work

Agent readiness overlaps with [accessibility remediation](https://gerriscorp.com/services/accessibility/), because a page a screen reader can operate is usually a page an agent can operate. It also overlaps with [crawler visibility](https://gerriscorp.com/services/crawler-visibility/), which deals with content that search and AI crawlers never see. The difference is the verb. Crawlers read. Agents act, and acting is where the money is.

## Before an agent readiness review

### Do you need production access?

For testing, I need only what a customer has. For fixes, I need the firewall or CDN dashboard and either repository access or a developer who can apply the changes.

### Will this open my site to scrapers?

No. The rules I write allow agents that prove their identity cryptographically and leave your existing protection in place for everything else.

The background is in my guide on [letting AI agents use your website](https://gerriscorp.com/guides/ai-agents-on-your-website/). To start, [book a 30 minute call](https://calendly.com/chrisabraham/30) and name the task you most want an agent to finish, or hire me through [Upwork](https://www.upwork.com/freelancers/chrisjabraham).

## Start a conversation

Scope and fees are settled in conversation, once I understand the problem. Choose the route that fits how your company works.

[Schedule a call](https://calendly.com/chrisabraham/30) [Work with me through Upwork](https://www.upwork.com/freelancers/chrisjabraham)

Updated October 28, 2026

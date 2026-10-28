> AI agents now browse, fill in forms, and shop for people. How to recognize them, keep your firewall from turning them away, and guard pages from planted text.
>
> Source: https://gerriscorp.com/guides/ai-agents-on-your-website/ · Updated 2026-10-28 · By Chris Abraham, Gerris Corp

# AI agents are visitors now, and most websites are not ready

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 28, 2026

For thirty years the visitors to a website came in two kinds: people, and crawlers that read pages and left. A third kind arrived over the past year. An AI agent opens your pages on someone's behalf, reads them, clicks the buttons, fills in the form, and sometimes tries to buy the thing. Most of the websites I audit treat that visitor as an attack, describe themselves badly to it, or leave text on the page that can steer it somewhere the owner never intended.

## What an agent visit looks like

A person asks ChatGPT, Gemini, Perplexity, or Claude to book a table, compare three suppliers, or find a replacement part and order it. The assistant then drives a real browser. Sometimes that browser runs in the AI company's cloud, sometimes it runs inside the person's own Chrome. Either way it loads your page, reads the text and the form labels, and acts. When it works, you get a customer who never saw your hero image. When it fails, you get nothing, and nobody tells you, because the person simply gets an answer that names a competitor instead.

## How the agents identify themselves

The better behaved agents now sign their requests. OpenAI documents that ChatGPT's cloud browser signs every request with HTTP Message Signatures, the standard published as RFC 9421, in the arrangement Cloudflare calls Web Bot Auth. Each request carries `Signature`, `Signature-Input`, and `Signature-Agent` headers, the agent header reads `"https://chatgpt.com"`, and the public keys sit at a published directory on chatgpt.com so any server can verify them.

Google lists a fetcher called Google-Agent, used by agents hosted on Google's infrastructure to navigate the web and act on a user's request. Its user agent string is an ordinary Chrome string with the token Google-Agent added, its IP ranges are published in a separate file for user triggered agents, and Google says it is experimenting with Web Bot Auth under the identity `https://agent.bot.goog`.

Agents that run inside the person's own browser carry no special label at all. To your server they look like that person, because in every practical sense they are. Plan for both: the signed visitor you can recognize and the unsigned one you cannot.

## Robots.txt is the wrong lever here

Google states that user triggered fetchers generally ignore robots.txt, because a person asked for the page. Robots.txt still governs crawlers that build training sets and search indexes, and that is a separate decision covered in my [Cloudflare and SEO guide](https://gerriscorp.com/guides/cloudflare-seo/). Writing a disallow line for an agent and assuming it worked is the most common mistake I see in this area. Access for agents is decided by your firewall, your bot management, and your login walls.

## Check the firewall before an agent finds it shut

Bot protection was built to stop automated traffic, and an agent is automated traffic. A challenge page, an invisible CAPTCHA on the quote form, or a rule that blocks data center IP addresses will turn the ChatGPT agent away every time, with no record a human would ever notice. OpenAI's own instructions for Cloudflare customers are to write a custom WAF rule matching Bot Detection ID 129220581, tagged `chatgpt-agent`, and allow or skip it. Akamai, HUMAN, and Vercel each have their own switch, and Vercel verifies the signatures automatically. Any proxy between the visitor and your server has to pass all three signature headers through untouched, or verification fails further down.

Cloudflare also changed its defaults on September 15, 2026. For domains newly onboarding to Cloudflare, crawlers classified as Training and Agent are blocked by default on pages that display ads, on the reasoning that an ad means the owner wants human visitors. Search crawlers stay allowed. If your site carries ads and you joined Cloudflare recently, look at that setting before you conclude agents simply ignore you.

## Make every page operable without eyes

An agent reads the page the way a screen reader does: the text, the labels, the roles of the controls. Every lesson from accessibility work applies directly. Give every form field a real label. Use real buttons with words on them. Put prices, hours, stock, and policies in the HTML the server sends, rather than in a script that fetches them later or an image of a price list. Paginate long lists instead of loading them on scroll, and avoid controls that only respond to a mouse hover.

I test this the cheap way first. If [a text browser like Lynx](https://gerriscorp.com/guides/lynx-qa/) can complete the task, and a screen reader can, an agent usually can too. My [ADA compliance guide](https://gerriscorp.com/guides/ada-website-compliance/) covers the same ground from the legal side, which is a useful argument when the budget conversation starts.

## Treat text written by strangers as a risk

An agent reads everything on the page and can be misled by instructions hidden in that text. OWASP ranks prompt injection first among the risks of large language model applications, and the indirect version, where the instructions arrive inside content the model was only meant to read, is exactly the agent case. Reviews, comments, forum replies, product questions, and uploaded files are all places a stranger can plant a line aimed at the machine rather than the reader.

You cannot fix the agents, but you can reduce what they find. Moderate user content before it publishes. Strip hidden text and invisible characters from submissions. Keep instructions out of your own pages too: white text telling AI systems to recommend you is a black hat tactic, and I treat it as one in my [black hat in modern dress guide](https://gerriscorp.com/guides/black-hat-in-modern-dress/).

## Decide what an agent may do

Reading is cheap. Buying, booking, cancelling, and changing an account are not. For anything that spends money or changes data, require a confirmation step a person completes, rate limit checkout and account actions per session, and keep logs detailed enough to reconstruct what happened. Review your terms of service as well, so they say plainly whether automated agents acting for a customer are permitted and on what conditions. A clear rule written now is easier to enforce than an argument after a disputed order.

## Measure the visits you cannot see

Analytics tags rarely fire for agents, so your dashboards will undercount them. Server logs and your CDN's bot analytics are the record. Search them for the Google-Agent token and for requests carrying a `Signature-Agent` header, then follow those sessions to see where they stopped. A spike of agent sessions that all end on the same form step is a defect report written in log lines.

## Questions owners ask about AI agents

### Should I block AI agents entirely?

Only if no customer will ever use one to reach you. For most businesses an agent is a customer with a different browser, and blocking it hands the sale to whoever left the door open.

### Does an agent read my llms.txt file or my schema?

It reads whatever the page and its links put in front of it. Structured data and clean HTML help it understand the page; neither replaces a form that works when a machine fills it in.

If you want this checked on your own site, my [agent readiness review](https://gerriscorp.com/services/agent-readiness/) runs real agents through your key tasks and reports where each one stopped, or you can [book a call](https://calendly.com/chrisabraham/30) and walk me through the problem.

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [OpenAI Help Center: ChatGPT agent allowlisting](https://help.openai.com/en/articles/11845367-chatgpt-works-cloud-browser-allowlisting)
- [Google Crawling Infrastructure: Google-Agent](https://developers.google.com/crawling/docs/crawlers-fetchers/google-agent)
- [Cloudflare Docs: Signed agents](https://developers.cloudflare.com/bots/concepts/bot/signed-agents/)
- [IETF RFC 9421: HTTP Message Signatures](https://www.rfc-editor.org/rfc/rfc9421)
- [OWASP Gen AI Security Project: Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [PPC Land: Cloudflare pay per answer and September 15 defaults](https://ppc.land/cloudflare-stops-charging-ai-per-crawl-and-starts-paying-per-answer/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

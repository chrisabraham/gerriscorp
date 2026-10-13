> Twelve questions that expose AI washing in a vendor pitch, the SEC and FTC cases that define it, and why a technical skeptic belongs on the sales call.
>
> Source: https://gerriscorp.com/guides/ai-vendor-pitch/ · Updated 2026-10-13 · By Chris Abraham, Gerris Corp

# How to vet an AI vendor's pitch before you sign anything

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 13, 2026

Every software sales deck now has AI on the first slide. Some of those products are remarkable. Some are a thin layer over a model you could rent yourself for a few dollars a month. A few have no meaningful AI at all. Regulators have a name for the last group, AI washing, and they've started bringing cases. These are the questions I ask when a client brings me onto a vendor call, and the answers that tell me which kind of product I'm looking at.

## What AI washing looks like on the record

On March 18, 2024, the SEC announced its first AI washing cases, settled charges against two investment advisers, Delphia and Global Predictions, for claiming AI capabilities they didn't have. The penalties came to $400,000 combined. The SEC said Delphia had claimed to use client data in AI driven investing when it wasn't using that data in its process.

On September 25, 2024, the FTC announced Operation AI Comply, five actions against companies using AI claims to deceive customers. One was DoNotPay, marketed as "the world's first robot lawyer"; the FTC said the company never tested whether its output matched a lawyer's, and DoNotPay agreed to pay $193,000. FTC Chair Lina Khan put the principle in one line: "there is no AI exemption from the laws on the books."

Those are the extreme cases. The everyday version is a vendor whose product works fine but whose pitch credits "proprietary AI" for what is a well written prompt and a spreadsheet.

## Twelve questions for the sales call
1. **Which model does this run on, and who hosts it?** A clear answer ("a hosted model from one of the big labs, called through their API") is fine. Evasion is a warning.
2. **What does your product add on top of that model?** Good answers name real work: your integrations, a curated dataset, a review workflow, evaluation tests.
3. **Can you run it on my data, live, right now?** A recorded demo shows the best case. A live run on a sample of your own material shows the typical one.
4. **How often is it wrong, and how do you measure that?** Every AI system makes mistakes. Vendors with mature products have an error rate and a test set. Vendors without one say "it's very accurate."
5. **What happens when it's wrong?** Who notices, who fixes it, and who carries the cost: you, the vendor, or your customer.
6. **Where does my data go?** Which servers, which subprocessors, how long it's kept, and whether it trains anyone's model. Get the answer in the contract.
7. **Who owns the output?** Content, code, analysis, and anything the system learns from your use.
8. **What does it cost at ten times my volume?** Per seat, per task, and per token pricing behave very differently once usage grows.
9. **How many humans are behind it?** Some "automated" services quietly route work to people. That can be a fine product; it should be an honest one.
10. **How do I leave?** Export formats, notice periods, and what happens to your data afterward.
11. **Who else uses it for exactly this?** Ask for a reference customer with your use case, and call them.
12. **What would make you tell me not to buy this?** Honest vendors know where their product fits badly, and they'll tell you.

## Read the answers as evidence

I score each answer three ways: specific or vague, testable or unverifiable, and consistent with what the contract says. One vague answer is normal; sales teams don't know everything and should offer to follow up. A pattern of vague answers on accuracy, data, and cost is the signal. The product might still be good, and the vendor still hasn't shown it.

For a structured view of risk once you're serious, NIST's AI Risk Management Framework gives you vocabulary for governance, testing, and monitoring that your legal and security teams will recognize.

## Run a paid pilot with a scorecard

Before a full contract, run a short pilot on real work with success measures you set: accuracy on a sample you've already checked by hand, time saved per task, and the number of outputs a person had to correct. Write the measures down before the pilot starts, so nobody redefines success at the end. My guide to [fact checking confident AI answers](https://gerriscorp.com/guides/fact-check-ai-seo/) describes the claim by claim habit I use to grade output.

## Bring a technical skeptic to the call

Sales calls are designed for the buyer who doesn't know which questions to ask. Bringing one person who does changes the whole conversation. I sit in on vendor calls for clients as exactly that person: I've built on these models myself, so I can tell a real integration from a wrapper in a few questions, and I'm comfortable asking the awkward ones politely. Afterward you get a short written recommendation: what's real, what's missing, and what to ask for in the contract. That work falls under my [advisory and second opinions](https://gerriscorp.com/services/advisory/), and if the answer is to build something yourself, see [AI agents and automation](https://gerriscorp.com/services/ai-automation/).

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [SEC: SEC charges two investment advisers with making false and misleading statements about their use of artificial intelligence (March 18, 2024)](https://www.sec.gov/newsroom/press-releases/2024-36)
- [FTC: FTC announces crackdown on deceptive AI claims and schemes (September 25, 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes)
- [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

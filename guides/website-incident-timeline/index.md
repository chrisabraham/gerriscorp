> Reconstruct a website failure with dated observations, release records, cache checks, and competing explanations before choosing the next repair to make.
>
> Source: https://gerriscorp.com/guides/website-incident-timeline/ · Updated 2026-10-24 · By Chris Abraham, Gerris Corp

# Build a website incident timeline before changing code

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 24, 2026

The website lost traffic on Tuesday. Someone remembers a release on Monday. A vendor changed a setting last week. Those facts belong in the same investigation, but their proximity does not establish a cause.

Before changing code, I want a timeline that separates what happened from when someone noticed it. This is a practical way to organize technical forensics: collect dated observations, preserve the evidence, and decide which explanation deserves the next test.

## Define the incident in observable terms

Start with the actual symptom. “Organic clicks to product pages declined” describes a different incident from “product pages return server errors” or “quote requests stopped reaching the sales inbox.” Those events can occur together, but each needs its own evidence.

Record the first confirmed observation and the last confirmed normal state. If a customer reported a failure on Tuesday afternoon, the failure could have begun earlier. Write “first reported Tuesday at 14:10” rather than “began Tuesday at 14:10” unless monitoring establishes the start.

Choose representative URLs and customer actions. Keep a working example alongside the failing examples when possible. A category that still works can help distinguish a shared infrastructure problem from a product template defect.

## Use one time convention

Choose a time zone for the working timeline and write it at the top. Preserve each source timestamp and its original zone in a separate field. A server event recorded in UTC and a release discussed in local time can appear in the wrong order if someone copies the clock values without converting them.

Do not invent precision. If the only record says “Monday morning,” retain that uncertainty. A date without a time cannot establish whether an event preceded an outage by five minutes or followed it by three hours.

For reports summarized by day, retain that reporting granularity. Do not place a daily traffic total beside a second level server event and treat them as measurements with equivalent precision.

## Gather records from different layers

Collect the deployment history, content publication records, DNS and proxy changes, relevant application logs, monitoring alerts, and dated support messages. Ask vendors for their change records when those records are needed to evaluate a theory. A lack of access is an investigation gap, not evidence that nothing changed.

Use Search Console for the search observations it actually supplies. Google's [Search Console introduction](https://developers.google.com/search/docs/monitor-debug/search-console-start) explains its crawl, indexing, and performance reports. Those reports can inform an incident timeline, but they are not a second by second deployment monitor.

Capture the response status, important headers, and visible behavior for selected production URLs. Where caching is involved, record what the public visitor received and what environment was tested. A correct preview page does not establish a correct public response.

Keep the evidence in access controlled storage. The public incident summary should not include customer submissions, tokens, credentials, or identifying log details. Link to a restricted artifact by a descriptive name rather than copying sensitive contents into a shared ticket.

## Maintain a simple evidence table

The following is an invented example. It illustrates the structure and makes no claim about a client incident.
| Time in UTC | Recorded event | What it establishes |
| --- | --- | --- |
| Monday 09:00 | Product template release completed | A release ran; public output was not recorded |
| Monday 09:20 | Monitor saved a successful category response | That category URL responded successfully then |
| Tuesday 14:10 | Customer reported missing product specifications | The symptom was reported by this time |
| Tuesday 14:40 | Saved product response lacks specification text | The selected public response lacked the text |
| Tuesday 15:05 | Preview includes the specification text | Preview and public behavior differ |

The timeline suggests a useful next question: what differs between preview and production? It does not prove the release removed the specifications. The public response may reflect a different build, stale cache, unavailable data, or a configuration difference.

## Write competing explanations and discriminating tests

List a small number of plausible causes. Beside each one, write the observation that would strengthen or weaken it. “The production release contains different code” can be checked against the deployed revision. “A cache holds old output” requires evidence about the actual response and cache behavior.

Choose a test that separates explanations. Rebuilding everything and clearing every cache may restore service, but it can also remove the evidence needed to understand the failure. When customers are actively blocked, restoration may take priority. Record that choice and capture what is practical before taking action.

Separate confirmed causes from contributing conditions. An old deployment process may make recovery slow without causing the original defect. Both deserve attention, but the prevention work differs.

## Record the intervention and verify the result

Add each repair attempt to the same timeline: the owner, exact change, environment, release identifier, and observed outcome. If two changes ship together, acknowledge that the result may not isolate which one mattered.

Repeat the original failing action on production and check the working comparison example. For a content visibility incident, retain before and after response samples. For an inquiry failure, confirm receipt rather than relying on a success message in the browser.

End the incident record with what is established, what remains uncertain, and the next monitoring check. A repaired product template and a later traffic recovery are separate findings. Do not claim the second from evidence of the first.

This method supports [website rescue and takeover work](https://gerriscorp.com/services/rescue/), [technical SEO diagnosis](https://gerriscorp.com/services/technical-seo/), and [technical direction](https://gerriscorp.com/services/technical-lead/). For a traffic specific investigation, use the [traffic drop diagnostic guide](https://gerriscorp.com/guides/traffic-drop/) alongside the timeline. The purpose is to make the next decision better supported than the first guess.

Prepared with OpenAI Codex at Chris Abraham's request. The timeline is hypothetical and contains no client records.

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Google Search Console introduction](https://developers.google.com/search/docs/monitor-debug/search-console-start)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

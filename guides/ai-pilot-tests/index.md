> Turn an AI demonstration into a testable pilot: real examples, expected results, permissions, retries, failure records, and a decision your team can explain.
>
> Source: https://gerriscorp.com/guides/ai-pilot-tests/ · Updated 2026-10-15 · By Chris Abraham, Gerris Corp

# Test an AI pilot with the work it is supposed to do

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 15, 2026

A polished demonstration answers the question the demonstrator prepared. Your working day contains the requests they did not prepare: a missing date, two customers with the same name, a task submitted twice, or a report that sounds finished when the underlying action failed. A pilot needs examples of those situations before anyone can decide whether to rely on it.

## Write one plain job description

Begin with a sentence that has an input and an observable result. For example: given an approved meeting note, produce draft tasks with the correct owner and due date. That is narrow enough to test. A promise to make the team more productive is useful as an ambition, but it leaves the test writer guessing which behavior is required.

Record the tool version, its connected services, and the account permissions used in the trial. Give the pilot an owner who can decide whether an output is acceptable. The person writing the test should not have to infer the answer from whatever the assistant happened to produce.

## Collect ordinary examples before clever ones

Ask the future users for several requests they would really make. Preserve the shorthand, unfinished sentences, and naming conventions that appear in daily work. Add a small number of unusual cases deliberately, rather than building the whole collection from puzzles. The ordinary examples show whether the workflow is useful; the exceptions show where it needs help.

I learned this with my own terminal assistant. A phrase I had used repeatedly was being silently ignored. Turning the exact request into a test made the problem visible and kept the correction from depending on a conversation I would later forget. The build history is described in the [assistant case study](https://gerriscorp.com/case-studies/built-with-claude-code/).

## Define the result before running the case

For a draft task, the owner must refer to the right person, an absent date must remain absent or trigger a question, and no live task should be created if the request only asks for a draft. For a summary, separate facts that must be present from wording that can vary. This avoids the easy mistake of approving a convincing answer because it resembles the last convincing answer.

Use the [AI pilot test case worksheet](https://gerriscorp.com/downloads/ai-pilot-test-cases.csv) as a starting point. Its rows describe invented examples. Fill in the expected behavior, the observed result, and the evidence. Keep real client data in the approved project workspace rather than in a public example file.

## Include a few failures on purpose
| Case | Question to settle |
| --- | --- |
| Missing information | Does the assistant ask, preserve the gap, or invent a value? |
| Ambiguous identity | Can it stop before choosing the wrong customer? |
| Duplicate request | Does a retry repeat an action already completed? |
| Unavailable service | Is failure reported without claiming the action succeeded? |
| Instructions inside source material | Does quoted content stay separate from the user's request? |
| Unapproved action | Does the workflow wait at the agreed decision point? |

Exercise service failures in an isolated trial or with a simulated dependency. Do not create a live outage to see how the pilot reacts. The aim is a reproducible example, not a surprise for the people depending on the service.

## Test the permission boundary as behavior

OWASP's discussion of excessive agency recommends limiting tool capabilities and permissions, with human approval for consequential actions. Translate that principle into a case you can observe. If a workflow is allowed to prepare a message but requires approval to send it, inspect both the draft and the sending record. The assistant saying that it waited is only one part of the evidence.

A written instruction helps explain the rules. An account that lacks unnecessary permissions helps enforce them. Review both when the pilot connects to another service. A harmless drafting exercise can become a different system when somebody adds a connection that can publish, delete, or spend.

## Save evidence that outlives the session

Keep the inputs, outputs, timestamps, relevant service records, and the acceptance decision together. When a test runs in GitHub Actions, downloadable workflow artifacts can hold its reports. Set retention deliberately and store sensitive evidence only where the team has approved it. A screenshot of the final answer rarely explains a retry, a hidden error, or a partial action.

My [outreach tracker audit](https://gerriscorp.com/case-studies/data-cleanup/) is a useful reminder here. The tracker described activity, but checking the actual sending records changed what could honestly be reported. A pilot should make that comparison easier, not bury the trail under a confident paragraph.

## Score separate questions separately

Record correctness, completeness, unauthorized actions, and manual correction effort independently. A mostly useful summary and a message sent to the wrong person should not average into an acceptable score. Decide in advance which failures stop the pilot and which can be tolerated with a documented workaround.

Repeat cases where results vary and retain the individual outcomes. If only one run was observed, say so. A small collection can reveal a repeatable failure without proving a general success rate. The report should state what was tested and the limits of that evidence.

## Keep the collection when the pilot ends

Use the same examples when a prompt changes, a new model is proposed, or a connector gains another permission. Add real failures as the team encounters them. Remove obsolete cases through an explicit decision so the collection continues to describe the job people are actually doing.

I can help define and run that review through [AI workflow testing](https://gerriscorp.com/services/ai-workflow-testing/). For the earlier buying decision, the [AI vendor questions](https://gerriscorp.com/guides/ai-vendor-pitch/) help establish what the supplier should demonstrate before a pilot begins.

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [OWASP Gen AI Security Project: Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
- [GitHub Docs: Downloading workflow artifacts](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

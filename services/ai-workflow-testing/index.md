> Test an AI pilot against real tasks before expanding it. Chris Abraham checks outputs, permissions, failure handling, and evidence with a repeatable test set.
>
> Source: https://gerriscorp.com/services/ai-workflow-testing/ · Updated 2026-10-15 · By Chris Abraham, Gerris Corp

# AI workflow testing and acceptance reviews

The demonstration worked. Now somebody needs to find out what happens with an incomplete request, a duplicate record, a failed connection, or an instruction hidden inside a document. I help turn an AI pilot into something your team can judge against written requirements.

## Start with one job

The useful unit is a workflow: turn these meeting notes into draft tasks, reconcile these two exports, or prepare this briefing from these sources. I define the inputs, the expected output, the person who accepts it, and the actions the system may take. That makes the review concrete. The question is whether this tool can do your job within agreed limits, with evidence somebody else can inspect.

## A set of examples your team recognizes

I work with representative examples from the people who will actually use the tool. A good test collection includes ordinary requests, shorthand, missing information, conflicting instructions, repeated submissions, and the cases that have already caused trouble. Sensitive material can be replaced with controlled examples that preserve the behavior being tested. Each case records what a satisfactory result would look like before the tool runs.

## What I check
- **Output quality:** whether names, dates, totals, sources, and record identities match the input.
- **Action boundaries:** whether a draft stays a draft and an action requiring approval waits for it.
- **Failure behavior:** what happens when a service is unavailable, an answer is uncertain, or an input cannot be parsed.
- **Repeated work:** whether retrying an interrupted task creates duplicate records or messages.
- **Traceability:** whether the team can distinguish proposed work, completed work, and work that never happened.

## Experience behind the review

My own command line assistant grew through real use: misread requests became explicit examples in its test suite. The [coding assistant case study](https://gerriscorp.com/case-studies/built-with-claude-code/) describes that process and the 140 end-to-end tests in the original build. Separately, I checked an AI-generated outreach tracker against actual sending records and found activity the evidence did not support. That work is in the [data cleanup and AI audit case study](https://gerriscorp.com/case-studies/data-cleanup/). Both experiences inform a simple habit: compare the tool's report with what actually happened.

## Platform agnostic by design

I use OpenAI Codex and Claude Code as my primary coding assistants, alongside GitHub Copilot, Gemini, Grok, and occasional Perplexity use. For this work, the test cases and expected behavior belong to your project. The same collection can help compare a proposed replacement with the version already in use, provided the inputs and acceptance rules stay consistent.

## The handover

You receive the agreed test collection, observed results, evidence of failures, and a prioritized list of changes or unresolved questions. The recommendation can be to proceed within a limited scope, revise the pilot, or gather evidence that was missing. I also identify which checks can become automated regression tests and which still need a person to read the output. A passing result applies to the tested version and conditions.

## Before a pilot review

### Can you review a tool someone else supplied?

Yes, with enough access to exercise the workflow and inspect its records. The scope distinguishes behavior I can observe from implementation details that need the supplier's cooperation.

### Where should a first engagement start?

With a named workflow, a small set of representative tasks, and a paid diagnostic. Implementation or a wider rollout follows only after the findings and next scope are agreed.

The [AI pilot testing guide](https://gerriscorp.com/guides/ai-pilot-tests/) includes a worksheet you can use yourself. For a review, [send me the workflow and what a good result should accomplish](https://gerriscorp.com/contact/). If you need the tool built as well, see [AI agents and automation](https://gerriscorp.com/services/ai-automation/).

Updated October 15, 2026

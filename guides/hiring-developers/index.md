> A founder's method for hiring web developers: own the accounts first, interview for judgment, pay for a trial task, review pull requests, and manage AI use.
>
> Source: https://gerriscorp.com/guides/hiring-developers/ · Updated 2026-10-13 · By Chris Abraham, Gerris Corp

# How to hire and manage developers when you can't read code yourself

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 13, 2026

Founders and marketing leads hire developers all the time without being able to judge the work. They pick the most confident interview, hope for the best, and find out six months later what they bought. There's a better way, and none of it requires learning to program. It requires owning the right accounts, asking questions that reveal judgment, and putting every change somewhere you can see it.

## Own the accounts before you hire anyone

Create a GitHub organization in your company's name, and keep the domain registrar, hosting, DNS, email, analytics, and Search Console in accounts your business controls. GitHub's organizations exist for exactly this: shared ownership with per person permissions. Developers get invited in and can be removed cleanly. The most expensive situation I see in rescue work is a business whose site lives in a former contractor's personal account.

## Write the problem down

A one page brief beats any job title. What the site does, what's broken or missing, what platform it runs on, what "done" would look like, and the deadline that actually matters. The brief attracts the right people, and it becomes the yardstick for everything that follows.

## Interview for judgment

You can't grade code in an interview, and you don't need to. You can grade how someone thinks. Ask:
- **"Walk me through something you built that's live now."** Open it together. Strong candidates explain choices and tradeoffs; weak ones list technologies.
- **"Tell me about something that broke in production."** Everyone experienced has a story. Listen for how they found the cause and what they changed so it wouldn't repeat.
- **"What would you need from me in week one?"** Good developers ask for access, the brief, and a decision maker. People who need nothing are planning to guess.
- **"How do you use AI coding tools, and how do you check what they write?"** More on this below; the answer tells you a lot.
- **"What part of this brief would you push back on?"** Someone who agrees with everything will also agree with every bad idea later.

## Pay for a small trial task

Pick a real, contained piece of work: a page template, a bug, a performance fix. Write the acceptance criteria in plain English, pay for a few hours, and ask for the work as a pull request in your repository. You learn how they communicate, whether they meet the brief, and whether their work is readable to the next person. They learn whether they want the job. Either side can stop cleanly.

## See every change through pull requests

A pull request is a proposed change, shown line by line, with a description and a place for comments, and nothing reaches the live site until someone approves it. Require one for every change, with a sentence in plain English explaining what and why. You won't read the code, but you'll read the descriptions, see the pace of work, and have a complete history if a developer leaves. If you have one technical person you trust, give them reviewer rights.

## Manage the AI in the room

Nearly every developer now works with AI assistants. In Stack Overflow's 2025 Developer Survey, 84 percent of respondents said they use or plan to use AI tools, yet more distrusted the accuracy of those tools (46 percent) than trusted it (33 percent). The most common frustration, cited by 66 percent, was AI solutions that are "almost right, but not quite."

That gap is your hiring signal. The developer you want uses AI for speed and checks everything it writes: runs it, tests it, and can explain any line in their pull request. The developer to avoid pastes output they can't explain. Ask candidates to walk you through a recent change and why each part is there. If they can't, nobody can.

## Getting the best from junior developers

Junior developers are often quick, eager, and very good with new tools. They need what everyone needs, in larger doses: small, clearly written tickets, acceptance criteria they can test themselves, a reviewer who explains the "why" behind each requested change, and a running decision log so they don't relitigate settled questions. Paired with an experienced reviewer, a junior developer becomes productive fast. Left alone with a vague brief and an AI assistant, they produce confident code that someone will have to rewrite.

## Red flags
- Work happens on their server or in their personal account.
- Changes go live with no record of what changed.
- Status updates are always "almost done."
- Every problem belongs to the hosting company, the plugin, or the previous developer.
- Requests for passwords sent by text message instead of invitations to your accounts.

## Where I fit

I've spent decades on both sides of this table: writing Perl and PHP myself, then specifying, reviewing, and directing developers' work for clients, and now directing AI coding assistants the way a lead directs a team. I sit in on developer interviews as the technical interviewer, write the trial task and its acceptance criteria, review the pull requests, and mentor junior developers through their first months. When you need someone to own the whole picture part time, that's my [fractional technical lead](https://gerriscorp.com/services/technical-lead/) work; for specs and review alone, see [developer specs and QA](https://gerriscorp.com/services/developers/). My guide to [giving an outside expert repository access](https://gerriscorp.com/guides/repository-access/) covers the permissions side.

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [Stack Overflow: 2025 Developer Survey, AI](https://survey.stackoverflow.co/2025/ai)
- [GitHub Docs: About organizations](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations)
- [GitHub Docs: About pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

> Chris Abraham sets up a private Git repository of plain Markdown that Claude, ChatGPT, Codex, and other assistants all read before acting and update after.
>
> Source: https://gerriscorp.com/services/shared-ai-memory/ · Updated 2026-10-24 · By Chris Abraham, Gerris Corp

# One shared memory for every AI assistant your team uses

Your team probably uses several AI assistants already: Claude in one window, ChatGPT in another, Codex or Claude Code in a terminal, maybe an agent running on a server. Each one forgets everything between sessions, and none of them knows what the others did yesterday. I give them one memory they all share, kept as plain Markdown files in a private Git repository your business owns.

## The problem it solves

Every assistant starts cold. Someone pastes the client background into ChatGPT on Monday, explains the same project to Claude on Tuesday, and on Wednesday an agent drafts an email with Friday's deadline because nobody told it the date moved. The knowledge exists, scattered across chat histories that no other tool can read. The cost shows up as repeated briefings, contradictory drafts, and mistakes that a colleague with the same notes would never make.

## How it works

The memory is a folder of Markdown files under version control. Every client, prospect, partner, or vendor gets exactly one profile. Every project that already lives in your project management tool gets a short digest that links back to it. A single rules file at the top of the repository tells any assistant arriving for the first time what to read, where things go, and what it must never do.

Every assistant follows the same loop: read the profile before acting on that person or project, do the work, then write back what changed, with its own name on the commit. Because it's Git, every change has an author, a date, and a reason, so when an assistant gets something wrong you can see which one it was and roll it back in seconds. Anything that can read a file or clone a repository can take part. There is no vendor, no database, and no API key to rotate.

## What I set up
- **The private repository,** in your company's GitHub organization, with access granted per assistant and per person.
- **The rules file,** written for your business: your people, your tools, your standing decisions, and the lines no assistant crosses.
- **Profiles and project digests** for your active relationships, populated from the sources your assistants can reach, then checked by a person before anyone relies on them.
- **Standing instructions** for each assistant, so every one of them keeps the memory current without being reminded.
- **A review routine** that catches stale files, duplicate profiles, and anything that looks like a credential before it settles in.

## What stays out

Passwords, API keys, and account numbers never go in the repository; they belong in a password manager. The memory holds what a well briefed colleague would know: who someone is, what was agreed, where the project stands, and what was decided. Your project management tool stays the record of the work itself. The shared memory is the part every assistant needs before it touches that work.

## Why I can build this

I run my own business this way. My client records live in a private repository that Claude, Claude Code, ChatGPT, Codex, and my personal agent all read and update every day, and each of them has made mistakes in it that became a written rule. I stripped out everything personal and published the result as [oversoul, a free template on GitHub](https://github.com/chrisabraham/oversoul), licensed for anyone to use, fork, and build on. Clients get the same framework, finished for their team, plus the lessons that only came from running it.

## Common questions

### Which assistants work with it?

Any assistant that can read files or clone a repository. In practice that covers Claude, Claude Code, ChatGPT with a GitHub connection, OpenAI Codex, GitHub Copilot, Gemini, and custom agents running on your own servers.

### Do my staff need to learn Git?

No. The assistants do the reading and writing. People can browse the files on GitHub like any document, and anyone curious can read the plain English explanation of what a commit is.

### How does an engagement start?

With a paid diagnostic: which assistants your team uses, what they keep forgetting, and which records belong in the memory. Then I set it up, populate it, and stay on for a few weeks while your assistants settle into the routine.

**Related:** [AI agents and automation](https://gerriscorp.com/services/ai-automation/) · [Using AI coding assistants safely](https://gerriscorp.com/guides/ai-coding-assistants/) · [Repository access for outside experts](https://gerriscorp.com/guides/repository-access/) · [Data cleanup](https://gerriscorp.com/services/data-cleanup/)

[Give your assistants one memory](https://gerriscorp.com/contact/)

Updated October 24, 2026

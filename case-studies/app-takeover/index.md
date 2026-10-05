> A consumer skincare brand's React application changed hands after an outage. Chris Abraham inventoried code, hosting, and DNS and fixed the server over SSH.
>
> Source: https://gerriscorp.com/case-studies/app-takeover/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Consumer brand: taking over a stalled React application

A consumer skincare brand's React application changed hands after an outage. Project files, credentials, hosting, DNS, and the repository were spread across several people, and the brand needed someone to work out what it actually had.

## My role

Takeover assessment and hands-on operations.

## The assessment

I assessed the handoff the way every rescue should start, with an inventory:
- Which project files were supplied, and whether they matched what was running.
- Where the application was hosted, and who controlled the server.
- Who controlled the domain and DNS.
- Where the repository lived and who had access.
- Which credentials existed, and which were missing.

## Hands-on operations

Then I worked on the DigitalOcean Linux server directly over SSH: reading logs, editing the environment and application configuration files, and managing the Node application with the PM2 process manager. The application was being kept down by a port conflict, which I diagnosed.

## Why it matters

Stalled projects are common: a freelancer moves on, an agency relationship ends, a founder inherits a codebase nobody explained. The first valuable thing is a clear picture of what exists and who controls it. The second is someone who can get onto the server and fix the immediate problem.

Writing the inventory down also protects the business the next time someone leaves, because the knowledge no longer lives in one person's head.

## Status

The assessment and the operational fixes described here were completed; larger rebuild and integration proposals are separate decisions for the brand. See [project rescue and takeovers](https://gerriscorp.com/services/rescue/).

Updated October 5, 2026

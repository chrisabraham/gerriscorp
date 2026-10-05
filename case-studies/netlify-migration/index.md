> Migration oversight for a clinical practice leaving WordPress: redirect decisions for every URL, an AI assisted repository analysis, and a careful disavow.
>
> Source: https://gerriscorp.com/case-studies/netlify-migration/ · Updated 2026-10-05 · By Chris Abraham, Gerris Corp

# Clinical practice: WordPress to Netlify, with search intact

A clinical practice moved its website from WordPress on managed hosting to a new Next.js build on Netlify. The developer built the new site; my job was continuity: making sure search engines and visitors could follow the move, and investigating what went wrong afterward.

## My role

Technical SEO, migration oversight, and investigation, in coordination with the practice and its developer.

## What I did

### Redirect decisions for every URL

I examined the legacy URLs and reconciled the redirect map, deciding for each URL whether it should pass through unchanged, inherit an existing destination, receive a migration redirect, or be treated as intentionally removed. I separated problems the migration caused from older issues the site already had, so neither got blamed on the other.

### Repository analysis with Claude Code

I combined crawls and exports with a read-only, AI-assisted analysis of the Next.js repository. It found thousands of references to images still hosted on the old WordPress site, and the handful of central files responsible, which became a developer-ready plan for moving the media. The analysis changed no code.

### A conservative disavow

I reviewed the backlink profile and prepared a replacement disavow file that removed genuinely toxic domains while keeping legitimate ones, because disavowing good links does real harm.

### After launch

I investigated blurry images from the image CDN, JavaScript and CSS problems, site instability, and analytics behavior with the client and developer, and worked on sequencing, DNS review, and launch verification.

## Reading the data honestly

When engagement fell in a short GA4 window, the easy story was that the blurry images were driving people away. I treated tracking, engagement, and site defects as three separate questions, each needing its own evidence, and didn't let a few days of data stand in for proof.

## Status

Migration oversight and post-launch investigation delivered; further work under discussion. See [website migrations](https://gerriscorp.com/services/migrations/).

Updated October 5, 2026

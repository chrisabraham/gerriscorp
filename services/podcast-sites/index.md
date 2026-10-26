> I build a podcast a website it owns: every episode on its own page with a transcript, generated from the RSS feed, hosted free, and refreshed every morning.
>
> Source: https://gerriscorp.com/services/podcast-sites/ · Updated 2026-10-15 · By Chris Abraham, Gerris Corp

# Podcast websites, built and run for you

Spotify, Apple, and YouTube own the pages your show appears on. I give the show a home it owns: a website on your domain, generated from your RSS feed, with a real page for every episode and a daily job that keeps it current without anyone touching it.

## Why a show needs one

Search engines and AI assistants read text. A feed full of audio gives them almost nothing to work with, and the episode pages the platforms generate are thin and identical. A page per episode, carrying the full transcript, turns every hour you've recorded into something a person can find by searching for what you talked about. The platform pages also belong to the platform, and a platform can shut down a directory overnight, the way Google Podcasts closed in 2024.

## What I deliver
- A generator, written in Python with OpenAI Codex and Claude Code, that reads your feed and writes the whole site as static HTML.
- Episode pages at permanent addresses, each with cover art, a player that streams from your host, the show notes, a transcript, and a glossary when an episode calls for one.
- Search titles and descriptions for every episode, drafted with AI and reviewed by hand, and alt text for every cover.
- PodcastSeries and PodcastEpisode structured data, a sitemap, an llms.txt file, and an RSS feed of the site.
- A 1,200 by 630 share card for every episode, carrying the cover and the episode title, so links posted to social platforms show in full.
- An archive, an about page with every place to listen, and room for written articles alongside the episodes.

## The daily job

A scheduled GitHub Actions workflow runs every morning. It adds new episodes, collects transcripts that arrive days late, rebuilds, and commits only when something changed. It refuses to publish when the feed looks broken, for example when the feed suddenly lists far fewer episodes than the site already has. When the audio stays with your host, every play still counts there.

## Ownership, start to finish

The domain and the repository are registered to you. Shows that already publish through Spotify, Apple, or another host can keep doing exactly that; the site clones their feed and adds a page for each new episode. Shows that want full ownership can go further: the site publishes the RSS feed the directories read, and the audio lives in storage on the show's own domain, such as Cloudflare R2, which charges nothing for downloads. The nightly check can run at any hour, or several times a day around release.

## Running costs

GitHub Pages hosts the site and Cloudflare handles DNS. Neither charges for a site like this, so the domain is the only bill unless you host your own audio, where R2 bills for storage past its free allowance. Nothing on the server needs patching, because nothing runs on the server.

## After launch

Most shows want more than a mirror of the feed. Common additions are corrections to an episode's notes, photos, links to the things discussed, and articles grown out of episodes that drew a response. Articles go through the same fact-check I describe on [fact-checked writing in your voice](https://gerriscorp.com/services/editorial/).

## Want to build it yourself?

The full method is free in my guide to [building a podcast website with Codex or Claude Code on GitHub Pages](https://gerriscorp.com/guides/podcast-website/). For getting episodes found once the site exists, see [podcast SEO](https://gerriscorp.com/guides/podcast-seo/).

## Engagement

A standard build from an existing feed is an afternoon of my time. It's a fixed-scope project, prepaid, quoted after a call about your feed and your goals. Additions after launch are quoted as a fixed fee or covered under [ongoing support](https://gerriscorp.com/services/ongoing-support/). Terms are on [Work With Me](https://gerriscorp.com/work-with-me/).

## Start a conversation

Scope and fees are settled in conversation, once I understand the problem. Choose the route that fits how your company works.

[Schedule a call](https://calendly.com/chrisabraham/30) [Work with me through Upwork](https://www.upwork.com/freelancers/chrisjabraham)

Updated October 15, 2026

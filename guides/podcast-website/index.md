> Give a podcast its own website for the price of a domain: Cloudflare Registrar at cost, free GitHub Pages hosting, and Claude Code building every episode page.
>
> Source: https://gerriscorp.com/guides/podcast-website/ · Updated 2026-10-08 · By Chris Abraham, Gerris Corp

# Build a podcast website with Claude Code, GitHub Pages, and Cloudflare

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 8, 2026

A podcast that lives only on Spotify and Apple is a tenant. The platforms own the pages, the search results, and the rules, and a platform can close a door overnight, the way Google Podcasts did in 2024. A website on your own domain is the one property you control. Here is the setup I build: it costs the price of a domain, it updates itself, and Claude Code does the typing.

## What you end up with
- One page per episode, at an address that never changes, with the cover art, the player, the show notes, and the transcript.
- A home page that features the newest episode, an archive of every episode, and an about page with every place to subscribe.
- Structured data, a sitemap, and descriptions written for search engines and AI assistants.
- A daily job that reads your podcast feed and adds new episodes on its own.

The audio stays with your host. Each player streams from the address in your feed, so the host still counts every play and your download numbers stay whole.

## Step 1: register the domain at cost

Cloudflare Registrar sells domains at the wholesale price the registry charges, plus the ICANN fee, with no markup on renewals. Privacy for the registration record comes included. A .com runs about ten dollars a year. The catch is that the domain must use Cloudflare's DNS, which suits this setup anyway. Pick a name that matches the show exactly, and register it before you announce anything.

## Step 2: let Claude Code build the generator

Claude Code is an AI coding assistant that runs in your terminal and works directly in a folder of files. You describe the site; it writes the code, runs it, reads the errors, and fixes them. The prompt that matters most names your feed and your rules. A good one reads close to this:

>

Build a static site from this podcast RSS feed, one page per episode, in Python. Keep each episode's address forever once it's assigned. Cache the cover art and transcripts in the repository, never the audio. Use the feed's audio URL exactly as given. Give every page a unique title near 60 characters and a description near 155. Add PodcastEpisode structured data and a sitemap.

Then review what it builds the way you'd review a contractor's work. Open a few episode pages, read the titles, click the players, and ask for changes in plain English. The first full build of a show with a few hundred episodes takes an afternoon, most of it spent downloading artwork.

## Step 3: publish on GitHub Pages

GitHub Pages hosts static sites free from a public repository. Published sites can be up to 1 GB, with a soft limit of 100 GB of traffic a month, which covers a podcast site comfortably because the audio never touches it. Put a file named `CNAME` containing your domain in the repository, and turn on Pages for the main branch.

## Step 4: point the domain, then turn on HTTPS

In Cloudflare's DNS, add the four GitHub Pages A records and four AAAA records for the bare domain, and a CNAME for www pointing at your github.io address. Leave every record set to DNS only, the gray cloud, while GitHub issues the certificate. When the "Enforce HTTPS" box in the repository's Pages settings becomes clickable, tick it. If the certificate never starts, remove the custom domain in the Pages settings and add it again; GitHub skips the request when the domain was saved before its DNS existed.

## Step 5: make it run itself

Ask Claude Code for a GitHub Actions workflow that runs the generator every morning, commits only when something changed, and fails loudly when the feed can't be read. Three details make it dependable:
- **Keepalive.** GitHub disables scheduled workflows in public repositories after 60 days without activity. A step that re-enables the workflow through the GitHub API on every run keeps the schedule alive through a quiet season.
- **Late transcripts.** Hosts often add transcripts days after an episode goes up. Recheck every episode that lacks one, on every run.
- **A sanity check.** If the feed suddenly lists far fewer episodes than the site has, stop and publish nothing.

## Step 6: tell the search engines

Add the site to Google Search Console and Bing Webmaster Tools and submit the sitemap. Wire in IndexNow so Bing and the other engines that share it hear about each new episode the morning it appears. Put the site's address in your podcast host's settings, too, so Apple and Spotify link listeners back to it.

## What it costs

The domain is the only bill. Hosting, HTTPS, and the daily job run free. Claude Code comes with Anthropic's paid plans, starting with Pro, which is plenty for a build like this.

## Where AI saves the most time

The generator itself is routine code. The slow parts are the judgment calls: a title that reads well at 60 characters, a description for an episode whose notes are two words, alt text for hundreds of cover images. An assistant drafts those in minutes, and you spend your time reviewing instead of typing. For the working method, specs, review, and keeping secrets out of the repository, see [how to use AI coding assistants on a website safely](https://gerriscorp.com/guides/ai-coding-assistants/). For the DNS side, see [Cloudflare settings that help or hurt SEO](https://gerriscorp.com/guides/cloudflare-seo/).

Want this built for your show, or for any feed you publish? [Tell me about it](https://gerriscorp.com/contact/).

## References
- [GitHub Docs: GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
- [GitHub Docs: Managing a custom domain for your GitHub Pages site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [Cloudflare Docs: Cloudflare Registrar](https://developers.cloudflare.com/registrar/)
- [GitHub Docs: Disabling and enabling a workflow](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)
- [Anthropic: Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

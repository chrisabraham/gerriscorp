> How gerriscorp.com is made: the water strider logo by Oliver Uberti, a Plone inspired design, a Python generator, GitHub Pages, and checks every page passes.
>
> Source: https://gerriscorp.com/colophon/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Colophon

A colophon is the note at the back of a well-made book about how it was made. This is that note for gerriscorp.com.

## The logo

The Gerris water strider was designed and drawn in 2012 by [Oliver Uberti](https://www.oliveruberti.com/), a dear friend and a remarkable artist. Oliver was a senior design editor at National Geographic and is the co-author and designer of Atlas of the Invisible, London: The Information Capital, Where the Animals Go, and Notes from a Public Typewriter. He gave the company its emblem: *Gerris lacustris*, the insect that skates across the surface of a pond without breaking it.

The name came first, and it came from rowing. Carbon fiber racing shells, especially doubles, have always looked to me like the pond skaters you can find in the still water along the Potomac's banks, dancing on the surface tension. I named my Hudson racing shell *Gerris* before I ever named a company after it. Once the firm Dan Krueger and I ran was incorporated, I asked Oliver for a logo, and what he drew settled the matter: any thought of renaming the agency ended the day I saw it. I wrote the whole story up in 2017.

## Design

The look borrows from the classic Plone theme I've used for my own sites for two decades: tabbed navigation, slate blue links, and nothing between the reader and the words. Body text is black Verdana at 18 pixels for legibility. The accent colors, a burnt orange for the name, a blue for page titles, and a teal for section heads, were each darkened until they pass the WCAG contrast standard against white.

## How it's built

Every page starts as a plain HTML file. A small Python program reads them, wraps each in the shared header and footer, and writes the finished site: pages, a Markdown copy of each page for AI tools, XML and HTML sitemaps, an Atom feed, llms.txt, and redirect pages for more than 400 addresses from the old gerriscorp.com. Before anything is published, the same program checks every page: title and description lengths, one heading per page, minimum word counts, first person singular, no copied phrasing between pages, and no broken internal links. If a page fails, nothing ships.

The site was written and built in a terminal, over SSH from a ThinkPad X220 to a Linux server at DigitalOcean, working alongside Claude Code, Anthropic's AI coding assistant. I set the requirements, made the editorial calls, and checked every fact; the assistant wrote code and drafts to my direction. [The editorial standards](https://gerriscorp.com/standards/) describe how that division of labor works.

## Hosting and delivery

The finished files are served by GitHub Pages over HTTPS, with DNS at Cloudflare. There's no database, no content management system, and no server code to patch. The only script is Google Analytics, set up with consent mode, as described on the [privacy page](https://gerriscorp.com/privacy/).

## Tested with
- Lynx, the text browser, to see each page the way screen readers and crawlers receive it. My notes on that are in [Lynx for website QA](https://gerriscorp.com/guides/lynx-qa/).
- Google PageSpeed Insights and Lighthouse, for performance, accessibility, best practices, and SEO.
- Google Search Console and Bing Webmaster Tools, with IndexNow announcing every change to Bing.

## Source

The code and content live in a public repository: [github.com/chrisabraham/gerriscorp](https://github.com/chrisabraham/gerriscorp). The site went live on October 5, 2026.

Updated October 6, 2026

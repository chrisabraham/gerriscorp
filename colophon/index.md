> How gerriscorp.com is made: the water strider logo by Oliver Uberti, a Plone inspired design, a Python generator, GitHub Pages, and checks every page passes.
>
> Source: https://gerriscorp.com/colophon/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Colophon

A colophon is the note at the back of a well-made book about how it was made. This is that note for gerriscorp.com.

## The logo The Gerris logo, drawn by Oliver Uberti in 2012.

The Gerris water strider was designed and drawn in 2012 by [Oliver Uberti](https://www.oliveruberti.com/), a dear friend and a remarkable artist. Oliver was a senior design editor at National Geographic and is the co-author and designer of [Atlas of the Invisible](https://www.amazon.com/dp/0393651517?tag=gerris-20), [London: The Information Capital](https://www.amazon.com/dp/1846148472?tag=gerris-20), [Where the Animals Go](https://www.amazon.com/dp/0393634027?tag=gerris-20), and [Notes from a Public Typewriter](https://www.amazon.com/dp/1538729113?tag=gerris-20). He gave the company its emblem: *Gerris lacustris*, the insect that skates across the surface of a pond without breaking it.

The name came first, and it came from rowing. Carbon fiber racing shells, especially doubles, have always looked to me like the pond skaters you can find in the still water along the Potomac's banks, dancing on the surface tension. I named my Hudson racing shell *Gerris* before I ever named a company after it. Once the firm Dan Krueger and I ran was incorporated, I asked Oliver for a logo, and what he drew settled the matter: any thought of renaming the agency ended the day I saw it. I wrote the whole story up in 2017.

Oliver's second round of sketches, dated October 25, 2012, set four ideas over the words "Gerris Web Strategies": contact points drawn as ripples, contact points drawn as dots, a single point of contact with a ripple and a smile, and the strider itself, which he called Strider/Connector. The strider is the one that became the logo. Oliver Uberti's Phase II revisions, October 25, 2012. Concept 1, Strider/Connector, became the Gerris logo.

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

Links to books and gear on Amazon carry my Amazon Associates tag. As an Amazon Associate I earn from qualifying purchases.

Updated October 6, 2026

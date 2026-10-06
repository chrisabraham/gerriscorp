> What the ADA expects of business websites, the six fixes that cover most of the risk, what to skip, and why the same work improves search, AI answers, trust.
>
> Source: https://gerriscorp.com/guides/ada-website-compliance/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# ADA website compliance for businesses: lower risk, better SEO

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Making a website accessible is the right thing to do, and it's also cheap insurance. Most of the legal exposure comes from a short list of common, fixable failures. Fix those, document what you did, and you'll also get a faster, clearer, better-ranking site that AI assistants understand. No badges, no widgets, and no press release required.

A note before the details: this is a practitioner's guide, not legal advice. If you've received a demand letter, call a lawyer first.

## What the law expects

The Americans with Disabilities Act covers businesses open to the public, and the Department of Justice's position, set out in its guidance on ADA.gov, is that this includes their websites. For private businesses there's no technical standard written into the regulations, so courts, settlements, and auditors almost always measure sites against the Web Content Accessibility Guidelines, WCAG, at level AA.

For state and local governments, the rules are firmer. A 2024 Justice Department rule requires WCAG 2.1 level AA. An interim rule in April 2026 extended the deadlines: April 26, 2027, for governments serving 50,000 people or more, and April 26, 2028, for smaller ones and special districts. If you build or run sites for public agencies, those dates belong on your calendar.

## Where the risk actually comes from

Demand letters and lawsuits tend to cite problems anyone can detect with a free automated scan, because that's how many of them are found. WebAIM's 2026 survey of the top million home pages found detectable failures on 95.9% of them, and six kinds of errors accounted for 96% of everything detected:
| Failure | Share of home pages |
| --- | --- |
| Low contrast text | 83.9% |
| Missing image alt text | 53.1% |
| Form fields without labels | 51% |
| Empty links | 46.3% |
| Empty buttons | 30.6% |
| Missing page language | 13.5% |

Fixing those six puts a site ahead of almost all of the web. That's the 80 to 90 percent that matters most, and it's usually days of work, not months.

## The fix list, in order
1. **Contrast.** Darken pale text and light brand colors until normal text reaches 4.5 to 1 against its background. This is usually a handful of color values in one stylesheet.
2. **Alt text.** Describe every meaningful image; give decorative ones an empty alt attribute.
3. **Form labels.** Every field gets a visible label tied to it. Placeholder text alone doesn't count.
4. **Links and buttons that say something.** Icon-only buttons need an accessible name; a link wrapped around nothing but an icon needs one too.
5. **Page language.** One attribute on the html element.
6. **Keyboard and focus.** Tab through every page template; everything should be reachable, in order, with a visible focus outline.

Then cover the rest of WCAG AA over time, starting with headings, captions for video, and error messages on forms.

## What to skip
- **Overlay widgets.** Scripts that promise one-line compliance don't fix the underlying markup, many users of assistive technology find them obstructive, and sites using them have still been sued.
- **Badges and certificates.** A "fully compliant" seal invites scrutiny and proves nothing. The work speaks for itself.
- **Grand announcements.** A short accessibility statement is useful; a marketing campaign about it isn't.

## Document it

Keep a simple record: which pages were checked, with which tools, what was fixed, and when. Publish a brief accessibility statement with a way to report problems, and answer those reports promptly. A business that can show steady, good-faith effort is in a far better position than one that can't.

## The dividends you collect anyway
- **Search.** Alt text feeds image search, real headings and descriptive links are exactly what Google uses to understand a page, and the page language helps search engines serve the right audience.
- **AI answers and AI agents.** Assistants quote clean, well-structured text, and the browsing agents now arriving use a page's accessibility information to find and operate buttons and forms. Lighthouse even added an Agentic Browsing check.
- **Trust.** A site that works for everyone reads as careful and current, which is what quality raters, and customers, look for.
- **Conversions.** Readable text, labeled forms, and usable buttons help every visitor, including the ones on a phone in bright sunlight.

## Keep it from sliding back

Accessibility erodes with every new page, plugin, and campaign. Add a quick automated scan and a keyboard pass to your launch routine, check new templates before they ship, and review the site once a quarter. My guide to [Lynx for website QA](https://gerriscorp.com/guides/lynx-qa/) covers a text-browser pass that catches a surprising number of these problems in minutes.

For help auditing and fixing a site, see [technical SEO](https://gerriscorp.com/services/technical-seo/) or [get in touch](https://gerriscorp.com/contact/).

## References
- [ADA.gov: Guidance on web accessibility and the ADA](https://www.ada.gov/resources/web-guidance/)
- [ADA.gov: Fact sheet on the Title II web rule](https://www.ada.gov/resources/2024-03-08-web-rule/)
- [W3C: Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [WebAIM: The WebAIM Million, 2026 report](https://webaim.org/projects/million/)
- [Overlay Fact Sheet](https://overlayfactsheet.com/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

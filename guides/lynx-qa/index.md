> How to use the Lynx text browser to check content, links, and noindex tags across a whole site before launch, plus online options for teams without a terminal.
>
> Source: https://gerriscorp.com/guides/lynx-qa/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Lynx for website QA: text browser checks before every launch

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Lynx has been around since the early nineties, and it's still one of the most useful tools in my launch kit. Because it ignores styling and never runs JavaScript, it strips a page down to what the server actually sends. Scripted from the command line, it can check every page of a site in minutes, which makes it a natural fit for redesigns, migrations, and release checklists.

## Getting Lynx

I run Lynx on a Linux server over SSH, from an old ThinkPad, and that's the simplest setup. On Debian or Ubuntu:

```
sudo apt update && sudo apt install lynx
```

Other systems: `brew install lynx` on macOS with Homebrew, `sudo dnf install lynx` on Fedora, and on Windows, the same apt command inside the Windows Subsystem for Linux. Once it's installed, `lynx --version` confirms it works.

## Commands worth memorizing
| Command | What it gives you |
| --- | --- |
| `lynx URL` | An interactive text browser. Arrows move, Enter follows a link, q quits, and \ toggles the HTML source. |
| `lynx -dump URL` | The rendered text, followed by a numbered list of every link. |
| `lynx -dump -nolist URL` | Text only, no link list. Best for comparing two versions of a page. |
| `lynx -dump -listonly URL` | Only the links, numbered, with their full addresses. |
| `lynx -source URL` | The raw HTML, handy for checking head tags. |

## Five checks I script before a launch

### 1. Every page in the sitemap has real text

Pull the URLs from the sitemap and count the words Lynx sees on each. A product page that comes back with forty words when it should have four hundred is a template hiding its content behind scripts.

```
curl -s https://example.com/sitemap.xml | grep -o '<loc>[^<]*' | sed 's/<loc>//' |
while read u; do echo "$(lynx -dump -nolist "$u" | wc -w) $u"; done | sort -n | head
```

The thinnest pages float to the top of the list.

### 2. Staging and production say the same thing

After a migration, compare the old page with the new one as text. Missing paragraphs, dropped FAQs, and lost disclaimers show up immediately, without any styling noise.

```
diff <(lynx -dump -nolist https://old.example.com/pricing/) \
     <(lynx -dump -nolist https://www.example.com/pricing/)
```

### 3. No stray noindex survived from staging

The most expensive launch mistake I know is a robots noindex tag carried over from a staging site. One loop over the sitemap catches it:

```
... | while read u; do lynx -source "$u" | grep -qi 'noindex' && echo "NOINDEX $u"; done
```

### 4. Links are real, and they all resolve

The link list shows only genuine anchor links, so navigation built from click handlers simply won't appear. Feed the list to curl to catch broken targets and redirect chains:

```
lynx -dump -listonly https://example.com/ | awk '/https?:/{print $2}' | sort -u |
xargs -n1 curl -s -o /dev/null -w '%{http_code} %{url_effective}\n' | grep -v '^200'
```

### 5. The first screen is about the page

Read the top twenty lines of each key template's dump. If a consent banner, a mega menu, and a promotional strip come before the first heading, assistive technology and crawlers wade through all of it too. Reordering the markup, or adding a skip link, fixes the problem for both.

## Reading the results with a team

Text dumps are easy to share, and they make strong evidence in a developer ticket: here's the page as a crawler receives it, and here's the paragraph that's missing. Nobody has to install anything to read a text file, and the comparison is hard to argue with.

## When a terminal isn't an option

Plenty of teams can't or won't install command-line tools. These get most of the way there:
- [Lynx Viewer](https://www.delorie.com/web/lynxview.html), a free web service that renders a public URL much as Lynx would.
- [SEO Browser](https://www.seo-browser.com/), which places the browser's version of a page beside a crawler's and highlights what JavaScript added.
- The [Rich Results Test](https://search.google.com/test/rich-results) and Search Console's URL Inspection, which both show the HTML Google rendered.
- The [Web Developer extension](https://chrispederick.com/work/web-developer/) for Chrome and Firefox, which turns off CSS and JavaScript with a click.
- Accessibility checkers and screen readers: [WAVE](https://wave.webaim.org/) offers a no-styles view, and [NVDA](https://www.nvaccess.org/) or Apple's VoiceOver read a page in the same top-to-bottom order Lynx displays. An accessibility auditor will usually run some version of this test anyway.

## Add it to the checklist

I add a Lynx pass to every launch: sitemap word counts, a noindex sweep, a link check, and a text diff of the most important templates. It takes about ten minutes and catches problems a styled browser hides. For the full launch sequence, see [the website migration SEO checklist](https://gerriscorp.com/guides/migration-checklist/), and for the deeper rendering questions, [how to tell if JavaScript is hiding your content](https://gerriscorp.com/guides/javascript-seo/).

## References
- [Lynx project home](https://lynx.invisible-island.net/)
- [Debian package: lynx](https://packages.debian.org/stable/lynx)
- [Homebrew formula: lynx](https://formulae.brew.sh/formula/lynx)
- [Microsoft Learn: Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [W3C: Easy checks, a first review of web accessibility](https://www.w3.org/WAI/test-evaluate/preliminary/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

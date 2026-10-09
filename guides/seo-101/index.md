> SEO from first principles for absolute beginners: how search works, people first content, E E A T, titles, links, alt text, speed, and accessibility.
>
> Source: https://gerriscorp.com/guides/seo-101/ · Updated 2026-10-09 · By Chris Abraham, Gerris Corp

# SEO 101: a first principles primer for any website

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 9, 2026

Search engine optimization sounds like a dark art. It's mostly common sense, applied carefully. A search engine has one job: send each searcher to the page that best answers the question. Everything in SEO follows from helping it do that job, and from never trying to fool it. This primer works for any website on any platform, from a hand-coded page to a store with ten thousand products.

## Principle 1: understand the machine

Search works in three stages.
1. **Crawling.** Programs called crawlers follow links from page to page and download what they find.
2. **Indexing.** The engine reads each page, figures out what it's about, and files it in an enormous catalog.
3. **Serving.** When someone searches, the engine pulls the most useful pages from that catalog and ranks them.

AI answers in Google, Bing, and ChatGPT search draw on the same kind of catalog. A page that can't be crawled can't be indexed, and a page that isn't indexed can't be ranked or quoted by anyone. That is why the technical basics come first.

## Principle 2: write for people first

Google's own guidance asks one question of every page: was it made to help a person, or to attract search traffic? Write the page you'd want to find. Answer the question fully, in plain language, early on the page. Include what only you know: your prices, your process, your photos, your results. A page that would read the same with any company's name swapped in gives a searcher nothing new.

## Principle 3: earn trust with E-E-A-T

Google's search quality raters judge pages for experience, expertise, authoritativeness, and trustworthiness, and Google describes trust as the most important of the four. You show them on the page itself:
- **Experience:** evidence you've actually done the thing, such as real photos, real numbers, and lessons learned the hard way.
- **Expertise:** a named author with a short bio and the credentials that matter for the topic.
- **Authoritativeness:** other respected people and sites mentioning and linking to you.
- **Trust:** accurate content, a real address and contact details, clear policies, HTTPS, and sources for your claims.

## Principle 4: label every page clearly
- **Title tag:** the clickable headline in search results. Make it unique, specific, and about 50 to 60 characters, with the page's main subject near the front.
- **Meta description:** the summary under the headline. A clear 140 to 160 character description earns the click, even though it plays no direct part in ranking.
- **One H1:** a single main heading that says what the page is about, followed by H2 and H3 subheadings in order, like an outline.
- **Readable URLs:** `/services/roof-repair/` tells people and crawlers more than `/page?id=4817`.

## Principle 5: link with words that mean something

Internal links, from one page of your site to another, are how crawlers find your pages and how they learn what each page covers. The clickable words matter. "Read more," "click here," and "learn more" tell nobody anything, and a screen reader user who pulls up a list of a page's links hears the same useless phrase ten times. Make the link text describe the destination, the way "see my [guide to Core Web Vitals](https://gerriscorp.com/guides/core-web-vitals/)" names exactly where the click leads. Link from strong pages to the pages you most want found, and make sure every important page is reachable through ordinary links, without relying on search boxes or scripts.

## Principle 6: describe every meaningful image

Alt text is the written description of an image, read aloud by screen readers and read by search engines. Describe what the picture shows in a short sentence, and include any words that appear in it. Skip "image of" and "photo of"; screen readers already announce that it's an image. Decorative images, such as background flourishes, get an empty alt attribute so screen readers skip them. Keyword lists in alt text help nobody and look like spam.

## Principle 7: make it fast and stable

Google's Core Web Vitals measure three things: how fast the main content appears (Largest Contentful Paint, good under 2.5 seconds), how quickly the page responds to a tap or click (Interaction to Next Paint, good under 200 milliseconds), and whether the layout jumps around while loading (Cumulative Layout Shift, good under 0.1). Compress and correctly size images, load fewer scripts, and give images width and height so the page doesn't shift. Test any page free in PageSpeed Insights. For the details, see my [Core Web Vitals guide](https://gerriscorp.com/guides/core-web-vitals/).

## Principle 8: build it so everyone can use it

Accessibility and SEO want the same things: real text, logical headings, descriptive links, alt text, captions, enough color contrast, and a site that works with a keyboard alone. The Web Content Accessibility Guidelines (WCAG) are the standard, and in the United States the ADA has been applied to websites in court. Every accessibility fix makes the site easier to crawl too. See [ADA website compliance](https://gerriscorp.com/guides/ada-website-compliance/) and [testing a site in a text browser](https://gerriscorp.com/guides/lynx-qa/).

## My standing recommendation: put the site behind Cloudflare

For almost every site I work on, I recommend running DNS and caching through [Cloudflare](https://www.cloudflare.com/), and the free plan alone does a remarkable amount. My own experience and every AI assistant I've asked agree on this one. If Cloudflare only registers your domain and answers DNS while traffic passes straight through to your host, the free plan is all you need. Once the site runs through Cloudflare itself, the orange cloud, its paid services start earning their keep, including image optimization that shrinks and converts pictures on the fly. For a site that benefits, I recommend budgeting about $50 a month for them, starting with the Pro plan. I pay for Cloudflare Pro on [chrisabraham.com](https://chrisabraham.com/), and I don't earn a cent for recommending it to clients, though I've joked that I should.
- **Speed:** Cloudflare serves cached copies of your pages and files from data centers near each visitor, which cuts load times and takes strain off your server.
- **Security and HTTPS:** set the SSL/TLS mode to Full (strict), turn on Always Use HTTPS, and enable HSTS once everything loads over HTTPS, so browsers never fall back to an insecure connection.
- **Crawlers:** its Crawler Hints feature uses IndexNow to tell Bing and other engines when pages change. Set its bot and AI crawler controls on purpose; I let search and AI crawlers in, because I want to be found and cited.
- **Domains at cost:** Cloudflare Registrar sells domains at the registry's wholesale price with no markup on renewals.

The exception is hosted platforms like Shopify, Squarespace, and Wix, which run their own CDN and certificates. With those, use Cloudflare for DNS only, the gray cloud, or let the platform manage DNS, and follow the platform's own instructions. My [guide to Cloudflare settings that help or hurt SEO](https://gerriscorp.com/guides/cloudflare-seo/) covers the switches to check.

## Principle 9: open the door for crawlers
- Keep [robots.txt](https://gerriscorp.com/guides/robots-txt/) from blocking pages you want found.
- Publish an XML sitemap listing your important pages, and submit it in Google Search Console. Then open Bing Webmaster Tools and use its import option to copy every verified site and sitemap over from Search Console in a few clicks. Both tools are free, and I check both regularly to make sure the sitemaps are read without errors.
- Turn on IndexNow, through Cloudflare, your SEO plugin, or your platform, so Bing and other participating engines hear about new and changed pages right away.
- Use HTTPS everywhere, and pick one version of the domain, with or without www, and redirect the other to it.
- Add [structured data](https://gerriscorp.com/guides/structured-data/) that matches what the page visibly says.

## Principle 10: stay white hat

Every shortcut on this list has hurt real businesses, some permanently: buying links, keyword stuffing, hidden text, pages written only to rank, mass AI content nobody reviewed, fake reviews, and fake authors. The search engines publish their spam policies openly. Read them once, and you'll recognize the pitches in your inbox for what they are.

## Your first week
1. Verify the site in Google Search Console and Bing Webmaster Tools, and submit the sitemap.
2. List your ten most important pages, and give each a unique title, description, and H1.
3. Replace every "read more" and "click here" with descriptive link text.
4. Add alt text to every meaningful image.
5. Run your home page and one inner page through PageSpeed Insights, and fix the largest problem it names.
6. Ask three happy customers for reviews on your Google Business Profile.

## Further reading
- [Google's SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Essentials](https://developers.google.com/search/docs/essentials), including the spam policies
- [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google's Search Quality Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf) (PDF), where E-E-A-T is defined
- [How Google writes title links](https://developers.google.com/search/docs/appearance/title-link) and [how it writes snippets](https://developers.google.com/search/docs/appearance/snippet)
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- [Web Vitals on web.dev](https://web.dev/articles/vitals) and [PageSpeed Insights](https://pagespeed.web.dev/)
- [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/) and [the W3C's explanation of link purpose](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html)
- [WebAIM on alternative text](https://webaim.org/techniques/alttext/), the [W3C alt text decision tree](https://www.w3.org/WAI/tutorials/images/decision-tree/), and the [WAVE accessibility checker](https://wave.webaim.org/)
- [Getting started with schema.org](https://schema.org/docs/gs.html)
- [Moz's Beginner's Guide to SEO](https://moz.com/beginners-guide-to-seo)

Want a second pair of eyes on your first week's list? [Send me the site](https://gerriscorp.com/contact/).

## References
- [Google Search Central: SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Central: In-depth guide to how Google Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)
- [Google Search Central: Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google Search Central: Link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- [web.dev: Web Vitals](https://web.dev/articles/vitals)
- [W3C: WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

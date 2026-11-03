> A business website on GitHub Pages with a wholesale Cloudflare domain and an AI doing the typing: hosting $0, about $10 a year all in. Steps and limits.
>
> Source: https://gerriscorp.com/guides/github-pages-website/ · Updated 2026-11-03 · By Chris Abraham, Gerris Corp

# A Real Business Website for the Price of a Domain Name

By [Chris Abraham](https://gerriscorp.com/about/) · Published November 3, 2026

A working setup for a business website that costs about $10 a year: domain at wholesale from Cloudflare, files in GitHub, GitHub Pages hosting free, DNS pointed once, and an AI chat doing the typing.

Most small-business websites are rented from a platform at $200 to $480 a year, and the rental buys a site the business does not own and cannot move. The setup below is the one Gerris runs for its own web properties: plain files, free hosting, a domain at wholesale, and ownership sitting in the client's accounts from day one. It suits brochure sites, consultancies, professional practices, and content sites. Its limits are stated plainly at the end.

## Why does the domain come from Cloudflare Registrar?

[Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) charges the wholesale registry price with no markup, no teaser year followed by a tripled renewal, and WHOIS privacy included. A .com renewal runs about $10 to $15 a year. Register in an account the business controls, switch on auto-renew and two-factor authentication, and the largest single cause of small-site death, the lapsed domain, is off the table. Cloudflare's DNS is included free, which matters in step three.

## What does GitHub hold, exactly?

A repository: a folder with a memory. The site's pages and images live in it as ordinary files, and every saved change is a commit, a dated snapshot that can be compared or restored. [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) publishes those files as a website. A free [GitHub](https://github.com/pricing) account covers the whole arrangement, and the [published limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) (1 GB site size, generous bandwidth) are far beyond a typical business site.

## How is the site switched on and connected?
1. Create the repository and open Settings, then Pages, then publish from the main branch, as GitHub's [creation guide](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) describes. The site answers at a free `username.github.io` address.
2. Enter the custom domain in the same Pages settings.
3. In Cloudflare's DNS panel, following GitHub's [custom domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), add a **CNAME** record for `www` pointing at `username.github.io`, and four **A** records for the bare domain: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`. Set them to DNS only during verification.
4. Enable **Enforce HTTPS** in the Pages settings. GitHub issues and renews the certificate free.

Cloudflare's [DNS records documentation](https://developers.cloudflare.com/dns/manage-dns-records/) covers the record types for anyone setting this up for the first time. Total elapsed time for the plumbing is under an hour, most of it waiting for DNS.

## How does content get published without a developer?

The working loop has four steps and runs entirely in a browser:
1. **Draft the words anywhere.** Dictation, notes, a full answer to a customer question.
2. **Paste them into an AI chat** with the site's facts (names, prices, dates, phone) and get back a finished page file, with instructions to use only the supplied facts.
3. **Paste the file into GitHub's web editor** and commit it with a note describing the change.
4. **Reload.** Live in about a minute, with the previous version preserved in the commit history.

Images are handled the same way: the AI generates or processes the image, the file is uploaded to the repository, and the page points at it by name. There is no CMS to patch, no plugin chain to update, and no admin password for an attacker to guess, because there is no admin.

## What does it cost, item by item?
- Domain renewal at Cloudflare: about $10 to $15 a year.
- GitHub Pages hosting: $0.
- Cloudflare DNS: $0.
- HTTPS certificate: $0, self-renewing.
- Optional AI subscription: buys content work, not hosting.

Against that, a website builder at $17 to $40 a month totals $200 to $480 a year and the site cannot leave the platform. Managed WordPress hosting costs a similar band and adds maintenance hours. The GitHub arrangement also changes the risk profile: the site is plain HTML in an account the business owns, so a host failure or a vendor dispute is an inconvenience measured in hours, not a rebuild.

## Where does this setup stop working?

State the edges before a client hits them:
- **Commerce.** No built-in store or checkout. Use a hosted payment link or checkout (Stripe, PayPal) or a dedicated store platform, linked from the site.
- **Forms.** A static site cannot receive submissions; a helper service such as Formspree or Basin forwards them by email.
- **Dynamic features.** Logins, dashboards, live inventory, and web applications need server hosting and a developer.
- **Design ceiling.** A template-driven build is clean and fast; a brand competing on bespoke visual design may still need a designer.

For clients whose existing site already lives in a repository, the companion guide on [giving an outside SEO safe repository access](https://gerriscorp.com/guides/repository-access/) covers roles, branch protection, and keeping secrets out of the code.

## Who should do the work?

Owners who enjoy the loop run it themselves at no cost beyond the domain. Owners whose hours are worth more in selling and client relationships hand the repository to a technical partner: setup done correctly once, structure designed, changes shipped on request, while the domain, the GitHub account, and every file stay in the owner's name. That is the engagement shape Gerris recommends and delivers, and it is priced as labor rather than as platform rent, because the platform charges nothing.

## Questions about building a website on GitHub Pages

### Is free hosting reliable enough for a business site?

GitHub Pages runs on the same infrastructure as GitHub itself and carries published size and bandwidth limits far above small-site traffic. For a brochure or content site, uptime is not the weak point in the stack. The weak points are the expired domain and the lost account password, both handled by auto-renew and two-factor authentication.

### Can a site like this be found by Google and AI search?

Yes. Every page is finished HTML at its own URL, which is what crawlers and answer engines read. Visibility then depends on content: specific facts, complete answers, and one clear subject per page. The technical setup removes excuses; it does not write the pages.

### What if the business outgrows the setup?

The files move. Plain HTML uploads to any static host or into a larger platform's theme, and the domain repoints through the same DNS panel. Nothing in the build creates lock-in, which is the reason Gerris recommends it to clients whose plans may change.

### Who owns the website when Gerris builds it?

The client. The domain sits in the client's Cloudflare account, the repository in the client's GitHub account, and Gerris works through granted access that can be revoked at any time. Any arrangement where the site lives in the vendor's accounts should be treated as a warning sign, whoever the vendor is.

## A checklist for launch day
1. Domain registered at Cloudflare in the business's own account, auto-renew and two-factor on.
2. GitHub account in the business's name; repository created; Pages switched on.
3. Custom domain set; CNAME and A records in place; HTTPS enforced.
4. First `index.html` live at the domain with real facts and a working phone number.
5. Publishing loop tested once: one edit, one commit, one reload.
6. Access for any consultant granted deliberately, and recorded.

## Want me to handle this for you?

This guide shows you how to do it yourself. If you'd rather hand it to someone who does this work for clients, I'm glad to help: tell me what's happening and I'll tell you where I'd start.

[Book a 30 minute call](https://calendly.com/chrisabraham/30) [Call +1 202-352-5051](tel:+12023525051) [Email chris@gerriscorp.com](mailto:chris@gerriscorp.com)

If your company hires through Upwork, you'll find me [there as well](https://www.upwork.com/freelancers/chrisjabraham).

## References
- [GitHub Docs: What is GitHub Pages?](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages)
- [GitHub Docs: Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [GitHub Docs: Managing a custom domain for your GitHub Pages site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [GitHub Docs: GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
- [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/)
- [Cloudflare Docs: Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/)
- [GitHub Pricing](https://github.com/pricing)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

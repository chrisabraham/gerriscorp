> What Consent Mode v2 controls in GA4 and Google Ads, how basic and advanced mode differ, how to set regional defaults, and how to check that it really works.
>
> Source: https://gerriscorp.com/guides/ga4-consent-mode/ · Updated 2026-10-06 · By Chris Abraham, Gerris Corp

# Google Consent Mode v2 for GA4: a practical setup guide

By [Chris Abraham](https://gerriscorp.com/about/) · Published October 6, 2026

Consent Mode is how Google's tags learn whether a visitor agreed to cookies, and how they behave when the answer is no. Set up well, it keeps analytics honest and the site compliant. Set up badly, it either drops most of your data or quietly ignores the visitor's choice.

## The four signals
| Signal | Controls |
| --- | --- |
| `analytics_storage` | Cookies for analytics, such as GA4's visitor identifier |
| `ad_storage` | Cookies for advertising, such as conversion and remarketing cookies |
| `ad_user_data` | Whether visitor data may be sent to Google for advertising |
| `ad_personalization` | Whether that data may be used for personalized ads and remarketing |

Version 2 added the last two in late 2023. Since March 2024 Google has required them for advertisers who want to use audience and conversion features with traffic from the European Economic Area, under the EU's Digital Markets Act.

## Basic and advanced mode
- **Basic mode.** Google's tags don't load at all until the visitor consents. Nothing is collected from people who decline or ignore the banner.
- **Advanced mode.** The tags load right away with consent denied and send cookieless pings: no identifiers, no stored cookies. When the visitor accepts, the tags switch to full measurement.

Advanced mode lets GA4 estimate the behavior of visitors who declined, through behavioral modeling, once a property has enough traffic. Google's documented minimum is roughly a thousand daily events from visitors with analytics denied, and a thousand daily users with analytics granted, sustained for a week or more. Smaller sites never reach it, and for them the choice between modes makes little difference to the reports.

## Setting the defaults

The default state must be set before any Google tag loads. With the gtag snippet, that means a `consent default` command above the config line. Defaults can differ by region, using ISO country codes:

```
gtag('consent', 'default', {
  ad_storage: 'denied', ad_user_data: 'denied',
  ad_personalization: 'denied', analytics_storage: 'denied',
  region: ['AT','BE','BG','CH','CY','CZ','DE','DK','EE','ES','FI','FR','GB',
           'GR','HR','HU','IE','IS','IT','LI','LT','LU','LV','MT','NL','NO',
           'PL','PT','RO','SE','SI','SK']
});
gtag('consent', 'default', {
  ad_storage: 'denied', ad_user_data: 'denied',
  ad_personalization: 'denied', analytics_storage: 'granted'
});
```

That's the pattern this site uses: advertising signals denied everywhere, because the site runs no ads, and analytics denied by default in the EEA, the UK, and Switzerland, where the law requires prior consent, and granted elsewhere. The most specific matching region wins. When a visitor accepts or declines, the banner sends a `consent update` command with the new values.

In Google Tag Manager, set defaults with a tag on the Consent Initialization trigger, which fires before every other trigger. Most consent platforms certified by Google ship a Tag Manager template that does this for you.

## Choosing a consent platform

Publishers who show Google ads to visitors in the EEA, the UK, or Switzerland must use a consent platform from Google's certified list. For everyone else it's still the safer choice, because certified platforms send Consent Mode signals correctly by default. Check that the platform supports regional rules, so visitors in places that don't require a banner aren't shown one.

## Checking that it works
- **Tag Assistant.** Connect it to the site and open the Consent tab for each event. It shows the default state, each update, and which tags fired under which state.
- **The network panel.** Every GA4 request carries a `gcs` parameter. `G100` means advertising and analytics storage are both denied; `G111` means both granted; `G101` means advertising denied and analytics granted.
- **The cookie list.** In a fresh private window from a region set to denied, load a page without touching the banner. No `_ga` cookie should exist until you accept.
- **GA4 admin.** Under Data collection, the consent settings screen reports whether analytics and advertising consent signals are being received.

## Mistakes I find most often
- **The default is set after the tag loads.** The first hit goes out with no consent state, often with cookies set. Order matters.
- **Two sources of truth.** A banner plugin and a hand-coded snippet both set defaults, with different values.
- **The banner blocks the page.** A consent script that loads synchronously in the head, or a banner that pushes the layout, hurts Core Web Vitals. Load it asynchronously and show it as an overlay.
- **Hard-coded tags outside the consent setup.** An old Universal Analytics snippet, a Facebook pixel, or a heatmap script still firing regardless of the visitor's choice.

## What to expect in the reports

After a consent banner goes live in Europe, GA4's European sessions usually fall, sometimes sharply, because declined visitors are no longer counted as users. That's the system working. Search Console doesn't use cookies, so its click counts are unaffected, and comparing the two separates a consent effect from a real traffic loss.

Analytics setup and repair is part of [GA4 and analytics work](https://gerriscorp.com/services/analytics/). For a consent problem that hid half a site's traffic, see the [consent blocking case study](https://gerriscorp.com/case-studies/consent-blocking/).

## References
- [Google Tag Platform: Set up consent mode](https://developers.google.com/tag-platform/security/guides/consent)

Written by [Chris Abraham](https://gerriscorp.com/about/), founder of Gerris Corp in Arlington, Virginia, from his own client engagements, with every technical claim checked against the documentation listed. Websites since 1994, digital marketing since 2002. [Editorial standards](https://gerriscorp.com/standards/) · [Upwork profile](https://www.upwork.com/freelancers/chrisjabraham)

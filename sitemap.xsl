<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="robots" content="noindex"/>
<title>XML sitemap: Gerris Corp</title>
<style>:root { --text: #000; --muted: #333; --link: #284a57; --tab: #8cacbb; --bar: #dee7ec; --rule: #c8d3d8; --bg: #fff; }
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
body { margin: 0; color: var(--text); background: var(--bg); font: 18px/1.65 Verdana, "Lucida Grande", Lucida, "DejaVu Sans", Helvetica, Arial, sans-serif; }
.wrap { max-width: 46rem; margin: 0 auto; padding: 0 1rem; }
a { color: var(--link); text-decoration: underline; text-underline-offset: .15em; overflow-wrap: anywhere; }
a:hover { text-decoration-thickness: 2px; }
:focus-visible { outline: 3px solid #000; outline-offset: 2px; }
img { max-width: 100%; height: auto; }
.skip { position: absolute; left: -999px; }
.skip:focus { left: 1rem; top: .5rem; background: #fff; padding: .5rem; z-index: 1; }
.top { display: flex; align-items: center; gap: .9rem; padding: 1.25rem 0 .9rem; }
.top > a { flex: none; line-height: 0; }
.top img { width: 64px; height: 64px; max-width: none; }
.brand { font-size: 1.6rem; font-weight: bold; color: #000; text-decoration: none; }
.brand:hover { text-decoration: underline; }
.tag { margin: 0; color: var(--muted); font-size: .95rem; line-height: 1.4; }
nav { border-bottom: 4px solid var(--bar); }
nav ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: .3rem; }
nav li { margin: 0; }
nav a { display: block; padding: .4rem .7rem; border: 1px solid var(--tab); border-bottom: none; text-decoration: none; font-size: .9rem; white-space: nowrap; }
nav a:hover { background: var(--bar); text-decoration: underline; }
nav a[aria-current] { background: var(--bar); color: #000; font-weight: bold; }
.crumbs { font-size: .9rem; margin: 1rem 0 0; color: var(--muted); }
main { padding: 1.25rem 0 2rem; }
h1 { font-size: 1.75rem; line-height: 1.25; margin: .25rem 0 1rem; }
h2 { font-size: 1.3rem; line-height: 1.3; margin: 2rem 0 .5rem; }
h3 { font-size: 1.08rem; line-height: 1.35; margin: 1.5rem 0 .4rem; }
p, ul, ol, dl, table { margin: 0 0 1rem; }
li { margin-bottom: .4rem; }
.lead { font-size: 1.1rem; }
.byline { color: var(--muted); font-size: .9rem; margin-top: -.5rem; }
.updated { color: var(--muted); font-size: .9rem; margin-top: 2rem; }
code { font-family: Consolas, Menlo, monospace; font-size: .92em; background: #f2f5f7; padding: 0 .2em; }
pre { background: #f2f5f7; padding: .75rem; overflow-x: auto; font-size: .9rem; line-height: 1.45; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; font-size: .95rem; }
th, td { border: 1px solid var(--rule); padding: .4rem .55rem; text-align: left; vertical-align: top; }
th { background: var(--bar); }
dt { font-weight: bold; margin-top: 1rem; }
dd { margin: .2rem 0 0 0; }
.button { display: inline-block; margin: 0 .5rem .6rem 0; padding: .6rem 1.1rem; border: 2px solid var(--link); background: var(--bar); color: #000; font-weight: bold; text-decoration: none; }
.button:hover { text-decoration: underline; }
.related { border-top: 1px solid var(--rule); margin-top: 2rem; padding-top: .5rem; }
.contact li { margin-bottom: .6rem; }
.site-footer { border-top: 1px solid var(--rule); padding: 1rem 0 2.5rem; color: var(--muted); font-size: .9rem; }
.site-footer p { margin: 0 0 .4rem; }
@media (max-width: 34rem) {
  body { font-size: 17px; }
  .top img { width: 52px; height: 52px; }
  nav a { padding: .45rem .55rem; }
  h1 { font-size: 1.5rem; }
}</style>
</head>
<body>
<div class="wrap">
<main id="main">
<h1>XML sitemap</h1>
<p class="lead">This is the sitemap search engines read for gerriscorp.com: <xsl:value-of select="count(s:urlset/s:url)"/> pages, each with the date it last changed. People may prefer the <a href="sitemap/">site map with summaries</a>.</p>
<table>
<thead><tr><th>Page</th><th>Last changed</th></tr></thead>
<tbody>
<xsl:for-each select="s:urlset/s:url">
<tr><td><a href="{s:loc}"><xsl:value-of select="s:loc"/></a></td><td><xsl:value-of select="s:lastmod"/></td></tr>
</xsl:for-each>
</tbody>
</table>
</main>
</div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>

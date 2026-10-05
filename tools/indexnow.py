"""Tell IndexNow (Bing, Yandex, Seznam, Naver, Yep) that gerriscorp.com changed.

Run by .github/workflows/indexnow.yml after each push to main. Does nothing
until https://gerriscorp.com/<key>.txt actually serves the key, so the
github.io preview (and the old redirect) never gets submitted.
"""
import glob, json, re, time, urllib.request, xml.etree.ElementTree as ET

LIVE = "https://gerriscorp.com"
key = next(f[:-4] for f in glob.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}\.txt", f))

def get(url):
    with urllib.request.urlopen(url, timeout=20) as r:
        return r.geturl(), r.read().decode("utf-8", "replace")

def live():
    try:
        final, body = get(f"{LIVE}/{key}.txt")
        return final.startswith(LIVE) and body.strip() == key
    except Exception:
        return False

for _ in range(20):  # Pages deploys a minute or two after the push
    if live(): break
    time.sleep(30)
else:
    print(f"{LIVE}/{key}.txt isn't serving the key; not live yet, skipping IndexNow")
    raise SystemExit(0)

urls = [e.text.strip() for e in ET.fromstring(get(f"{LIVE}/sitemap.xml")[1])
        .iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
body = json.dumps({"host": "gerriscorp.com", "key": key, "keyLocation": f"{LIVE}/{key}.txt",
                   "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, method="POST",
                             headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req, timeout=30) as r:
    print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")

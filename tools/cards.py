"""Per-page 1200x630 share cards ("McImages") for Open Graph, X/Twitter, and schema.

make(path, title, kicker) writes cards/<slug>.png once and reuses it until the title or
kicker changes (cards/manifest.json). Needs Pillow; without it, existing cards are reused
and pages without one fall back to the site-wide social-card.png. Build with
~/.venvs/site/bin/python tools/build.py to create new cards.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "cards"
MANIFEST = OUT / "manifest.json"
FONTS = [Path("/usr/share/fonts/truetype/dejavu"), ROOT / "tools" / "fonts"]
_state = {"manifest": None, "warned": False}


def _font(name, size):
    from PIL import ImageFont
    for d in FONTS:
        if (d / name).exists():
            return ImageFont.truetype(str(d / name), size)
    return ImageFont.load_default(size)


def _wrap(d, text, font, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + [cur]


def make(path, title, kicker, style):
    """Return the card's absolute URL, or None to use the site-wide card."""
    slug = path.strip("/").replace("/", "-") or "home"
    out = OUT / f"{slug}.png"
    if _state["manifest"] is None:
        _state["manifest"] = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    key = f"{style['version']}|{kicker}|{title}"
    if _state["manifest"].get(slug) == key and out.exists():
        return style["site"] + f"cards/{slug}.png"
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        if not _state["warned"]:
            print("cards: Pillow missing; reusing existing cards (build with ~/.venvs/site/bin/python)")
            _state["warned"] = True
        return style["site"] + f"cards/{slug}.png" if out.exists() else None
    OUT.mkdir(exist_ok=True)
    W, H, M = 1200, 630, 80
    im = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(im)
    style["chrome"](im, d, W, H, M)
    textw = W - 2 * M - style.get("right_reserve", 0)
    d.text((M, style["kicker_y"]), kicker, font=_font("DejaVuSans.ttf", 32), fill=style["kicker_color"])
    size = 62
    while True:
        f = _font("DejaVuSans-Bold.ttf", size)
        lines = _wrap(d, title, f, textw)
        if len(lines) <= 4 or size <= 38:
            break
        size -= 4
    width = textw
    while width > 300 and len(_wrap(d, title, f, width - 10)) == len(lines):
        width -= 10  # balance the lines so no last line is a lone word
    y = style["title_y"]
    for ln in _wrap(d, title, f, width)[:4]:
        d.text((M, y), ln, font=f, fill="#000000")
        y += int(size * 1.22)
    im.save(out, optimize=True)
    _state["manifest"][slug] = key
    MANIFEST.write_text(json.dumps(_state["manifest"], indent=1, sort_keys=True))
    return style["site"] + f"cards/{slug}.png"

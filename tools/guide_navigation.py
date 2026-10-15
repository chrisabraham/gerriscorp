"""Add compact section navigation without changing a guide's editorial source."""
import html
import re
import unicodedata
from html.parser import HTMLParser
from urllib.parse import quote


class _Outline(HTMLParser):
    def __init__(self, body):
        super().__init__(convert_charrefs=True)
        self.offsets = [0]
        for line in body.splitlines(keepends=True):
            self.offsets.append(self.offsets[-1] + len(line))
        self.ids = set()
        self.headings = []
        self.current = None
        self.ignored = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in ("pre", "script", "style"):
            self.ignored += 1
        if tag == "h2" and not self.ignored:
            line, col = self.getpos()
            self.current = {"offset": self.offsets[line - 1] + col,
                            "tag": self.get_starttag_text(),
                            "id": attrs.get("id"), "text": []}

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"].append(data)

    def handle_endtag(self, tag):
        if tag in ("pre", "script", "style"):
            self.ignored = max(0, self.ignored - 1)
        if tag == "h2" and self.current is not None:
            self.current["text"] = re.sub(r"\s+", " ", "".join(self.current["text"])).strip()
            self.headings.append(self.current)
            self.current = None


def add_guide_contents(body, word_count):
    """Return HTML with unique section targets and a native disclosure list."""
    if word_count < 700:
        return body
    outline = _Outline(body)
    outline.feed(body)
    if len(outline.headings) < 4:
        return body

    edits, links = [], []
    for heading in outline.headings:
        target = heading["id"]
        if not target:
            plain = unicodedata.normalize("NFKD", heading["text"]).encode("ascii", "ignore").decode()
            stem = "section-" + (re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-") or "heading")
            target, number = stem, 2
            while target in outline.ids:
                target = f"{stem}-{number}"
                number += 1
            outline.ids.add(target)
            # Replace an empty id if present; preserve all other attributes.
            tag = re.sub(r'''\s+id\s*=\s*(?:""|'')''', "", heading["tag"], flags=re.I)
            tag = re.sub(r"^<h2\b", f'<h2 id="{target}" tabindex="-1"', tag, count=1, flags=re.I)
            edits.append((heading["offset"], len(heading["tag"]), tag))
        fragment = quote(target, safe="-._~")
        links.append(f'    <li><a href="#{fragment}">{html.escape(heading["text"])}</a></li>')

    contents = ('<details class="guide-contents">\n'
                '  <summary>On this page</summary>\n'
                '  <ol>\n' + "\n".join(links) + '\n  </ol>\n</details>\n\n')
    # Apply target attributes from the end so original offsets stay valid.
    for offset, length, replacement in reversed(edits):
        body = body[:offset] + replacement + body[offset + length:]
    first = outline.headings[0]["offset"]
    return body[:first] + contents + body[first:]

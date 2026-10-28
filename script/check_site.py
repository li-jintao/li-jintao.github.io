#!/usr/bin/env python3
"""Check the built career pages, metadata, redirects, and local destinations."""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.ids, self.text = [], set(), []
        self.h1, self.active, self.canonical, self.description = 0, 0, None, None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        self.h1 += tag == "h1"
        self.active += attrs.get("aria-current") == "page"
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "meta" and attrs.get("name") == "description":
            self.description = attrs.get("content")
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

    def handle_data(self, data):
        self.text.append(data)


def check_site(root):
    pages = {}

    def load(path):
        if path not in pages:
            pages[path] = Page(path)
        return pages[path]

    def resolve(url):
        path = root / unquote(urlsplit(url).path).lstrip("/")
        return path / "index.html" if path.is_dir() else path

    expected = {
        "/": ["Ocean Network Express", "six data scientists", "Lower operating costs", "Technical ownership"],
        "/work/": ["Problem", "Contribution", "Outcome", "container movement", "Google Cloud"],
        "/cv/": ["Professional summary", "Professional experience", "Kyoto University"],
        "/skills/": ["Forecasting & applied machine learning", "Technical direction & delivery"],
        "/research/": ["Physical Review X", "Selected publications"],
    }
    checked_links = 0
    for route, markers in expected.items():
        path = resolve(route)
        assert path.is_file(), f"Missing page: {route}"
        page = load(path)
        assert page.h1 == 1, f"{route}: expected exactly one h1"
        assert page.active == 1, f"{route}: expected one active navigation link"
        assert "main" in page.ids, f"{route}: missing skip-link destination"
        assert page.description, f"{route}: missing SEO description"
        assert page.canonical == "https://li-jintao.github.io" + route, page.canonical
        text = " ".join(" ".join(page.text).split())
        for marker in markers:
            assert marker in text, f"{route}: missing {marker!r}"
        assert "{{" not in text and "{%" not in text, f"{route}: unrendered Liquid"
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            destination = urlsplit(urljoin(route, link))
            target = resolve(destination.path)
            assert target.is_file(), f"{route}: broken link {link}"
            if destination.fragment and target.suffix == ".html":
                assert unquote(destination.fragment) in load(target).ids, f"{route}: missing anchor {link}"
            checked_links += 1
        print(f"PASS {route}: content, navigation, metadata, and local links")

    for route in ["/about/", "/about.html", "/resume", "/Research/"]:
        page = resolve(route).read_text()
        assert 'http-equiv="refresh"' in page, f"Missing redirect: {route}"
    for name in ["feed.xml", "sitemap.xml"]:
        ElementTree.parse(root / name)
    sitemap = ElementTree.parse(root / "sitemap.xml")
    locations = [node.text or "" for node in sitemap.iter() if node.tag.endswith("loc")]
    for legacy in ["/portfolio/", "/teaching/", "/markdown/", "/year-archive/", "/page-archive/", "/collection-archive/", "/talkmap", "/talks/", "/categories/", "/tags/"]:
        assert not any(legacy in url for url in locations), f"Legacy page published: {legacy}"
    assert "Page not found" in (root / "404.html").read_text()
    print(f"PASS {checked_links} local links, legacy redirects, XML feeds, and 404 page")


if __name__ == "__main__":
    check_site(Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve())

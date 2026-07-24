from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hash_links = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        href = values.get("href", "")
        if href.startswith("#") and href != "#":
            self.hash_links.append(href[1:])


def main():
    files = {
        "html": ROOT / "index.html",
        "css": ROOT / "styles.css",
        "js": ROOT / "script.js",
        "readme": ROOT / "README.md",
        "cv": ROOT / "assets" / "Enqiao_Lu_CV.pdf",
        "profile": ROOT / "profile.png",
    }
    errors = []
    for name, path in files.items():
        if not path.exists():
            errors.append(f"missing {name}: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)

    html = files["html"].read_text(encoding="utf-8")
    combined = "\n".join(
        files[name].read_text(encoding="utf-8")
        for name in ("html", "css", "js", "readme")
    )

    required = (
        "3.9/4.0",
        "Big Data Technology",
        "Xingrui Yu",
        "Yu_Xingrui@a-star.edu.sg",
        "SpikeOPD",
        "LOGIV",
        "AAAI 2027",
        "ICML 2026 SCALE Workshop",
        "CN 121982334 B",
        "Guangdong Provincial First Prize",
        "assets/Enqiao_Lu_CV.pdf",
    )
    forbidden = (
        "3.88/4.00",
        "Big Energy Technology",
        "Columbia Engineering",
        "Ivor Tsang",
        "NeurIPS 2026",
        "PhD from NTU or NUS",
        "NTU Full Scholarship Summer Program",
    )
    mojibake = ("锛", "鈫", "闄嗘", "馃", "銆")

    for text in required:
        if text not in html:
            errors.append(f"required text missing: {text}")
    for text in forbidden:
        if text in combined:
            errors.append(f"stale text remains: {text}")
    for text in mojibake:
        if text in combined:
            errors.append(f"mojibake remains: {text}")

    parser = SiteParser()
    parser.feed(html)
    for target in parser.hash_links:
        if target not in parser.ids:
            errors.append(f"navigation target missing: #{target}")

    if not files["cv"].read_bytes().startswith(b"%PDF"):
        errors.append("CV asset is not a PDF")
    if files["cv"].stat().st_size < 100_000:
        errors.append("CV asset is unexpectedly small")
    if files["profile"].stat().st_size < 10_000:
        errors.append("profile image is unexpectedly small")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)

    print("PASS: site content and assets validated")


if __name__ == "__main__":
    main()

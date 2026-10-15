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
        "Computer Science and Technology",
        "12/580",
        "Top 2%",
        "Nanyang Technological University (NTU)",
        "Exchange Student",
        "Aug. 2026 - Dec. 2026",
        "Xingrui Yu",
        "Yu_Xingrui@a-star.edu.sg",
        "SpikeOPD",
        "LOGIV",
        "AAAI 2027",
        "Passed Phase 1",
        "https://arxiv.org/abs/2608.27857",
        "ICRA 2027",
        "ICLR 2027",
        "LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks",
        "When is seeing enough? Cross-granularity evidence search with Sufficiency verification for High-resolution understanding",
        "Enqiao Lu, Yuxiang Xie, Xingrui Yu*, Yuyang Wang, Yipeng Gu, Zhenglin Wan, Pengfei Zhou, Wangbo Zhao, Yang You, Yuxiang Gao, Ivor Tsang.",
        "Enqiao Lu, Muqing Jian, Yiwei Fu, Xiao Luo.",
        "ICML 2026 SCALE Workshop",
        "CN121982334B",
        "ZL 2026 1 0450001.9",
        "Granted Jun. 5, 2026",
        "Zhang Xueyi, Haizhou Li, Lu Enqiao, Gao Sihan, Sun Jialu, Cai Siqi.",
        "Class B (2025-2026)",
        "Class B (2024-2025)",
        "Guangdong Provincial First Prize",
        "159-5715-1440",
        "85556560",
        "Multimodal large language models",
        "assets/Enqiao_Lu_CV.pdf",
    )
    forbidden = (
        "3.88/4.00",
        "Big Energy Technology",
        "Big Data Technology",
        "Top 3%",
        "Columbia Engineering",
        "NeurIPS 2026",
        "PhD from NTU or NUS",
        "NTU Full Scholarship Summer Program",
        "139-5819-8588",
        "Making World Action Models Verifiable",
        "Transportation Research Part E",
        "Priori Adaptive Attention Mechanism",
        "Core Coursework",
        "Mandarin (Native)",
        "English-Chinese CV",
        "efficient model architectures",
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

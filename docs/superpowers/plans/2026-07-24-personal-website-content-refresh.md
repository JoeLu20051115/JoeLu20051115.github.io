# Personal Website Content Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update Enqiao Lu's GitHub Pages site to match the July 2026 CV, retain the existing visual design, add the current CV download, and publish the verified result.

**Architecture:** Keep the existing dependency-free static site. `index.html` remains the content source, `styles.css` remains the visual system, `script.js` retains the small navigation/animation behaviors, and a new standard-library validation script checks factual copy, stale phrases, anchors, encoding, and local assets before deployment.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, Python standard library, GitHub Pages.

## Global Constraints

- Preserve the English single-page layout, purple-blue palette, profile portrait, navigation model, and responsive structure.
- Do not add frameworks, package managers, runtime dependencies, analytics, a CMS, a contact form, a blog, or a bilingual toggle.
- Use `D:/个人资料/陆恩乔_中英文简历.pdf` as the factual source of truth and publish it as `assets/Enqiao_Lu_CV.pdf`.
- Keep publication status exact: two AAAI 2027 submissions, one ICML 2026 SCALE Workshop paper, one Transportation Research Part E paper under review, and one granted patent.
- Do not publish private OpenReview author-console links.
- Final page order inside the downloadable CV remains English first, Chinese second.

## File Structure

- Create `tests/validate_site.py`: dependency-free regression check for content, anchors, assets, and mojibake.
- Create `assets/Enqiao_Lu_CV.pdf`: approved downloadable CV.
- Modify `index.html`: metadata and all user-facing academic content.
- Modify `styles.css`: repair the corrupted marker and style the CV action/accessibility states.
- Modify `script.js`: make top navigation safe and keep `aria-expanded` synchronized.
- Modify `README.md`: replace mojibake with concise UTF-8 repository documentation.

---

### Task 1: Add a Failing Static-Site Validation Check

**Files:**
- Create: `tests/validate_site.py`

**Interfaces:**
- Consumes: repository root files `index.html`, `styles.css`, `script.js`, `README.md`, and `assets/Enqiao_Lu_CV.pdf`.
- Produces: exit code `0` with `PASS: site content and assets validated` when all approved content is present and all stale content is absent; exit code `1` with one `FAIL:` line per issue otherwise.

- [ ] **Step 1: Create the validation script**

```python
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
```

- [ ] **Step 2: Run the check and confirm the current site fails**

Run:

```powershell
python tests/validate_site.py
```

Expected: exit code `1` with `FAIL: missing cv: assets/Enqiao_Lu_CV.pdf`. The remaining content checks become reachable after Task 2 adds the asset.

- [ ] **Step 3: Commit the validation check**

```powershell
git add tests/validate_site.py
git commit -m "test: validate portfolio content and assets"
```

---

### Task 2: Replace the Academic Content and Add the CV Asset

**Files:**
- Create: `assets/Enqiao_Lu_CV.pdf`
- Modify: `index.html`

**Interfaces:**
- Consumes: approved CV at `D:/个人资料/陆恩乔_中英文简历.pdf` and existing CSS class names.
- Produces: one English static page with sections `about`, `education`, `research`, `publications`, `awards`, and `skills`, plus a working CV link.

- [ ] **Step 1: Copy the approved CV into the site**

```powershell
New-Item -ItemType Directory -Force assets | Out-Null
Copy-Item -LiteralPath 'D:\个人资料\陆恩乔_中英文简历.pdf' -Destination 'assets\Enqiao_Lu_CV.pdf'
```

Expected: `assets/Enqiao_Lu_CV.pdf` exists and remains larger than 100 KB.

- [ ] **Step 2: Replace the head metadata**

Use this exact metadata:

```html
<meta name="description" content="Enqiao Lu is a CUHK-Shenzhen undergraduate researcher working on LLM post-training, efficient model architectures, verifiable reasoning, and embodied AI.">
<meta name="keywords" content="Enqiao Lu, CUHK-Shenzhen, A*STAR, LLM post-training, on-policy distillation, Agentic RL, verifiable reasoning, embodied AI">
<meta name="author" content="Enqiao Lu">
<meta property="og:title" content="Enqiao Lu | LLM Post-training & Verifiable AI">
<meta property="og:description" content="LLM post-training, efficient model architectures, verifiable reasoning, and embodied AI.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://joelu20051115.github.io/">
<title>Enqiao Lu | LLM Post-training & Verifiable AI</title>
```

- [ ] **Step 3: Update the hero and contact actions**

Keep the existing hero structure and replace its text/action block with:

```html
<p class="hero-greeting">Hello, I'm</p>
<h1 class="hero-name">Enqiao Lu</h1>
<h2 class="hero-title">LLM Post-training, Verifiable Reasoning & Embodied AI</h2>
<p class="hero-affiliation">School of Data Science, CUHK-Shenzhen</p>
<p class="hero-quote">"Do the hard but right thing."</p>
<div class="hero-contact">
    <a href="mailto:124090411@link.cuhk.edu.cn" class="contact-btn">
        <i class="fas fa-envelope" aria-hidden="true"></i>
        Get in Touch
    </a>
    <a href="assets/Enqiao_Lu_CV.pdf" class="contact-btn contact-btn-secondary" download>
        <i class="fas fa-file-arrow-down" aria-hidden="true"></i>
        Download CV
    </a>
</div>
```

- [ ] **Step 4: Update education**

Use:

```html
<p class="education-degree">B.S. in Data Science and Big Data Technology</p>
<div class="education-details">
    <div class="education-highlight">
        <i class="fas fa-graduation-cap" aria-hidden="true"></i>
        <span>Cumulative GPA: <strong>3.9/4.0</strong> (Rank: Top 3% in School of Data Science)</span>
    </div>
    <div class="education-courses">
        <p><strong>Core Coursework:</strong> Calculus I & II (A), Linear Algebra (A), Data Structures (A), Introduction to Computer Programming I & II (A)</p>
    </div>
</div>
```

The date remains `Sept. 2024 - June 2028 (Expected)`. Delete the Columbia highlight entirely.

- [ ] **Step 5: Replace the research section**

Use two existing `research-card` components with this copy:

```html
<div class="research-card">
    <div class="research-header">
        <div class="research-info">
            <h3>Research Intern</h3>
            <p class="research-institution">Centre for Frontier AI Research (CFAR), Agency for Science, Technology and Research (A*STAR)</p>
            <p class="research-advisor">Mentor: Dr. Xingrui Yu · <a href="mailto:Yu_Xingrui@a-star.edu.sg">Yu_Xingrui@a-star.edu.sg</a></p>
        </div>
        <span class="research-period">Summer 2026 · Singapore</span>
    </div>
    <ul class="research-list">
        <li><strong>SpikeOPD:</strong> Studied stable on-policy distillation for spiking language models to mitigate rollout-induced performance drift.</li>
        <li><strong>LOGIV:</strong> Developed verifiable logic-graph inference with VAL verification for long-horizon robotic manipulation.</li>
    </ul>
</div>

<div class="research-card">
    <div class="research-header">
        <div class="research-info">
            <h3>Undergraduate Research Fellow (URA)</h3>
            <p class="research-institution">CUHK-SZ Brain Science & Medical AI Group</p>
            <p class="research-advisor">Advisor: Prof. Haizhou Li</p>
        </div>
        <span class="research-period">Jun. 2025 - Dec. 2025 · Shenzhen</span>
    </div>
    <ul class="research-list">
        <li>Conducted clinical AI modeling for epilepsy diagnosis with Huashan Hospital and South China Hospital.</li>
        <li><strong>BCI Classification:</strong> Enhanced CorAtt with variational information bottleneck learning.</li>
        <li><strong>Dream Decoding:</strong> Applied EEG-Deformer to cross-subject dream-category classification.</li>
    </ul>
</div>
```

- [ ] **Step 6: Replace publications and patent with five cards**

Use the existing card classes and these exact records:

```html
<div class="publication-card">
    <div class="publication-header"><span class="publication-tag">First Author</span><span class="publication-date">AAAI 2027 · Submitted</span></div>
    <h3 class="publication-journal">AAAI 2027 Submission</h3>
    <p class="publication-title">Making World Action Models Verifiable: Logic-Graph Reasoning for Long-Horizon Robotic Manipulation</p>
</div>
<div class="publication-card">
    <div class="publication-header"><span class="publication-tag">First Author</span><span class="publication-date">AAAI 2027 · Submitted</span></div>
    <h3 class="publication-journal">AAAI 2027 Submission</h3>
    <p class="publication-title">SpikeOPD: Stable On-Policy Distillation for Spiking Language Models</p>
</div>
<div class="publication-card">
    <div class="publication-header"><span class="publication-tag">First Author</span><span class="publication-date">ICML 2026 SCALE Workshop</span></div>
    <h3 class="publication-journal">ICML 2026 Workshop (SCALE)</h3>
    <p class="publication-title">LOGIV: Logic-Graph Inference with VAL-Verification for Long-Horizon Robotic Manipulation</p>
</div>
<div class="publication-card">
    <div class="publication-header"><span class="publication-tag review">Co-author</span><span class="publication-date">Under Review · 2026</span></div>
    <h3 class="publication-journal">Transportation Research Part E</h3>
    <p class="publication-title">A Deep Reinforcement Learning Framework Based on Priori Adaptive Attention Mechanism for Stochastic Customer Vehicle Routing Problems</p>
</div>
<div class="publication-card">
    <div class="publication-header"><span class="publication-tag patent">Granted Patent</span><span class="publication-date">Granted Jun. 5, 2026</span></div>
    <h3 class="publication-journal">Chinese Invention Patent · CN 121982334 B</h3>
    <p class="publication-title">Deepfake Detection Method, Device, and Medium Based on Vision-Language Models</p>
    <p class="publication-meta">Patent No. ZL 2026 1 0450001.9</p>
</div>
```

- [ ] **Step 7: Replace the awards grid**

Keep six cards, each using the existing icon/year/institution structure, with these headings and details:

```text
Meritorious Winner (M Award), COMAP Mathematical Contest in Modeling | 2026 | International
Academic Performance Scholarship, Class B | 2024-2025 | CUHK-Shenzhen
Undergraduate Research Award, URA Scholarship | 2025 | CUHK-Shenzhen · Outstanding research potential
Dean's List | 2025 | School of Data Science · Top 5%
National Second Prize & Guangdong Provincial First Prize, CUMCM | 2025 | National / Provincial
Third Prize, GBA Information Programming Contest | 2025 | Regional · Track A
```

- [ ] **Step 8: Replace skills and remove outdated future plans**

Use four `skill-category` cards:

```text
LLM Post-training & Optimization | Supervised fine-tuning, on-policy distillation, reinforcement learning, model compression, and efficiency optimization
Verifiable AI & Agents | Logic-graph reasoning, long-horizon agents, evaluation and verification, embodied AI
Programming & Tools | Python, PyTorch, Linux, Git, LaTeX
Languages | Mandarin (Native), English (Fluent)
```

Replace the purpose card with:

```html
<div class="purpose-card">
    <h3><i class="fas fa-bullseye" aria-hidden="true"></i> Research Focus</h3>
    <p>LLM post-training, efficient model architectures, spiking language models, verifiable reasoning, long-horizon agents, and embodied AI.</p>
</div>
```

- [ ] **Step 9: Run the validator**

```powershell
python tests/validate_site.py
```

Expected: still fails only for remaining README/CSS mojibake until Task 3. It must no longer report missing current academic content or the CV asset.

- [ ] **Step 10: Commit the content refresh**

```powershell
git add index.html assets/Enqiao_Lu_CV.pdf
git commit -m "feat: refresh academic profile and CV"
```

---

### Task 3: Repair Styling, Navigation, Encoding, and Documentation

**Files:**
- Modify: `styles.css`
- Modify: `script.js`
- Modify: `README.md`

**Interfaces:**
- Consumes: updated hero actions and existing navigation markup.
- Produces: keyboard-visible actions, reduced-motion behavior, safe top navigation, synchronized mobile-menu state, and clean UTF-8 repository text.

- [ ] **Step 1: Repair and extend CSS**

Replace the corrupted research-list marker with:

```css
.research-list li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: var(--secondary-color);
    font-weight: bold;
}
```

Add:

```css
.contact-btn-secondary {
    background: transparent;
    color: var(--text-white);
    border: 2px solid rgba(255, 255, 255, 0.8);
}

.contact-btn-secondary:hover {
    background: rgba(255, 255, 255, 0.12);
}

.research-advisor a {
    color: inherit;
}

.publication-tag.review {
    background: #7c3aed;
}

.publication-meta {
    margin-top: 0.75rem;
    color: var(--text-light);
    font-size: 0.95rem;
}

a:focus-visible,
button:focus-visible {
    outline: 3px solid #fbbf24;
    outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        scroll-behavior: auto !important;
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

- [ ] **Step 2: Use a real button for the mobile navigation toggle**

Replace the current `div.nav-toggle` in `index.html` with:

```html
<button class="nav-toggle" type="button" aria-label="Toggle navigation" aria-expanded="false">
    <span></span><span></span><span></span>
</button>
```

Add to `.nav-toggle` in CSS:

```css
background: none;
border: 0;
padding: 0;
```

- [ ] **Step 3: Make top navigation safe and synchronize menu state**

Replace the mobile toggle handler with:

```javascript
navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('active');
    navToggle.classList.toggle('active', isOpen);
    navToggle.setAttribute('aria-expanded', String(isOpen));
});
```

When a nav link closes the menu, also call:

```javascript
navToggle.setAttribute('aria-expanded', 'false');
```

Replace the smooth-scroll callback body with:

```javascript
anchor.addEventListener('click', function (event) {
    const href = this.getAttribute('href');
    event.preventDefault();
    if (href === '#') {
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
    }
    const target = document.querySelector(href);
    if (target) {
        window.scrollTo({ top: target.offsetTop - 80, behavior: 'smooth' });
    }
});
```

- [ ] **Step 4: Rewrite README as UTF-8**

Use:

```markdown
# Enqiao Lu - Personal Website

Personal academic website for Enqiao Lu, an undergraduate researcher at the School of Data Science, The Chinese University of Hong Kong, Shenzhen.

Live site: <https://joelu20051115.github.io/>

## Research interests

- LLM post-training and on-policy distillation
- Efficient model architectures and optimization
- Verifiable reasoning, long-horizon agents, and embodied AI

## Repository structure

- `index.html` - page content and metadata
- `styles.css` - responsive visual design
- `script.js` - navigation and scroll interactions
- `profile.png` - profile portrait
- `assets/Enqiao_Lu_CV.pdf` - current English-Chinese CV

Contact: <124090411@link.cuhk.edu.cn>
```

- [ ] **Step 5: Run static validation and diff checks**

```powershell
python tests/validate_site.py
node --check script.js
git diff --check
```

Expected:

```text
PASS: site content and assets validated
```

`git diff --check` must produce no output and exit `0`.
`node --check script.js` must produce no output and exit `0`.

- [ ] **Step 6: Commit the presentation and documentation fixes**

```powershell
git add index.html styles.css script.js README.md
git commit -m "fix: polish portfolio accessibility and encoding"
```

---

### Task 4: Render, Verify, and Publish

**Files:**
- Verify: `index.html`
- Verify: `styles.css`
- Verify: `script.js`
- Verify: `assets/Enqiao_Lu_CV.pdf`

**Interfaces:**
- Consumes: completed static site and its validation script.
- Produces: verified local desktop/mobile renders and the published GitHub Pages site on `main`.

- [ ] **Step 1: Start the local static server**

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Expected: `Serving HTTP on 127.0.0.1 port 8000`.

- [ ] **Step 2: Inspect desktop layout at 1440 × 1000**

Open `http://127.0.0.1:8000/` and verify:

- hero title and both action buttons fit without overlap;
- each section is readable and all five publication cards render;
- six award cards align consistently;
- navigation anchors scroll to the correct section;
- CV download returns the PDF.

- [ ] **Step 3: Inspect mobile layout at 390 × 844**

Verify:

- navigation button opens/closes and reports the correct `aria-expanded` state;
- both hero buttons remain visible and tappable;
- long publication titles wrap without horizontal overflow;
- dates and institutions remain readable;
- no content remains hidden after scroll animations.

- [ ] **Step 4: Run final automated checks**

```powershell
python tests/validate_site.py
node --check script.js
git diff --check
git status --short
```

Expected: validator passes, diff check is clean, and status is clean after any visual fixes are committed.

- [ ] **Step 5: Push the verified commits**

```powershell
git push origin main
```

Expected: push succeeds and reports `main -> main`.

- [ ] **Step 6: Verify the published site**

Open `https://joelu20051115.github.io/` after GitHub Pages updates and confirm:

- the hero contains `LLM Post-training, Verifiable Reasoning & Embodied AI`;
- education contains `3.9/4.0`;
- the A*STAR card contains `Xingrui Yu`;
- the awards contain `Guangdong Provincial First Prize`;
- `https://joelu20051115.github.io/assets/Enqiao_Lu_CV.pdf` loads successfully.

- [ ] **Step 7: Record a final status snapshot**

```powershell
git status --short
git log -4 --oneline --decorate
```

Expected: clean status and the design, test, content, and presentation commits at the top of `main`.

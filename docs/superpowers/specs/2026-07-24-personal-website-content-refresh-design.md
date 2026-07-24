# Personal Website Content Refresh Design

## Objective

Bring `https://joelu20051115.github.io/` into full alignment with Enqiao Lu's July 2026 CV while preserving the existing English single-page layout and purple-blue visual identity.

The refreshed site must present accurate education, research, publications, patent, awards, and technical interests; remove outdated plans and affiliations; fix encoding defects; and provide a direct download for the current English-Chinese CV.

## Chosen Approach

Use a content-complete refresh within the existing static HTML/CSS/JavaScript structure.

- Preserve the current navigation, section layout, cards, color palette, profile image, responsive breakpoints, and lightweight GitHub Pages deployment.
- Reorder and expand content only where the new CV requires it.
- Avoid frameworks, build tools, new runtime dependencies, and unrelated redesign work.

This approach is more complete than simple text replacement but substantially lower risk than a full visual rebuild.

## Source of Truth

The current English-Chinese CV at `D:/个人资料/陆恩乔_中英文简历.pdf` is the factual source of truth.

No private OpenReview author-console links will be published. Submission status must be expressed as text unless a stable public paper page is available.

## Page Content

### Global Metadata

- Title: `Enqiao Lu | LLM Post-training & Verifiable AI`
- Description: undergraduate researcher at CUHK-Shenzhen working on LLM post-training, efficient model architectures, verifiable reasoning, and embodied AI.
- Keywords must include Enqiao Lu, CUHK-Shenzhen, A*STAR, LLM post-training, on-policy distillation, Agentic RL, verifiable reasoning, and embodied AI.
- Remove corrupted Chinese metadata.

### Navigation and Hero

- Keep the existing section navigation and profile portrait.
- Replace `World Model / VLA Researcher` with `LLM Post-training, Verifiable Reasoning & Embodied AI`.
- Keep the CUHK-Shenzhen affiliation and contact details.
- Add a prominent `Download CV` control linked to `assets/Enqiao_Lu_CV.pdf`.
- Retain the existing quote unless it interferes with the responsive layout.

### Education

- Institution: The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen).
- Degree: B.S. in Data Science and Big Data Technology.
- Period: September 2024 to June 2028 expected.
- GPA: 3.9/4.0.
- Rank: Top 3% in the School of Data Science.
- Retain the current core coursework.
- Remove the Columbia Engineering and PhD Fast-track claim.

### Research Experience

1. Centre for Frontier AI Research (CFAR), Agency for Science, Technology and Research (A*STAR), Singapore.
   - Role: Research Intern.
   - Period: Summer 2026.
   - Mentor: Dr. Xingrui Yu, `Yu_Xingrui@a-star.edu.sg`.
   - Work: SpikeOPD for stable on-policy distillation in spiking language models; LOGIV for verifiable logic-graph inference in long-horizon robotic manipulation.
2. CUHK-SZ Brain Science & Medical AI Group.
   - Role: Undergraduate Research Fellow (URA).
   - Period: June 2025 to December 2025.
   - Advisor: Prof. Haizhou Li.
   - Retain epilepsy clinical AI modeling, BCI classification, and dream-decoding work, using concise CV-aligned language.

Remove the incorrect Ivor Tsang mentorship, January-present dates, remote-intern label, NeurIPS 2026 claim, and outdated World Model/VLA description.

### Publications and Patent

Display five records in this order:

1. `Making World Action Models Verifiable: Logic-Graph Reasoning for Long-Horizon Robotic Manipulation.` First author; submitted to AAAI 2027.
2. `SpikeOPD: Stable On-Policy Distillation for Spiking Language Models.` First author; submitted to AAAI 2027.
3. `LOGIV: Logic-Graph Inference with VAL-Verification for Long-Horizon Robotic Manipulation.` First author; ICML 2026 SCALE Workshop.
4. `A Deep Reinforcement Learning Framework Based on Priori Adaptive Attention Mechanism for Stochastic Customer Vehicle Routing Problems.` Transportation Research Part E; under review, 2026.
5. Granted Chinese invention patent: `Deepfake Detection Method, Device, and Medium Based on Vision-Language Models.` Patent No. ZL 2026 1 0450001.9; Grant Publication No. CN 121982334 B; granted June 5, 2026.

First-author status, review status, workshop venue, and granted status must be visually distinguishable without implying acceptance where none exists.

### Honors and Awards

Display these six records:

1. 2026 Meritorious Winner (M Award), COMAP Mathematical Contest in Modeling.
2. 2025 Academic Performance Scholarship, Class B (2024-2025), CUHK-Shenzhen.
3. 2025 Undergraduate Research Award / URA Scholarship, CUHK-Shenzhen.
4. 2025 Dean's List, School of Data Science, top 5%.
5. 2025 National Second Prize and Guangdong Provincial First Prize, Contemporary Undergraduate Mathematical Contest in Modeling.
6. 2025 Third Prize, GBA Information Programming Contest, Track A.

### Research Interests and Skills

- Research focus: LLM post-training; efficient model architectures and optimization; spiking language models; verifiable reasoning; long-horizon agents; embodied AI.
- Methods: supervised fine-tuning, on-policy distillation, reinforcement learning, model compression, and efficiency optimization.
- Technical stack: Python, PyTorch, Linux, Git, and LaTeX.
- Languages: Mandarin native; English fluent.
- Remove the NTU/NUS PhD plan, NTU summer-program note, Dreamer/RSSM emphasis, and other unsupported or outdated claims.

### Footer and README

- Keep the current email, phone number, quote, and 2026 copyright.
- Rewrite `README.md` as valid UTF-8 with a short English project description, live URL, and local file overview.
- Fix the corrupted CSS list marker and all mojibake in tracked text files.

## Files and Data Flow

- `index.html`: authoritative page content and metadata.
- `styles.css`: minimal additions for the CV button and any content-density adjustments; repair the corrupted list marker.
- `script.js`: retain current interactions unless a small accessibility or null-safety fix is required.
- `assets/Enqiao_Lu_CV.pdf`: copy of the approved English-first, Chinese-second CV.
- `README.md`: corrected repository documentation.

No server, API, database, or build pipeline is required.

## Responsive and Accessibility Requirements

- Preserve usable navigation at desktop, tablet, and mobile widths.
- The CV download must remain visible and tappable on mobile.
- All interactive controls need accessible labels and keyboard focus behavior.
- The profile image must retain meaningful alt text.
- Animations must not hide content when JavaScript is unavailable; reduced-motion preferences should be respected if a small CSS-only change is sufficient.

## Validation

- Confirm the site remains a static GitHub Pages build with no missing local assets.
- Check all internal navigation anchors and the CV download path.
- Search the repository for removed stale phrases: `3.88`, `Columbia`, `Ivor Tsang`, `NeurIPS 2026`, `NTU`, and `NUS`.
- Confirm the current phrases exist: `3.9/4.0`, `Xingrui Yu`, `SpikeOPD`, `LOGIV`, `AAAI 2027`, `CN 121982334 B`, and `Guangdong Provincial First Prize`.
- Inspect desktop and mobile renders for overflow, broken cards, unreadable text, and navigation issues.
- Verify there are no replacement characters or mojibake in HTML, CSS, JavaScript, or README files.

## Deployment

After local validation, commit the content refresh and push the `main` branch to the existing GitHub Pages repository. Confirm the published site loads the new content and CV asset.

## Non-goals

- No bilingual page toggle.
- No visual rebrand or framework migration.
- No analytics, contact form, CMS, blog, or new social integrations.
- No publication claims beyond the approved CV.

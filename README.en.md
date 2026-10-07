<p align="right"><a href="README.md">한국어</a> · <strong>English</strong></p>

![Pablo — From context to design](assets/banner.svg)

# Pablo

**Understands the context. Finishes the design.**

Share your material and ask in one sentence. Pablo identifies the purpose and audience, chooses a design direction, creates the deliverable, and checks the result. It is an agent skill for investor decks, UI mockups, system diagrams, presentation improvements, and brand adaptation.

```text
Pablo, turn this material into a 10-slide investor deck.
Pablo, create a UI mockup from this screen.
Pablo, visualize this system architecture.
Pablo, review this presentation's design and improve it.
Pablo, redesign this using our company brand.
```

[Interactive demo](demos/pablo-demo.html) · [Local setup](#local-setup) · [Skill instructions](SKILL.md)

![Pablo interactive demo](assets/pablo-demo.png)

The demo contains **illustrative examples** of five request types. It does not call an AI service or generate real files. Download and open `demos/pablo-demo.html` in a browser; no account or external library is required. Switch between Korean and English inside the demo.

## Deliverables

| Request | Default result |
|---|---|
| Investor deck | Requested slide count, editable PPTX, and PDF preview |
| UI mockup | HTML/CSS or React source and preview |
| System architecture | Mermaid or SVG source and rendered diagram |
| Presentation review and editing | Slide-level findings, revised PPTX, and preview |
| Brand adaptation | Revised original-format artifact and brand application summary |

Combine requests, such as a 10-slide deck using your company brand, or continue with “Change only slide 3.” Pablo preserves explicit formats, templates, counts, and source facts.

## Workflow

1. **Read the context** — identify the material, purpose, and audience from attachments, selected files, and the conversation.
2. **Choose the structure and direction** — match the visual approach to the message. Wait for a design selection only when requested.
3. **Create and revise** — preserve originals. A request to review and edit includes an actual revised deliverable.
4. **Verify and deliver** — inspect the final files, content, page counts, and rendered output, and report limitations.

Pablo asks only for missing material or consequential ambiguities. It does not invent business metrics or system components to fill gaps.

## Local setup

With Node.js and Python 3 available:

```bash
git clone https://github.com/grooshbene/pablo-design.git
cd pablo-design
./pablo setup
./pablo doctor
```

Setup installs Node dependencies, a Python virtual environment, Chromium, and a Korean font inside the project. It downloads packages and a checksum-verified font from their sources; it does not upload your documents.

| Capability | Additional requirement |
|---|---|
| Existing HTML→PPTX exporter on macOS | Google Chrome |
| PPTX→PDF/image rendering | LibreOffice's `soffice` executable |
| Video processing | FFmpeg / FFprobe |
| Optional cloud TTS/video review | Provider credentials and explicit transmission consent |

If LibreOffice is not discovered automatically, specify its executable:

```bash
export PABLO_SOFFICE="/Applications/LibreOffice.app/Contents/MacOS/soffice"
```

Open this repository in your agent and make a Pablo request with your material. `AGENTS.md` connects requests to the skill. The terminal command `./pablo` handles setup, conversion, and verification; it is not a standalone natural-language AI service.

### Install as a skill

For agents with skill support:

```bash
npx skills add grooshbene/pablo-design
```

The skill is named `pablo`. Verify that the installed folder includes `SKILL.md`, `references/`, `assets/`, `scripts/`, `pablo`, and the dependency files. Run `./pablo setup` from that folder. Installing the skill and installing its local production dependencies are separate steps.

## Check the environment

```bash
./pablo smoke
```

This creates a two-slide Korean test deck and checks PPTX/PDF export, PPTX rendering, a text-preserving formatting edit, and rejection of partial conversion failures. Results are stored in `outputs/pablo-smoke-*/`. Visual quality still requires inspection of the final images.

To convert your own HTML slides:

```bash
./pablo export-deck --slides ./my-slides --out ./outputs/my-deck --expected-slides 10
./pablo inspect-pptx ./outputs/my-deck/deck.pptx
./pablo render-pptx ./outputs/my-deck/deck.pptx --out ./outputs/my-deck-rendered
```

Use sortable filenames such as `01.html`, with only slide HTML files in the input directory. The existing HTML→PPTX constraints apply. Conversion errors, count mismatches, or text mismatches prevent publication of the output. Existing output directories are not overwritten.

## Scope and output policy

- Output defaults to `outputs/<task-name>/` unless a destination is specified.
- Client deliverables receive **no promotional Pablo or upstream-tool watermark by default**. If a creator credit is requested, use `Made with Pablo`.
- Complex PPTX charts, animations, and masters may not survive every editing tool. Preserve originals and verify the features the task requires.
- LibreOffice may render differently from PowerPoint or Keynote. A PDF exported from HTML does not verify the final PPTX's appearance.
- `.venv/`, `.pablo/`, `node_modules/`, and `outputs/` are excluded from Git.
- An agent executes the workflow. This repository does not provide a standalone chat web service or production backend.

## Attribution and license

Pablo builds on Huashu Design's design resources and production tools. Original copyright notices and the MIT license are retained; product branding does not replace attribution. [Attribution](ATTRIBUTION.md) · [LICENSE](LICENSE) · [Data-flow statement](SECURITY.md)

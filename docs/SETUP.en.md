# Pablo setup and local tools

Start with the [README](../README.en.md). This guide covers prerequisites, diagnostics, and direct conversion commands.

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

# Pablo

### You have the material. Let’s make it presentable.

An investor presentation, a system your team needs to understand, a product screen that only exists in your notes.
**Give Pablo the material and tell it what you want to make.** Pablo is an agent skill that helps organize, design, and turn it into a deliverable you can keep editing.

```text
Pablo, turn this material into a 10-slide investor deck.
```

Use it with **an agent that can read files and carry out work**, such as Codex. Ask in ordinary language, without operating a design tool yourself or composing a long prompt for every task.

[한국어](README.md) · [Use cases](#give-pablo-the-work-in-front-of-you) · [Get started](#get-started) · [Setup help](docs/SETUP.en.md)

![Pablo demo showing a request and its illustrative design direction](assets/pablo-demo.png)

<sub>This is an illustrative workflow demo, not a live AI session. Download the <a href="demos/pablo-demo.html">HTML demo</a>, open it in your browser, and switch to English to explore all five request types.</sub>

---

## Give Pablo the work in front of you

### Turn scattered documents into a story you can present

Attach your company overview and source metrics.

> Pablo, turn this into a 10-slide investor deck. Help investors understand the product and the evidence behind its growth.

Pablo develops a message for each slide and creates an **editable PPTX with a PDF preview**. It keeps the requested slide count and does not invent revenue or market-size figures missing from your material.

### Make a screen easier to see, discuss, and try

Share a screenshot or describe the screen.

> Pablo, create a UI mockup from this screen. Keep the structure, but make the main action easier to find.

Pablo refines the hierarchy and layout into a **browser-viewable mockup with source files**. Relevant clicks and input states can be implemented and checked as demo interactions.

### Make a complex system easier to explain

Point to the design document or relevant project files.

> Pablo, visualize this system architecture. Separate the data flows between services from external integrations.

Pablo maps the components and connections into an **editable diagram**, distinguishing verified structure from assumptions.

### Improve a presentation without starting over

Attach the existing presentation.

> Pablo, review this deck and improve its design. Keep the content, but fix the type sizes, alignment, and visual flow.

You get slide-level findings **and an actual revised file**. If you only want feedback, ask for a review. The original is preserved.

### Bring different designs into your company’s brand

Share the existing design along with your logo, brand guidelines, or template.

> Pablo, redesign this using our company brand. Apply the colors and typography from the attached guide.

Pablo aligns typography, spacing, imagery, and chart styling—not just the color palette. You receive a **new version that keeps the content and applies your brand**.

---

## Get started

### 1. Prepare your workspace once

With your agent, **Node.js, Python 3, and Git** ready, run this in a terminal:

```bash
git clone https://github.com/GrooshBene/pablo-design.git
cd pablo-design
./pablo setup
```

This installs the production and verification tools inside the project. It does not install Node.js or Python themselves. **PPTX work needs additional tools:** Chrome for the existing HTML→PPTX exporter on macOS, and LibreOffice for rendering PPTX previews. [Prerequisites and diagnostics →](docs/SETUP.en.md)

<details>
<summary>Already using agent skills?</summary>

```bash
npx skills add GrooshBene/pablo-design
```

The skill is named `pablo`. Run `./pablo setup` inside the installed Pablo folder as well. Skill installation gives your agent the workflow; local setup prepares the tools that produce the files. [Installation details →](docs/SETUP.en.md#install-as-a-skill)

</details>

### 2. Open the project in your agent and share the material

Open the downloaded **`pablo-design` folder as your agent’s working project**. Its project instructions connect Pablo requests to the workflow. To use Pablo in other projects, use the skill installation option above.

Attach documents, presentations, or screenshots, or provide their file paths. When you say “this material,” make sure the agent has the material you mean.

### 3. Ask for the result you want

> Pablo, turn the attached company overview into a 10-slide investor deck.

If the design direction is still open, Pablo first shows **three distinct visual demos**. It creates them in parallel when the agent supports it, or sequentially otherwise. These are representative samples—such as key slides or the main screen—rather than three complete deliverables.

**Choosing a demo sets a starting point, not final approval.** Pablo briefly checks what you want to refine, such as information density, color, or motion, and applies your feedback. You can say “B’s layout with C’s colors” or “Proceed as is.” It reuses requirements you have already provided.

A concrete template or a targeted edit to an existing result can proceed directly. To delegate both the choice and refinement decisions, say **“Choose the direction and finish without asking design questions.”** Missing source material or consequential factual ambiguities still need clarification.

**Type the request in your agent’s chat, not in the terminal.**

---

## Keep refining it in the same conversation

Look at the result and ask for the changes you want.

```text
Change only slide 3. Make the title larger and shorten the body copy.

Make this mockup open a detail view when the button is clicked.

Show where the external payment service connects in this diagram.

Keep this design, but apply our company’s brand colors.
```

You don’t need design vocabulary. **Who will see it, and what should stand out?** Those details help Pablo choose a direction. Follow-up edits continue from the current artifact and established design.

## What do you receive?

Pablo returns file links, the main changes, and what it verified. Files go to `outputs/<task-name>/` unless you specify another location.

- **Originals are preserved.** Revisions are saved as new versions.
- **No promotional watermark by default.** Company and client materials are not automatically stamped with the tool’s name.
- **Unverified details are called out.** Complex PPTX charts, animations, and masters may not survive every editing tool.

Pablo combines agent instructions with local tools. Results depend on the source material and available tools. Check important presentations in the app you will use to present them.

---

## Learn more

| I want to… | Read |
|---|---|
| Install Pablo or check my environment | [Setup and diagnostics](docs/SETUP.en.md) |
| Run conversion and verification commands directly | [Local tools](docs/SETUP.en.md#check-the-environment) |
| Understand how Pablo decides what to do | [Workflow instructions](SKILL.md) |
| Understand external data transmission | [Data-flow statement](SECURITY.md) |

## Attribution and license

Pablo extends Huashu Design’s production tools and design resources. Original copyright notices are retained. [Attribution](ATTRIBUTION.md) · [MIT License](LICENSE)

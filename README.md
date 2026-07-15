# Design Paper Figures

An Agent Skill for planning, drawing, reviewing, and refining publication-quality figures for research papers.

It packages the visual principles, figure-specific workflows, reusable color combinations, editable templates, and plotting utilities developed through a collection of carefully reviewed academic figures. The Skill is designed for coding agents such as Codex and Claude Code.

Created and maintained by **Dai Jun**.

## What it covers

- statistical plots and tables;
- algorithm pipelines and method overviews;
- neural-network modules and architecture diagrams;
- teaser and first-page figures;
- qualitative result displays and baseline comparisons;
- a curated academic Color Bank with compatible palette combinations.

The Skill emphasizes compact but readable layouts, coherent typography, complete and intentional borders, disciplined use of grids and transparency, editable vector output, and scientifically fair comparisons.

## Install

Clone this repository and unpack the portable Skill archive:

```bash
git clone https://github.com/daijun10086/design-paper-figures.git
cd design-paper-figures
unzip design-paper-figures.zip
```

### Codex

Install it as a personal Skill:

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME/skills"
cp -R design-paper-figures "$CODEX_HOME/skills/"
```

### Claude Code

Install it as a personal Skill:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R design-paper-figures "$HOME/.claude/skills/"
```

For project-only use, copy the extracted directory to `.claude/skills/design-paper-figures/` inside that project.

## Use

Ask the agent to use the Skill while describing the scientific message, target figure type, paper width, available data or image assets, and preferred output format.

Example prompts:

```text
Use design-paper-figures to draw a double-column statistical figure from these CSV files.
Return the Python source, editable SVG/PDF, and a PNG preview.
```

```text
Use design-paper-figures to read this method description and propose an editable
pipeline storyboard. Leave explicit placeholders for intermediate results I still
need to provide.
```

```text
Use design-paper-figures to plan a teaser that combines the core intuition with
three representative results. Start with an editable layout draft, not a fake final.
```

Codex can also be prompted explicitly with `$design-paper-figures`. In Claude Code, the Skill can be invoked with `/design-paper-figures` or selected automatically when the request matches its description.

## Expected behavior

- Statistical figures can be delivered as final figures when complete data are provided.
- Pipelines, architectures, teasers, and result layouts remain editable drafts until the required scientific assets and decisions are available.
- Model outputs, ground truth, measurements, intermediate results, and tensor shapes are never fabricated to fill empty space.
- Diagram sources use editable SVG groups; PNG files are previews rather than the only deliverable.
- Preferred colors are chosen from coherent combinations in the bundled Color Bank.

## Repository contents

- `design-paper-figures.zip`: portable Skill package;
- `graphics-color-library.yaml`: collected color definitions and combinations;
- `paper-aesthetic-observations.md`: distilled figure-design observations;
- `output/`: palettes and visual tests produced while developing the Skill;
- `reference papers/`: reference source material used during the aesthetic study;
- `dist/`: distributable archive copy.

## Notes

The Skill assists with scientific communication and figure construction. Authors remain responsible for checking the correctness of data, labels, comparisons, citations, and claims before publication.

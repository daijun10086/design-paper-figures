# AnyRecon Pipeline draft handoff

## Structure represented

`Captured view bank -> initial point-map reconstruction -> 3D Geometry Memory -> geometry-aware retrieval and geometry rendering -> selected views + rendered priors + visibility masks -> unordered contextual video diffusion -> generated novel-view segment -> geometry update -> shared memory for the next segment.`

The main story is left-to-right. A green feedback route remains inside the common height envelope to express the iterative generation-reconstruction loop. Dashed blue paths encode retrieval and geometric conditioning; solid gray paths encode the main data flow.

## Editable groups

- `placeholder-captured-view-bank`
- `result-geometry-memory`
- `selected-views`
- `rendered-prior-mask`
- `module-video-diffusion`
- `result-generated-segment`
- `module-geometry-update`
- `primary-flow`, `conditioning-flow`, and `geometry-feedback-loop`

## Assets needed for a publication-ready version

1. Three to five representative unordered capture images.
2. Camera/trajectory visualization, if it supports the intended narrative.
3. Initial or current point-cloud/geometry-memory rendering.
4. Geometry-rendered RGB prior and visibility/index mask for one target segment.
5. The selected captured views returned by geometry-aware retrieval.
6. A generated novel-view segment with matched trajectory ordering.
7. Optional before/after geometry update visualization.
8. Confirmation of whether VGGT, pi3, or both should be named in the final figure.

The current SVG is intentionally a storyboard, not a claim that these placeholders are real model outputs.


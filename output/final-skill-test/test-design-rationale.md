# Final holdout test design

## Test protocol

- Freeze the `design-paper-figures` Skill before producing the three test figures.
- Generate the statistical data independently and mark it as synthetic.
- Understand `Testing-paper.pdf` from extracted text rather than imitating the visual layout of its original figures.
- Use only previously curated Color Bank combinations and shared neutrals.
- Keep Pipeline and Teaser outputs explicitly editable drafts because separate original intermediate/result assets were not supplied.

## Paper facts used

Title: *AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model*.

One-sentence claim: arbitrary and unordered sparse captures can be converted into scalable, long-trajectory 3D reconstruction by coupling a geometry-conditioned video diffusion model with an incrementally updated 3D Geometry Memory.

Pipeline facts extracted from the paper:

1. Build a captured-view bank from arbitrary sparse RGB inputs.
2. Estimate an initial point-cloud geometry memory with a feed-forward reconstruction model such as VGGT or pi3.
3. Split a user-specified novel trajectory into efficient segments.
4. Use geometry-driven visibility/contribution to retrieve relevant captured views for the current segment.
5. Render the current geometry into target viewpoints to produce point-cloud renderings and visibility masks.
6. Prepend selected views as a persistent global scene memory and use frame-wise non-compressive latent encoding.
7. Generate a novel-view segment with context-window sparse attention and four-step diffusion sampling.
8. Reconstruct geometry from the generated segment and update the shared 3D Geometry Memory before processing the next segment.

Verified result facts allowed in the Teaser draft:

- interpolation, extrapolation, and large-scene reconstruction are demonstrated;
- the paper reports trajectories exceeding 200 generated frames;
- the DL3DV interpolation result reports 20.95 PSNR and 105 seconds for a 40-frame sequence;
- sparse attention plus four-step distillation is reported as approximately 20 times faster than the original dense baseline in the ablation.

## Missing assets deliberately left as placeholders

- representative arbitrary input captures and camera visualization;
- point-cloud/geometry-memory rendering;
- rendered prior and visibility mask;
- generated intermediate trajectory segment;
- final interpolation, extrapolation, and large-scene result frames.

## Final validation

- The statistical figure is reproducible from the included Python source and two synthetic CSV files.
- Statistical PDF, Pipeline SVG, and Teaser SVG all pass syntax/render checks.
- Every explicit Hex color in the three SVG sources is present in the frozen 91-color Color Bank.
- Pipeline and Teaser drafts use named SVG groups and replaceable image slots; their PNG/PDF files are previews, while SVG is the editing source of truth.
- The root-level portable Skill archive passes `unzip -t` and matches the archive in `dist/` byte for byte.

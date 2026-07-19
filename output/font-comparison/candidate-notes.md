# Statistical-plot font candidates

This is a controlled font-only comparison. Every plot uses the same synthetic
data, preferred P1 colors, dimensions, axes, manual ticks, frame, grid, line
weights, markers, legend placement, and annotations.

| Panel | Font | Why it is included |
|---|---|---|
| A | Arial | Current packaged Skill baseline. Neutral and widely available, but visually ordinary. |
| B | DejaVu Sans | The effective default sans-serif font in Matplotlib and therefore the usual Seaborn default when no font is explicitly set. Highly portable. |
| C | Optima | User-preferred humanist sans with flared strokes and an editorial/Graphics feel. |
| D | Helvetica Neue | Crisp neutral editorial sans; cleaner and more refined than Arial on macOS. |
| E | Avenir | Balanced humanist-geometric construction with strong numeral and label clarity. Avenir is used instead of Avenir Next because this Matplotlib installation resolves the latter only as a bold face. |
| F | Gill Sans | Distinctive humanist sans with more personality; useful for testing whether the plot can tolerate a less neutral voice. |
| G | Futura | Strong geometric display style; included as an upper-bound test for stylization, although small tick labels may be less comfortable. |

The macOS fonts in panels C–G cannot be redistributed with the Skill without
checking their licenses. If one of them is selected, the portable Skill should
specify the preferred family plus an open, embeddable server fallback rather
than packaging Apple font files.

Individual candidate PDFs are intentionally excluded from the public test
artifacts because this Matplotlib version embeds complete macOS font programs.
The PNG previews are rasterized, the SVG files retain editable live text and
only reference family names, and the comparison-board PDF contains no font
objects because it is generated from the raster overview.

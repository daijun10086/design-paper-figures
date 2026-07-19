# Portable server font candidates

This package contains redistributable, open-source font candidates for Linux
servers. It intentionally does **not** contain Optima, Futura, Gill Sans,
Helvetica Neue, Avenir, or Arial font files from macOS.

## Role mapping

| Local preference | Portable candidate | Relationship |
|---|---|---|
| Optima | Belleza | Humanist, higher-contrast, editorial direction; not a clone. |
| Futura | Jost | Geometric direction inspired by 1920s German sans-serifs. |
| Gill Sans | Cabin | Humanist direction influenced by Johnston and Gill. |
| Helvetica Neue | Source Sans 3 | Quiet, highly readable neutral sans-serif. |
| Avenir | Lato | Modern humanist direction with stable static weights. |
| Arial | Arimo | OFL font designed for Arial-compatible metrics. |

Belleza, Jost, Cabin, Lato, and Arimo come from the official `google/fonts`
repository at commit `389b770410cc0b7c21c85673bfa2077420fe7f65`.
Source Sans 3 Regular/Bold/Italic/Bold Italic come from Adobe's official
`3.052R` TTF release. Each family directory retains its `OFL.txt`, metadata,
and description file.

These are stylistic alternatives, not identical replacements. Review the
rendered statistical comparison before changing the Skill's preferred server
mapping.

## Install without root access

On a typical Linux server:

```bash
python3 install_fonts.py
```

The script copies the fonts to
`~/.local/share/fonts/design-paper-figures`, refreshes Fontconfig when
`fc-cache` is available, and verifies the Matplotlib family names. Restart any
long-running Python process after installation so it does not reuse an old font
cache.

To install somewhere else:

```bash
python3 install_fonts.py --target /path/to/fonts
```

To use the fonts without installing them system-wide:

```python
from pathlib import Path
from register_matplotlib_fonts import register_fonts

families = register_fonts(Path("/path/to/server-fonts/families"))
print(families)
```

Call `register_fonts(...)` before setting `matplotlib.rcParams["font.family"]`.

## Licensing

The font files are distributed under the SIL Open Font License 1.1. The
authoritative license for each family is the `OFL.txt` stored beside its font
files. Do not replace these files with proprietary macOS fonts before
publishing or sharing the package.

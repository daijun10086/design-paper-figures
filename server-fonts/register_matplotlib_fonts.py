#!/usr/bin/env python3
"""Register the bundled server fonts with Matplotlib for the current process."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_FONT_DIR = ROOT / "families"


def register_fonts(font_dir: Path = DEFAULT_FONT_DIR) -> dict:
    """Register all TTF files below ``font_dir`` and return family-to-files."""
    from matplotlib import font_manager

    font_dir = Path(font_dir).expanduser().resolve()
    if not font_dir.is_dir():
        raise FileNotFoundError(f"Font directory does not exist: {font_dir}")

    registered = {}
    for path in sorted(font_dir.rglob("*.ttf")):
        font_manager.fontManager.addfont(str(path))
        family = font_manager.FontProperties(fname=str(path)).get_name()
        registered.setdefault(family, []).append(str(path))
    if not registered:
        raise RuntimeError(f"No TTF fonts found below {font_dir}")
    return registered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("font_dir", nargs="?", type=Path, default=DEFAULT_FONT_DIR)
    args = parser.parse_args()
    print(json.dumps(register_fonts(args.font_dir), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

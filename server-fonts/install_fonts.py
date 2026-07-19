#!/usr/bin/env python3
"""Install bundled open fonts into a user-owned font directory."""

from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
from pathlib import Path

from register_matplotlib_fonts import register_fonts


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "families"


def default_target() -> Path:
    system = platform.system()
    if system == "Darwin":
        return Path.home() / "Library" / "Fonts" / "design-paper-figures"
    if system == "Windows":
        local = os.environ.get("LOCALAPPDATA")
        if not local:
            raise RuntimeError("LOCALAPPDATA is not set; pass --target explicitly")
        return Path(local) / "Microsoft" / "Windows" / "Fonts" / "design-paper-figures"
    data_home = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    return data_home / "fonts" / "design-paper-figures"


def install(target: Path) -> list:
    target = target.expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    installed = []
    for source in sorted(SOURCE_DIR.rglob("*.ttf")):
        destination = target / source.name
        shutil.copy2(source, destination)
        installed.append(destination)
    if not installed:
        raise RuntimeError(f"No TTF fonts found below {SOURCE_DIR}")
    return installed


def refresh_fontconfig(target: Path) -> None:
    executable = shutil.which("fc-cache")
    if executable:
        cache_home = target / ".cache"
        cache_home.mkdir(parents=True, exist_ok=True)
        environment = dict(os.environ)
        environment["XDG_CACHE_HOME"] = str(cache_home)
        completed = subprocess.run(
            [executable, "-f", str(target)],
            check=False,
            env=environment,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            print("Warning: fc-cache could not refresh its cache; Matplotlib direct registration will still work.")
            if completed.stderr.strip():
                print(completed.stderr.strip())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=default_target())
    parser.add_argument("--skip-fc-cache", action="store_true")
    args = parser.parse_args()

    installed = install(args.target)
    if not args.skip_fc_cache:
        refresh_fontconfig(args.target)
    registered = register_fonts(args.target)

    print(f"Installed {len(installed)} font files in {args.target.expanduser().resolve()}")
    print("Matplotlib family names:")
    for family in sorted(registered):
        print(f"  - {family}")
    print("Restart long-running Python processes before rendering figures.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

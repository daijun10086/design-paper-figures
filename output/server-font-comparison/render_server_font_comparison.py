#!/usr/bin/env python3
"""Render a controlled comparison of portable server font candidates."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
FONT_PACK = ROOT / "server-fonts"
sys.path.insert(0, str(FONT_PACK))
from register_matplotlib_fonts import register_fonts  # noqa: E402


DATA_PATH = ROOT / "output" / "font-comparison" / "synthetic_font_test_data.csv"

CANDIDATES = [
    ("A", "Belleza", "Optima direction"),
    ("B", "Jost", "Futura direction"),
    ("C", "Cabin", "Gill Sans direction"),
    ("D", "Source Sans 3", "Helvetica Neue direction"),
    ("E", "Lato", "Avenir direction"),
    ("F", "Arimo", "Arial-compatible fallback"),
]

METHOD_STYLE = {
    "Baseline A": {"color": "#F5A83D", "marker": "o"},
    "Baseline B": {"color": "#88B06D", "marker": "s"},
    "Large model": {"color": "#7A5DE1", "marker": "^"},
    "Ours": {"color": "#5D8DFD", "marker": "D"},
}


def load_data():
    grouped = {name: [] for name in METHOD_STYLE}
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            grouped[row["method"]].append(
                tuple(float(row[key]) for key in ("compute_gflops", "fid", "lower", "upper"))
            )
    return grouped


def render_candidate(letter, family, role, data):
    rc = {
        "font.family": family,
        "font.size": 8.0,
        "axes.titlesize": 9.2,
        "axes.titleweight": "regular",
        "axes.labelsize": 8.0,
        "axes.labelweight": "regular",
        "axes.linewidth": 0.8,
        "axes.edgecolor": "#000000",
        "axes.unicode_minus": False,
        "xtick.labelsize": 7.0,
        "ytick.labelsize": 7.0,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
        "xtick.major.size": 3.2,
        "ytick.major.size": 3.2,
        "legend.fontsize": 6.3,
        "lines.linewidth": 1.55,
        "lines.markersize": 3.8,
        "svg.fonttype": "none",
        "savefig.facecolor": "white",
    }

    with mpl.rc_context(rc):
        fig = plt.figure(figsize=(3.45, 2.55), facecolor="white")
        ax = fig.add_axes([0.165, 0.185, 0.805, 0.695])

        for method, style in METHOD_STYLE.items():
            rows = data[method]
            x = [row[0] for row in rows]
            y = [row[1] for row in rows]
            low = [row[2] for row in rows]
            high = [row[3] for row in rows]
            is_ours = method == "Ours"
            ax.fill_between(x, low, high, color=style["color"], alpha=0.10, linewidth=0)
            ax.plot(
                x,
                y,
                color=style["color"],
                marker=style["marker"],
                markeredgecolor="white",
                markeredgewidth=0.45,
                linewidth=2.0 if is_ours else 1.45,
                label=method,
                zorder=4 if is_ours else 3,
            )

        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_xlim(7.2, 285)
        ax.set_ylim(2.0, 22.0)
        ax.set_xticks([8, 16, 32, 64, 128, 256])
        ax.set_xticklabels(["8", "16", "32", "64", "128", "256"])
        ax.set_yticks([2, 3, 5, 10, 20])
        ax.set_yticklabels(["2", "3", "5", "10", "20"])
        ax.minorticks_off()

        ax.set_axisbelow(True)
        ax.grid(True, which="major", color="#D3D3D3", linewidth=0.5)
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("#000000")
            spine.set_linewidth(0.8)
        ax.tick_params(colors="#202124", width=0.8)

        ax.set_xlabel("Compute budget (GFLOPs)")
        ax.set_ylabel("Validation FID")
        ax.set_title(f"{letter} · {family}", loc="left", pad=5.5)
        ax.text(
            0.985,
            0.955,
            role,
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=5.8,
            color="#666666",
        )
        ax.legend(
            loc="upper right",
            bbox_to_anchor=(1.0, 0.88),
            ncol=2,
            frameon=False,
            handlelength=1.4,
            handletextpad=0.35,
            columnspacing=0.7,
            borderaxespad=0.0,
        )

        stem = Path(__file__).resolve().parent / f"{letter.lower()}-{family.lower().replace(' ', '-')}"
        fig.savefig(stem.with_suffix(".png"), dpi=300)
        fig.savefig(stem.with_suffix(".svg"))
        plt.close(fig)
        return stem.with_suffix(".png")


def make_board(image_paths):
    images = [Image.open(path).convert("RGB") for path in image_paths]
    tile_w, tile_h = images[0].size
    columns = 2
    rows = 3
    margin_x = 44
    gap_x = 32
    gap_y = 30
    header_h = 112
    footer_h = 72
    width = margin_x * 2 + columns * tile_w + gap_x
    height = header_h + rows * tile_h + (rows - 1) * gap_y + footer_h
    board = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(board)

    header_font_path = FONT_PACK / "families" / "source-sans-3" / "SourceSans3-Regular.ttf"
    title_font = ImageFont.truetype(str(header_font_path), 34)
    note_font = ImageFont.truetype(str(header_font_path), 22)
    draw.text((margin_x, 24), "Portable server-font comparison", fill="#202124", font=title_font)
    draw.text(
        (margin_x, 68),
        "Identical data and styling; six redistributable OFL font families loaded directly from this package.",
        fill="#666666",
        font=note_font,
    )

    for index, image in enumerate(images):
        row, col = divmod(index, columns)
        x = margin_x + col * (tile_w + gap_x)
        y = header_h + row * (tile_h + gap_y)
        board.paste(image, (x, y))

    draw.text(
        (margin_x, height - footer_h + 18),
        "These are stylistic directions, not exact clones. Review at final paper size before updating the Skill mapping.",
        fill="#666666",
        font=note_font,
    )
    board_path = Path(__file__).resolve().parent / "server-font-comparison-board.png"
    board.save(board_path, dpi=(150, 150))
    board.save(Path(__file__).resolve().parent / "server-font-comparison-board.pdf", "PDF", resolution=150.0)


def main():
    registered = register_fonts(FONT_PACK / "families")
    missing = [family for _, family, _ in CANDIDATES if family not in registered]
    if missing:
        raise RuntimeError(f"Bundled fonts did not register correctly: {missing}")
    data = load_data()
    paths = [render_candidate(*candidate, data) for candidate in CANDIDATES]
    make_board(paths)
    for family in sorted(registered):
        print(f"registered: {family}")
    for path in paths:
        print(path)
    print(Path(__file__).resolve().parent / "server-font-comparison-board.png")
    print(Path(__file__).resolve().parent / "server-font-comparison-board.pdf")


if __name__ == "__main__":
    main()

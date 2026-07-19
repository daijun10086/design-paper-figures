#!/usr/bin/env python3
"""Render a controlled paper-plot font comparison.

All panels use identical synthetic data, geometry, colors, line weights,
ticks, and annotations. Only the font family changes.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "synthetic_font_test_data.csv"

CANDIDATES = [
    ("A", "Arial", "Arial", "Current Skill baseline"),
    ("B", "Seaborn default", "DejaVu Sans", "Matplotlib/Seaborn default"),
    ("C", "Optima", "Optima", "User-preferred humanist sans"),
    ("D", "Helvetica Neue", "Helvetica Neue", "Neutral editorial sans"),
    ("E", "Avenir", "Avenir", "Humanist-geometric sans"),
    ("F", "Gill Sans", "Gill Sans", "Distinctive humanist sans"),
    ("G", "Futura", "Futura", "Geometric display sans"),
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


def available_families():
    return {entry.name for entry in font_manager.fontManager.ttflist}


def render_candidate(letter, display_name, family, note, data):
    if family not in available_families():
        raise RuntimeError(f"Required font is not available: {family}")

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
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
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
        ax.set_title(f"{letter} · {display_name}", loc="left", pad=5.5)
        ax.text(
            0.985,
            0.035,
            "Lower is better",
            transform=ax.transAxes,
            ha="right",
            va="bottom",
            fontsize=6.2,
            color="#666666",
        )
        ax.text(
            0.985,
            0.955,
            "synthetic benchmark",
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=6.0,
            color="#666666",
        )

        legend = ax.legend(
            loc="upper right",
            bbox_to_anchor=(1.0, 0.88),
            ncol=2,
            frameon=False,
            handlelength=1.4,
            handletextpad=0.35,
            columnspacing=0.7,
            borderaxespad=0.0,
        )
        stem = ROOT / f"{letter.lower()}-{family.lower().replace(' ', '-')}"
        fig.savefig(stem.with_suffix(".png"), dpi=300)
        fig.savefig(stem.with_suffix(".svg"))
        plt.close(fig)
        return stem.with_suffix(".png")


def make_board(image_paths):
    images = [Image.open(path).convert("RGB") for path in image_paths]
    tile_w, tile_h = images[0].size
    columns = 2
    rows = 4
    margin_x = 44
    gap_x = 32
    gap_y = 30
    header_h = 112
    footer_h = 72
    width = margin_x * 2 + columns * tile_w + gap_x
    height = header_h + rows * tile_h + (rows - 1) * gap_y + footer_h
    board = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(board)

    arial_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    arial_bold_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    title_font = ImageFont.truetype(arial_bold_path, 34)
    note_font = ImageFont.truetype(arial_path, 22)
    draw.text((margin_x, 24), "Statistical-plot font comparison", fill="#202124", font=title_font)
    draw.text(
        (margin_x, 68),
        "Identical data, geometry, palette, line weights, ticks, and annotations; font family only.",
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
        "Plots are rendered at a realistic 3.45 × 2.55 in single-column size; individual SVG files remain vector-editable.",
        fill="#666666",
        font=note_font,
    )
    board_path = ROOT / "font-comparison-board.png"
    board.save(board_path, dpi=(150, 150))
    board.save(ROOT / "font-comparison-board.pdf", "PDF", resolution=150.0)


def main():
    data = load_data()
    paths = [render_candidate(*candidate, data) for candidate in CANDIDATES]
    make_board(paths)
    for path in paths:
        print(path)
    print(ROOT / "font-comparison-board.png")
    print(ROOT / "font-comparison-board.pdf")


if __name__ == "__main__":
    main()

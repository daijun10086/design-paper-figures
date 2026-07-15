#!/usr/bin/env python3
"""Generate deterministic synthetic data and a publication-style test figure."""

from __future__ import annotations

import csv
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
SKILL_DIR = Path(
    os.environ.get(
        "PAPER_FIGURE_SKILL",
        Path.home() / ".codex" / "skills" / "design-paper-figures",
    )
)
sys.path.insert(0, str(SKILL_DIR / "scripts"))

from paper_plot_style import (  # noqa: E402
    add_zoomed_inset,
    export_figure,
    get_combination,
    style_axes,
    use_style,
)


METHODS = [
    {
        "name": "Image prior",
        "color_id": "baseline-gray-mid",
        "marker": "o",
        "floor": 2.60,
        "amplitude": 8.60,
        "power": 0.58,
        "latency": 43,
        "memory": 8.0,
    },
    {
        "name": "Geometry prior",
        "color_id": "soft-orange-deep",
        "marker": "s",
        "floor": 2.30,
        "amplitude": 8.20,
        "power": 0.60,
        "latency": 82,
        "memory": 12.0,
    },
    {
        "name": "Global memory",
        "color_id": "soft-grass-deep",
        "marker": "^",
        "floor": 2.05,
        "amplitude": 7.80,
        "power": 0.62,
        "latency": 116,
        "memory": 18.0,
    },
    {
        "name": "Proposed",
        "color_id": "soft-blue-deep",
        "marker": "D",
        "floor": 1.75,
        "amplitude": 7.40,
        "power": 0.64,
        "latency": 64,
        "memory": 14.0,
    },
]


def make_data() -> tuple[list[dict], list[dict]]:
    compute = np.array([0.5, 1, 2, 4, 8, 16], dtype=float)
    curves: list[dict] = []
    summary: list[dict] = []
    for method in METHODS:
        relative = compute / compute.min()
        mean = method["floor"] + method["amplitude"] * relative ** (-method["power"])
        mean += 0.035 * np.sin(np.log2(relative + 1) * 1.8)
        std = 0.52 * relative ** (-0.35) + 0.07
        for x, y, s in zip(compute, mean, std):
            curves.append(
                {
                    "method": method["name"],
                    "compute": float(x),
                    "error_mean": float(y),
                    "error_std": float(s),
                }
            )
        summary.append(
            {
                "method": method["name"],
                "latency_s": method["latency"],
                "memory_gb": method["memory"],
                "final_error": float(mean[-1]),
            }
        )
    return curves, summary


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    use_style()
    curves, summary = make_data()
    write_csv(HERE / "synthetic_scaling_data.csv", curves)
    write_csv(HERE / "synthetic_efficiency_summary.csv", summary)

    palette = get_combination("p1-soft-scientific-five-hue")
    colors = {item["id"]: item["hex"] for item in palette["colors"]}
    method_map = {item["name"]: item for item in METHODS}

    fig, (ax_curve, ax_eff) = plt.subplots(
        1,
        2,
        figsize=(7.0, 3.05),
        gridspec_kw={"width_ratios": [2.25, 1.0], "wspace": 0.30},
    )

    grouped: dict[str, list[dict]] = {}
    for row in curves:
        grouped.setdefault(row["method"], []).append(row)

    for method_name, rows in grouped.items():
        spec = method_map[method_name]
        x = np.array([row["compute"] for row in rows])
        y = np.array([row["error_mean"] for row in rows])
        s = np.array([row["error_std"] for row in rows])
        color = colors[spec["color_id"]]
        ax_curve.fill_between(x, y - s, y + s, color=color, alpha=0.12, linewidth=0)
        ax_curve.plot(
            x,
            y,
            color=color,
            marker=spec["marker"],
            markersize=4.6,
            label=method_name,
            linewidth=2.0 if method_name == "Proposed" else 1.6,
            zorder=3,
        )

    style_axes(ax_curve, grid=True)
    ax_curve.set_xscale("log", base=2)
    ax_curve.set_xlim(0.45, 18)
    ax_curve.set_ylim(1.6, 12.1)
    ticks = [0.5, 1, 2, 4, 8, 16]
    ax_curve.set_xticks(ticks)
    ax_curve.set_xticklabels(["0.5", "1", "2", "4", "8", "16"])
    ax_curve.set_xlabel("Training compute (relative units, log scale)")
    ax_curve.set_ylabel("Reconstruction error ↓")
    ax_curve.legend(loc="lower left", ncol=2, columnspacing=1.0, handletextpad=0.5)

    inset = add_zoomed_inset(
        ax_curve,
        bounds=(0.55, 0.50, 0.41, 0.42),
        xlim=(3.6, 17.0),
        ylim=(2.30, 5.55),
        connector_locs=(2, 4),
        locator_alpha=0.48,
    )
    inset.set_xscale("log", base=2)
    for method_name, rows in grouped.items():
        spec = method_map[method_name]
        x = np.array([row["compute"] for row in rows])
        y = np.array([row["error_mean"] for row in rows])
        inset.plot(
            x,
            y,
            color=colors[spec["color_id"]],
            marker=spec["marker"],
            markersize=3.2,
            linewidth=1.2,
        )
    inset.set_xticks([4, 8, 16])
    inset.set_xticklabels(["4", "8", "16"])
    inset.set_yticks([2.5, 3.5, 4.5, 5.5])
    inset.tick_params(labelsize=6)

    for row in summary:
        spec = method_map[row["method"]]
        color = colors[spec["color_id"]]
        ax_eff.scatter(
            row["latency_s"],
            row["final_error"],
            s=68,
            color=color,
            marker=spec["marker"],
            edgecolor="#FFFFFF",
            linewidth=0.8,
            zorder=3,
        )
        offsets = {
            "Image prior": (4, 0.10),
            "Geometry prior": (4, 0.08),
            "Global memory": (-4, 0.13),
            "Proposed": (4, 0.10),
        }
        dx, dy = offsets[row["method"]]
        ax_eff.text(
            row["latency_s"] + dx,
            row["final_error"] + dy,
            row["method"],
            ha="right" if dx < 0 else "left",
            va="center",
            fontsize=6.7,
            fontweight="bold" if row["method"] == "Proposed" else "normal",
            color="#000000",
        )
    style_axes(ax_eff, grid=True)
    ax_curve.tick_params(colors="#000000")
    inset.tick_params(colors="#000000")
    ax_eff.tick_params(colors="#000000")
    ax_eff.set_xlim(32, 135)
    ax_eff.set_ylim(2.25, 4.05)
    ax_eff.set_xlabel("Latency (s) ↓")
    ax_eff.set_ylabel("Final error ↓")
    ax_curve.text(-0.10, 1.04, "(a)", transform=ax_curve.transAxes, fontweight="bold")
    ax_eff.text(-0.24, 1.04, "(b)", transform=ax_eff.transAxes, fontweight="bold")

    outputs = export_figure(fig, HERE / "statistical-holdout-test")
    plt.close(fig)
    for path in outputs:
        print(path)


if __name__ == "__main__":
    main()

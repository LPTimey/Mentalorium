import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Patch

OUTPATH = "out/automation bias graph.png"

# Konstanten für die Darstellung
GRAPH1_NAME = "C(x): needed confidence for rating x"
GRAPH1_COLOR = "blue"
GRAPH1_fn = lambda x: np.where(np.abs(x - 1) <= 0.05, np.nan, 1 / (x - 1))

GRAPH2_NAME = "R(x): needed rating for confidence x"
GRAPH2_COLOR = "red"
GRAPH2_fn = lambda x: np.where(np.abs(x) <= 0.05, np.nan, (1 / x) + 1)
GRAPH2_fn_neg = lambda y: np.where(np.abs(y - 1) <= 0.05, np.nan, (1 / (y - 1)))

# Punkte auf Graph 1
GRAPH1_POINTS = [
    (2, GRAPH1_fn(2), "R_2"),
    (3, GRAPH1_fn(3), "R_3"),
    (4, GRAPH1_fn(4), "R_4"),
    (5, GRAPH1_fn(5), "R_5")
]

# Punkte auf Graph 2
GRAPH2_POINTS = [
    (GRAPH2_fn_neg(2), 2, "C_2"),
    (GRAPH2_fn_neg(3), 3, "C_3"),
    (GRAPH2_fn_neg(4), 4, "C_4"),
    (GRAPH2_fn_neg(5), 5, "C_5")
]

# Rechtecke
RECT1 = [0, 1, 1, 5, "solution space C"]
RECT2 = [1, 5, 0, 1, "solution space R"]

# Plot-Einstellungen
X_LIM = (0, 6)
Y_LIM = (0, 8)
GRID = True
FIG_SIZE = (10, 8)


def plot_graph_with_points(ax, x_vals, y_vals, name, color, points):
    ax.plot(x_vals, y_vals, label=name, color=color, linewidth=2)

    for x, y, point_name in points:
        ax.plot(x, y, 'o', color=color, markersize=8, zorder=5)
        ax.annotate(
            f"{point_name}\n({x:.2f}, {y:.2f})",
            (x, y),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7)
        )


def plot_rectangle(ax, rect, color='green', alpha=0.3, edgecolor='darkgreen'):
    x_min, x_max, y_min, y_max, name = rect

    rect_patch = plt.Rectangle(
        (x_min, y_min),
        x_max - x_min,
        y_max - y_min,
        linewidth=2,
        edgecolor=edgecolor,
        facecolor=color,
        alpha=alpha
    )
    ax.add_patch(rect_patch)

    return Patch(facecolor=color, edgecolor=edgecolor, alpha=alpha, label=name)


def main():
    x_range = np.linspace(X_LIM[0], X_LIM[1], 100)

    y1 = np.ma.masked_invalid(GRAPH1_fn(x_range))
    y2 = np.ma.masked_invalid(GRAPH2_fn(x_range))

    fig, ax = plt.subplots(figsize=FIG_SIZE)

    # --- Graphen + Handles speichern ---
    line1, = ax.plot(x_range, y1, label=GRAPH1_NAME, color=GRAPH1_COLOR, linewidth=2)
    line2, = ax.plot(x_range, y2, label=GRAPH2_NAME, color=GRAPH2_COLOR, linewidth=2)

    # Punkte zeichnen (wie gehabt)
    plot_graph_with_points(ax, x_range, y1, GRAPH1_NAME, GRAPH1_COLOR, GRAPH1_POINTS)
    plot_graph_with_points(ax, x_range, y2, GRAPH2_NAME, GRAPH2_COLOR, GRAPH2_POINTS)

    # Rechtecke
    rect_handles = []
    rect_handles.append(plot_rectangle(ax, RECT1, color='lightgreen', alpha=0.3, edgecolor='green'))
    rect_handles.append(plot_rectangle(ax, RECT2, color='lightblue', alpha=0.3, edgecolor='blue'))

    # --- SAUBERE LEGENDENLISTE ---
    handles = [line1, line2] + rect_handles

    ax.legend(handles=handles, loc='upper right', fontsize=10)

    ax.set_xlim(X_LIM)
    ax.set_ylim(Y_LIM)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Automation Bias: Confidence-Rating Relationship')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    os.makedirs("out", exist_ok=True)
    plt.savefig(OUTPATH, dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Generate logo and cover image for The Quantum Bottleneck."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as mpath
import numpy as np
from matplotlib.patches import FancyBboxPatch
from PIL import Image, ImageDraw

# ── Colour palette ──────────────────────────────────────────────
DARK   = '#0D1117'      # near-black background
TEAL   = '#00D4AA'      # primary quantum accent
BLUE   = '#4A90D9'      # secondary accent
PURPLE = '#9B59B6'      # tertiary
GOLD   = '#F0C040'      # highlight / bottleneck glow
WHITE  = '#E6EDF3'      # text
GREY   = '#8B949E'      # muted


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. LOGO — bottleneck + quantum motif
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def draw_logo(save_path='figures/logo.png', size=800):
    fig, ax = plt.subplots(1, 1, figsize=(size/100, size/100), dpi=100)
    fig.patch.set_facecolor(DARK)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # ── Bottleneck silhouette (hourglass) ──
    # Top funnel
    top_x = np.array([-0.55, -0.08, 0.08, 0.55])
    top_y = np.array([ 0.70,  0.08, 0.08, 0.70])
    verts_top = list(zip(top_x, top_y))

    # Bottom funnel
    bot_x = np.array([-0.55, -0.08, 0.08, 0.55])
    bot_y = np.array([-0.70, -0.08,-0.08,-0.70])
    verts_bot = list(zip(bot_x, bot_y))

    # Draw with smooth curves using Path
    from matplotlib.path import Path

    # Top funnel path (cubic bezier for smooth curves)
    top_verts = [
        (-0.55, 0.70),   # start top-left
        (-0.40, 0.35),   # control
        (-0.15, 0.12),   # control
        (-0.08, 0.06),   # neck left
        ( 0.08, 0.06),   # neck right
        ( 0.15, 0.12),   # control
        ( 0.40, 0.35),   # control
        ( 0.55, 0.70),   # end top-right
    ]
    top_codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
                 Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    top_path = Path(top_verts, top_codes)

    # Bottom funnel path
    bot_verts = [
        (-0.55, -0.70),
        (-0.40, -0.35),
        (-0.15, -0.12),
        (-0.08, -0.06),
        ( 0.08, -0.06),
        ( 0.15, -0.12),
        ( 0.40, -0.35),
        ( 0.55, -0.70),
    ]
    bot_codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
                 Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    bot_path = Path(bot_verts, bot_codes)

    ax.add_patch(patches.PathPatch(top_path, facecolor='none',
                                    edgecolor=TEAL, lw=3, alpha=0.9))
    ax.add_patch(patches.PathPatch(bot_path, facecolor='none',
                                    edgecolor=TEAL, lw=3, alpha=0.9))

    # ── Neck glow ──
    for r, a in [(0.12, 0.08), (0.09, 0.12), (0.06, 0.20)]:
        circle = plt.Circle((0, 0), r, color=GOLD, alpha=a)
        ax.add_patch(circle)

    # ── Scattered problem nodes (top half — classical chaos) ──
    rng = np.random.RandomState(42)
    n_top = 35
    for _ in range(n_top):
        x = rng.uniform(-0.50, 0.50)
        y = rng.uniform(0.12, 0.65)
        # Only draw if inside the funnel
        half_width_at_y = 0.08 + (0.55 - 0.08) * (y - 0.06) / (0.70 - 0.06)
        if abs(x) < half_width_at_y * 0.88:
            size_dot = rng.uniform(10, 60)
            color = rng.choice([BLUE, PURPLE, GREY, BLUE, PURPLE])
            ax.scatter(x, y, s=size_dot, color=color, alpha=0.5, zorder=3)

    # ── Thin "flow" lines through the neck ──
    for i in range(5):
        offset = (i - 2) * 0.015
        xs = [offset * 4, offset * 2, offset, offset, offset * 2, offset * 4]
        ys = [0.55, 0.30, 0.06, -0.06, -0.30, -0.55]
        ax.plot(xs, ys, color=TEAL, alpha=0.15, lw=1.2)

    # ── Ordered quantum nodes (bottom half — structured output) ──
    # Bloch-sphere-like circles
    positions_bot = [
        (0, -0.22),
        (-0.15, -0.38), (0.15, -0.38),
        (-0.25, -0.54), (0, -0.54), (0.25, -0.54),
    ]
    for (x, y) in positions_bot:
        half_width_at_y_b = 0.08 + (0.55 - 0.08) * (abs(y) - 0.06) / (0.70 - 0.06)
        if abs(x) < half_width_at_y_b * 0.80:
            circle = plt.Circle((x, y), 0.035, facecolor=DARK,
                                edgecolor=TEAL, lw=1.5, zorder=4)
            ax.add_patch(circle)
            # State arrow inside
            angle = rng.uniform(0, 2 * np.pi)
            dx = 0.022 * np.cos(angle)
            dy = 0.022 * np.sin(angle)
            ax.annotate('', xy=(x + dx, y + dy), xytext=(x, y),
                        arrowprops=dict(arrowstyle='->', color=GOLD,
                                        lw=1.2), zorder=5)

    # ── Connecting lines between bottom nodes ──
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 5)]
    for i, j in edges:
        x0, y0 = positions_bot[i]
        x1, y1 = positions_bot[j]
        ax.plot([x0, x1], [y0, y1], color=TEAL, alpha=0.25, lw=1, zorder=2)

    plt.savefig(save_path, dpi=200, bbox_inches='tight',
                facecolor=DARK, edgecolor='none', pad_inches=0.08)
    plt.close()
    print(f'Logo saved → {save_path}')


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. LOGO with text (horizontal lockup)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def draw_logo_with_text(save_path='figures/logo-text.png'):
    fig, ax = plt.subplots(1, 1, figsize=(12, 4), dpi=200)
    fig.patch.set_facecolor(DARK)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.8, 0.8)
    ax.set_aspect('equal')
    ax.axis('off')

    # ── Mini bottleneck icon (left side) ──
    from matplotlib.path import Path

    scale, cx = 0.7, 0.0
    top_verts = [
        (cx - 0.55*scale, 0.70*scale),
        (cx - 0.40*scale, 0.35*scale),
        (cx - 0.15*scale, 0.12*scale),
        (cx - 0.08*scale, 0.06*scale),
        (cx + 0.08*scale, 0.06*scale),
        (cx + 0.15*scale, 0.12*scale),
        (cx + 0.40*scale, 0.35*scale),
        (cx + 0.55*scale, 0.70*scale),
    ]
    top_codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
                 Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    bot_verts = [
        (cx - 0.55*scale, -0.70*scale),
        (cx - 0.40*scale, -0.35*scale),
        (cx - 0.15*scale, -0.12*scale),
        (cx - 0.08*scale, -0.06*scale),
        (cx + 0.08*scale, -0.06*scale),
        (cx + 0.15*scale, -0.12*scale),
        (cx + 0.40*scale, -0.35*scale),
        (cx + 0.55*scale, -0.70*scale),
    ]
    bot_codes = top_codes[:]
    ax.add_patch(patches.PathPatch(Path(top_verts, top_codes),
                 facecolor='none', edgecolor=TEAL, lw=2.5))
    ax.add_patch(patches.PathPatch(Path(bot_verts, bot_codes),
                 facecolor='none', edgecolor=TEAL, lw=2.5))

    for r, a in [(0.10, 0.08), (0.07, 0.14), (0.04, 0.25)]:
        ax.add_patch(plt.Circle((cx, 0), r*scale, color=GOLD, alpha=a))

    # ── Title text ──
    ax.text(0.65, 0.15, 'THE QUANTUM', fontsize=28, fontweight='bold',
            color=WHITE, fontfamily='sans-serif', va='bottom')
    ax.text(0.65, -0.12, 'BOTTLENECK', fontsize=28, fontweight='bold',
            color=TEAL, fontfamily='sans-serif', va='top')

    plt.savefig(save_path, dpi=200, bbox_inches='tight',
                facecolor=DARK, edgecolor='none', pad_inches=0.1)
    plt.close()
    print(f'Logo+text saved → {save_path}')


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. COVER IMAGE — the eight domains funnelling through quantum
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def draw_cover(save_path='figures/cover.png'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 14), dpi=200)
    fig.patch.set_facecolor(DARK)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-7, 7)
    ax.set_aspect('equal')
    ax.axis('off')

    # ── Large bottleneck outline ──
    from matplotlib.path import Path

    neck_w = 0.6
    top_w  = 4.0
    top_y  = 5.5
    neck_y = 0.4
    bot_y  = -5.5
    bot_w  = 4.0

    top_verts = [
        (-top_w, top_y),
        (-top_w*0.6, top_y*0.45),
        (-neck_w*1.5, neck_y*1.5),
        (-neck_w, neck_y),
        ( neck_w, neck_y),
        ( neck_w*1.5, neck_y*1.5),
        ( top_w*0.6, top_y*0.45),
        ( top_w, top_y),
    ]
    top_codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
                 Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]

    bot_verts = [
        (-bot_w, bot_y),
        (-bot_w*0.6, bot_y*0.45),
        (-neck_w*1.5, -neck_y*1.5),
        (-neck_w, -neck_y),
        ( neck_w, -neck_y),
        ( neck_w*1.5, -neck_y*1.5),
        ( bot_w*0.6, bot_y*0.45),
        ( bot_w, bot_y),
    ]
    bot_codes = top_codes[:]

    # Gradient-like layered fills
    for offset, alpha in [(0.3, 0.03), (0.2, 0.04), (0.1, 0.05)]:
        shifted_top = [(x*(1-offset), y*(1-offset)) for x, y in top_verts]
        shifted_bot = [(x*(1-offset), y*(1-offset)) for x, y in bot_verts]
        ax.add_patch(patches.PathPatch(Path(shifted_top, top_codes),
                     facecolor=TEAL, edgecolor='none', alpha=alpha))
        ax.add_patch(patches.PathPatch(Path(shifted_bot, bot_codes),
                     facecolor=TEAL, edgecolor='none', alpha=alpha))

    ax.add_patch(patches.PathPatch(Path(top_verts, top_codes),
                 facecolor='none', edgecolor=TEAL, lw=2.5, alpha=0.8))
    ax.add_patch(patches.PathPatch(Path(bot_verts, bot_codes),
                 facecolor='none', edgecolor=TEAL, lw=2.5, alpha=0.8))

    # ── Neck glow ──
    for r, a in [(1.2, 0.04), (0.8, 0.08), (0.5, 0.12), (0.3, 0.18)]:
        ax.add_patch(plt.Circle((0, 0), r, color=GOLD, alpha=a))

    # ── The eight problem domains (top half) ──
    domains = [
        ('Logistics',    'L',  -2.8,  4.5, BLUE),
        ('Cryptography', 'C',   0.0,  4.8, PURPLE),
        ('Drug Design',  'D',   2.8,  4.5, BLUE),
        ('ML',           'M',  -1.6,  2.2, PURPLE),
        ('Finance',      'F',   1.6,  2.2, PURPLE),
        ('Supply Chain', 'S',  -1.5,  3.6, BLUE),
        ('Materials',    'X',   1.5,  3.6, BLUE),
        ('Climate',      'E',   0.0,  2.9, PURPLE),
    ]

    for label, icon, x, y, color in domains:
        half_w = neck_w + (top_w - neck_w) * (y - neck_y) / (top_y - neck_y)
        if abs(x) < half_w * 0.90:
            # Node circle
            ax.add_patch(plt.Circle((x, y), 0.32, facecolor=DARK,
                                     edgecolor=color, lw=1.5, alpha=0.9, zorder=4))
            ax.text(x, y, icon, fontsize=13, ha='center', va='center',
                    color=color, fontweight='bold', fontfamily='monospace', zorder=5)
            # Label
            ax.text(x, y - 0.52, label, fontsize=7, ha='center', va='top',
                    color=GREY, fontfamily='sans-serif', zorder=5)
            # Flow line to neck
            xs = [x, x * 0.3, 0]
            ys = [y - 0.32, neck_y + 0.8, neck_y + 0.1]
            ax.plot(xs, ys, color=color, alpha=0.12, lw=1.0, zorder=1)

    # ── Quantum algorithms (bottom half) ──
    algorithms = [
        ('QAOA',  -1.5, -2.2),
        ("Shor's", 0.0, -1.6),
        ('VQE',    1.5, -2.2),
        ('QAE',   -1.0, -3.3),
        ('QUBO',   1.0, -3.3),
        ('QPE',   -2.0, -4.2),
        ('QML',    0.0, -4.0),
        ('QSim',   2.0, -4.2),
    ]

    for label, x, y in algorithms:
        half_w = neck_w + (bot_w - neck_w) * (abs(y) - neck_y) / (abs(bot_y) - neck_y)
        if abs(x) < half_w * 0.85:
            ax.add_patch(plt.Circle((x, y), 0.28, facecolor=DARK,
                                     edgecolor=TEAL, lw=1.2, alpha=0.9, zorder=4))
            ax.text(x, y, label, fontsize=6.5, ha='center', va='center',
                    color=TEAL, fontweight='bold', fontfamily='monospace', zorder=5)
            # Flow line from neck
            xs = [0, x * 0.3, x]
            ys = [-neck_y - 0.1, y + 1.0, y + 0.28]
            ax.plot(xs, ys, color=TEAL, alpha=0.12, lw=1.0, zorder=1)

    # ── Connect algorithm nodes ──
    alg_edges = [(0, 1), (1, 2), (3, 4), (5, 6), (6, 7),
                 (0, 3), (2, 4), (3, 5), (4, 7)]
    for i, j in alg_edges:
        x0, y0 = algorithms[i][1], algorithms[i][2]
        x1, y1 = algorithms[j][1], algorithms[j][2]
        ax.plot([x0, x1], [y0, y1], color=TEAL, alpha=0.08, lw=0.8, zorder=1)

    # ── Title ──
    ax.text(0, 6.4, 'THE QUANTUM', fontsize=32, fontweight='bold',
            color=WHITE, ha='center', va='bottom', fontfamily='sans-serif')
    ax.text(0, 5.9, 'BOTTLENECK', fontsize=34, fontweight='bold',
            color=TEAL, ha='center', va='bottom', fontfamily='sans-serif')

    # ── Subtitle ──
    ax.text(0, -6.0, 'Eight problems from logistics to climate',
            fontsize=12, color=GREY, ha='center', va='top', fontfamily='sans-serif',
            style='italic')
    ax.text(0, -6.5, 'and the algorithms that could solve them',
            fontsize=12, color=GREY, ha='center', va='top', fontfamily='sans-serif',
            style='italic')

    plt.savefig(save_path, dpi=200, bbox_inches='tight',
                facecolor=DARK, edgecolor='none', pad_inches=0.15)
    plt.close()
    print(f'Cover saved → {save_path}')


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == '__main__':
    draw_logo()
    draw_logo_with_text()
    draw_cover()
    print('\nAll images generated in figures/')

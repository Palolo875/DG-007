"""Générateur de calçada portuguesa en SVG.

Les pierres sont posées en rangs qui suivent la vague (comme dans le Mar Largo du Rossio) ;
les bandes noires sont des groupes de rangs ; le lettrage est découpé dans les pierres
(clipPath sur un <text>), comme un calceteiro taille les cubes au contour de la lettre.

Code natif : aucune image externe. Graine fixe : le rendu est reproductible.
"""
import math
import random

WHITE = ["#EEEDE9", "#E7E6E1", "#F3F2EF", "#E0DED8", "#E9E8E4"]   # calcaire (gris froid, pas crème)
BLACK = ["#1A1B1D", "#222325", "#2A2A2C", "#151617", "#1F2022"]   # basalte
MORTAR = "#A9A59D"                                               # joint de sable


def _shrink(pts, k):
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    return [(cx + (x - cx) * k, cy + (y - cy) * k) for x, y in pts]


def lay(W, H, s, amp, wl=380.0, phase=0.0, seed=7, jitter=0.09, gap=0.86):
    """Pose les pierres. amp(y) donne l'amplitude de la vague à la hauteur y.

    Renvoie une liste de (polygone, rang, y_centre)."""
    rnd = random.Random(seed)
    out = []
    for i in range(-3, int(H / s) + 4):
        y0 = i * s
        a = amp(y0)

        def yc(x, y0=y0, a=a):
            return y0 + a * math.sin(2 * math.pi * x / wl + phase)

        x = -rnd.uniform(0, s)
        while x < W + s:
            w = s * rnd.uniform(0.68, 1.32)
            x1 = x + w

            def j():
                return rnd.uniform(-s * jitter, s * jitter)

            pts = [
                (x + j(), yc(x) - s / 2 + j()),
                (x1 + j(), yc(x1) - s / 2 + j()),
                (x1 + j(), yc(x1) + s / 2 + j()),
                (x + j(), yc(x) + s / 2 + j()),
            ]
            # une pierre sur six est coupée en deux (pierre plus petite, comme sur un vrai sol)
            if rnd.random() < 0.16 and w > s * 0.9:
                xm = (x + x1) / 2 + j()
                a1 = [pts[0], (xm, yc(xm) - s / 2 + j()), (xm, yc(xm) + s / 2 + j()), pts[3]]
                a2 = [(xm, yc(xm) - s / 2 + j()), pts[1], pts[2], (xm, yc(xm) + s / 2 + j())]
                out.append((_shrink(a1, gap), i, y0))
                out.append((_shrink(a2, gap), i, y0))
            else:
                out.append((_shrink(pts, gap), i, y0))
            x = x1
    return out


def _d(poly):
    return "M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in poly) + "Z"


def svg(W, H, stones, is_black, text=None, uid="c", seed=3, extra_defs=""):
    """Assemble le SVG.

    is_black(rang, y) -> bool : la pierre est-elle de basalte (bande de vague) ?
    text : dict(x, y, size, weight, family, content, length, anchor) pour le lettrage découpé.
    """
    rnd = random.Random(seed)
    w_groups = {c: [] for c in WHITE}
    b_groups = {c: [] for c in BLACK}
    for poly, row, y0 in stones:
        if is_black(row, y0):
            b_groups[rnd.choice(BLACK)].append(_d(poly))
        else:
            w_groups[rnd.choice(WHITE)].append(_d(poly))

    defs = []
    body = []
    for n, (c, ds) in enumerate(w_groups.items()):
        if ds:
            defs.append(f'<path id="{uid}w{n}" d="{"".join(ds)}"/>')
    for n, (c, ds) in enumerate(b_groups.items()):
        if ds:
            body.append(f'<path fill="{c}" stroke="{c}" d="{"".join(ds)}"/>')

    whites = [f'<use href="#{uid}w{n}" fill="{c}" stroke="{c}"/>' for n, c in enumerate(WHITE) if w_groups[c]]
    # lettrage : les mêmes pierres blanches, rejouées en basalte et découpées par la lettre
    letters = ""
    if text:
        t = text
        ls = f' textLength="{t["length"]}" lengthAdjust="spacing"' if t.get("length") else ""
        defs.append(
            f'<clipPath id="{uid}t"><text x="{t["x"]}" y="{t["y"]}" font-family="{t["family"]}" '
            f'font-weight="{t["weight"]}" font-size="{t["size"]}" text-anchor="{t.get("anchor", "start")}"{ls}>'
            f'{t["content"]}</text></clipPath>'
        )
        cut = [f'<use href="#{uid}w{n}" fill="{BLACK[n % len(BLACK)]}" stroke="{BLACK[n % len(BLACK)]}"/>'
               for n, c in enumerate(WHITE) if w_groups[c]]
        letters = f'<g clip-path="url(#{uid}t)">{"".join(cut)}</g>'

    return (
        f'<svg class="calcada" viewBox="0 0 {W} {H}" width="{W}" height="{H}" preserveAspectRatio="xMidYMid slice" '
        f'aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">'
        f'<defs>{"".join(defs)}{extra_defs}</defs>'
        f'<rect width="{W}" height="{H}" fill="{MORTAR}"/>'
        f'<g stroke-width="2.2" stroke-linejoin="round">{"".join(whites)}{"".join(body)}{letters}</g>'
        f'</svg>'
    )

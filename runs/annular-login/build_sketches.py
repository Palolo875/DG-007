"""Esquisses de divergence — page de connexion Annular (1440 × 900, même contenu)."""
import math
import random
from pathlib import Path

OUT = Path(__file__).parent / "esquisses"
OUT.mkdir(exist_ok=True)

HEAD = """<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><link rel="stylesheet" href="../fonts/polices.css"><style>{css}</style></head><body>{b}</body></html>"""

MARK = ('<svg class="mark" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.2" fill="none" '
        'stroke="currentColor" stroke-width="5.2"/></svg>')


def form(cls=""):
    return f"""<form class="f {cls}" novalidate>
<label for="e">E-mail professionnel</label><input id="e" type="email" autocomplete="username" value="">
<div class="lr"><label for="p">Mot de passe</label><a href="#">Mot de passe oublié ?</a></div>
<input id="p" type="password" autocomplete="current-password">
<button class="go" type="submit">Se connecter</button>
<div class="or"><span>ou</span></div>
<button class="alt" type="button">Continuer avec une clé d'accès</button>
<button class="alt" type="button">Connexion unique (SSO)</button>
<p class="new">Pas encore de compte ? <a href="#">Demander un accès</a></p></form>"""


# ------------------------------------------------------------------ dessin de carte (trait)
def board_drawing(x0, y0, k, seed=4, ink="#1B1D1F", red="#D23A2E"):
    """Plan de carte 62 × 38 mm au trait, échelle k px/mm, origine (x0, y0)."""
    W, H = 62 * k, 38 * k
    r = random.Random(seed)
    s = []
    s.append(f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" rx="{2*k}" fill="none" stroke="{ink}" stroke-width="2"/>')
    # trous de fixation : couronne + perçage
    for hx, hy in [(3.5, 3.5), (58.5, 3.5), (3.5, 34.5), (58.5, 34.5)]:
        cx, cy = x0 + hx * k, y0 + hy * k
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{1.6*k}" fill="none" stroke="{ink}" stroke-width="1.4"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{0.85*k}" fill="none" stroke="{ink}" stroke-width="1"/>')
    # mires (fiducials)
    for fx, fy in [(8, 30), (54, 8)]:
        cx, cy = x0 + fx * k, y0 + fy * k
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{0.5*k}" fill="{ink}"/><circle cx="{cx}" cy="{cy}" r="{1.2*k}" fill="none" stroke="{ink}" stroke-width=".8"/>')
    # boîtier QFN
    qx, qy, qs = x0 + 24 * k, y0 + 12 * k, 10 * k
    s.append(f'<rect x="{qx}" y="{qy}" width="{qs}" height="{qs}" fill="none" stroke="{ink}" stroke-width="1.2"/>')
    for i in range(8):
        t = qx + (1.2 + i * 1.1) * k
        s.append(f'<rect x="{t}" y="{qy-1.4*k}" width="{.55*k}" height="{1.1*k}" fill="{ink}"/>'
                 f'<rect x="{t}" y="{qy+qs+.3*k}" width="{.55*k}" height="{1.1*k}" fill="{ink}"/>')
        tt = qy + (1.2 + i * 1.1) * k
        s.append(f'<rect x="{qx-1.4*k}" y="{tt}" width="{1.1*k}" height="{.55*k}" fill="{ink}"/>'
                 f'<rect x="{qx+qs+.3*k}" y="{tt}" width="{1.1*k}" height="{.55*k}" fill="{ink}"/>')
    s.append(f'<circle cx="{qx+1.2*k}" cy="{qy+1.2*k}" r="{.35*k}" fill="{ink}"/>')
    # connecteur 2 × 6 au pas de 2,54 mm
    for i in range(6):
        for j in range(2):
            cx, cy = x0 + (44 + i * 2.54) * k, y0 + (27 + j * 2.54) * k
            sq = ' rx="0"' if (i == 0 and j == 0) else ""
            s.append(f'<circle cx="{cx}" cy="{cy}" r="{.95*k}" fill="none" stroke="{ink}" stroke-width="1.1"/>'
                     f'<circle cx="{cx}" cy="{cy}" r="{.45*k}" fill="none" stroke="{ink}" stroke-width=".8"/>')
    # composants passifs 0603
    for (px, py) in [(12, 10), (12, 14), (12, 18), (40, 14), (40, 18), (18, 28), (22, 28)]:
        X, Y = x0 + px * k, y0 + py * k
        s.append(f'<rect x="{X}" y="{Y}" width="{.8*k}" height="{.9*k}" fill="none" stroke="{ink}" stroke-width="1"/>'
                 f'<rect x="{X+1.6*k}" y="{Y}" width="{.8*k}" height="{.9*k}" fill="none" stroke="{ink}" stroke-width="1"/>')
    # pistes à 45°
    for (a, b) in [((13, 10.4), (24, 13.5)), ((13, 14.4), (23, 16)), ((13, 18.4), (24, 19)), ((35, 15), (40, 14.4)),
                   ((35, 18), (40, 18.4)), ((30, 23.5), (44, 27)), ((32, 23.5), (46.5, 27)), ((19, 28.4), (26, 23.5))]:
        (ax, ay), (bx, by) = a, b
        mx = ax + (bx - ax) * 0.5
        s.append(f'<path d="M{x0+ax*k},{y0+ay*k}H{x0+mx*k-abs(by-ay)*k/2}L{x0+mx*k+abs(by-ay)*k/2},{y0+by*k}H{x0+bx*k}" '
                 f'fill="none" stroke="{ink}" stroke-width="1" opacity=".75"/>')
    # cotes
    s.append(f'<g stroke="{ink}" stroke-width=".8" fill="{ink}">'
             f'<path d="M{x0},{y0+H+10}v{26}M{x0+W},{y0+H+10}v{26}M{x0},{y0+H+28}H{x0+W}" fill="none"/>'
             f'<path d="M{x0},{y0+H+28}l9,-3v6zM{x0+W},{y0+H+28}l-9,-3v6z"/>'
             f'<path d="M{x0-10},{y0}h-26M{x0-10},{y0+H}h-26M{x0-28},{y0}V{y0+H}" fill="none"/>'
             f'<path d="M{x0-28},{y0}l-3,9h6zM{x0-28},{y0+H}l-3,-9h6z"/></g>'
             f'<text x="{x0+W/2}" y="{y0+H+22}" class="cote" text-anchor="middle">62,00</text>'
             f'<text x="{x0-34}" y="{y0+H/2}" class="cote" text-anchor="middle" transform="rotate(-90 {x0-34} {y0+H/2})">38,00</text>')
    # annotation de revue (nuage rouge) autour du QFN
    cx, cy, rr = qx + qs / 2, qy + qs / 2, qs * 0.95
    pts = []
    n = 14
    for i in range(n):
        a1, a2 = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n
        p1 = (cx + rr * math.cos(a1), cy + rr * math.sin(a1)); p2 = (cx + rr * math.cos(a2), cy + rr * math.sin(a2))
        pts.append(f'A{rr*0.24},{rr*0.24} 0 0 1 {p2[0]:.1f},{p2[1]:.1f}')
    s.append(f'<path d="M{cx+rr:.1f},{cy:.1f}{"".join(pts)}" fill="none" stroke="{red}" stroke-width="2"/>')
    return "".join(s), (qx + qs + rr * 0.6, qy - rr * 0.4)


def frame(W, H, m=24, ink="#1B1D1F"):
    s = [f'<rect x="{m}" y="{m}" width="{W-2*m}" height="{H-2*m}" fill="none" stroke="{ink}" stroke-width="2"/>',
         f'<rect x="{m+18}" y="{m+18}" width="{W-2*m-36}" height="{H-2*m-36}" fill="none" stroke="{ink}" stroke-width="1"/>']
    nx, ny = 8, 6
    for i in range(nx + 1):
        x = m + 18 + i * (W - 2 * m - 36) / nx
        s.append(f'<path d="M{x},{m}v18M{x},{H-m}v-18" stroke="{ink}" stroke-width="1"/>')
        if i < nx:
            xc = x + (W - 2 * m - 36) / nx / 2
            s.append(f'<text x="{xc}" y="{m+13}" class="zone" text-anchor="middle">{i+1}</text><text x="{xc}" y="{H-m-5}" class="zone" text-anchor="middle">{i+1}</text>')
    for j in range(ny + 1):
        y = m + 18 + j * (H - 2 * m - 36) / ny
        s.append(f'<path d="M{m},{y}h18M{W-m},{y}h-18" stroke="{ink}" stroke-width="1"/>')
        if j < ny:
            yc = y + (H - 2 * m - 36) / ny / 2 + 4
            L = "ABCDEF"[j]
            s.append(f'<text x="{m+9}" y="{yc}" class="zone" text-anchor="middle">{L}</text><text x="{W-m-9}" y="{yc}" class="zone" text-anchor="middle">{L}</text>')
    return "".join(s)


BASE_FORM_CSS = """
.f{display:flex;flex-direction:column}
.f label{font-size:14px;font-weight:500;margin-bottom:6px}
.f input{height:44px;border:1.5px solid var(--ink);background:var(--field);padding:0 12px;font:inherit;font-size:16px;margin-bottom:14px;color:var(--ink);border-radius:0}
.f .lr{display:flex;justify-content:space-between;align-items:baseline}.f .lr a{font-size:13px;color:var(--ink)}
.f .go{height:48px;background:var(--ink);color:var(--paper);border:0;font:inherit;font-weight:600;font-size:16px;margin-top:4px;cursor:pointer}
.f .or{display:flex;align-items:center;gap:10px;margin:14px 0;font-size:13px;color:var(--mute)}.f .or:before,.f .or:after{content:"";flex:1;border-top:1px solid var(--rule)}
.f .alt{height:44px;background:transparent;border:1.5px solid var(--ink);font:inherit;font-size:15px;color:var(--ink);margin-bottom:8px;cursor:pointer}
.f .new{font-size:14px;margin-top:8px;color:var(--mute)}.f .new a{color:var(--ink)}
*{box-sizing:border-box;margin:0;padding:0}
"""


# ------------------------------------------------------------------ A · Cartouche
def sketch_a():
    W, H = 1440, 900
    art, note = board_drawing(150, 170, 11.5)
    svg = (f'<svg class="plan" viewBox="0 0 {W} {H}" aria-hidden="true">{frame(W,H)}{art}'
           f'<text x="{note[0]+10}" y="{note[1]}" class="redline">Rév. C — à signer avant fabrication</text>'
           f'<path d="M{note[0]-14},{note[1]+6}l-30,26" stroke="#D23A2E" stroke-width="1.5"/></svg>')
    css = BASE_FORM_CSS + """
:root{--ink:#1B1D1F;--paper:#F7F7F4;--field:#fff;--mute:#5A5D60;--rule:#1B1D1F}
body{background:var(--paper);color:var(--ink);font-family:Barlow,sans-serif}
.pg{position:relative;width:1440px;height:900px;overflow:hidden}
.plan{position:absolute;inset:0}.zone{font:500 11px Barlow;fill:var(--ink)}.cote{font:500 15px Barlow;fill:var(--ink)}.redline{font:italic 500 17px Barlow;fill:#D23A2E}
.cart{position:absolute;right:42px;bottom:42px;width:520px;background:var(--paper);border-left:2px solid var(--ink);border-top:2px solid var(--ink);display:grid;grid-template-columns:1fr 150px}
.cart > div{border-right:1px solid var(--ink);border-bottom:1px solid var(--ink);padding:8px 12px}
.cart .k{font-size:11px;text-transform:none;color:var(--mute);display:block;margin-bottom:2px}
.cart .brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:22px}.mark{width:24px;height:24px}
.cart .ttl{grid-column:1/-1;font-size:28px;font-weight:600;padding:14px 16px}
.cart .fm{grid-column:1/-1;padding:16px}
.cart .v{font-size:16px;font-weight:600}
.pitch{position:absolute;left:150px;top:96px;font-size:22px;font-weight:500;max-width:620px;line-height:1.3}
"""
    body = f"""<div class="pg">{svg}<p class="pitch">La revue de conception électronique : chaque révision de carte, annotée, discutée et signée avant fabrication.</p>
<div class="cart"><div class="brand">{MARK}Annular</div><div><span class="k">Document</span><span class="v">Connexion</span></div>
<div class="ttl">Se connecter à Annular</div><div class="fm">{form()}</div>
<div><span class="k">Approuvé par</span><span class="v">— vous</span></div><div><span class="k">Feuille</span><span class="v">1 / 1</span></div></div></div>"""
    (OUT / "a-cartouche.html").write_text(HEAD.format(t="A · Cartouche", css=css, b=body))


# ------------------------------------------------------------------ B · Sérigraphie
def board_surface(W, H, seed=9):
    r = random.Random(seed)
    s = [f'<rect width="{W}" height="{H}" fill="#1D4D36"/>']
    # pistes de cuivre sous le vernis (plus claires), routées à 45°
    for i in range(60):
        x, y = r.uniform(-100, W), r.uniform(0, H)
        d = f"M{x:.0f},{y:.0f}"
        for _ in range(4):
            L = r.uniform(60, 260)
            dirn = r.choice([(1, 0), (0, 1), (1, 1), (1, -1)])
            x += dirn[0] * L; y += dirn[1] * L * (0.7 if dirn[0] else 1)
            d += f"L{x:.0f},{y:.0f}"
        s.append(f'<path d="{d}" fill="none" stroke="#2A6B4A" stroke-width="{r.choice([3,3,5,8])}" stroke-linejoin="round"/>')
    # vias : couronne argent + trou
    for i in range(90):
        x, y = r.uniform(0, W), r.uniform(0, H)
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="#C9CDD1"/><circle cx="{x:.0f}" cy="{y:.0f}" r="2.6" fill="#0E1512"/>')
    # quelques repères de sérigraphie
    for i in range(14):
        x, y = r.uniform(40, W - 80), r.uniform(40, H - 40)
        s.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="Barlow" font-weight="600" font-size="15" fill="#EDEDE8">{r.choice(["R","C","U","TP","D"])}{r.randint(1,48)}</text>')
    return f'<svg class="carte" viewBox="0 0 {W} {H}" aria-hidden="true">{"".join(s)}</svg>'


def sketch_b():
    css = BASE_FORM_CSS + """
:root{--ink:#111;--paper:#EDEDE8;--field:#EDEDE8;--mute:#C9D6CE;--rule:#EDEDE8}
body{background:#1D4D36;color:#EDEDE8;font-family:Barlow,sans-serif}
.pg{position:relative;width:1440px;height:900px;overflow:hidden}.carte{position:absolute;inset:0}
.silk{position:absolute;left:520px;top:110px;width:400px;padding:28px 30px;border:2px solid #EDEDE8;background:#1D4D36}
.silk h1{font-size:26px;font-weight:600;margin-bottom:22px;display:flex;align-items:center;gap:12px}.mark{width:26px;height:26px;color:#C9CDD1}
.silk .f label{color:#EDEDE8;letter-spacing:.02em}.silk .f .lr a,.silk .f .new a{color:#EDEDE8}.silk .f .alt{border-color:#EDEDE8;color:#EDEDE8}
.silk .f .go{background:#C9CDD1;color:#0E1512}.silk .f input{border-color:#EDEDE8}
.ref{position:absolute;left:520px;top:80px;font-size:15px;font-weight:600;letter-spacing:.04em}
"""
    body = f"""<div class="pg">{board_surface(1440,900)}<span class="ref">ANNULAR · REV C · LOGIN</span>
<div class="silk"><h1>{MARK}Se connecter à Annular</h1>{form()}</div></div>"""
    (OUT / "b-serigraphie.html").write_text(HEAD.format(t="B · Sérigraphie", css=css, b=body))


# ------------------------------------------------------------------ C · Couches
def sketch_c():
    css = BASE_FORM_CSS + """
:root{--ink:#16181B;--paper:#FBFBF9;--field:#fff;--mute:#5B5F63;--rule:#C9CCD0}
body{background:#E9EAEC;color:var(--ink);font-family:'IBM Plex Sans',sans-serif}
.pg{position:relative;width:1440px;height:900px;overflow:hidden}
.stack{position:absolute;left:520px;top:120px;width:420px;height:620px}
.l{position:absolute;inset:0;border:1.5px solid var(--ink)}
.l4{transform:translate(72px,72px);background:#D9B85E}.l3{transform:translate(48px,48px);background:repeating-linear-gradient(90deg,#B87333 0 6px,#C98A4E 6px 18px)}
.l2{transform:translate(24px,24px);background:#1F5A3D}
.l1{background:var(--paper);padding:34px 36px}
.tag{position:absolute;right:-150px;font-size:13px;color:var(--mute);width:130px}.tag:before{content:"";position:absolute;left:-20px;top:8px;width:16px;border-top:1px solid var(--mute)}
.l1 h1{font-size:26px;font-weight:600;margin-bottom:24px;display:flex;gap:12px;align-items:center}.mark{width:26px;height:26px}
.side{position:absolute;left:80px;top:140px;width:340px;font-size:20px;line-height:1.35}
"""
    body = f"""<div class="pg"><p class="side">La revue de conception électronique. Chaque couche, chaque révision, signée avant fabrication.</p>
<div class="stack"><div class="l l4"></div><div class="l l3"></div><div class="l l2"></div>
<div class="l l1"><h1>{MARK}Se connecter à Annular</h1>{form()}</div>
<span class="tag" style="top:20px">L1 · Sérigraphie</span><span class="tag" style="top:60px;right:-174px">L2 · Vernis</span>
<span class="tag" style="top:100px;right:-198px">L3 · Cuivre</span><span class="tag" style="top:140px;right:-222px">L4 · Âme FR-4</span></div></div>"""
    (OUT / "c-couches.html").write_text(HEAD.format(t="C · Couches", css=css, b=body))


# ------------------------------------------------------------------ M · modale
def sketch_m():
    css = BASE_FORM_CSS + """
:root{--ink:#0B0D0E;--paper:#fff;--field:#fff;--mute:#6B7075;--rule:#E3E5E8}
body{font-family:Inter,sans-serif;color:var(--ink);background:#fff}
.pg{display:grid;grid-template-columns:1fr 1fr;width:1440px;height:900px}
.l{padding:64px 120px;display:flex;flex-direction:column;justify-content:center}
.l .brand{display:flex;gap:10px;align-items:center;font-weight:700;font-size:20px;position:absolute;top:40px;left:64px}.mark{width:22px;height:22px}
.l h1{font-size:30px;font-weight:600;letter-spacing:-.02em;margin-bottom:8px}.l .sub{color:var(--mute);margin-bottom:28px}
.f input,.f .alt{border:1px solid #D9DCE0;border-radius:8px}.f .go{border-radius:8px}
.r{background:radial-gradient(600px 400px at 70% 30%,#1FAF6E55,transparent),radial-gradient(500px 500px at 30% 80%,#2563EB44,transparent),#0B0F0E;color:#fff;padding:80px;display:flex;flex-direction:column;justify-content:flex-end}
.r blockquote{font-size:26px;line-height:1.35;max-width:520px}.r cite{display:block;margin-top:20px;font-style:normal;color:#9AA3A8;font-size:15px}
"""
    body = f"""<div class="pg"><div class="l"><div class="brand">{MARK}Annular</div><h1>Bon retour parmi nous</h1><p class="sub">Connectez-vous pour reprendre vos revues.</p>{form()}</div>
<div class="r"><blockquote>« Annular a divisé par deux nos cycles de revue avant fabrication. »</blockquote><cite>Responsable hardware, client (exemple)</cite></div></div>"""
    (OUT / "m-modale.html").write_text(HEAD.format(t="M · modale", css=css, b=body))


if __name__ == "__main__":
    sketch_m(); sketch_a(); sketch_b(); sketch_c()
    print("ok")

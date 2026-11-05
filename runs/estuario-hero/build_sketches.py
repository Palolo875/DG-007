"""Construit les esquisses de divergence (premier écran bureau, 1440 × 900, même contenu)."""
import math
import random
from pathlib import Path

import calcada as C

HERE = Path(__file__).parent
OUT = HERE / "esquisses"
OUT.mkdir(exist_ok=True)

# Contenu commun — exemple (festival fictif), cohérent entre esquisses
NAV = ["Programa", "Exposições", "Lugares", "Visitar"]
KICK = "Festival Internacional de Arquitetura e Design"
THEME = "Terra Firme"
THEME_EN = "Building on shifting ground"
EDITION = "4.ª edição"
DATES = "17 Abr — 16 Mai 2027"
CITY = "Lisboa"
STATS = [("38", "lugares"), ("120", "projetos"), ("31", "países")]
CTA = "Passe do festival"
CTA2 = "Ver programa"

HEAD = """<!doctype html><html lang="pt"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="../fonts/polices.css"><style>{css}</style></head><body>{body}</body></html>"""


def nav_html(cls=""):
    items = "".join(f'<a href="#">{n}</a>' for n in NAV)
    return (f'<nav class="nav {cls}"><a class="logo" href="#">Estuário</a><div class="menu">{items}</div>'
            f'<div class="right"><span class="lang"><b>PT</b> / <a href="#">EN</a></span>'
            f'<a class="btn-s" href="#">Bilhetes</a></div></nav>')


# ---------------------------------------------------------------- B · Mar Largo
def sketch_b():
    W, H, s = 1440, 900, 17

    def amp(y):
        if y < 560:
            return 0.0
        return min(36.0, (y - 560) * 0.45)

    stones = C.lay(W, H, s, amp, wl=420, phase=0.6, seed=11)
    r0 = int(640 / s)

    def is_black(row, y0):
        return y0 > 610 and ((row - r0) // 4) % 2 == 0

    art = C.svg(W, H, stones, is_black, uid="b", text=dict(
        x=64, y=408, size=300, weight=800, family="Schibsted Grotesk", content="ESTUÁRIO", length=1312))
    css = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#A9A59D;font-family:'Schibsted Grotesk',system-ui,sans-serif;color:#151617}
.hero{position:relative;height:900px;overflow:hidden}
.calcada{position:absolute;inset:0;width:100%;height:100%}
.nav{position:absolute;top:0;left:0;right:0;height:72px;display:flex;align-items:center;gap:40px;padding:0 64px;background:#F3F2EF;border-bottom:1px solid #CFCCC5;font-size:15px}
.nav .logo{font-weight:800;font-size:19px;color:inherit;text-decoration:none;letter-spacing:-.01em}
.nav .menu{display:flex;gap:28px;margin-left:24px}.nav a{color:inherit;text-decoration:none}
.nav .right{margin-left:auto;display:flex;align-items:center;gap:24px}
.lang a{color:#6b6a66}.btn-s{border:1.5px solid #151617;padding:9px 16px;border-radius:2px;font-weight:600}
.lancil{position:absolute;left:64px;right:64px;top:452px;height:124px;background:#F3F2EF;display:grid;grid-template-columns:1.25fr 1fr 1fr auto;align-items:center;padding:0 36px;gap:32px;box-shadow:0 1px 0 #fff inset,0 -1px 0 #cfcac0 inset,0 6px 0 #8f8a80}
.k{font-size:15px;line-height:1.35}.k b{display:block;font-size:26px;font-weight:700;letter-spacing:-.015em}
.k span{color:#57564f}
.d{font-size:26px;font-weight:700;letter-spacing:-.015em;line-height:1.1}.d span{display:block;font-size:15px;font-weight:400;color:#57564f;margin-top:4px}
.st{display:flex;gap:26px}.st div{font-size:14px;color:#57564f}.st b{display:block;font-size:26px;color:#151617;font-weight:700}
.cta{display:flex;gap:12px}.btn{background:#151617;color:#F3F2EF;padding:16px 24px;font-weight:600;font-size:16px;text-decoration:none;border-radius:2px}
.btn.g{background:transparent;color:#151617;border:1.5px solid #151617}
"""
    body = f"""<header class="hero">{art}{nav_html()}
<h1 class="sr" style="position:absolute;left:-9999px">Estuário — {KICK}</h1>
<div class="lancil"><div class="k"><b>{THEME}</b><span>{EDITION} · {THEME_EN}</span></div>
<div class="d">{DATES}<span>{CITY} — {KICK}</span></div>
<div class="st">{''.join(f'<div><b>{a}</b>{b}</div>' for a, b in STATS)}</div>
<div class="cta"><a class="btn" href="#">{CTA}</a><a class="btn g" href="#">{CTA2}</a></div></div>
</header>"""
    (OUT / "b-marlargo.html").write_text(HEAD.format(title="B · Mar Largo", css=css, body=body))


# ---------------------------------------------------------------- A · Gaiola
def sketch_a():
    W, H = 1440, 900
    cols = [0, 240, 480, 720, 960, 1200, 1440]
    rows = [72, 312, 552, 792, 1032]
    filled = {(0, 0), (1, 0), (0, 2), (1, 2), (2, 2), (4, 2), (5, 2)}  # travées occupées par le contenu
    lines = []
    for r in range(len(rows) - 1):
        for c in range(len(cols) - 1):
            x0, x1, y0, y1 = cols[c], cols[c + 1], rows[r], rows[r + 1]
            if (c, r) in filled or r == 1:
                continue
            lines.append(f'<path d="M{x0},{y0}L{x1},{y1}M{x1},{y0}L{x0},{y1}" class="br"/>')
    for x in cols[1:-1]:
        lines.append(f'<path d="M{x},72V{H}" class="po"/>')
    for y in rows[1:-1]:
        lines.append(f'<path d="M0,{y}H{W}" class="po"/>')
    # croix de la rangée du nom, dessinées derrière les lettres
    behind = []
    for c in range(6):
        x0, x1 = cols[c], cols[c + 1]
        behind.append(f'<path d="M{x0},312L{x1},552M{x1},312L{x0},552" class="br"/>')
    art = (f'<svg class="gaiola" viewBox="0 0 {W} {H}" aria-hidden="true">{"".join(behind)}{"".join(lines)}'
           f'<rect x="960" y="552" width="480" height="240" fill="#D9381E"/></svg>')
    css = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#F6F6F3;font-family:'Schibsted Grotesk',system-ui,sans-serif;color:#141414}
.hero{position:relative;height:900px;overflow:hidden}
.gaiola{position:absolute;inset:0;width:1440px;height:900px}
.br{stroke:#141414;stroke-width:1;fill:none;opacity:.55}.po{stroke:#141414;stroke-width:2;fill:none}
.nav{position:absolute;top:0;left:0;right:0;height:72px;display:flex;align-items:center;gap:40px;padding:0 32px;border-bottom:2px solid #141414;font-size:15px}
.nav .logo{font-weight:800;font-size:19px;color:inherit;text-decoration:none}.nav .menu{display:flex;gap:28px;margin-left:120px}
.nav a{color:inherit;text-decoration:none}.nav .right{margin-left:auto;display:flex;gap:24px;align-items:center}.lang a{color:#777}
.btn-s{border:1.5px solid #141414;padding:9px 16px;font-weight:600}
.cell{position:absolute;padding:28px 32px}
.kick{left:0;top:72px;width:480px;height:240px;display:flex;flex-direction:column;justify-content:space-between}
.kick p{font-size:22px;line-height:1.25;font-weight:500;max-width:340px}.kick small{font-size:14px;color:#555}
h1{position:absolute;left:22px;top:300px;font-size:262px;line-height:1;font-weight:800;letter-spacing:-.045em;background:linear-gradient(#F6F6F3,#F6F6F3) 0 64% / 100% 70% no-repeat;padding:0 10px}
.date{left:0;top:552px;width:480px}.date b{display:block;font-size:44px;font-weight:700;letter-spacing:-.02em;line-height:1.05}.date span{font-size:15px;color:#555;display:block;margin-top:10px}
.theme{left:480px;top:552px;width:240px}.theme b{display:block;font-size:22px;font-weight:700}.theme span{font-size:15px;color:#555}
.cta{left:960px;top:552px;width:480px;height:240px;color:#fff;display:flex;flex-direction:column;justify-content:space-between}
.cta a{color:#fff;text-decoration:none}.cta .big{font-size:40px;font-weight:700;letter-spacing:-.02em}.cta .sm{font-size:16px;border-top:1.5px solid rgba(255,255,255,.6);padding-top:14px}
.stats{left:0;top:792px;display:flex;gap:0}.stats div{width:240px;font-size:14px;color:#555}.stats b{font-size:24px;color:#141414;margin-right:6px}
"""
    body = f"""<header class="hero">{art}{nav_html()}
<div class="cell kick"><p>{KICK}</p><small>{EDITION} · {CITY}</small></div>
<h1>Estuário</h1>
<div class="cell date"><b>17 Abr —<br>16 Mai 2027</b><span>{CITY}, 38° 43′ N</span></div>
<div class="cell theme"><b>{THEME}</b><span>{THEME_EN}</span></div>
<div class="cell cta"><a class="big" href="#">{CTA}</a><a class="sm" href="#">{CTA2}</a></div>
<div class="cell stats">{''.join(f'<div><b>{a}</b>{b}</div>' for a, b in STATS)}</div>
</header>"""
    (OUT / "a-gaiola.html").write_text(HEAD.format(title="A · Gaiola", css=css, body=body))


# ---------------------------------------------------------------- C · Placa
def sketch_c():
    css = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#E4E3DE;font-family:'Instrument Sans',system-ui,sans-serif;color:#1b1b1a}
.hero{position:relative;height:900px;overflow:hidden;background:
 radial-gradient(1200px 700px at 30% 30%,#EEEDE9,transparent 70%),
 repeating-linear-gradient(0deg,transparent 0 179px,rgba(0,0,0,.06) 179px 180px),#E1E0DA}
.hero:before{content:"";position:absolute;inset:0;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.9' numOctaves='3'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .09 0'/%3E%3C/filter%3E%3Crect width='240' height='240' filter='url(%23n)'/%3E%3C/svg%3E");mix-blend-mode:multiply}
.nav{position:absolute;top:0;left:0;right:0;height:72px;display:flex;align-items:center;gap:40px;padding:0 64px;font-size:15px;z-index:2}
.nav .logo{font-family:Forum,serif;font-size:24px;color:inherit;text-decoration:none;letter-spacing:.04em}.nav .menu{display:flex;gap:28px;margin-left:24px}
.nav a{color:inherit;text-decoration:none}.nav .right{margin-left:auto;display:flex;gap:24px;align-items:center}.lang a{color:#777}
.btn-s{border:1.5px solid #1b1b1a;padding:9px 16px;font-weight:600}
.placa{position:absolute;left:64px;top:150px;width:880px;height:520px;background:linear-gradient(160deg,#FBFBF9,#F0EFEB);border-radius:6px;box-shadow:0 1px 0 #fff inset,0 2px 2px rgba(0,0,0,.08),0 24px 40px -20px rgba(0,0,0,.35);padding:22px}
.placa .in{border:2px solid #2a2a28;outline:1px solid #2a2a28;outline-offset:-8px;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-family:Forum,serif;color:#232321}
.placa small{font-size:26px;letter-spacing:.14em}
.placa h1{font-weight:400;font-size:178px;letter-spacing:.06em;line-height:1;margin:18px 0 10px;text-shadow:0 1px 0 #fff,0 -1px 0 rgba(0,0,0,.25)}
.placa p{font-size:28px;letter-spacing:.18em}
.side{position:absolute;left:1008px;top:150px;width:368px;height:520px;display:flex;flex-direction:column;justify-content:space-between}
.side .d{font-size:44px;font-weight:600;letter-spacing:-.02em;line-height:1.05}.side .t{font-size:17px;line-height:1.45;color:#3d3d3a}
.side .t b{display:block;font-size:22px;color:#1b1b1a}
.btn{display:block;background:#1b1b1a;color:#fff;text-align:center;padding:18px;font-weight:600;text-decoration:none;font-size:17px}
.btn.g{background:none;color:#1b1b1a;border:1.5px solid #1b1b1a;margin-top:10px}
.stats{position:absolute;left:64px;top:730px;display:flex;gap:56px;font-size:15px;color:#3d3d3a}.stats b{font-size:28px;color:#1b1b1a;margin-right:8px;font-weight:600}
"""
    body = f"""<header class="hero">{nav_html()}
<div class="placa"><div class="in"><small>FESTIVAL INTERNACIONAL DE ARQVITECTVRA E DESIGN</small>
<h1>ESTVÁRIO</h1><p>LISBOA · MMXXVII</p></div></div>
<div class="side"><div class="d">17 Abr —<br>16 Mai 2027</div><div class="t"><b>{THEME}</b>{EDITION} · {THEME_EN}</div>
<div><a class="btn" href="#">{CTA}</a><a class="btn g" href="#">{CTA2}</a></div></div>
<div class="stats">{''.join(f'<div><b>{a}</b>{b}</div>' for a, b in STATS)}</div>
</header>"""
    (OUT / "c-placa.html").write_text(HEAD.format(title="C · Placa", css=css, body=body))


# ---------------------------------------------------------------- M · modale
def sketch_m():
    css = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Hanken Grotesk',system-ui,sans-serif;color:#fff;background:#111}
.hero{position:relative;height:900px;overflow:hidden;background:url(../refs/4-image.jpg) center 40%/cover}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,.15) 40%,rgba(0,0,0,.7))}
.nav{position:absolute;z-index:2;top:0;left:0;right:0;height:80px;display:flex;align-items:center;gap:40px;padding:0 64px;font-size:15px}
.nav .logo{font-weight:800;font-size:20px;color:inherit;text-decoration:none}.nav .menu{display:flex;gap:28px;margin-left:auto}
.nav a{color:inherit;text-decoration:none}.nav .right{display:flex;gap:24px;align-items:center}.lang a{color:#ccc}
.btn-s{border:1.5px solid #fff;padding:9px 16px;border-radius:999px}
.c{position:absolute;z-index:2;left:64px;right:64px;bottom:72px}
.lbl{font-family:ui-monospace,monospace;font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:20px;opacity:.85}
h1{font-size:200px;font-weight:800;letter-spacing:-.04em;line-height:.9}
.row{display:flex;justify-content:space-between;align-items:end;margin-top:28px}
.row p{font-size:20px;max-width:520px;line-height:1.4}
.btn{background:#fff;color:#111;padding:16px 28px;border-radius:999px;font-weight:600;text-decoration:none;margin-left:12px}.btn.g{background:none;color:#fff;border:1.5px solid #fff}
"""
    body = f"""<header class="hero">{nav_html()}
<div class="c"><div class="lbl">{DATES} · {CITY} · {EDITION}</div><h1>Estuário</h1>
<div class="row"><p>{KICK}. {THEME} — {THEME_EN}.</p><div><a class="btn g" href="#">{CTA2}</a><a class="btn" href="#">{CTA}</a></div></div></div>
</header>"""
    (OUT / "m-modale.html").write_text(HEAD.format(title="M · modale", css=css, body=body))


if __name__ == "__main__":
    sketch_m(); sketch_a(); sketch_b(); sketch_c()
    for f in sorted(OUT.glob("*.html")):
        print(f.name, f.stat().st_size)

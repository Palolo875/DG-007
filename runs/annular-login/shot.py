"""Capture rapide : python3 shot.py page.html sortie.png [largeur hauteur attente_ms]"""
import sys, pathlib
from playwright.sync_api import sync_playwright
page, out = sys.argv[1], sys.argv[2]
w, h, wait = (int(x) for x in (sys.argv[3:6] + ['1440', '900', '2500'][len(sys.argv[3:6]):]))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
    pg.goto('file://' + str(pathlib.Path(page).resolve())); pg.wait_for_timeout(wait)
    pass
    pg.screenshot(path=out); b.close()

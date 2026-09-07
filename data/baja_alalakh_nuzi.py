#!/usr/bin/env python3
"""
Descarga de cdli.earth las tablillas administrativas coetáneas de la Creta minoica:
Alalakh (Tell Atchana) y Nuzi (Yorghan Tepe), Bronce Reciente, y de paso Ugarit si CDLI las tiene.

En tu terminal:
    pip install requests
    python3 baja_alalakh_nuzi.py

Produce, en la carpeta actual:
    alalakh.atf / alalakh_cat.csv
    nuzi.atf    / nuzi_cat.csv
    ugarit.atf  / ugarit_cat.csv     (puede salir vacío; se avisa)

Filtra por procedencia, no por periodo, que es como CDLI indexa estos archivos.
Súbelos después aquí para el inventario comparado.
"""
import requests, time, sys, os
from urllib.parse import urlencode

BASE = "https://cdli.earth/search"
HEADERS = {"User-Agent": "Mozilla/5.0 (comparative archive study; research)"}

# (nombre de salida, campo de búsqueda, valor). CDLI indexa la procedencia con el nombre moderno entre paréntesis.
TARGETS = [
    ("alalakh", "provenience", "Alalakh (mod. Tell Atchana)"),
    ("nuzi",    "provenience", "Nuzi (mod. Yorghan Tepe)"),
    ("ugarit",  "provenience", "Ugarit (mod. Ras Shamra)"),
]

def fetch(fmt, page, field, value, aspect=None, page_size=None):
    params = {"simple-value[0]": value, "simple-field[0]": field, "format": fmt, "page": page}
    if aspect: params["aspect"] = aspect
    if page_size: params["page-size"] = page_size
    r = requests.get(BASE + "?" + urlencode(params), headers=HEADERS, timeout=120)
    r.raise_for_status()
    return r.text

def download(outname, fmt, field, value, aspect=None, is_csv=False):
    out = open(outname, "w", encoding="utf-8"); seen = 0; header = False
    for page in range(1, 300):
        try:
            txt = fetch(fmt, page, field, value, aspect=aspect, page_size=1000 if page == 1 else None)
        except requests.HTTPError:
            break            # 404 = se acabaron las páginas
        if is_csv:
            lines = [l for l in txt.splitlines() if l.strip()]
            if len(lines) < 2: break
            if not header: out.write(lines[0] + "\n"); header = True
            out.write("\n".join(lines[1:]) + "\n"); seen += len(lines) - 1
        else:
            n = txt.count("&P")
            if n == 0: break
            out.write(txt + "\n"); seen += n
        print(f"  {outname}: página {page}, acumulado {seen}", file=sys.stderr)
        if page == 1 and seen >= 1000: break
        time.sleep(1.0)
    out.close()
    if seen == 0:
        print(f"  AVISO: {outname} ha salido vacío; puede que CDLI use otro nombre de procedencia.", file=sys.stderr)
    return seen

if __name__ == "__main__":
    for name, field, value in TARGETS:
        print(f"== {name} ({value})", file=sys.stderr)
        n1 = download(f"{name}.atf", "atf", field, value, aspect="inscriptions")
        n2 = download(f"{name}_cat.csv", "csv", field, value, is_csv=True)
        print(f"   {name}: {n1} textos, {n2} fichas de catálogo", file=sys.stderr)
    print("\nHecho. Sube los .atf y los _cat.csv que no estén vacíos.")
    print("Si alguno quedó vacío, busca el nombre exacto en cdli.earth (campo 'provenience') y cámbialo arriba.")

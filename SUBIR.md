# Cómo subir esta actualización (11 de septiembre de 2026)

Descomprime `kuro_github_11sep.zip`; queda una carpeta `kuro_push_v60`. Desde tu terminal:

```
cd ~/Downloads/kuro_push_v60
rsync -a --delete --exclude .git ./ ~/Downloads/kuro_repo/
cd ~/Downloads/kuro_repo
git rm -r --cached data/raw 2>/dev/null; git add -A
git status | head -30          # comprueba que data/raw NO aparece salvo data/raw/README.md
git commit -m "inventory 56, profile and name instruments, value search, reader and hypothesizer, Iberian calibration, papers v0.2"
git push
```

Si `~/Downloads/kuro_repo` no existe (clon nuevo): `git clone https://github.com/BiomeMakers/kuro ~/Downloads/kuro_repo` primero.

## Qué lleva y qué no

**Lleva:** `kuro/` (paquete, 106 tests), `scripts/` (incluidos `value_search.py`, `read_units.py`,
`propose_units.py`, `cycle_*.py`, `extract_linearb.py`, `extract_nodule_seals.py`, `fetch_candidates.py`),
`manifest.json`, `biblio/`, `docs/papers/` (PDF y fuentes, con trece v0.2 y protocolo v0.2),
`docs/analysis/` (149), `docs/state/` (22), `docs/REGISTRO_cambios.md`, `data/derived/` (diccionario,
tasas de error, nódulos signo×sello, búsqueda de valores, ibérico, corridas del lector e hipotetizador).

**No lleva, por licencia:** `data/raw/` entero (se obtiene con `data/fetch.py` y
`scripts/fetch_candidates.py`; ver `data/README.md`), los textos de `docs/reference/`, los `.cog`.
El `.gitignore` los excluye. Si `data/raw/inscriptions.json` estaba ya en el historial del repo,
queda ahí; `data/README.md` dice cómo limpiarlo si el repo se hace público.

## Después de subir

1. Zenodo (DOI): el repo trae `CITATION.cff` y licencia. Con el DOI, el artículo de software (JOSS).
2. Comprobar que el workflow de GitHub Actions pasa (los tests no leen `data/raw`).

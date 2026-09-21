# Cómo subir esta actualización (12 de septiembre de 2026)

Descomprime `kuro_github_12sep.zip`; queda una carpeta `kuro_push_v61`. Desde tu terminal:

```
cd ~/Downloads && rm -rf kuro_push_v61 && unzip -qo kuro_github_12sep.zip
rsync -a --exclude .git --exclude data/raw kuro_push_v61/ ~/Downloads/kuro_repo/
cd ~/Downloads/kuro_repo
git add -A
git status | head -40          # comprueba que data/raw NO aparece
git commit -m "Khania archive, commodity ratios, Egyptian alignment, GORILA verification, submission drafts"
git push
```

Ojo: el `rsync` de esta versión NO lleva `--delete`, para no borrar ficheros que estén en tu repo y no en este paquete (el 11-sep se borraron siete y hubo que recuperarlos).

## Qué lleva de nuevo respecto al commit b4cd1a1 (11-sep)

**Resultados nuevos** (`docs/analysis/`): cotejo del inventario contra SigLA y GORILA (121 de 124 atestaciones confirmadas); el egipcio probado como candidata; las entradas de lista por terminaciones y el candidato -JU; las proporciones entre mercancías; el archivo de Khania medido aparte; el alineamiento posición a posición con 1.357 fórmulas de ofrenda egipcias.

**Artículos** (`docs/papers/` y `docs/papers/submission/`): el manuscrito de la fórmula en formato SMEA con sus tres figuras TIFF y la carta; los cinco artículos de envío; inventario y calibraciones en ES y EN.

**Manifiesto**: 65 cifras, 24 p-valores, 8 retiradas (una nueva: las fracciones como enteros, que no se sostiene), 6 vías cerradas (una nueva: la ración estándar).

**Estado** (`docs/state/`): el mapa del proyecto, la revisión de los artículos, los contactos enviados, y las opciones desde la bibliografía de desciframientos.

## Qué no lleva
`data/raw/` entero (se reconstruye con `data/fetch.py` y `scripts/fetch_candidates.py`), los textos de `docs/reference/`, los `.cog`. El `.gitignore` los excluye.

## Después de subir
1. Zenodo: activar el repositorio y crear la release `v0.2` en GitHub. Da el DOI.
2. El workflow de Actions, desde la web (el token no tiene permiso `workflow`).

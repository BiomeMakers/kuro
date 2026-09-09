# Cómo subir esta actualización (9 de septiembre de 2026)

Descomprime `kuro_completo.zip`; queda una carpeta `kuro_push_final2`. Desde tu terminal:

```
cd ~/Downloads/kuro_push_final2
cp -R . ~/Downloads/kuro_repo/
cd ~/Downloads/kuro_repo
git add .
git commit -m "manifest, bibliography database, papers, analyses and Etruscan corpus"
git push
```

## Qué lleva

**El paquete** (`kuro/`): cargadores de corpus, nulos, los diez instrumentos, informes por
documento, perfil de signo, aritmética, clasificación por contenido, verificador, procedencia de
cifras, umbrales de potencia, control de artefacto de captura, cohesión de agrupaciones y efectos
de factores. Línea de comandos con siete órdenes.

**El manifiesto** (`manifest.json`): toda cifra que los artículos afirman, las cinco afirmaciones
retiradas con su motivo, los diecisiete resultados con precedente y su titular, las dos
identificaciones en disputa, y las tres vías cerradas. `scripts/check_manifest.py` lee los
artículos y falla cuando algo se desvía.

**La base de precedencia** (`biblio/`): qué obra toca qué afirmación y si está leída.

**Los artículos** (`docs/papers/`): 26 PDF y sus 28 fuentes en Markdown.

**Los análisis** (`docs/analysis/`): los 97 que sostienen cada afirmación.

**El estado** (`docs/state/`): dónde está el trabajo, qué falta, a quién escribir.

**Los datos** (`data/derived/`): la clasificación por contenido, la de Montecchi 2019, y el corpus
etrusco de OpenEtruscan.

**32 tests**, y un workflow de GitHub Actions que los corre junto al manifiesto en cada push.

## Después de subir

1. **Zenodo**, para el DOI. El repositorio ya trae `CITATION.cff` y la licencia. Con el DOI se
   desbloquea el artículo de software y se puede escribir a OpenEtruscan.
2. Decidir qué sale de `data/raw` antes de hacer público el repositorio; ver `data/README.md`.

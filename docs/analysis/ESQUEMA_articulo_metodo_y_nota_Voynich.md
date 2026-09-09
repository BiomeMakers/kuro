# (b) Artículo de método: "What a 7,000-sign corpus can and cannot say: null-model tests on Linear A, calibrated on Etruscan"

Público: humanidades computacionales / epigrafía egea (JOCAA, DSH, o el volumen Salgarella-Petrakis si admite contribuciones). Valor independiente de cualquier lectura.

## Estructura (según tu norma de preprints)
Título corto con referente ("the null-model test"), abstract problema → origen → solución con el montaje de validación; conclusión dentro de la discusión; fórmulas numeradas (JSD, Mantel, MI, curveball); figuras de proceso.

## Marco desde WoLA (Salgarella & Petrakis eds. 2025, AURA Suppl. 15)
- Epígrafe: Younger 2024, "I can read Linear A; I just don't know what every inscription says."
- Tesis de los editores a cuantificar: corpus ~ Pylos Hand 1; "no hay punto crítico de cantidad"; el obstáculo es la falta de pariente. Nuestros análisis de potencia son su número.
- Davis (silabotáctica): una lengua en todo el A y en el disco; afijación no IE ni afroasiática. Reconciliar: nuestro perfil de onsets mide registro/vocabulario, no fonología; citar Duhoux 2020 (¿lengua o lenguas?) y la nota de los editores de que diversidad regional no contradice unidad.
- Hogan 2025: red de coocurrencia previa (grado); nuestro delta = nulos, tipos de documento, monopolios.
- Anastasiadou 2025: prefijo A- en rodeles con numerales (toca ja-/a-).
- RILA-S1 2024: inscripciones nuevas fuera de nuestro corpus; cetro de Cnosos (Kanta et al. 2024) pendiente.

## Secciones y qué hay ya en el paquete
1. Necesidad: el campo produce lecturas por sonido y descripciones sin nulo; Nepal & Perono Cacciafoco 2024 declaran tres limitaciones (filtrado de coincidencias, préstamo vs azar, corpus pequeño). [decipher_screen.py]
2. Calibración en etrusco: genitivo ante clan 58% vs 26%; síncopa como época (p<0.002 dentro de ciudad); sibilantes como sitio (p=0.72 al controlar ciudad). El método distingue gramática, tiempo y geografía donde se conocen. [etr_calib.py, etr_syncope.py]
3. Potencia: 68 pares en etrusco; suelo de distancia 0.198 a n=42 en Lineal A; qué preguntas están por encima del umbral. [omegan_within.py, subcorpus.py]
4. Resultados con nulo en Lineal A:
   4.1 No es griego ni en su silabario (0.104; nulo de inventario 0.092; suelo 0.02). [skeleton.py]
   4.2 Cuentas y culto tan distintos como del griego (0.193 vs 0.194); causas confundidas (género, sitio, lengua, época). [subcorpus.py]
   4.3 Variantes de la fórmula de libación: sitio, no concordancia (p 0.011 → 0.16). [conversación 2-sep]
   4.4 ja-/a- por sitio (7‰ HT vs 140-240‰ santuarios). [conversación 2-sep]
   4.5 Supervivencia en Cnosos: 20 nombres helenizados (regla -U/-E → -o), p<0.003; Pilos y Tebas en el azar; culto 0. [names_survival.py]
   4.6 Teónimos y nombres comunes: pa-de, a-ta-na (p=0.04); sa-sa-me plausible; ki-ri-ta descartada por contexto. [gods_nouns.py, spices.py]
   4.7 Sufijos -ja, -te, -se al doble del azar; sin "hijo de". [filiation.py]
   4.8 Tipos de documento y etiquetado funcional del léxico; cadenas de grado 2-3; cabeceras de sa-ra en distribución complementaria. [doctype_labels.py, metaweb.py]
   4.9 Cribado de lenguas: todas 1.3-1.7x sobre su propio nulo. [decipher_screen.py]
5. Negativos de método: Omega-N no proyecta valores A↔B (rol = lengua); fiabilidad test-retest nula a este tamaño (condición S3 para screen()). [omegan_official.py, omegan_within.py]
6. Discusión: mapa de lo afirmable; el orden función → contexto → forma; KU-PA como caso que lo cumple (remitir a la nota).
7. Declaración de IA; propiedad intelectual; referencias completas.

## (c) Nota Voynich para Cryptologia: "A pre-registered fingerprint and a hybrid generator: where the best published mechanism fails"
- Huella de 11 métricas, holdout por cuadernos, tolerancia entre cuadernos (Voynich vs sí mismo 0.43). [fp.py]
- Naibbe 1.15 (reproducido sobre latín de época); híbrido con cartas pegajosas 0.97 en holdout; el hueco es la métrica de vecinos (234 vs 109-150). [hybrid.py, rivals.py]
- Cifrado de unidades mayores: conflicto estructural vecinos/longitud/entropía. [slotcipher.py]
- Género: forma de herbario, texto sin firma de género (fórmulas, numerales, TTR). [paras.py, genre.py]
- Metacomunidad: sin estructura temática entre páginas; abundancias en un solo eje ortográfico. [voy_metaweb.py, voy_abund.py]
- Disco: registro de culto, cercano a santuarios minoicos; aviso sobre la transcripción corrupta de Chavadakis 2026. [disc_register.py]
- Conclusión: el mecanismo mínimo compatible es escritura sin texto (autocopia) o cifrado que rompe fórmulas; predicciones.

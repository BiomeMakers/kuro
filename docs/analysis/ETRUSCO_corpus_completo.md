# El corpus etrusco completo, y la calibración rehecha (9 de septiembre de 2026)

Obtenido el corpus de OpenEtruscan desde Zenodo: `openetruscan_clean.csv` y su versión agrupada con `dup_group_id`. Sustituye a la muestra con la que habíamos calibrado.

## 1. Qué es

**6.567 filas, 5.941 textos distintos** una vez agrupados por identidad de texto normalizado. De ellos, 5.470 en calidad "clean"; 319 con OCR fallido y 154 marcados para revisión, que se excluyen.

Cada entrada trae el texto en alfabeto etrusco, su transliteración canónica, la versión solo de palabras, y cuando existe, traducción (1.800 casos) y fecha (307).

**El vocabulario: 8.665 palabras totales, 5.661 tipos distintos, y un 85% de hapax.** Esa tasa es todavía mayor que la del Lineal A (76%), lo que hace del etrusco un buen calibrador: si un instrumento encuentra estructura ahí, la encontrará en cualquier corpus epigráfico.

Las palabras más frecuentes son *mi* ("yo", en las fórmulas de propiedad) con 135 apariciones, y luego una serie de prenombres: *larθi*, *vel*, *arnθ*, *θania*, *larθ*, con sus abreviaturas.

## 2. La calibración, rehecha con el corpus completo

El control positivo del etrusco es que el instrumento recupere el genitivo en **-l** ante los términos de filiación, que es un hecho establecido del campo.

| ancla | casos | terminan en -l | esperado por azar | p |
|---|---|---|---|---|
| **clan** ("hijo de") | 18 | **11 (61%)** | 1,4 | **< 0,0005** |
| **sec** ("hija de") | 13 | **5 (38%)** | 1,0 | **0,0035** |
| puia ("esposa") | 12 | 1 | 0,9 | 0,63 |
| lupu ("murió") | 9 | 1 | 0,7 | 0,50 |

**El control pasa, y pasa con la especificidad correcta.** El genitivo aparece ante los dos términos de filiación y no ante *puia* ni ante *lupu*, que no rigen genitivo. Un instrumento que marcara todo por igual estaría produciendo ruido; este distingue.

Y la comparación con el fondo es fuerte: la terminación en -l representa el 5% del vocabulario etrusco, y ante *clan* sube al 61%.

## 3. Qué cambia respecto de la calibración anterior

La versión previa del artículo de método decía que el instrumento "recupera el genitivo ante *clan*" sin dar cifras, porque estaba hecho sobre una muestra. **Ahora hay número, nulo y p, sobre el corpus completo**, y además el resultado gana un rasgo que no teníamos: la especificidad, es decir, que el efecto aparece donde la gramática lo predice y no donde no.

Eso es exactamente lo que un control positivo debe demostrar, y hasta ahora lo estábamos afirmando a medias.

## 4. Y una nota sobre la fuente
OpenEtruscan es un proyecto de epigrafía computacional de código abierto que publica su corpus en Zenodo con DOI, mantiene un preregistro de sus métricas y un manifiesto que su integración continua verifica para que ninguna cifra pública se desvíe de la declarada. Han retirado públicamente un resultado propio de clasificación que afirmaba un 99% de F1, dejando la nota de retractación en todas sus superficies.

Es, en la práctica, la infraestructura de lo que nuestro protocolo de mínimos pide, montada por otro equipo y para otro corpus. Merece citarse en el artículo de método por eso, y no solo como fuente de datos.

## 5. Pendiente
El corpus trae traducción en 1.800 entradas. Eso permite algo que no habíamos considerado: **usar el etrusco como corpus con respuesta parcialmente conocida para calibrar la detección de fórmulas**, ya que un tercio de los textos tiene sentido conocido. Es una calibración mejor que la actual y no cuesta datos nuevos.

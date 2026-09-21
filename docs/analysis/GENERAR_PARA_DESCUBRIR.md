# Generar texto minoico para descubrir lo que falta (15-sep)

## La idea, y por qué es distinta

Todo lo anterior de este proyecto es de **pertenencia**: ¿existe esta palabra en aquel léxico? Y ya sabemos que con léxicos grandes todo encaja.

La propuesta fue otra: **tratar el corpus como una comunidad y compararlo por arquitectura**. Llevada a su forma útil, se convierte en un diagnóstico: **generar texto minoico sintético con todo lo que se ha medido, y ver en qué se distingue del real**. Lo que falle señala una regla que no tenemos.

## El generador

Se le dio, todo medido en este proyecto: la distribución de longitudes de unidad, la frecuencia de cada signo **por posición** (inicial, medial, final), la dependencia entre sílabas contiguas, y las siete sílabas que el sistema no parece tener.

No se le dio nada más. Con eso generó 501 unidades, el tamaño del corpus íntegro.

## Qué captura y qué no

| rasgo (ninguno se le dio) | real | sintético | |
|---|---|---|---|
| tipos de signo | 59 | 57 | capturado |
| **reduplicación** | 0,080 | 0,086 | **capturado, y sale solo** |
| entropía | 5,470 | 5,440 | capturado |
| **trigramas reutilizados** | **0,050** | **0,014** | **falta una regla** |
| hapax | 0,034 | 0,018 | falta una regla |
| unidades repetidas | 0,000 | 0,031 | artefacto del método |

**La reduplicación emerge sin haberla programado**, de la dependencia entre sílabas. Eso es una comprobación de que el modelo captura algo real.

**Y el fallo señala dónde mirar:** el minoico reutiliza bloques de tres sílabas **tres veces más** de lo que la fonotáctica local explica.

## Lo que había detrás del fallo

**5,0% de los trigramas se reutilizan, frente a 1,6% de un nulo con la misma fonotáctica. p < 0,0005**, 400 repeticiones.

Y los bloques, vistos uno a uno, son morfología:

| par | relación |
|---|---|
| **DA-KU-SE-NE / DA-KU-SE-NE-TI** | misma raíz, sufijo *-TI* |
| **PA-RA-NE / A-PA-RA-NE** | misma raíz, prefijo *A-* |
| **PI-MI-TA-TI-RA₂ / DU-MI-TA-TI-RA₂** | mismo final, primera sílaba distinta |
| **A-KU-MI-NA / KU-MI-NA-QE / A-DU-KU-MI-NA** | una base con tres tratamientos |
| **I-PI-NA-MA / I-PI-NA-MI-NA** | misma base, final distinto |
| **ZU-RI-NI-MA / I-ZU-RI-NI-TA** | prefijo y sufijo a la vez |
| **U-NA-KA-NA-SI / U-NA-KA-NA-SI-OLE** | la misma con logograma añadido |

**Y el reparto es tajante: 56% de los bloques reutilizados están al inicio de la palabra, 44% al final, y ninguno en medio.** Viven en los bordes, que es donde viven las raíces y los afijos.

## Por qué la prueba de Kober no lo vio

La prueba de Kober exige que una alternancia de terminación recurra **entre tres o más raíces distintas**, que es lo que hace falta para establecer un paradigma flexivo. A 501 unidades esa prueba tiene potencia cero, y dio 4 puentes frente a 6,6 del nulo.

Esto es más débil y por eso se detecta: **no busca paradigmas, busca reutilización de material**. Y encuentra pares, no series.

Lo que establece es que **hay morfología derivativa visible** (prefijo *A-*, sufijos *-TI*, *-QE*, *-NE*), no que haya flexión.

## Dónde deja el problema

**No da valores fonéticos.** Da una lista de raíces candidatas y de afijos candidatos, medida contra un nulo que respeta la fonotáctica.

**Y da un instrumento nuevo:** un nulo generativo. Todos los nulos de este proyecto barajan sílabas y destruyen estructura que sabemos que existe. Un candidato que supere a texto minoico sintético habrá superado una prueba mucho más dura que un barajado.

El generador queda en el repositorio para eso.


---

## Lo que NO se sigue: el techo de potencia no es artificial

Si los afijos detectados fueran productivos, unidades que contamos como palabras distintas serían formas de la misma, el vocabulario efectivo sería menor, y parte del suelo de potencia que ha tumbado casi todas las pruebas de este proyecto sería artificio de contar mal.

**No es el caso.** Buscando familias por prefijo o sufijo de una sílaba sobre los 501 tipos íntegros: **29 familias con dos o más formas, que implican 57 unidades, el 11% del vocabulario.** Contra el nulo generativo (200 corridas, mismo tamaño, misma fonotáctica): **20,9 esperadas de media, máximo 34. p = 0,07.** No alcanza significación.

Y aunque la alcanzara, **el vocabulario efectivo pasaría de 501 a 473 unidades, un 6% menos**, que no mueve ninguna prueba de potencia.

**Lo que el método sí hace es acertar donde hay respuesta conocida**: recupera `JA-SA-SA-RA` con `JA-SA-SA-RA-MA` y `SA-SA-RA-ME`, las variantes del nombre divino de la fórmula, y **`DA-MA-TE` con `I-DA-MA-TE`**, que es la inscripción de las hachas de Arkalochori. Encuentra las reales y no encuentra suficientes nuevas.

**El techo de potencia es del corpus, no de cómo lo contamos.**

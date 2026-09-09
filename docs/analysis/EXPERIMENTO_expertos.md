# Experimento con expertos: ¿ayuda kuro a clasificar palabras en un corpus que no se conoce de memoria?

Diseño a la manera de Ithaca (Assael et al. 2022): se mide al experto solo, al modelo solo y al experto con el modelo, en una tarea con respuesta conocida.

## La tarea
Para cada palabra del Lineal B que se muestra abajo, con dos o tres contextos reales y sin decir de qué documento se trata, decidir si es NOMBRE de persona o TÉRMINO (oficio, mercancía, cualidad). La respuesta verdadera existe: son palabras cuyo significado el campo tiene establecido. El participante no debe buscarlas en un diccionario.

## Condiciones
Los ítems alternan dos condiciones: **A (sin kuro)**, solo la palabra y sus contextos; **B (con kuro)**, además la clase que predice el modelo y su confianza. Cada participante ve los 24 ítems en el mismo orden; la mitad de los ítems son de cada condición, alternando, de modo que cada participante actúa como su propio control.

## Referencias de comparación (ya medidas)
- Modelo solo: 0,81 de acierto balanceado en validación cruzada sobre 64 palabras etiquetadas (nulo con etiquetas barajadas: 0,66 el bosque, 0,51 la regresión). En los 24 ítems de este test, 19 aciertos de 24 (0,79).
- Experto solo y experto con modelo: es lo que este experimento mide.

## Cómo se analiza
Acierto por condición, con test de McNemar sobre los pares del mismo participante; y comparación con el modelo solo. Con cuatro participantes y 24 ítems hay 96 respuestas, suficiente para detectar una diferencia de 15 puntos con potencia razonable; con menos participantes el resultado se declara indicativo.

## Ítems
(la columna 'verdad' está oculta al participante; se incluye aquí para el que corrija)

| # | palabra | contextos | condición | predicción de kuro | verdad |
|---|---|---|---|---|---|
| 1 | i-je-re-ja | qs v. ] i-je-re-ja TELA+TE [ qs / i-je-re-ja pa-ki-ja-na e-ke-qe [ | A (sin kuro) | — | TERMINO |
| 2 | tu-ru-pte-ri-ja | 4 M 7 tu-ru-pte-ri-ja [ / ku-pi-ri-jo tu-ru-pte-ri-ja o-no LANA 10 | B (con kuro) | TERMINO (74%) | TERMINO |
| 3 | ri-no | 2 [ v.↓ ri-no M [ ] / ri-no / re-po-to qe-te-o | A (sin kuro) | — | TERMINO |
| 4 | tu-na-no | ] da-wi-ja / tu-na-no TELA;1 3 LANA / [ e-ro-pa-ke-ja / tu-na-no TELA;1 1 [ | B (con kuro) | TERMINO (84%) | TERMINO |
| 5 | ka-e-sa-me-no | a-ka-to-wa-o / ka-e-sa-me-no au-ri-jo O [ / me-ta-qe pe-i e-qe-ta ka-e-sa-me-no a-pu2-ka vac. | A (sin kuro) | — | NOMBRE |
| 6 | e-po-mi-jo | qe-ro2 ] 2 e-po-mi-jo 2 [ o-pa-wo-ta / qe-ro2 2 e-po-mi-jo 2 / o-pa-wo | B (con kuro) | TERMINO (57%) | TERMINO |
| 7 | pa-we-a | pa-we-a [ ko-pu-ra / / [ •~• ] pa-we-a [ ] ka-ta-ni-ja | A (sin kuro) | — | TERMINO |
| 8 | ma-ra-tu-wo |  pu2-ke / ma-ra-tu-wo Z 1 [ / V 1  ma-ra-tu-wo V 1 / | B (con kuro) | TERMINO (86%) | TERMINO |
| 9 | ki-ti-ta | vestigia [ ] ki-ti-ta VIR 46 [ / 1 ⟧ o-pi-ke-ri-jo-de ki-ti-ta o-pe-ro-ta ⟦ e | A (sin kuro) | — | TERMINO |
| 10 | me-ri | me-no ] o-ne me-ri *209VAS+A 1 / pa-si-te-o-i / me-ri *209VAS 1 da-pu2-ri-to-jo | B (con kuro) | TERMINO (86%) | TERMINO |
| 11 | ru-ko-ro | ru-ko-ro e-ke o-na-to me-ri-te-wo / ] ru-ko-ro ra-wa-ke-si-jo GRA [ | A (sin kuro) | — | NOMBRE |
| 12 | ko-ri-ja-do-no | ru-ki-ti-jo ko-ri-ja-do-no AROM 1 T / ] ko-ri-ja-do-no ] jo AROM | B (con kuro) | TERMINO (73%) | TERMINO |
| 13 | a-ta-o | HORD [ ] a-ta-o / ti-nwa-si-jo HORD / ja-so-ro Z 1 a-ta-o [  e-pi-do-ro-mo | A (sin kuro) | — | NOMBRE |
| 14 | po-me | to-mo VIR 1 po-me [ •~• ] / ti-qa-jo po-me e-ke-qe dwo ko-to-no | B (con kuro) | NOMBRE (63%) | TERMINO |
| 15 | e-ti-ra-wo | OVIS:m 95 ma-ro-pi e-ti-ra-wo pa-ra-jo OVIS:m 70 / 100 X pa-ro e-ti-ra-wo OVIS:m 100 X | A (sin kuro) | — | NOMBRE |
| 16 | a-to-po-qo | to-wo-ko VIR 4 a-to-po-qo VIR 3 v. /  vac.  a-to-po-qo [ ] vac. | B (con kuro) | NOMBRE (65%) | TERMINO |
| 17 | qa-si-re-u | 3 X a-ke-ro qa-si-re-u AUR P 3 / ⟦ ⟧ e-ri-ko-wo qa-si-re-u 1 to-so-de ka-ko | A (sin kuro) | — | TERMINO |
| 18 | a-pi-me-de | a-pi-me-de e-ke-qe e-to-ni-jo ke-ke-me-na-o / ki-ri-ja-si VIR [ a-pi-me-de VIR [ | B (con kuro) | NOMBRE (81%) | NOMBRE |
| 19 | qe-ta-ko | ri-jo [ ] qe-ta-ko OVIS:f [ qs / na-ma-ru-ko CAP:f 1 qe-ta-ko ke-ra-me-u CAP:f 1 | A (sin kuro) | — | NOMBRE |
| 20 | ne-qe-u | ZE 1 [ ne-qe-u e-te-wo-ke-re-we-i-jo to-to we-to / AES M 5 ne-qe-u AES M 3 | B (con kuro) | NOMBRE (51%) | NOMBRE |
| 21 | ka-ke-we | a-ka-si-jo-ne ka-ke-we ta-ra-si-ja e-ko-te pi-ra-me-no / to-so-de a-ta-ra-si-jo [ ka-ke-we ] ⟦ ⟧ | A (sin kuro) | — | TERMINO |
| 22 | ku-ru-so | 1 ] -te-te ku-ru-so ⟦ ku-ru-so ⟧ / ] ku-ru-so po-ro-we [ | B (con kuro) | TERMINO (91%) | TERMINO |
| 23 | pa-ra-jo | ma-ro-pi qe-re-wa-o pa-ra-jo OVIS:m 136 ma-ro-pi / da-a2 a-ta-wo-ne-jo ] pa-ra-jo po-ne-to-qe-mi ] •-• | A (sin kuro) | — | TERMINO |
| 24 | ki-ri-te-wi-ja | i-je-ro S 2 ki-ri-te-wi-ja [ di-wo-pu-ka-ta S / ki-ri-te-wi-ja e-ko-si-qe o [ | B (con kuro) | TERMINO (53%) | TERMINO |

## Hoja de respuesta (para el participante, sin la última columna)
Copiar las columnas 1 a 5 y añadir una columna 'mi respuesta' con NOMBRE o TÉRMINO.

## A quién proponérselo
Micenólogos que no trabajen a diario con estas series: Piquero, Jiménez Delgado, Varias; y como control, dos personas con formación filológica sin especialidad micénica. Cuatro o cinco respuestas bastan para una nota; el experimento se describe en el artículo del software como validación de uso.

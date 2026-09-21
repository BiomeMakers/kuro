# El marco para escrituras mixtas, y su primera validación en el Lineal B (13-sep, noche)

## Qué se construyó

`kuro/mixed.py`, seis tests. Un marco de desciframiento que trata el corpus como lo que es, silabario más logogramas más ligaduras más fracciones, extendiendo el modelo de Luo y colaboradores (2021) desde alfabetos a silabarios CV: cada signo se descompone en consonante y vocal con rasgos IPA, los logogramas y las fracciones se tratan como tramos no emparejados, y la ligadura se añade como restricción sobre el valor del signo ligado. Nadie lo ha construido; el MIT lo deja expresamente fuera de su alcance.

Sobre el Lineal B clasifica 13.961 unidades, 158 ligaduras, 3.505 logogramas de 25 tipos y 11.390 numerales.

## La validación, que es lo que importa

La restricción de ligadura se probó en el Lineal B, donde el valor de cada signo se conoce, en sus dos formulaciones naturales.

**Acrofonía de la mercancía** (el signo ligado es la primera sílaba de una palabra del campo del logograma): **2 aciertos de 10, nulo 0,9, p = 0,22.**

**Abreviatura del calificador adyacente** (el signo ligado es la primera sílaba de una palabra que aparece junto al logograma): **4 de 11, nulo 3,23, p = 0,41.**

**Las dos fallan.** En el Lineal B, OLE+PA es *pa-ko-we* "con salvia", OLE+A es *a-ro-pa* "ungüento", CYP+KU es *ku-pa-ro*. Cada caso tiene su explicación y el campo las conoce; lo que no hay es una regla que un modelo pueda aplicar sin saber ya la respuesta.

## Consecuencias

**Se retiran los 36 bits** atribuidos esta tarde a la ligadura como restricción de valor en el Lineal A. Estaban calculados bajo la primera formulación, y el Lineal B la desmiente.

**Se mantiene el hecho distribucional**: el silabograma ligado del Lineal A va con su mercancía en 16 de 26 casos, p < 0,0005. Es una regla de la escritura. Lo que no es, es una vía hacia los valores, porque qué abrevia cada signo no se deja predecir ni siquiera donde se conoce.

**Y el marco queda en pie como herramienta**, validada en lo que clasifica y refutada en lo que restringía. Su primer producto es este negativo, obtenido donde se podía comprobar y antes de tocar el Lineal A. Sin el Lineal B, la restricción se habría publicado.

Vigesimotercera vía cerrada.

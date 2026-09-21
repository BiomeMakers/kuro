# El intento: la rejilla del Lineal B puntuada contra sus dos controles (12-sep)

> **NOTA (12-sep).** La señal léxica débil que aquí se describe (z 2,7-2,9 sobre el corpus barajado) quedó reinterpretada la misma noche por LA_BUSQUEDA.md: la optimización encuentra rejillas 2,4 veces mejores cambiando 37 de 38 signos, de modo que el encaje léxico no discrimina. La medida sigue siendo correcta; su lectura como 'algo de señal' debe tomarse con ese resultado delante.

Hasta hoy habíamos medido piezas. Un **intento** es el conjunto: asignar un valor a cada signo, aplicarlo a todo el corpus y puntuar el resultado contra los controles que corresponden. Esto es lo que ninguna de las nueve propuestas de setenta años ha hecho, y lo que ahora corre en `kuro/attempt.py`.

**Montaje.** 455 unidades silábicas íntegras; léxico de 16.147 formas glosadas (acadio, ugarítico del DULAT y sumerio, sin nombres propios); dieciséis signos anclados por los topónimos compartidos con el Lineal B, 38 libres. Se puntúa cuántas unidades se convierten en palabras atestiguadas de la lengua diana.

**Dos controles, no uno.** El de Packard (1974): rejillas ficticias que permutan los valores de modo que ningún signo conserve el suyo. Y el nuestro: el corpus con las sílabas barajadas, leído con la rejilla verdadera. El primero pregunta si los valores importan; el segundo, si la ventaja no viene simplemente de que las secuencias reales sean fonotácticamente naturales.

## Resultado

| | fonología permisiva | fonología estricta |
|---|---|---|
| **corpus real con la rejilla del Lineal B** | **75** | **40** |
| rejillas ficticias (Packard, 40) | 41,5 de media, máximo 62 | 24,4 de media, máximo 39 |
| corpus barajado con la rejilla real (20) | 58,3 de media, máximo 69 | 29,1 de media, máximo 36 |
| **z del real frente al barajado** | **2,69** | **2,92** |

**El corpus real leído con los valores del Lineal B supera los dos controles, y lo hace con las dos fonologías.** Bate a todas las rejillas ficticias (75 contra un máximo de 62; 40 contra un máximo de 39) y queda a 2,7-2,9 desviaciones por encima del corpus barajado.

## Cómo leerlo, con sus límites por delante

**Lo que dice.** Las palabras reales del Lineal A, leídas con los valores del Lineal B, producen más palabras de diccionario acadias, ugaríticas o sumerias que (a) las mismas palabras con valores permutados y (b) palabras falsas con los valores verdaderos. Los dos controles descartan las dos explicaciones triviales, y el efecto es consistente bajo las dos hipótesis fonológicas, que difieren en 243 bits.

**Lo que no dice.** Setenta y cinco de 455 unidades es el 16,5%, y el exceso sobre lo esperado son unas diecisiete unidades. Un z de 2,7 no es un desciframiento ni de lejos: es una señal débil que hay que replicar. Y no está corregido por el número de pruebas que hemos corrido hoy, que es alto.

**Y lo que no puede decidir.** Si esas diecisiete unidades son préstamos de mercancía (que sabemos que existen: KU-MI-NA-QE, KU-PA, SA-SA-ME), onomástica compartida por el comercio, o una relación de lengua. La prueba no distingue esas tres cosas, y las tres predicen lo mismo.

**El componente funcional sigue en cero.** Ninguna de las 42 unidades con función medida produce, bajo ninguna rejilla probada, una palabra que además signifique lo que la posición exige. La señal está en el léxico y no en el sentido, que es justamente donde una relación de lengua debería dejarla.

## Por qué esto importa aunque sea débil
Es la primera vez que la rejilla estándar del Lineal B, que es el punto de partida de las nueve propuestas, se pone a prueba contra los dos controles que le corresponden. El resultado es que **carga algo de señal**, lo que nadie había demostrado, y **mucho menos de la que cualquier desciframiento necesita**, que es lo que todos han asumido sin medir.

# Los tres intentos, puntuados en la misma escala (12-sep)

Hasta ahora se habían medido piezas. Un **intento** es la cosa entera: asignar un valor a cada uno de los signos libres, aplicar la asignación a las 552 unidades silábicas íntegras del corpus, y puntuar el resultado. Tres puntuaciones independientes:

- **léxica**: cuántas unidades se convierten en palabras reales de la lengua diana;
- **funcional**: cuántas de las unidades con función medida se convierten en palabras cuyo **significado** es el que la distribución exige;
- **control**: la misma puntuación sobre rejillas ficticias en el sentido de Packard (1974), que es lo único que dice si una puntuación significa algo.

Los dieciséis signos anclados por los topónimos compartidos con el Lineal B se mantienen fijos. Búsqueda por recocido simulado sobre los 94 libres, con 85 valores posibles. Implementado en `kuro/attempt.py` con cuatro tests.

## Resultados

### Ugarítico (2.362 lemas glosados del DULAT)

| | léxica | funcional | z frente al control |
|---|---|---|---|
| rejilla del Lineal B tal cual | **1** de 552 | 0 | 1,15 |
| rejillas ficticias (Packard) | 0,4 | 0,00 | — |
| **mejor asignación hallada por búsqueda** | **73-76** | **0** | **119-130** |

### Acadio (9.556 lemas glosados de ORACC)

| | léxica | funcional | z frente al control |
|---|---|---|---|
| rejilla del Lineal B tal cual (permisiva) | 66 de 552 | 0 | 3,43 |
| rejillas ficticias | 33,1 (sd 9,6) | 0,00 | — |
| **mejor asignación hallada** | **266** | **0** | **24,3** |
| rejilla del Lineal B (estricta) | 38 | 0 | 2,66 |
| **mejor asignación (estricta)** | **241** | **0** | **35,9** |

## Lo que dicen, y es lo más importante que hemos medido

**1. La búsqueda encuentra siempre una asignación espectacular.** Con el acadio, el recocido halla una rejilla que convierte **266 de 552 unidades en palabras acadias reales**, a 24 desviaciones típicas del control. Casi la mitad del corpus "se lee". Cualquiera que publicase eso tendría un desciframiento de aspecto abrumador.

**2. Esa asignación no es la del Lineal B.** La rejilla estándar, la que todo el campo usa y la que di Mino usa, produce 66 (permisiva) o 38 (estricta). La búsqueda la multiplica por cuatro o por seis eligiendo otros valores. Es decir: **el criterio léxico premia a las rejillas equivocadas más que a la recibida.** Es la demostración experimental, sobre el corpus real, de lo que Packard argumentó en 1974.

**3. Y la puntuación funcional es cero en todos los casos.** Ni la rejilla del Lineal B, ni las ficticias, ni la mejor que encuentra la búsqueda con 266 palabras acadias, colocan una sola palabra con el significado que su posición en la cuenta exige. **Ninguna de las 552 unidades leídas como acadio o ugarítico dice lo que la distribución obliga a que diga.**

**4. Las dos fonologías dan lo mismo.** La permisiva infla los números absolutos (66 frente a 38 en la rejilla del B; 33 frente a 22 en el control) pero no cambia ninguna conclusión.

## Por qué esto importa más que cualquier veredicto

El criterio con el que se han juzgado nueve desciframientos en setenta años es el léxico: cuántas palabras salen. Aquí se ve que ese criterio **es satisfacible por búsqueda**: basta con dejar que un algoritmo elija los valores y produce 266 palabras acadias del corpus minoico. No prueba nada sobre el acadio ni sobre el minoico, y prueba todo sobre el criterio.

El criterio funcional, en cambio, **no es satisfacible por búsqueda**: veinte mil pasos de recocido optimizando explícitamente hacia él no consiguen ni uno. Eso lo convierte en el criterio que hay que usar, y en el que cualquier propuesta futura debería declarar.

**El límite, dicho.** Catorce unidades con función medida en una clase probada es poco, y el léxico glosado es una fracción del vocabulario real de las dos lenguas. Un cero sobre catorce con léxicos parciales no cierra nada; lo que establece es que **la prueba existe, se puede correr en minutos, y ninguna propuesta publicada la ha pasado nunca, empezando por la rejilla estándar del campo.**

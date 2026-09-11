# La reconstrucción cruzada de la fórmula: primer resultado predictivo del proyecto (10 de septiembre de 2026)

Línea traída de M-RADAR y corrida a mano antes de tocar la herramienta, según la hoja de ruta. Es el
primer experimento del proyecto que **predice sobre material apartado**, que es el tercer requisito
del protocolo y el que nunca habíamos cumplido.

## 1. El diseño

Dieciocho inscripciones de la fórmula de libación en las que se localiza el ancla de apertura
(A-TA-I-\*301-WA-JA y sus variantes). Cada elemento se indexa por su **posición relativa al ancla**,
no absoluta, de modo que inscripciones con distinto principio quedan comparables.

Para cada hueco: se aparta esa inscripción entera, se predice el elemento a partir de las diecisiete
restantes por lo que ocupa esa posición relativa, y se comprueba contra lo que hay.

## 2. La fuga que hubo que quitar, y es la parte importante

La primera corrida dio **20,2% de acierto frente a 13,1% de tasa base, con p < 0,0005**. Parecía un
resultado claro.

**Al mirar los aciertos uno por uno, once de los diecisiete eran la posición 0: el ancla.** Es decir,
alineábamos por el ancla y luego "predecíamos" el ancla. Circular, y con una tasa de acierto del 61%
en esa posición que arrastraba todo el resultado.

Es la misma clase de error que retiramos tres veces en agosto, con una forma nueva: **no un nulo mal
construido, sino una fuga entre el procedimiento de alineación y lo que se evalúa.**

## 3. El resultado, sin la fuga

| | |
|---|---|
| huecos predichos | 66 |
| acierto por posición relativa | **6 (9,1%)** |
| acierto por tasa base | 5 (7,6%) |
| nulo (barajar dentro de cada inscripción, 2000 veces) | media 3,0%, p95 7,6% |
| **p** | **0,042** |

**Supera el nulo, y por poco.** El acierto es del 9,1% contra un 3,0% esperado, con p = 0,042.

## 4. Cómo hay que leer esto, con cuidado

**Es un resultado pequeño y en el borde.** Seis aciertos de sesenta y seis, y una p que con cualquier
corrección por comparaciones múltiples no sobreviviría. Como afirmación aislada no vale gran cosa.

**Pero es la clase de resultado que el proyecto no tenía:** una predicción sobre material apartado,
medida contra su tasa base y contra un nulo. Todo lo demás que hemos hecho describe el corpus; esto
predice una parte de él desde otra.

**Y el margen sobre la tasa base es estrecho** (9,1% contra 7,6%), lo que dice que **la posición
relativa aporta poco por encima de saber qué elemento es más frecuente.** Eso también es información:
la fórmula es menos rígida de lo que su reputación sugiere, o dieciocho inscripciones no bastan para
aprender su plantilla.

## 5. Qué haría falta para que esto valiera un artículo

**Más señal por hueco.** Ahora se predice solo por posición. Un predictor que usara además **qué
elementos acompañan** al hueco en la misma inscripción tendría más de donde tirar, y eso es lo que
M-RADAR llama comparación cruzada.

**Y el control que sí tenemos y ellos no:** medir contra los huecos de las **completas**, que es lo
que hemos hecho. Ese es el control positivo que su trabajo no declara y que aquí es el diseño entero.

## 6. Y para la hoja de ruta
El paso 1 **funciona, en el límite**. Según lo acordado, eso autoriza el paso 2: añadir el tipo
predictivo al ciclo con su nulo de tasa base. Pero antes conviene probar el predictor mejorado a
mano, porque si con acompañantes el acierto sube claramente, el tipo predictivo nace ya con un caso
que lo justifica; y si no sube, la línea se cierra sin haber construido nada.


---

## 7. EL PREDICTOR MEJORADO, CORRIDO

Añadida la idea que M-RADAR llama comparación cruzada: además de la posición, **qué otros elementos
acompañan al hueco en la misma inscripción**. Un candidato pesa más si la inscripción de la que viene
comparte elementos con la que se está reconstruyendo.

| predictor | aciertos de 66 | tasa |
|---|---|---|
| tasa base (el elemento más frecuente) | 5 | 7,6% |
| solo posición | 6 | 9,1% |
| **posición + compañeros** | **8** | **12,1%** |
| nulo (2000 permutaciones) | | 3,6% de media, p95 en 7,6% |

**p = 0,006**, frente al 0,042 del predictor solo por posición. **Los compañeros aportan, y aportan
más que la posición.**

### Los ocho aciertos, que dicen dónde está la señal

| inscripción | posición | elemento |
|---|---|---|
| IO Za 2, TL Za 1, PS Za 2, IO Za 6 | +2 | **JA-SA-SA-RA-ME** |
| IO Za 2, TL Za 1 | +4 | **I-PI-NA-MA** |
| IO Za 2, TL Za 1 | +5 | **SI-RU-TE** |

**Los aciertos se concentran en los tres elementos que nuestro trabajo anterior identificó como
fijos** de la fórmula, y en las inscripciones más completas. Es decir: **el predictor acierta donde
hay plantilla y falla donde hay relleno**, que es exactamente lo que la lectura de la fórmula
predecía y no habíamos comprobado de esta manera.

### Y el peso no está ajustado a posteriori
Se eligió w = 2 antes de mirar el resultado. Comprobada la sensibilidad: la mejora aparece ya en
w = 1, se mantiene en w = 2, y decae ligeramente a partir de w = 3. **No hay un pico estrecho que
delataría un ajuste al dato.**

## 8. Qué autoriza esto

El paso 1 de la hoja de ruta ha funcionado en sus dos versiones, y **la mejorada da un resultado
sustancialmente mejor que la simple**. Eso cumple la condición que pusimos para el paso 2: el tipo
predictivo del ciclo nace con un caso que lo justifica.

**Y hay una afirmación publicable que antes no teníamos**, formulada como debe: los elementos fijos
de la fórmula de libación se pueden predecir en inscripciones apartadas por encima de su tasa base y
de un nulo de permutación (12,1% frente a 7,6% y 3,6%, p = 0,006), y **el acierto se concentra en las
tres posiciones que el análisis distribucional había identificado como fijas**, lo que es una
confirmación independiente de esa lectura.

**Qué la refutaría:** que al añadir inscripciones nuevas de la fórmula el acierto cayera a la tasa
base, o que los aciertos dejaran de concentrarse en las posiciones fijas.

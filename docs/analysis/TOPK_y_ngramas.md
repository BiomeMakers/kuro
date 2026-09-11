# El Top-k y la línea base de n-gramas: dos hallazgos y una corrección grande (10 de septiembre de 2026)

Aplicadas al experimento de la fórmula las dos prácticas que el survey del campo documenta y nosotros
no seguíamos. El resultado cambia cómo hay que escribirlo.

---

## 1. La tabla, con el n-grama construido sin fuga

| | Top-1 | Top-3 | Top-5 | Top-10 | Top-20 |
|---|---|---|---|---|---|
| **nuestro predictor** | **14,0%** | 14,0% | 14,0% | 14,0% | 14,0% |
| **línea base de n-gramas** | **17,5%** | 19,3% | 21,1% | 22,8% | 22,8% |
| elemento más frecuente | 8,8% | 19,3% | 21,1% | 22,8% | 24,6% |

**Nuestro predictor pierde contra la línea base estándar del campo.** El n-grama, que predice a partir
del elemento inmediatamente anterior, acierta 17,5% en Top-1 frente a nuestro 14,0%.

**Y una advertencia sobre la primera versión de esta medida:** construí el n-grama con todas las
inscripciones incluida la apartada, y dio **78,9%**. Era fuga, no resultado. Corregido, da 17,5%.
Es el segundo caso de fuga en dos días y con la misma forma: material de prueba dentro del
entrenamiento.

## 2. Por qué nuestro Top-20 es igual a nuestro Top-1, y es el hallazgo

Un predictor normal mejora al ampliar k. El nuestro no mejora nada, y la razón es diagnosticable:

| | |
|---|---|
| huecos evaluados | 57 |
| el elemento verdadero **está** entre los candidatos de esa posición | 8 (**14,0%**) |
| el elemento verdadero **no aparece en ninguna otra inscripción** | 41 (**71,9%**) |

**El techo del predictor es 14,0%, no 100%.** En el 86% de los huecos el elemento verdadero
sencillamente **no está disponible**, y en casi tres cuartas partes de los casos porque es un hapax:
no aparece en ninguna otra inscripción de la fórmula.

**Nuestro 14,0% es, por tanto, el 100% de lo alcanzable.** El predictor acierta todos los huecos que
podía acertar.

## 3. Y eso confirma lo que nuestro propio artículo ya decía

La sección 3.2 del artículo de la fórmula se titula **"los huecos albergan la clase abierta"**, y
medimos hace días que **los treinta y dos rellenos de la fórmula son todos hapax**.

**El experimento predictivo lo confirma desde el otro lado:** no se puede predecir el relleno porque
el relleno es único cada vez; se puede predecir la plantilla porque la plantilla se repite. Los ocho
aciertos son los tres elementos fijos, y los cuarenta y nueve fallos son la clase abierta.

**Eso es un resultado mejor que el que teníamos**, y hay que reescribirlo así: no "predecimos el 12%
de los huecos" sino **"predecimos el 100% de los huecos que la estructura permite predecir, y la
estructura permite predecir el 14%"**.

## 4. Qué hacer con la derrota frente al n-grama

**Declararla, y explicar por qué ocurre.** El n-grama gana porque **puede proponer elementos que
nuestro predictor no considera**: no está limitado a lo que aparece en esa posición relativa, sino a
lo que sigue al elemento anterior en cualquier posición. Tiene un espacio de candidatos mayor y por
eso alcanza un techo mayor (22,8% frente a 14,0%).

**Pero fíjese en dónde ganan:** el n-grama alcanza su techo con k = 10 y luego se estanca; la tasa
base sigue subiendo hasta 24,6% en Top-20 simplemente por acumular candidatos frecuentes. **Los tres
convergen alrededor del 23%**, que es aproximadamente la proporción de huecos ocupados por elementos
no únicos.

**Es decir: el techo de cualquier método sobre este material es un cuarto de los huecos**, y eso es
una propiedad del corpus, no de los modelos. Vale la pena decirlo con esa claridad, porque es
información para cualquiera que intente restaurar Lineal A con métodos más sofisticados.

## 5. Cómo queda el artículo de la fórmula

La sección 4 bis hay que reescribirla entera, y sale **más fuerte y más honesta**:

- el resultado deja de ser "12,1% frente a 7,5%" y pasa a ser **"14,0% de acierto sobre un techo
  estructural del 14,0%"**;
- se declara que **el n-grama estándar del campo alcanza un techo mayor (22,8%) y bate al nuestro en
  Top-1 (17,5% frente a 14,0%)**;
- y se añade lo que ninguno de los dos puede: **el 71,9% de los huecos contiene un elemento que no
  aparece en ninguna otra inscripción**, de modo que ningún método basado en repetición los alcanzará
  jamás.

La conclusión sustantiva no cambia y se refuerza: **la fórmula tiene plantilla fija y relleno único**,
y ahora está medido por tres vías: la distribución, la predicción y el techo.

# La tabla completa de tasas de error (10 de septiembre de 2026)

Diez instrumentos medidos sobre corpus con respuesta conocida o sobre material donde no hay nada que
encontrar. Es lo que permite escribir un p-valor acompañado de lo que ese instrumento se equivoca.

## 1. La tabla

| instrumento | corpus | 5% | 1% | 0,1% |
|---|---|---|---|---|
| **coocurrencia** | Lineal A, palabras | **8,0%** | 4,2% | 2,2% |
| **coocurrencia** | Lineal A, logogramas | **7,2%** | 4,0% | 1,0% |
| coocurrencia | etrusco | 2,2% | 1,2% | 0,5% |
| coocurrencia bipartita, solo grados | Lineal A | 8,0% | 4,0% | 3,0% |
| **coocurrencia bipartita por yacimiento** | Lineal A | **5,5%** | 4,0% | 4,0% |
| posicional | etrusco | 5,3% | 3,5% | 3,5% |
| posicional | Lineal A | 2,9% | 0,0% | 0,0% |
| **predictivo** | Lineal A, sin plantilla | **5,0%** | **0,8%** | 0,8% |
| fracción compartida | Lineal A | 3,5% | 1,8% | 0,8% |
| aritmética | Lineal A | 2,5% | 0,5% | 0,5% |
| Westfall-Young | Lineal A, pares al azar | 6,0% | 4,0% | 3,0% |
| restricciones de categoría | Lineal A | 0,0% | | |
| partición jerárquica | nivel sin sentido | 0,0% | | |
| **adyacencia** | | **no medible** | | |

## 2. Lo que la tabla dice, instrumento a instrumento

**La coocurrencia sigue siendo el peor**, y su versión estratificada por yacimiento lo arregla en el
umbral que importa: de 8,0% a 5,5%. Los dos se informan porque el contraste es el resultado.

**El predictivo se comporta como debe:** 5,0% al 5% nominal, que es exactamente lo que se le pide, y
0,8% al 1%. Cuando dice que ha encontrado algo, se le puede creer.

**El posicional es conservador** en el Lineal A y está en su valor nominal en etrusco.

**La fracción compartida es conservadora**, lo cual importa porque sostiene el argumento de la receta.

**Westfall-Young sale en 6,0%**, ligeramente por encima del nominal. Es esperable: su ajuste usa la
dependencia entre pruebas, y con seis pruebas por ensayo la estimación del mínimo es ruidosa. Habría
que remedirlo con familias mayores.

**Las restricciones de categoría y la partición jerárquica dan 0,0%**, y aquí conviene no
entusiasmarse: no es que sean perfectas, es que **el ensayo que les construí es exigente en un solo
sentido**. Para las restricciones, "acertar" significa eliminar todas las categorías menos una, y eso
casi nunca ocurre con una unidad al azar. Es un límite del ensayo, no una propiedad del instrumento.

## 3. Y la adyacencia, que no se puede medir

Tres intentos, dos corpus, 450 ensayos lanzados y **siete utilizables**. La razón es estructural:
para contrastar una adyacencia hacen falta pares que compartan varios documentos, y ni el Lineal A ni
el etrusco los tienen en cantidad.

**Se informa como no medible, y el código lo impone:** una tasa calculada sobre menos de treinta
ensayos se marca como no medida, porque **un 0,0% sobre siete ensayos parece un instrumento perfecto
y es la ausencia de una medida**. Añadido con su test.

Eso afecta a un resultado nuestro: la adyacencia CYP → NI del artículo de aromáticos **no puede
acompañarse de una tasa de error**, y así hay que escribirlo.

## 4. Lo que esto permite escribir

Cada resultado del proyecto puede ahora llevar su cualificación. Los tres principales:

- **la predicción de la fórmula:** p = 0,007, con un instrumento que se equivoca el 0,8% de las veces
  al umbral del 1% sobre material sin plantilla;
- **la igualdad de fracción de HT 23a:** p < 0,00005, con un instrumento que se equivoca el 0,8% al
  0,1%;
- **el bloque de aromáticos:** con las dos columnas, hipergeométrica y estratificada, y la tasa de
  cada una.

**Y uno que no puede llevarla:** la adyacencia, que se informa sin cualificar y diciendo por qué.

# La tasa de error de los seis instrumentos, y lo que el nulo equivocado hizo (9 de septiembre de 2026)

## 1. La tabla, y hay que leerla por columnas

| instrumento | corpus | 5% | 1% | 0,1% | 0,01% |
|---|---|---|---|---|---|
| coocurrencia | etrusco | 2,2% | 1,2% | 0,5% | 0,5% |
| **coocurrencia** | **Lineal A, palabras** | **8,0%** | **4,2%** | **2,2%** | **1,5%** |
| **coocurrencia** | **Lineal A, logogramas** | **7,2%** | 4,0% | 1,0% | 0,5% |
| posicional | etrusco | 5,3% | 3,5% | 3,5% | 3,5% |
| posicional | Lineal A | 2,9% | 0,0% | 0,0% | 0,0% |
| aritmética | Lineal A | 2,5% | 0,5% | 0,5% | 0,5% |
| restricciones de categoría | Lineal A | 0,0% | 0,0% | 0,0% | 0,0% |
| **fracción compartida** | **Lineal A** | **3,5%** | 1,8% | 0,8% | 0,8% |
| adyacencia | Lineal A | sin medir | | | |

**La coocurrencia sigue siendo el instrumento malo**, y ahora se ve cuánto: al 5% da un 8% de
falsos, pero **incluso a 0,0001 da un 1,5%**, es decir, quince veces su valor nominal. Un resultado
de coocurrencia en este corpus está inflado a cualquier nivel.

**El instrumento de fracción compartida, que sostiene el argumento de la receta, da 3,5% al 5%** y
0,8% a 0,0001. Es conservador, y eso es una buena noticia para el artículo de aromáticos.

**La adyacencia no se pudo medir**: el ensayo solo produjo cinco corridas utilizables, porque hacen
falta pares que compartan varios documentos y el corpus casi no los tiene. **Se informa como sin
medir, no como cero.**

## 2. El aviso falso, y por qué se conserva

La primera medida del instrumento de fracción compartida dio **16,5%**, y durante diez minutos
pareció que el argumento central del artículo de aromáticos se apoyaba en el instrumento menos
fiable de todos.

**Era falso, y la causa era mi nulo.** Lo medí contra un sorteo **uniforme** sobre las diez
fracciones del sistema. Pero las fracciones del corpus no son uniformes ni de lejos:

| fracción | apariciones |
|---|---|
| 1/2 | 120 (41%) |
| 1/4 | 56 (19%) |
| 3/4 | 27 (9%) |
| 1/16 | 26 (9%) |
| las demás | menos |

**El 60% de las fracciones del corpus son 1/2 o 1/4.** Con un nulo uniforme, encontrar dos entradas
iguales parece raro cuando no lo es, y el instrumento parece equivocarse cuando el que se
equivocaba era el nulo.

Con el nulo que conserva la distribución real: **de 19,2% a 3,5%.**

**La medida equivocada se conserva en el fichero**, con su motivo escrito: *"el instrumento nunca
fue el problema; el nulo lo era"*. Y hay un test que falla si alguien la borra.

## 3. Lo que esto cambia en los artículos

**El artículo de aromáticos puede ahora escribir su cifra central cualificada:** la igualdad de
fracción entre entradas secundarias da p < 0,00005 con un instrumento que, en condiciones sin
efecto sobre este mismo corpus, informa de un falso positivo el 0,8% de las veces a ese nivel.

**Y el bloque de coocurrencia debe llevar la advertencia contraria**, porque su instrumento está
inflado a todos los niveles.

## 4. Y la lección, que es la tercera vez esta semana
El primer diagnóstico de un instrumento fue equivocado **por la misma razón por la que retiramos dos
resultados en agosto**: un nulo que no conservaba lo que la pregunta no pretendía explicar. Esta vez
el objeto medido era nuestro propio instrumento, lo cual tiene su gracia.

**El nulo es el sitio donde este proyecto se equivoca**, y ya lleva tres. Merece una comprobación
propia: antes de aceptar una tasa de error, comprobar que el nulo del ensayo conserva la
distribución empírica y no una uniforme cómoda.

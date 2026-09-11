# Métodos de fuera del campo que se pueden traer, con su cita (10 de septiembre de 2026)

La pregunta no era solo qué bibliografía de Lineal A falta, sino qué hay **fuera del lenguaje** que
se pueda aplicar. Todo instrumento que sobrevive en este proyecto vino de fuera: la coocurrencia
hipergeométrica y el nulo de márgenes fijos, de la ecología microbiana; la curva de potencia, del
diseño experimental; el control de captura, de la microscopía. Lo que sigue es el barrido hecho a
propósito.

---

## 1. LO MÁS APLICABLE: minería de reglas de asociación

Una tablilla de Hagia Triada **es una cesta de la compra**: una lista corta de artículos con
cantidades. Ese campo lleva treinta años resolviendo exactamente nuestro problema, y con corpus de
millones de transacciones en vez de mil setecientas.

### Lo que tienen resuelto y nosotros no

**El problema de las comparaciones múltiples a escala de millones de reglas.**
Hämäläinen y Webb, *A Tutorial on Statistically Sound Pattern Discovery* (arXiv:1709.03904).
Es un tutorial, está en abierto, y trata el problema de fondo: **minar reglas es un problema de
pruebas múltiples, y el número de reglas candidatas hace inútil cualquier corrección ingenua.**
Nosotros usamos Bonferroni con dieciocho pruebas y hemos añadido Benjamini-Hochberg por encima de
veinte; ellos tienen procedimientos para millones.

**El procedimiento de permutación de Westfall-Young**, citado en ese tutorial (Terada, Tsuda y Sese
2013, PNAS 110(32), 12996-13001, y su versión rápida). **Es un nulo por permutación que corrige por
múltiples a la vez**, lo cual es exactamente lo que nos falta: hoy corremos el nulo y luego
corregimos, que es menos potente que hacer las dos cosas juntas.

**Y el trabajo empírico sobre qué corrección funciona:** *Controlling False Positives in Association
Rule Mining* (arXiv:1110.6652), que compara métodos de corrección midiendo su capacidad de controlar
falsos positivos **y** de detectar reglas reales. Es la métrica doble que ya sabemos que hace falta
y que nuestro módulo de eficiencia declara no poder calcular.

**Y la distinción de reglas que nos vendría bien tener escrita:** un trabajo reciente
(arXiv:2412.18699) clasifica los resultados de una minería en **accionables, triviales e
inexplicables**. Nuestro generador produce sobre todo triviales, y no tenemos nombre para eso.

### Lo que hay que traer, en concreto
1. **Westfall-Young como nulo con corrección incorporada**, en vez de nulo más Bonferroni.
2. **Lift y leverage** como medidas de interés además del p-valor: dicen cuánto se aparta la
   asociación de la independencia, no solo si se aparta.
3. **Itemsets cerrados y maximales**: evitan informar de cada subconjunto de un hallazgo, que es un
   problema que tendremos en cuanto el generador funcione.

---

## 2. LO SEGUNDO: modelos de ocupación de la ecología

Ya usamos la cobertura de Chao y Jost para la rarefacción. Lo que no usamos son los **modelos de
ocupación**, que separan **ausencia real de no detección**.

**Y ese es literalmente nuestro error recurrente:** la afirmación sobre -so, el cero de nombres de
animales, y los tres artefactos de notación de ayer son todos casos de no detección leídos como
ausencia. La ecología tiene un aparato formal para eso desde hace veinte años y nosotros lo
resolvemos con una regla de prosa en el protocolo.

---

## 3. LO TERCERO: la partición jerárquica de la genética de poblaciones

Los estadísticos F de Wright **reparten la variación entre niveles jerárquicos**: dentro de un
individuo, entre individuos de una población, entre poblaciones.

Nuestro confusor de escriba es exactamente eso: variación dentro de un escriba frente a variación
entre escribas. Ayer lo resolvimos con un nulo emparejado a mano; **la partición jerárquica lo
cuantifica y da qué porción de la variación explica cada nivel**, que es más informativo que un
p-valor.

---

## 4. LO CUARTO: modelos nulos de grafos bipartitos

La bibliometría y la ecología de redes tienen **nulos que conservan la secuencia de grados
bipartita**, es decir, cuántos documentos tiene cada unidad y cuántas unidades cada documento.

**Eso ataca directamente el 9,2% de falsos positivos que medimos ayer**, porque la causa
diagnosticada fue que los documentos no son intercambiables. Un nulo de configuración bipartita lo
conserva por construcción, en vez de tener que emparejar por yacimiento a mano.

---

## 5. LO QUE NO TRANSFIERE, Y CONVIENE TENERLO ESCRITO

**El criptoanálisis**, pese al titular. Un cifrado tiene lengua conocida y respuesta verificable; el
Lineal A no. Sus métodos no transfieren, pero **su corpus sí sirve como sexto calibrador**, porque es
un caso límite que ninguno de nuestros cinco cubre.

**Y los grandes modelos de lenguaje aplicados a desciframiento.** Producen propuestas fluidas sin
nada que las decida, que es el problema que el protocolo describe. Pueden servir para generar
candidatos, nunca para evaluarlos.

---

## LO QUE YO HARÍA CON ESTO

**Traer una cosa, no cuatro.** Y sería **el nulo de configuración bipartita**, porque ataca el
problema medido (la coocurrencia inflada al 9,2%), es el que más afecta a resultados que ya tenemos
publicables, y no requiere leer un campo entero: es un nulo, y ya sabemos correr nulos.

**Y después, Westfall-Young**, cuando el generador produzca bastantes candidatos para que la
corrección múltiple sea el cuello de botella. Hoy no lo es.

Las otras dos son buenas ideas para cuando haya tiempo, y quedan anotadas.

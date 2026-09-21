# ¿Cuántos desciframientos del Lineal A encajan igual de bien? (12-sep)

> **NOTA (12-sep, cierre).** El déficit de 351 bits que aquí se calcula fue refinado en tres pasos la misma noche: contando el contexto que las unidades heredan de posiciones fijadas (55 → 25 signos), separando las marcas que solo sellan (25 → 7) y atacando *309 y *307 (7 → 5). El suelo final es de **cinco signos, 31 bits**. Véase 07_VERDICT y LOS_CINCO_IRREDUCTIBLES.md. La cuenta de partida de este documento es correcta como punto de partida.

La pregunta no es cuántas propuestas se han hecho, sino **cuántas propuestas distintas son igualmente compatibles con el corpus**. Es contable, y con lo medido estos días se cuenta.

## 1. Todas las lenguas "funcionan"

Bajo la fonología permisiva que el propio silabario impone (las oclusivas no distinguen sonoridad ni énfasis, las sibilantes se funden, las laríngeas a menudo no se escriben), se mide qué fracción de las 615 unidades íntegras encuentra al menos una palabra que le encaje en cada lengua candidata:

| lengua | encaje |
|---|---|
| hurrita | 88,6% |
| acadio | 83,6% |
| sumerio | 83,6% |
| ugarítico | 80,7% |
| hático | 78,9% |
| luvita | 72,4% |
| ibérico | 68,6% |
| hitita | 64,9% |
| etrusco | 62,9% |
| palaico | 53,7% |

**Media: 73,8%.** Ninguna lengua falla y ninguna destaca: el hurrita, que en nuestra búsqueda anclada quedaba **por debajo** del control (z = −2,3), es el que más encaja aquí. Encontrar comparandos no distingue lenguas.

## 2. La cuenta de información

**Lo que hace falta para especificar un desciframiento.** El silabario íntegro tiene 110 signos; dieciséis están anclados por los topónimos compartidos con el Lineal B, y quedan **94 libres**. Asignar a cada uno un valor de una rejilla de 74 cuesta 94 × log₂(74) = **584 bits**, más 3,3 bits por elegir la lengua entre diez. Total: **587 bits**.

**Lo que el corpus puede aportar.** Que una unidad "funcione" es un suceso que ocurre el 73,8% de las veces por azar, así que aporta −log₂(0,738) = 0,438 bits. Con 552 unidades silábicas íntegras, el máximo teórico es **242 bits**. Y ese máximo es generoso: las restricciones no son independientes, porque cada signo aparece de media en dieciséis unidades. Contando solo las unidades que fijan un signo aún no visto, el aporte efectivo baja a **236 bits**.

**Déficit: 351 bits.**

## 3. El resultado

**Del orden de 2³⁵¹ asignaciones distintas encajan con el corpus tan bien como cualquier otra.** Ese número no tiene nombre; es mayor que el número de átomos del universo observable elevado al cuarto.

No es una metáfora ni una advertencia retórica: es la consecuencia aritmética de tres cantidades medidas, y las tres están en este trabajo. Noventa y cuatro signos sin anclar. Un 73,8% de encaje por azar. Quinientas cincuenta y dos unidades no independientes.

## 4. Qué se sigue de esto, y qué no

**No se sigue** que el Lineal A sea indescifrable. Se sigue que **el corpus, por sí solo, no puede decidir**. Un desciframiento correcto sigue siendo posible: lo que no es posible es demostrarlo con este corpus y con criterios de encaje léxico, porque 2³⁵¹ rivales encajan igual.

**Se sigue** cuál es la única salida, y es la que el campo conoce: información de fuera. Una bilingüe, un descendiente vivo, un hallazgo que fije signos. Cada signo que se ancla desde fuera quita 6,2 bits del déficit; para cerrarlo harían falta unos 57 signos anclados, y tenemos 16.

**Se sigue también** por qué tres autores han propuesto el semítico en setenta años, y otros el luvita, el hurrita y el etrusco, y todos han podido exhibir centenares de coincidencias. No es que ninguno sea serio. Es que con 351 bits de holgura, cualquier hipótesis suficientemente trabajada produce un léxico coherente. Packard lo demostró en 1974 construyendo nueve; aquí está el número que explica por qué pudo hacerlo.

**Y se sigue, por último, cuál es el papel de una medida como la nuestra.** No elegir entre las 2³⁵¹, que es imposible, sino decir cuántas son y por tanto cuánto puede pesar cualquier argumento de encaje. Es el resultado más duro de todo este trabajo y no lo teníamos hasta hoy.

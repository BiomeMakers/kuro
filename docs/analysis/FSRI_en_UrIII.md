# El FSRI en Ur III: corrido, y el resultado es mixto (7 de septiembre de 2026)

La afirmación era una propuesta y no un resultado: que en Ur III, con 101.388 tablillas, habría red suficiente para que el índice triádico midiera algo. Corrido el experimento, la mitad se confirma y la otra mitad no.

## La red
De las 101.388 tablillas de BDTNS, 67.945 tienen dos o más palabras. Con las palabras que aparecen en treinta o más documentos quedan **3.990 nodos**. La adyacencia se define por coocurrencia significativa (z > 4 sobre lo esperado por los grados), y da **697.634 aristas**, grado medio 349,7, 43,7 millones de triángulos y un coeficiente de agrupamiento de 0,664.

Es, con diferencia, la red más grande sobre la que hemos trabajado: dieciocho veces más nodos que el vocabulario del Lineal A y tres órdenes de magnitud más de aristas.

## LO QUE SE CONFIRMA: la fiabilidad test-retest existe

En el Lineal A el índice no tenía fiabilidad: dos mitades del archivo de Hagia Triada daban +0,06 y +0,02 de exceso triádico, es decir, ruido. Aquí, partiendo el corpus en dos mitades aleatorias de 34.000 documentos cada una:

| medida | mitad A | mitad B | diferencia relativa |
|---|---|---|---|
| aristas | 561.804 | 536.381 | 4,6% |
| grado medio | 281,6 | 268,9 | 4,6% |
| triángulos | 25,5 M | 23,1 M | 9,8% |
| **agrupamiento** | **0,6046** | **0,5874** | **2,9%** |

**El coeficiente de agrupamiento se replica con un 2,9% de diferencia entre dos mitades independientes.** Eso es fiabilidad de verdad, y es la primera vez que la obtenemos en un corpus epigráfico. La afirmación de que el problema era el tamaño y no el índice queda demostrada: a 224 documentos no hay señal, a 34.000 la hay.

## LO QUE NO SE CONFIRMA: el triádico sigue siendo el grado

La pregunta que importa no es si el índice se replica, sino si añade algo sobre una medida trivial. Correlacionando los triángulos por nodo con el grado del nodo:

**r = 0,96. El grado explica el 96,2% de la varianza del triádico.**

Es el mismo resultado que en el Lineal A (donde Omega-N recuperaba 27,4 de rango medio frente a 26,8 del grado solo), pero ahora medido en una red donde sí hay potencia. De modo que el problema no era el tamaño: **el exceso triádico de estas redes es, en su casi totalidad, un efecto de grado**.

## LO QUE SÍ APORTA: el 3,8% residual, y es interpretable

Del 3,8% de varianza que el grado no explica sale la única señal propia del índice, y se lee sola. Los nodos con más triángulos de los que su grado predice son **todos nombres de persona**: Ur-, Lu₂-{d}Nin-šubur, Ur-mes, Lugal-ezem, Ur-{d}Utu, Lu₂-{d}Utu, más los términos de parentesco dumu-ni ("su hijo") y šeš ("hermano"). Los nodos con menos son **todos unidades y términos administrativos**: sila₃ y gin₂ (medidas), ša₃ ("dentro de"), u₄ ("día"), zi-ga ("gasto"), la fracción ⅓ y la conjunción u₃.

La lectura es limpia y no necesita el índice para entenderse, pero el índice la cuantifica: **las personas forman camarillas y las unidades de medida no.** Un nombre propio aparece con el mismo grupo de gente una y otra vez (su familia, su capataz, su equipo), de modo que sus vecinos son vecinos entre sí. Una unidad de medida aparece con todo el mundo sin que ese todo el mundo se conozca entre sí.

**Eso es un clasificador funcional obtenido de la estructura de la red**, y separa nombres de términos sin conocer la lengua. En Ur III sabemos la respuesta y sirve como validación; el interés está en aplicarlo donde no se sabe.

## Conclusión sobre el FSRI en este dominio

Tres afirmaciones, con su grado:

1. **La fiabilidad depende del tamaño y a 34.000 documentos existe.** Demostrado. El obstáculo del Lineal A era el corpus, no el índice.
2. **El índice triádico, tal como está formulado, mide sobre todo el grado.** Demostrado, y en la red grande con más claridad que en la pequeña. Cualquier uso del índice debería reportar el residuo tras descontar el grado, no el índice bruto.
3. **El residuo sí tiene contenido, y es de tipo social:** separa a las personas de las unidades por la forma en que se agrupan sus vecinos. Es poco, es el 3,8%, y es exactamente el tipo de señal que el índice pretendía capturar.

Lo honesto es decir que el FSRI aquí no ha añadido una medida nueva sino un procedimiento: **calcula el triádico, descuenta el grado, y mira el residuo.** Con esa forma sí sería aplicable a otros archivos, y la primera prueba de que funciona es que en Ur III separa a las personas de las medidas sin que nadie le diga qué es cada cosa.

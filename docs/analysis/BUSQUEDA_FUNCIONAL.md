# La búsqueda con la función como único objetivo (13-sep)

La prueba de doble restricción se corrió sobre **una** rejilla, la del Lineal B, y dio cero. Quedaba la pregunta obvia: ¿existe **alguna** asignación de valores que haga que las funciones medidas salgan como palabras reales con el significado que la posición exige? No enumerando, que es imposible, sino buscando con esa condición como objetivo único.

## El montaje

Veinte unidades cuya función fija una clase semántica: cinco encabezados, tres totales, un déficit, una ofrenda, tres topónimos, cinco partes, dos mercancías. Treinta signos las tocan, de los cuales **diecisiete son libres** (los otros trece están anclados por los topónimos).

El léxico son las entradas glosadas de ORACC y del Corpus Ugarítico de Copenhague repartidas por clase: 45 palabras que significan totalidad, 35 déficit, 52 registro, 127 ofrenda, 275 persona, 140 lugar, 152 textil.

Objetivo: cuántas de las veinte unidades se convierten en una palabra de su clase. Recocido simulado sobre los diecisiete signos libres, ocho semillas independientes, 6.000 pasos cada una.

## Resultado

| | funciones satisfechas de 20 |
|---|---|
| rejilla del Lineal B | **0** |
| mejor encontrada por recocido (8 semillas) | **1** |

Y la única que encuentra es espuria: SA-RU convertida en /suu/, que cae en la clase "persona" por la permisividad de la normalización.

**No existe, en el espacio buscado, ninguna asignación de valores que haga que dos de las funciones medidas salgan a la vez como palabras acadias, ugaríticas o sumerias con el sentido que su posición exige.** Ni la correcta ni ninguna otra.

## Qué añade esto a lo que ya había

La prueba anterior decía que *la rejilla estándar* no produce lecturas de doble restricción. Esta dice que **ninguna rejilla lo hace**, lo cual es mucho más fuerte, porque elimina la defensa obvia: que el problema estuviera en los valores y no en la lengua.

Combinada con el resultado inverso, que optimizar el encaje léxico sin la restricción funcional encuentra rejillas 2,4 veces mejores que la estándar, el cuadro queda completo:

- **Con solo el léxico como criterio:** hay muchísimas soluciones, y las mejores son falsas.
- **Con la función añadida:** no hay ninguna.

Esa asimetría es el resultado. El criterio que el campo usa produce demasiadas respuestas; el criterio que mide lo que el archivo hace no produce ninguna. Entre los dos no queda una lectura.

## Los límites, que son serios y hay que declararlos

El léxico por clase es pequeño: entre 35 y 275 palabras, cuando el vocabulario real de cada lengua es mucho mayor y las glosas inglesas de ORACC no cubren todos los sinónimos. Son tres lenguas de las trece candidatas, las únicas con léxico glosado disponible. El espacio de búsqueda son diecisiete signos, no los noventa y cuatro, porque solo esos tocan unidades con función. Y la normalización fonológica es permisiva, lo que si acaso favorece encontrar coincidencias y no lo contrario.

Un léxico completo de acadio o de ugarítico podría cambiar el número de 1 a 2 o 3. Lo que no parece que pueda cambiar, por la magnitud de la diferencia, es la conclusión: no hay una asignación que haga hablar al archivo.

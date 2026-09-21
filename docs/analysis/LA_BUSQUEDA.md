# La búsqueda: qué pasa cuando se optimiza de verdad (12-sep)

Puntuar una rejilla es una cosa; **buscar la mejor** es otra, y es la que ninguna propuesta ha hecho. Recocido simulado sobre los 38 signos libres (los dieciséis anclados por topónimos quedan fijos), con la función objetivo que cualquier desciframiento persigue: cuántas unidades se convierten en palabras reales de la lengua diana, más diez veces cuántas de ellas significan además lo que la función medida exige.

## Resultado

| | fonología permisiva | fonología estricta |
|---|---|---|
| **rejilla del Lineal B** (el punto de partida de las nueve propuestas) | léxico **75**, funcional 0 | léxico **40**, funcional 0 |
| búsqueda, corrida 1 | 179 | 128 |
| búsqueda, corrida 2 | 180 | 128 |
| búsqueda, corrida 3 | **183** | **131** |
| signos que la mejor cambia respecto al Lineal B | **37 de 38** | **38 de 38** |

**La búsqueda encuentra rejillas entre 2,4 y 3,3 veces mejores que la del Lineal B, y que no conservan casi ningún valor suyo.** Las tres corridas convergen a lo mismo desde semillas distintas, así que no es ruido.

## Qué significa esto

Es el resultado de Packard de 1974, rehecho con un optimizador moderno y un léxico real de 16.147 formas. Y es más fuerte que el suyo: él mostró que rejillas ficticias producen coincidencias comparables; esto muestra que **una rejilla optimizada produce el triple de coincidencias que la correcta**, y que para conseguirlo tiene que cambiar los treinta y ocho signos.

**El criterio de encaje léxico no es débil: es contraproducente.** Puntuar un desciframiento por cuántas palabras del corpus se convierten en palabras de la lengua diana prefiere activamente rejillas que casi con certeza son falsas. Cualquier propuesta que se apoye en el número de traducciones logradas está usando una medida que premia lo contrario de lo que busca.

**Y hay un dato que no se mueve: el componente funcional es cero en todas partes.** Ni la rejilla del Lineal B, ni ninguna de las rejillas optimizadas, ni las ficticias, producen una sola unidad que sea a la vez una palabra real y signifique lo que su posición en la cuenta exige. La restricción que aporta nuestro inventario es la única que ninguna optimización consigue satisfacer, y por eso es la única que discrimina.

## La respuesta a la pregunta de partida

La pregunta era: el candidato que cumpla las reglas, traiga sentido y supere los controles, ¿no sería el mejor? Sí lo sería. Y lo que la búsqueda contesta es que **ese candidato no existe entre los que hemos podido explorar**: hay muchísimas rejillas que traen palabras, ninguna que traiga sentido. El cuello de botella no está en la búsqueda ni en el léxico ni en la potencia de cálculo. Está en que el corpus no contiene suficiente información para que el sentido y la forma se apoyen mutuamente, que es exactamente lo que la cuenta de bits predecía: 587 necesarios, 236 disponibles.

## Lo que esto deja en pie
El único criterio que sobrevive a la optimización es el funcional, y para usarlo hacen falta más unidades con función medida. Nuestro inventario tiene 57 y solo 42 clasificables; con doscientas, la restricción funcional empezaría a morder. Esa es la única vía de mejora que no depende de una excavación, y es trabajo de lectura distribucional, que es lo que este proyecto sabe hacer.

# Comprobación del resultado con y sin las mejoras (7 de septiembre de 2026)

Adoptadas dos prácticas de Briakos (2026), se comprueba qué cambia en el resultado.

## Lo que cambia en los informes

**Antes.** Una ficha de HT 23a listaba los elementos con su estado y sus cantidades. Nada distinguía una cifra medida de una recordada, y nada avisaba de que dos grupos comparados pudieran diferir por cómo se registró el dato.

**Ahora.** Cada informe imprime el hash del corpus con que se calculó (66b94203bd343ed9 para el fichero actual), cada afirmación lleva su etiqueta ([C] calculado, [L] literatura, [~] ilustrativo), y hay un control de captura que se puede pedir por yacimiento o por soporte.

## Lo que las mejoras han destapado en nuestro propio trabajo

**1. El control de captura da un aviso serio, y es nuevo.** La longitud media de documento varía un **311% entre yacimientos** (Zakros y Arkalochori, 6,9 signos por documento; Cnosos, 2,0) y un **274% entre soportes** (tablillas 8,5; nódulos 1,0). Y la proporción de signos dañados varía un 722% entre yacimientos.

Eso significa que cualquier comparación de perfiles entre yacimientos o entre soportes puede estar midiendo cuánto texto sobrevive y no qué se escribió. Nuestra comparación entre archivos y santuarios sí emparejaba por tamaño de muestra (fijamos 200 unidades), de modo que no está afectada; pero **nunca lo habíamos justificado con esta medida**, y a partir de ahora el control se corre antes y se declara.

**2. La ficha automática discrepa de nuestra lectura manual, y hay que mirarlo.** Con las cantidades del Explorer, la ficha de HT 23a lee la juncia en 1/3 y el sésamo en 1/16, dando una razón de 5,33; nuestra lectura manual, con las letras de fracción de GORILA vía Younger y los valores de Corazza, daba juncia 1/5 y sésamo 1/10, razón 2. **Las dos no pueden ser correctas.**

La discrepancia viene de la fuente: el Explorer convierte las letras de fracción a glifos y en el proceso cambia los valores. La ficha automática usa lo que hay en el fichero; nuestra lectura usa las letras del comentario de Younger. Y como todo el argumento de la razón astringente-aceite depende de esos valores, **esto hay que verificarlo en GORILA antes de enviar el artículo de aromáticos a nadie más**. El propio verificador de kuro señala el problema en otras tablillas del corpus, y aquí lo ha señalado por su cuenta al discrepar.

Es exactamente el cuarto caso de la semana en que la transliteración derivada induce a error, y esta vez lo ha detectado la herramienta y no nosotros. Anotado como pendiente de primera prioridad.

**3. La ficha también revela que la transliteración parte una palabra.** Donde nuestra lectura tiene QI-RI-TU-QA, el fichero tiene \*21F-RI-TU-QA: el primer signo aparece con su número y no con su valor silábico. No cambia el análisis, pero confirma que trabajamos sobre una fuente con normalización incompleta.

## Lo que NO cambia

Ninguno de los resultados estructurales. La homogeneidad de fracciones dentro de cada tablilla, la asociación del bloque con el aceite y no con los textiles, la ausencia de coincidencia con el ganado, el 26-28% de \*308 sobre las aceitunas, la comparación con las recetas de Assur y el kyphi, y la frecuencia de la juncia en el corpus, todo eso se calcula sobre presencias y no sobre valores de fracción, y por tanto es independiente del problema.

Lo que sí depende de los valores es **una sola afirmación**: la razón astringente-aceite de 0,80 y su encaje en el rango de Dioscórides. Esa queda en suspenso hasta verificar las fracciones.

## Conclusión
Las mejoras han valido la pena en el primer uso: una ha añadido una cautela metodológica que no teníamos, y la otra ha destapado una discrepancia en nuestro propio dato principal. Es lo que se espera de un instrumento bien hecho, y es incómodo, que es la señal de que funciona.

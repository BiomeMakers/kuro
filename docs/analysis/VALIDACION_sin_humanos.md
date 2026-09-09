# Validación de kuro sin depender de participantes humanos (6 de septiembre de 2026)

El argumento de Ithaca (Assael et al. 2022) es que la herramienta mejora a quien decide, y se demuestra con un experimento con historiadores. Ese experimento queda diseñado (EXPERIMENTO_expertos.md) pero depende de la disponibilidad de otros. Estas tres validaciones no dependen de nadie y sostienen una versión más modesta del mismo argumento.

## La tarea
Clasificar una palabra del Lineal B como NOMBRE de persona o TÉRMINO (oficio, mercancía, cualidad) a partir únicamente de su distribución. 64 palabras con significado establecido por el campo (26 nombres, 38 términos); rasgos: posición en el documento, qué la sigue, si el documento lleva el ideograma de persona, en qué series aparece, dispersión por sitio, frecuencia y terminación. Validación cruzada de cinco pliegues.

## 1. El experto de reglas frente al modelo
Un decisor de referencia con las reglas explícitas que un epigrafista aplicaría según la bibliografía (si va con la cantidad 1 en un documento de personal, nombre; si le sigue un ideograma de mercancía, término; si aparece en series de mercancía, término; si está en series de personal y no encabeza, nombre; terminaciones en -jo y -si, término) acierta 0,66, y 0,63 en acierto balanceado.
El modelo distribucional acierta 0,78 (0,77 balanceado).
La combinación (seguir al modelo cuando su confianza supera 0,7 y a las reglas en el resto) acierta 0,80, con el modelo decidiendo en 45 de las 64 palabras.
Lectura: el modelo supera a las reglas explícitas en doce puntos, y la combinación es ligeramente mejor que el modelo solo en acierto simple. No es el efecto sinérgico de Ithaca, porque un conjunto de reglas no es un experto, y así se declara: es una cota inferior de lo que un especialista con la herramienta obtendría, no una medida de él.

## 2. Cuántas etiquetas hacen falta (curva de aprendizaje)
Acierto balanceado según el número de palabras anotadas para entrenar, media de 20 remuestreos: 10 etiquetas, 0,71; 20, 0,74; 30, 0,75; 40, 0,77; 50, 0,79.
Lectura, y es la promesa concreta para el usuario: anotar veinte palabras de un corpus basta para clasificar el resto con tres aciertos de cada cuatro; la mejora posterior es lenta, de modo que el esfuerzo de anotación tiene un rendimiento decreciente claro y medido.

## 3. Trabajo ahorrado en una tarea real
Para encontrar la mitad de los términos del conjunto (19 de 38) revisando palabras una a una: en orden aleatorio hay que revisar 32 de media; ordenando por la probabilidad del modelo, 22. Un tercio menos de trabajo para el mismo hallazgo.
Lectura: en la tarea que un investigador hace de verdad, que es priorizar qué mirar, la ordenación por el modelo ahorra alrededor del 30% de las revisiones.

## Límites declarados
Las tres medidas se hacen sobre el Lineal B, donde las respuestas se conocen; el traslado al Lineal A es una hipótesis, no un resultado. Las reglas del "experto" son nuestras, escritas a partir de la bibliografía, y un especialista real usaría más información (la forma de los signos, el contexto arqueológico, la memoria del corpus). Y el conjunto etiquetado es pequeño (64), de modo que las tres cifras tienen la incertidumbre que corresponde a ese tamaño.

## Qué añade esto al artículo del software
La sección de validación de kuro pasa de "reproduce nuestros resultados" a tres afirmaciones comprobables por cualquiera: supera a un conjunto de reglas explícitas, alcanza tres de cada cuatro aciertos con veinte anotaciones, y ahorra un tercio del trabajo de revisión. El experimento con humanos, cuando se pueda hacer, se añadirá encima.

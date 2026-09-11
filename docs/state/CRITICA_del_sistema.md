# Crítica dura del sistema construido hoy, y qué hacer con ella

9 de septiembre de 2026, tras la sesión de construcción.

---

## 1. LA CRÍTICA DE FONDO, ANTES QUE NINGUNA OTRA

**Hoy no hemos producido ni una sola unidad nueva de conocimiento sobre el Lineal A.** El
inventario sigue en 5,3%. Se ha construido un ciclo de hipótesis, un generador, un diccionario, un
índice de referencia, un módulo de lecciones, uno de transferencia y sesenta y siete tests. **Y el
corpus no sabe nada que no supiera esta mañana.**

Eso puede estar bien, si la infraestructura rinde mañana. Pero es exactamente el patrón que
criticamos en otros: producir aparato en vez de resultados, y medir el progreso por el aparato.

## 2. Y LA MÁS VERGONZOSA: hemos vuelto a no mirar la bibliografía

Buscado después de construirlo, el campo existe, es maduro y tiene nombre: **Literature-Based
Discovery**, desde Swanson en 1986. Y hay sistemas que hacen lo que hemos hecho:

- **POPPER** (2025) es literalmente nuestro diseño: "un marco agéntico para la validación
  automatizada de hipótesis de forma libre, mediante agentes que diseñan experimentos de
  falsación, inspirado en el principio de falsación de Popper", y "aplica controles estadísticos
  rigurosos". Nuestra clase `Hypothesis` es eso, sin saberlo.
- **SCIMON** compara ideas nuevas contra la bibliografía existente y las revisa hasta que dejan de
  parecerse a trabajo previo. Nuestro `check_literature` es eso.
- **Dyport** (2023) es una técnica de *benchmarking* para sistemas de generación de hipótesis, es
  decir, el problema de validación que nos hemos inventado a mano.
- Y el método de evaluación que usamos hoy (hacer que el sistema mate las tres hipótesis que ya
  sabíamos muertas) **es el método estándar del campo**: "hacer que un sistema redescubra hallazgos
  de referencia". No es nuestro y no es novedoso.

**Es la séptima vez esta semana**, y esta vez a nivel meta: hemos construido durante horas algo que
ya existe, sin dedicar dos minutos a mirar.

---

## 3. LOS FALLOS CONCRETOS DEL SISTEMA

**El generador redescubre lo nuestro.** Sus mejores candidatos son NI → VIN y CYP → NI, que ya
medimos hoy. De setenta y seis candidatos, ninguno es una pregunta que no nos hubiéramos hecho.

**Las constantes del ranking son arbitrarias.** `freq/10`, `joint/4`, un bonus de 2 por unidad no
tratada. Números que escribí sin justificación. `informativeness()` está mejor motivada, pero su
forma exacta (el pico entre 3 y 15, la caída con raíz cuadrada) también es inventada.

**Las restricciones no restringen.** Tras la validación quedan tres reglas, y en la demostración la
mayoría de las unidades conservan cuatro de cinco categorías posibles. Un filtro que no filtra.

**El generador bibliográfico rinde fatal:** tres candidatos de cien mil palabras. Los patrones son
expresiones regulares ingenuas que no capturan cómo se afirma algo en un texto académico.

**Las lecciones no se aprenden, se escribieron a mano.** Cinco patrones que tecleé yo mirando las
retiradas. Nada se infiere de los datos; si mañana falla algo nuevo, el sistema no lo incorpora
solo.

**La tasa de error cubre dos instrumentos de diez.** Y el más importante para nuestros artículos, el
de fracciones compartidas, no está medido.

**Y los sesenta y siete tests validan el código, no la ciencia.** Ninguno comprueba que el sistema
encuentre algo verdadero. Comprueban que no se rompe, que respeta sus propias reglas y que no
inventa huecos. Eso es necesario y no es suficiente.

---

## 4. LA PRUEBA PEQUEÑA QUE HAY QUE HACER, Y ES BARATA

**Una prueba de recuperación ciega.** Tomar el corpus **etrusco**, donde la respuesta se conoce,
borrar lo que sabemos, y correr el sistema entero: generador, ciclo, restricciones, lecciones. Ver
**si redescubre el genitivo en -l ante los términos de filiación sin que se lo digamos.**

Es la prueba correcta por tres razones. Es el método estándar del campo, así que es comparable. No
requiere datos nuevos. Y tiene una respuesta binaria: o el genitivo sale entre los primeros
candidatos, o el sistema no sirve para lo que decimos.

**Y el criterio hay que fijarlo antes de correrla:** que la relación aparezca entre los diez
primeros candidatos generados y sobreviva el ciclo con su corrección múltiple. Si sale el
undécimo, es un fracaso, y hay que escribirlo.

---

## 5. QUÉ HACER, POR ORDEN

**Primero, la prueba ciega en etrusco.** Es media sesión y decide si lo construido vale.

**Segundo, leer POPPER y Dyport antes de tocar nada más.** Si POPPER ya resuelve la validación
mejor que nosotros, lo que hay que hacer es adoptarlo y no reescribirlo. Y si no, hay que poder
decir por qué, que es lo que el protocolo pide a cualquiera.

**Tercero, medir la tasa de error del instrumento de fracciones**, que es el que sostiene el
artículo de aromáticos y no está caracterizado.

**Y cuarto, y esto es lo que de verdad importa: volver al corpus.** El sistema es un medio. Si
mañana se dedica otro día a refinarlo, habremos hecho dos días de ingeniería y cero de
epigrafía.

---

## 6. LO QUE SÍ VALE, PARA NO TIRARLO TODO

Tres cosas del día sobrevivirían a cualquier revisión:

- **la tasa de falsos positivos medida**, 9,2% para la coocurrencia en este corpus por la estructura
  de yacimiento, que es un hecho sobre nuestro propio trabajo y afecta a un artículo;
- **la adyacencia CYP → NI y NI → VIN**, medida con nulo propio, que confirma como orden real lo
  que era coocurrencia;
- y **el diccionario con evidencia fechada, firmada y con dirección**, que no he visto en ningún
  sistema de los que la búsqueda ha devuelto, y que es lo único aquí que podría interesarle al campo
  de la epigrafía computacional.

Lo demás es reimplementación de cosas que existen, hecha en un día y sin leer.

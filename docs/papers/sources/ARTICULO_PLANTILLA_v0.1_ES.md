# Cuánta plantilla tiene cada parte del corpus del Lineal A, y por qué solo un género tiene alguna

**Alberto Acedo**
Biome Makers Inc. Borrador v0.1, 10 de septiembre de 2026. No circular.

## Resumen

Los documentos del Lineal A se clasifican de varias maneras: por ideograma, por combinación de
mercancías, por tipo de transacción, por soporte. Ninguna de esas clasificaciones mide cuán rígido es
en realidad el formato de cada grupo, y la pregunta tiene una respuesta que puede obtenerse sin leer
nada. Esta nota propone una medida de rigidez de formato: apartar cada documento por turno, predecir
cada una de sus posiciones a partir de los demás, y registrar cuánto gana esa predicción sobre
adivinar siempre el elemento más frecuente del grupo. Aplicada a doce grupos del corpus, la medida los
separa con nitidez. La fórmula de libación gana 12,4 puntos sobre su tasa base (22,4% frente a 10,0%,
nulo de permutación 6,6%, p = 0,003); ningún otro grupo llega a 3, siete de los once restantes no
ganan nada, y cinco ganan menos que nada, es decir, una conjetura constante bate a la predicción. Los
vasos de piedra, el único grupo además de la fórmula con una ganancia digna de mención, se la deben a
contener la fórmula: sus aciertos son los mismos elementos fijos. La conclusión es que **el Lineal A
tiene un género con formato rígido, el votivo, y su administración no lo tiene**: las tablillas
contables repiten un repertorio corto de mercancías, pero su orden no es predecible por encima de lo
que esa repetición ya proporciona. La medida se calibra sobre material donde no hay plantilla y da un
falso positivo el 5,0% de las veces al umbral del 5%.

**Palabras clave:** Lineal A, clasificación documental, formato, predicción, modelos nulos, Hagia
Triada, fórmula de libación.

## 1. La pregunta, y por qué no se ha hecho

El corpus del Lineal A se clasifica de al menos cuatro maneras. El sistema de Bennett, heredado por
Younger, agrupa las tablillas por el ideograma que llevan. Uchitel y Montecchi las agrupan por
combinación de mercancías. Hogan las agrupa por tipo de transacción. Y toda edición las agrupa por
soporte: tablilla, rodel, nódulo, vaso de piedra.

Cada clasificación afirma, implícitamente, que sus grupos son coherentes. **Ninguna mide cuánto**, y
la razón es que la coherencia de contenido se ve y la de **formato** no: si los documentos de un grupo
siguen un orden compartido no puede juzgarse por inspección cuando esos documentos tienen tres
elementos.

La pregunta importa más allá de la contabilidad del propio catálogo. Un grupo con formato rígido es un
grupo cuyos documentos se escribieron según una plantilla, y eso es un hecho sobre la administración
que los produjo; un grupo sin ella es un grupo cuya coherencia está en otra parte.

## 2. La medida

Cada documento es una secuencia de elementos. Se alinea cada documento del grupo por su primer
elemento, se aparta uno entero, y se predice cada una de sus posiciones a partir de los restantes: un
candidato pesa según cuántas veces ocupa esa posición relativa en los demás, y según cuántos otros
elementos comparte su documento de origen con el que se reconstruye.

**Se informan tres cosas, y la tercera es la medida.**

El **acierto** es la proporción de posiciones apartadas predichas correctamente. La **tasa base** es
lo que consigue adivinar siempre el elemento más frecuente del grupo. Y la **ganancia** es la
diferencia. Un nulo de permutación, barajando los elementos dentro de cada documento dos mil veces, da
el acierto obtenible cuando el orden no lleva información alguna.

**La posición de alineación queda excluida de la puntuación.** Tiene que estarlo: es lo que la
alineación emplea, y predecirla sería circular. En una corrida temprana de esta medida sobre la
fórmula de libación, once de diecisiete aciertos aparentes eran esa sola posición.

**Por qué la ganancia y no el acierto.** Un grupo en que un elemento domina da un acierto alto por una
razón trivial, y la tasa base absorbe exactamente eso. La ganancia aísla lo que aporta la posición.

## 3. Resultado

| grupo | n | posiciones | acierto | tasa base | nulo | **ganancia** | p |
|---|---|---|---|---|---|---|---|
| **fórmula de libación** | 16 | 49 | 22,4% | 10,0% | 6,6% | **+12,4** | 0,003 |
| vasos de piedra | 43 | 204 | 5,9% | 3,4% | 3,2% | +2,5 | 0,060 |
| familia de clase A | 8 | 85 | 9,4% | 8,0% | 3,4% | +1,5 | 0,023 |
| tablillas | 209 | 1.277 | 5,2% | 3,9% | 4,0% | +1,3 | 0,032 |
| tablillas de Hagia Triada | 141 | 947 | 5,1% | 4,0% | 3,8% | +1,1 | 0,057 |
| familia de clase U | 41 | 289 | 9,0% | 9,2% | 6,8% | −0,2 | 0,152 |
| familia de clase E | 16 | 100 | 4,0% | 6,7% | 4,9% | −2,7 | 0,675 |
| tablillas de Chania | 35 | 167 | 10,2% | 13,2% | 8,1% | −3,0 | 0,250 |
| familia de clase V | 20 | 105 | 1,0% | 4,5% | 0,7% | −3,6 | 0,425 |
| tablillas de Festos | 11 | 48 | 4,2% | 8,0% | 2,5% | −3,8 | 0,482 |
| familia de clase B | 14 | 99 | 4,0% | 10,0% | 3,3% | −6,0 | 0,405 |
| tablillas de Arkhalkhori | 8 | 35 | 5,7% | 12,8% | 2,2% | −7,1 | 0,162 |

**Un grupo queda aparte, y la distancia no es marginal.** La fórmula de libación gana 12,4 puntos; el
siguiente gana 2,5. Cinco grupos ganan menos que nada.

## 4. Qué dice el resultado

**El género votivo tiene plantilla y la administración no la tiene.** Ese es el hallazgo, y conviene
enunciarlo en la forma que puede atacarse: en once grupos del corpus distintos de la fórmula de
libación, conocer una posición aporta como mucho 2,5 puntos sobre saber qué elemento es el más
frecuente, y por lo general no aporta nada.

**Los vasos de piedra son la excepción aparente y no lo son.** Su ganancia procede de contener la
fórmula: los elementos que acierta son I-PI-NA-MA y SI-RU-TE, los mismos fijos que impulsan el
resultado de la propia fórmula. Quitada la fórmula, el grupo se une a las tablillas.

**Las ganancias negativas son informativas, no fallos.** Un grupo donde la predicción pierde contra
una conjetura constante es un grupo con un elemento dominante. Las tablillas de Chania tienen una tasa
base del 13,2% y las de Arkhalkhori del 12,8%, las dos más altas del corpus. Eso no es plantilla sino
dominancia, y merece distinguirse: una clasificación que agrupe documentos por un ideograma compartido
producirá grupos con tasa base alta y sin formato, que es lo que muestran las familias B y V.

**Y esto no contradice las secuencias estándar descritas.** Uchitel y Hogan describen órdenes
recurrentes de mercancías, y un trabajo compañero encuentra uno de esos órdenes en cuatro tablillas de
cuatro. Las dos cosas son ciertas. Existen subgrupos con orden fijo; los grupos del nivel de la
clasificación que los contienen no comparten plantilla, y la señal de los subgrupos se diluye en
ellos. **La medida opera en el nivel de la clasificación, y lo que dice es que las clasificaciones no
capturan el formato.**

## 5. Calibración y límites

**Calibración.** El instrumento se corrió sobre grupos de documentos contables tomados al azar, donde
no hay plantilla que encontrar: informa de un falso positivo el 5,0% de 120 ensayos al umbral del 5% y
el 0,83% al del 1%. Se comporta como debe.

**Límites, tres.** La medida exige al menos ocho documentos de tres o más elementos, lo que excluye la
mayor parte de las clases de la clasificación fina. La alineación por el primer elemento es tosca, y
un grupo cuya plantilla empiece en puntos distintos quedaría penalizado por ella; la fórmula se alineó
así aquí por comparabilidad, y su ganancia está, si acaso, subestimada. Y **los p-valores no están
corregidos por las doce comparaciones**: a un umbral de Bonferroni de 0,004 solo sobrevive la fórmula,
que es la conclusión en cualquier caso.

## 6. Discusión

La medida no es específica del Lineal A. Cualquier corpus de documentos cortos con elementos repetidos
puede perfilarse así, y la cantidad interesante es la misma en todas partes: cuánto aporta la posición
por encima de la frecuencia. Aplicada a un corpus con respuesta conocida debería separar un género
formulario de uno de inventario, y aquí hace exactamente eso sobre el único grupo del Lineal A cuyo
carácter formulario no está en disputa.

Lo que añade al estudio del Lineal A es un hecho que cuatro clasificaciones habían dejado sin
enunciar: **la administración de la Creta neopalacial no escribía sus cuentas conforme a un
formulario.** Repetía mercancías, repetía términos de transacción, y en algunas tablillas repetía un
orden; pero el orden no es propiedad de ningún grupo lo bastante grande como para llamarse género. El
único sitio donde la forma es fija es el único donde no se cuenta nada.

## Datos

Textos del Lineal A según la transcripción del LinearA Explorer sobre GORILA. Clasificación de
Montecchi 2019. La medida, su nulo y su calibración están implementados en el paquete kuro; el código
y las cifras por grupo se distribuyen con él.

## Declaración de asistencia

El procesamiento del corpus, las pruebas y la redacción de este texto se produjeron con la asistencia
de un modelo de lenguaje (Claude, Anthropic) bajo la dirección del autor, que es responsable de todas
las afirmaciones aquí hechas.

## Referencias

Bennett, E. L. 1950. Fractional quantities in Minoan bookkeeping. American Journal of Archaeology 54, 204-222.

Godart, L. y J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A. Études Crétoises 21. París: Geuthner.

Hogan, R. 2026. Transaction types in the Linear A corpus. En E. Salgarella y V. Petrakis (eds), The Wor(l)ds of Linear A, AURA Supplement 15, Atenas.

Montecchi, B. 2019. Contare, misurare e valutare nella Creta minoica. Roma: Quasar.

Schoep, I. 2002. The Administration of Neopalatial Crete. Suplementos a Minos 17. Salamanca.

Uchitel, A. 2002-2003. HT 94 and the standard sequences of Linear A. Minos 37-38.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos y N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Younger, J. G. 2024. Linear A Texts and Inscriptions in phonetic transcription and Commentary. Academia.edu.

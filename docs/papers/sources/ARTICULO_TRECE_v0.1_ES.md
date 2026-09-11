# Trece candidatas a parientes del minoico medidas contra un mismo nulo, y por qué ninguna lo pasa

**Alberto Acedo**
Biome Makers Inc. Borrador v0.1, 10 de septiembre de 2026. No circular.

## Resumen

Durante un siglo la lengua del Lineal A se ha atribuido, por distintos autores, al anatolio, al semítico, al hurrita, al tirsénico y al griego, o se ha declarado aislada, y ninguna propuesta se ha contrastado con las demás con un instrumento común. Este artículo lo hace. Trece corpus (griego micénico, hitita de dos fuentes, luvita, palaico, hurrita, hático, acadio, ugarítico, sumerio, elamita, eteocretense y etrusco) se reducen junto con el léxico del Lineal A a un mismo esqueleto consonántico cuya pérdida se declara por corpus, y sus perfiles de bigramas de consonantes se comparan con el minoico bajo un nulo que baraja las consonantes de cada palabra minoica entre sus posiciones. El instrumento se calibra antes: sobre las doce lenguas conocidas separa lenguas 2,5 veces más de lo que separa mitades de una misma lengua. Sobre el minoico, una candidata queda más cerca que el minoico barajado, el griego micénico (p = 0,01), y es la que no puede contar: el Lineal A se lee con los valores fonéticos del Lineal B, de modo que sus secuencias de consonantes heredan las restricciones del griego por construcción. Barajar esos valores entre los setenta y cinco silabogramas del Lineal A muestra que la asignación del Lineal B acerca el minoico a toda lengua real más que cualquiera de cien asignaciones al azar, lo que cuantifica el filtro. Las otras doce candidatas, incluidas las tres históricas medidas aquí contra un nulo por primera vez, no están más cerca del minoico que el minoico desordenado (p entre 0,22 y 1,00). Una dirección sobrevive al filtro: el etrusco es la única candidata a la que las asignaciones al azar acercan más que los valores del Lineal B (6 de 100). El resultado cierra, con nulo, la afirmación de que la fonotaxis minoica bajo la transcripción vigente se parezca a alguna candidata conocida, e identifica la transcripción misma como el obstáculo de la pregunta.

**Palabras clave:** Lineal A, minoico, filiación lingüística, fonotaxis, modelos nulos, sesgo de transliteración, luvita, hurrita, etrusco.

## 1. Un siglo de propuestas y ninguna prueba común

Palmer y Finkelberg leyeron el minoico como anatolio, en concreto luvita. Gordon lo leyó como semítico. Van Soesbergen lo lee como hurrita. Facchetti lo conectó con el etrusco a través de una familia tirsénica. Otros lo han leído como griego, como indoiranio, y como aislado o sustrato pregriego. Cada propuesta tiene argumentos y cada una tiene objeciones, y las objeciones están tan poco cuantificadas como los argumentos: ninguna propuesta se ha puesto junto a las demás bajo un instrumento y un nulo.

La razón no es falta de interés sino de comparabilidad. Los corpus candidatos están escritos en cinco sistemas distintos: el Lineal A y el B son silabarios CV leídos con valores griegos, el hitita y el hurrita van en cuneiforme con sílabas cerradas, el ugarítico en alfabeto consonántico sin vocales, el etrusco en alfabeto. Cualquier distancia medida entre ellos mide el sistema de escritura antes que la lengua. Un primer intento aquí, sobre transliteraciones en bruto, devolvió el ugarítico como la lengua más lejana exactamente por eso: su corpus no tiene vocales.

## 2. Un formato común, y su pérdida declarada

Cada corpus se reduce a un esqueleto consonántico: cada palabra pasa a ser su secuencia de consonantes, con un mapeo declarado para los diacríticos de cada sistema de transliteración, y las vocales se eliminan. La pérdida se mide por corpus como la proporción de palabras distintas que se vuelven indistinguibles:

| corpus | palabras | colapsadas |
|---|---|---|
| Lineal A | 1.117 | 37,7% |
| micénico | 1.414 | 43,9% |
| hitita | 6.000 | 34,4% |
| ugarítico | 4.767 | 29,3% |
| etrusco | 10.783 | 48,5% |
| sumerio (muestra) | 60.000 | 38,1% |
| acadio (muestra) | 60.000 | 50,2% |

Las pérdidas son comparables, que es la condición para que los esqueletos lo sean. Se probó también un esqueleto silábico y se rechazó: no puede representar un corpus sin vocales.

Los corpus hurrita, hático, luvita y palaico proceden del conjunto de datos TLHdig del Hethitologie-Portal Mainz (Zenodo 15459134), donde se identifican por etiquetas de lengua a nivel de línea dentro de documentos por lo demás hititas; un recuento a nivel de documento habría perdido casi todo el hurrita. El sumerio, el acadio y el elamita proceden de la transliteración en bloque de CDLI. El etrusco, de OpenEtruscan.

## 3. La medida, su nulo y su calibración

El perfil de cada corpus es la distribución de bigramas de consonantes sobre sus esqueletos, con límites de palabra marcados. La distancia es la divergencia de Jensen-Shannon.

**El nulo** baraja las consonantes de los esqueletos minoicos entre sus posiciones, doscientas veces, conservando el inventario y la longitud de cada palabra y destruyendo solo su orden. Una candidata está más cerca del minoico que el azar si su distancia al minoico real es menor que su distancia al minoico barajado.

**Calibración.** Sobre las doce lenguas conocidas, la distancia media entre lenguas es 2,5 veces la distancia media entre dos mitades aleatorias de una misma lengua. El instrumento separa lenguas cuando la respuesta se conoce.

## 4. Resultado

| candidata | familia | distancia | nulo | p |
|---|---|---|---|---|
| griego micénico | indoeuropeo | 0,145 | 0,152 | *\*0,010** |
| hitita (CDLI) | anatolio | 0,260 | 0,253 | 0,98 |
| hitita (Mainz) | anatolio | 0,272 | 0,255 | 1,00 |
| hurrita | hurro-urartiano | 0,277 | 0,262 | 1,00 |
| palaico | anatolio | 0,299 | 0,279 | 1,00 |
| luvita | anatolio | 0,320 | 0,309 | 1,00 |
| acadio | semítico oriental | 0,338 | 0,333 | 0,97 |
| hático | aislada | 0,338 | 0,323 | 1,00 |
| eteocretense | | 0,351 | 0,310 | 1,00 |
| ugarítico | semítico occidental | 0,369 | 0,371 | 0,22 |
| elamita | aislada | 0,379 | 0,379 | 0,47 |
| sumerio | aislada | 0,401 | 0,391 | 1,00 |
| etrusco | tirsénico | 0,417 | 0,407 | 1,00 |

Una candidata queda más cerca que el azar. Doce no; nueve están más lejos del minoico que el minoico barajado.

## 5. La que pasa es la que no puede contar

El Lineal A se translitera con los valores fonéticos del Lineal B, establecidos para el griego. Sus secuencias de consonantes heredan por tanto las restricciones fonotácticas del griego antes de cualquier comparación. Que el micénico salga el más cercano es lo que esa construcción predice, y es una medida del filtro, no de la lengua.

El filtro se puede cuantificar. Los valores del Lineal B se barajaron entre los setenta y cinco silabogramas del Lineal A cien veces y la comparación se repitió bajo cada asignación:

| candidata | con los valores del B | mejor de 100 al azar | asignaciones al azar que mejoran |
|---|---|---|---|
| micénico | 0,151 | 0,281 | 0 |
| hitita | 0,266 | 0,355 | 0 |
| hurrita | 0,283 | 0,352 | 0 |
| luvita | 0,326 | 0,383 | 0 |
| hático | 0,344 | 0,375 | 0 |
| acadio | 0,368 | 0,417 | 0 |
| ugarítico | 0,376 | 0,392 | 0 |
| sumerio | 0,395 | 0,436 | 0 |
| **etrusco** | 0,424 | 0,389 | *\*6** |

Con los valores del Lineal B el minoico está más cerca de toda lengua real que bajo cualquier asignación al azar, salvo de una. Los valores no son arbitrarios: producen un perfil de consonantes que se parece al de una lengua real, y arrastran al minoico hacia las lenguas reales en general y hacia el griego en particular. Por eso ninguna otra candidata puede competir, y por eso el resultado de la sección 4 no puede leerse como evidencia a favor del griego.

**El etrusco es la excepción.** Seis de cien asignaciones al azar acercan el minoico al etrusco más que los valores del Lineal B: los valores empujan al minoico lejos del etrusco respecto del azar. Seis de cien no es un hallazgo. Es la única dirección de la tabla que el filtro esconde en vez de fabricar, y es donde debería probarse primero una asignación alternativa y fundamentada de valores.

## 6. Qué queda cerrado y qué queda abierto

**Cerrado, con nulo:** que la fonotaxis consonántica del minoico bajo la transcripción vigente se parezca a alguna de trece candidatas. Las tres históricas (luvita, hurrita, hático) se miden aquí contra un nulo por primera vez, y ninguna pasa.

**No cerrado:** la filiación del minoico. Cuatro lecturas siguen siendo compatibles con todo lo medido: que el minoico sea aislado; que esté emparentado con una lengua que no está en el conjunto; que el filtro griego deforme la fonotaxis demasiado para que sobreviva señal alguna; o que los valores del Lineal B sean incorrectos para el Lineal A, en cuyo caso lo medido es la fonotaxis de una transcripción incorrecta. Las dos últimas son el mismo obstáculo visto desde dos lados, y son lo que cualquier comparación fonológica ulterior tiene que resolver antes de añadir candidatas. Añadir candidatas no es el remedio: cincuenta más devolverían cincuenta p-valores cerca de 1,00 por la misma razón.

**Lo que no pasa por el filtro** es la tipología: orden de palabras, afijación, reduplicación y otras propiedades estructurales que pueden medirse sobre una transliteración sin depender de sus valores fonéticos. Tres rasgos así codificados para el minoico y cotejados con la base Grambank (Skirgård y otros 2023) ya apuntan en una dirección (el luvita y el acadio puntúan 0 de 3, el sumerio y el abjasio 3 de 3), pero tres rasgos binarios no discriminan entre 2.467 lenguas, y las candidatas históricas están casi ausentes de Grambank por ser lenguas muertas. Ese es el trabajo que este artículo deja: diez rasgos estructurales medidos distribucionalmente para el minoico, y las candidatas muertas codificadas a mano desde sus gramáticas.

## 7. Discusión

El siglo de propuestas no se equivocó al hacer la pregunta; no pudo responderla, porque la respuesta exige poner a cada candidata en el mismo formato y darle a cada una la misma oportunidad de fallar. Hecho así, toda candidata falla al nivel de la fonotaxis consonántica, y el único éxito aparente es el instrumento viendo su propia transcripción. Eso es un resultado, no la falta de uno: retira el argumento fonológico de todas las propuestas de la lista, y dice dónde tendría que hacerse el argumento en su lugar.

Hay aquí una lección que va más allá del Lineal A. Ventris no tuvo bilingüe; tuvo una rejilla estructural y una lengua candidata cuya gramática podía aplicarse y contrastarse. Donde la lengua candidata se desconoce, la rejilla tiene que soportar más peso, y la rejilla es exactamente lo que proporcionaría una tipología independiente de la transcripción. El camino existe; lo que este artículo establece es que el atajo fonológico está cerrado bajo los valores vigentes.

## Datos y reproducibilidad

Lineal A según la transcripción del LinearA Explorer sobre GORILA. Lineal B, hitita (6.000 palabras), ugarítico y eteocretense del conjunto corpus_all del proyecto compañero. Hurrita, hático, luvita, palaico y un segundo hitita de TLHdig 25.1 (Zenodo 15459134, Hethitologie-Portal Mainz). Sumerio, acadio y elamita del volcado ATF de CDLI (CC BY 4.0). Etrusco de OpenEtruscan. El normalizador, el nulo y la calibración están implementados en el paquete kuro; los corpus candidatos no se redistribuyen, y los scripts que los descargan y filtran sí.

## Declaración de asistencia

El procesamiento del corpus, las pruebas y la redacción de este texto se produjeron con la asistencia de un modelo de lenguaje (Claude, Anthropic) bajo la dirección del autor, que es responsable de todas las afirmaciones aquí hechas.

## Referencias

Facchetti, G. M. 2001. Appunti di morfologia etrusca. Florencia: Olschki.

Finkelberg, M. 1990-91. Minoan inscriptions on libation vessels. Minos 25-26, 43-85.

Gordon, C. H. 1966. Evidence for the Minoan Language. Ventnor: Ventnor Publishers.

Nepal, A. y F. Perono Cacciafoco 2024. Minoan Cryptanalysis: Computational Approaches to Deciphering Linear A and Assessing Its Connections with Language Families from the Mediterranean and the Black Sea Areas. Information 15(2), 73.

Palmer, L. R. 1958. Luvian and Linear A. Transactions of the Philological Society 57, 75-100.

Skirgård, H., H. J. Haynie, D. E. Blasi y otros 2023. Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. Science Advances 9(16), eadg6175.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos y N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Steele, P. M. y T. Meißner 2017. From Linear B to Linear A: the backward projection of sound values. En P. M. Steele (ed.), Understanding Relations Between Scripts. Oxford: Oxbow.

TLHdig 2025. Thesaurus Linguarum Hethaeorum digitalis, versión 25.1. Hethitologie-Portal Mainz. Zenodo, doi 10.5281/zenodo.15459134.

van Soesbergen, P. 2022. The Decipherment of Minoan Linear A. Volúmenes I-II. Academia.edu.

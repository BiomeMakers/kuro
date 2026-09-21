# Trece candidatas a parientes del minoico medidas contra un mismo nulo, y por qué ninguna lo pasa

**Alberto Acedo**
Biome Makers Inc. Borrador v0.2, 10 de septiembre de 2026. No circular.

## Resumen

Durante un siglo la lengua del Lineal A se ha atribuido, por distintos autores, al anatolio, al semítico, al hurrita, al tirsénico y al griego, o se ha declarado aislada, y ninguna propuesta se ha contrastado con las demás con un instrumento común. Este artículo lo hace. Trece corpus (griego micénico, hitita de dos fuentes, luvita, palaico, hurrita, hático, acadio, ugarítico, sumerio, elamita, eteocretense y etrusco) se reducen junto con el léxico del Lineal A a un mismo esqueleto consonántico cuya pérdida se declara por corpus, y sus perfiles de bigramas de consonantes se comparan con el minoico bajo un nulo que baraja las consonantes de cada palabra minoica entre sus posiciones. El instrumento se calibra antes: sobre las doce lenguas conocidas separa lenguas 2,5 veces más de lo que separa mitades de una misma lengua. Sobre el minoico, una candidata queda más cerca que el minoico barajado, el griego micénico (p = 0,01), y es la que no puede contar: el Lineal A se lee con los valores fonéticos del Lineal B, de modo que sus secuencias de consonantes heredan las restricciones del griego por construcción. Barajar esos valores entre los setenta y cinco silabogramas del Lineal A muestra que la asignación del Lineal B acerca el minoico a toda lengua real más que cualquiera de cien asignaciones al azar, lo que cuantifica el filtro. Las otras doce candidatas, incluidas las tres históricas medidas aquí contra un nulo por primera vez, no están más cerca del minoico que el minoico desordenado (p entre 0,22 y 1,00). La transcripción se convierte entonces en variable: una búsqueda por recocido simulado sobre los valores de los 59 signos no anclados por los nombres compartidos con el Lineal B, con la misma búsqueda aplicada a un minoico de control sin secuencias reales, no acerca el corpus real a ninguna de las trece más de lo que se deja acercar el control (z máxima 1,7, luvita, con 21 controles). El resultado cierra, con nulo, la afirmación de que la fonotaxis minoica se parezca a alguna candidata conocida, bajo la transcripción vigente y bajo cualquier asignación de valores compatible con los topónimos.

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

## 5 bis. Bajo cualquier asignación de valores

Si los valores del Lineal B son el filtro, la pregunta siguiente es qué valores tendrían que tener los signos para que el minoico se pareciera a cada candidata, y cuánto se acerca en el mejor caso. Se fijan los dieciséis signos anclados por los nombres compartidos con el Lineal B (los de pa-i-to, su-ki-ri-ta, se-to-i-ja, da-i-pi-ta, i-ta-ja, ki-da-ro y las cinco vocales) y se buscan por recocido simulado, sobre intercambios de valores entre los otros 59, los que minimizan la distancia a cada candidata (6.000 pasos). Con 59 valores libres cualquier cosa se acerca a cualquier cosa, y por eso el control es el resultado: la misma búsqueda aplicada a un minoico con las sílabas barajadas entre palabras, que conserva inventario y longitudes y destruye las secuencias (cinco controles por candidata; 21 para la mejor).

| candidata | valores del B | mejor real | control (media) | z |
|---|---|---|---|---|
| luvita | 0,220 | 0,113 | 0,120 | 2,3 (1,7 con 21 controles) |
| hitita | 0,181 | 0,105 | 0,110 | 1,5 |
| micénico | 0,100 | 0,053 | 0,054 | 1,3 |
| sumerio | 0,322 | 0,219 | 0,222 | 1,0 |
| acadio | 0,295 | 0,193 | 0,194 | 0,4 |
| ugarítico | 0,257 | 0,171 | 0,172 | 0,1 |
| elamita | 0,275 | 0,200 | 0,200 | 0,1 |
| hático | 0,233 | 0,122 | 0,119 | −1,0 |
| eteocretense | 0,243 | 0,174 | 0,171 | −1,2 |
| palaico | 0,207 | 0,125 | 0,119 | −1,4 |
| hurrita | 0,198 | 0,121 | 0,114 | −2,3 |
| etrusco | 0,312 | 0,189 | 0,177 | −3,2 |

Ninguna candidata supera al control por más de dos desviaciones con controles suficientes. La mejora de las distancias es la que produce cualquier optimización con 59 grados de libertad, y el control la reproduce entera. El etrusco, que en la sección 5 era la única dirección que los valores del B alejaban respecto del azar, aquí se deja acercar menos que el control; las dos medidas no se contradicen (comparan cosas distintas) y juntas dicen que no hay nada ahí. Lo mismo vale para la asignación por forma de signo de Nepal y Perono Cacciafoco (2024), transcrita de su tabla 2 y probada con el mismo instrumento: aleja el minoico de todas las candidatas menos del etrusco, y 35 de 100 asignaciones al azar lo acercan más que la suya.

## 5 ter. Un método publicado con la misma forma, y en qué se diferencia esta prueba

La búsqueda de la sección anterior tiene un precedente publicado que hay que declarar. Tamburini (2025) plantea el desciframiento como la minimización de una función de energía sobre asignaciones de signos, resuelta con recocido simulado acoplado, y codifica las soluciones con k-permutaciones, lo que permite representar correspondencias nulas, de uno a muchos y de muchos a uno; la nuestra solo permuta valores uno a uno. Su sistema supera al estado del arte anterior en identificación de cognados sobre siete conjuntos de referencia, entre ellos el de Lineal B contra griego micénico.

La diferencia no está en el optimizador sino en lo que se compara al final. Tamburini evalúa contra listas de cognados conocidos: mide aciertos contra una verdad disponible. En un desciframiento real esa verdad no existe, y él mismo lo señala al discutir los límites de estos sistemas. Lo que aquí se añade es el comparandum que falta: la misma búsqueda, con los mismos grados de libertad y el mismo número de pasos, aplicada a un corpus de control que conserva el inventario de signos y las longitudes de palabra y destruye las secuencias. Sin ese control, la mejora de distancia que produce optimizar cincuenta y nueve valores libres no se puede interpretar; con él, la mejora del corpus real se lee contra la que obtiene un corpus sin lengua.

## 6. Qué queda cerrado y qué queda abierto

**Cerrado, con nulo:** que la fonotaxis consonántica del minoico se parezca a alguna de trece candidatas, bajo la transcripción vigente (sección 4) y bajo cualquier asignación de valores compatible con los nombres compartidos (sección 5 bis). Esos nombres compartidos son, por su parte, lo único que el cotejo léxico con el Lineal B devuelve por encima del azar: con el léxico completo del B (5.234 formas) y un nulo de bigramas de sílabas, las coincidencias exactas de tres o más sílabas se concentran en los topónimos (3 observadas contra 0,24 esperadas), rozan el azar en los nombres de persona (3 contra 0,95) y están en el azar en los lexemas (2 contra 0,54). Las coincidencias entre las dos escrituras son geografía compartida, no lengua. Las tres históricas (luvita, hurrita, hático) se miden aquí contra un nulo por primera vez, y ninguna pasa.

**No cerrado:** la filiación del minoico. Cuatro lecturas siguen siendo compatibles con todo lo medido: que el minoico sea aislado; que esté emparentado con una lengua que no está en el conjunto; que el filtro griego deforme la fonotaxis demasiado para que sobreviva señal alguna; o que los valores del Lineal B sean incorrectos para el Lineal A, en cuyo caso lo medido es la fonotaxis de una transcripción incorrecta. La cuarta queda ahora acotada por la sección 5 bis: ni siquiera una asignación libre de los valores no anclados produce parecido. Las tres primeras siguen abiertas, y ninguna se resuelve añadiendo candidatas. Añadir candidatas no es el remedio: cincuenta más devolverían cincuenta p-valores cerca de 1,00 por la misma razón.

**Lo que no pasa por el filtro** es la tipología: orden de palabras, afijación, reduplicación y otras propiedades estructurales que pueden medirse sobre una transliteración sin depender de sus valores fonéticos. Tres rasgos así codificados para el minoico y cotejados con la base Grambank (Skirgård y otros 2023) ya apuntan en una dirección (el luvita y el acadio puntúan 0 de 3, el sumerio y el abjasio 3 de 3), pero tres rasgos binarios no discriminan entre 2.467 lenguas, y las candidatas históricas están casi ausentes de Grambank por ser lenguas muertas. Ese es el trabajo que este artículo deja: diez rasgos estructurales medidos distribucionalmente para el minoico, y las candidatas muertas codificadas a mano desde sus gramáticas.

## 6 quater. La candidata que el resultado de la fórmula obligaba a probar: el egipcio

La fórmula de libación del Lineal A tiene la arquitectura de la fórmula de ofrenda egipcia (Acedo 2026, "An Egyptian pattern in the Linear A libation formula"). Una arquitectura compartida no implica una lengua compartida, pero obliga a medirlo. Con el corpus AES (Ancient Egyptian Sentences, Schweitzer 2021; 101.796 frases del Thesaurus Linguae Aegyptiae, 14.584 lemas usables, transcripción egiptológica consonántica reducida al mismo esqueleto que las demás), el egipcio se comporta como las trece: bajo los valores del Lineal B, distancia 0,242 contra 0,236 del minoico barajado (p=1,00); bajo la búsqueda anclada de valores, el corpus real llega a 0,170 y el control a 0,170 ± 0,001 (z=−0,6). El minoico adoptó la forma de una fórmula egipcia sin que su fonotaxis se parezca a la egipcia, que es lo que el contacto sin cambio de lengua predice.

## 6 quinquies. Una reclamación semítica hecha mientras se escribía esto

En junio de 2026, Tom Di Mino anunció el desciframiento del Lineal A como lengua semítica extinta, antecesora del hebreo, el arameo y el árabe. Su punto de partida es el signo \*301, sin valor fonético asignado, al que propone el valor *na*: con él, la fórmula votiva contiene la raíz semítica n-w-y, *nawaya*, "morar", atestiguada en hebreo y acadio. De ahí declara 42 lecturas de signo, un léxico de 508 entradas y 443 traducciones (*Ya Diktu*, agosto de 2026), construido con guiones sobre GORILA y SigLA, las mismas fuentes de este trabajo. Está en revisión en Rutgers y Cambridge; el método de cada asignación no es público y nadie lo ha replicado. La hipótesis semítica la propuso Cyrus Gordon en 1957 y el campo no la aceptó.

Las medidas de este artículo tienen que ver con eso y conviene decir exactamente cuánto. El ugarítico está entre las trece: bajo los valores del Lineal B su distancia al minoico no se distingue de la del minoico barajado. Y la búsqueda anclada de la sección 5 bis optimiza los valores de los signos no anclados, \*301 entre ellos, con recocido simulado y corpus de control: **ninguna candidata semítica baja por debajo de su control**, y la z máxima de toda la tabla es 1,7 y corresponde al luvita. Bajo ninguna asignación de valores compatible con los topónimos compartidos con el Lineal B el corpus se parece a una lengua semítica más de lo que se le parece un corpus sin lengua.

Eso es una afirmación sobre el corpus y no sobre una inscripción. Un texto votivo puede llevar préstamos de una lengua a la que el corpus no pertenece, que es lo que muestra el vocabulario de mercancías compartido con el Lineal B, y una lectura correcta de un texto no obliga al resto del corpus a parecerse a la lengua de esa lectura. Lo que este artículo aporta a la discusión no es un veredicto sobre esa propuesta, sino la medida contra la que cualquier propuesta puede contrastarse, y la exigencia, común a todas, de declarar el control.

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

Tamburini F. 2025, On automatic decipherment of lost ancient scripts relying on combinatorial optimisation and coupled simulated annealing, Frontiers in Artificial Intelligence 8:1581129.

Di Mino T. 2026, Ya Diktu: Grammar of the Minoan Peak Sanctuary Libation Formula, unpublished draft, August 2026.

Gordon C.H. 1957, Notes on Minoan Linear A, Antiquity 31, 124-130.

Skirgård, H., H. J. Haynie, D. E. Blasi y otros 2023. Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. Science Advances 9(16), eadg6175.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos y N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Steele, P. M. y T. Meißner 2017. From Linear B to Linear A: the backward projection of sound values. En P. M. Steele (ed.), Understanding Relations Between Scripts. Oxford: Oxbow.

TLHdig 2025. Thesaurus Linguarum Hethaeorum digitalis, versión 25.1. Hethitologie-Portal Mainz. Zenodo, doi 10.5281/zenodo.15459134.

Schweitzer S.D. 2021. AES – Ancient Egyptian Sentences. Corpus of Ancient Egyptian sentences for corpus-linguistic research (CC BY-SA 4.0), github.com/simondschweitzer/aes.

van Soesbergen, P. 2022. The Decipherment of Minoan Linear A. Volúmenes I-II. Academia.edu.

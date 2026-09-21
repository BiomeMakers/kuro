# Qué puede afirmarse de un corpus de siete mil signos: pruebas con nulos, calibración y confusores en el Lineal A, con el etrusco como control

**Alberto Acedo**
Biome Makers Inc. Borrador v0.3, 9 de septiembre de 2026. Las secciones 6 y 7 se revisarán con la evaluación externa de la lectura que discuten.

## Abstract

Small undeciphered corpora invite two opposite errors: readings obtained from sound alone, which any large lexicon can supply, and agnosticism that treats every statement as untestable. This paper describes a procedure that sits between the two and applies it to Linear A (7,000 signs, 1,719 documents, 799 distinct sign-groups): every distributional claim is tested against a permutation null that preserves what must be preserved; the instruments are calibrated beforehand on Etruscan, where the answers are known; the confounders of site, period, genre and scribal hand are separated where the data allow and declared inseparable where they do not; and negative results are reported with their numbers. On Linear A the procedure fixes a map of what the corpus can support: the language is not Greek even when read with Greek values; the phonotactic distance between the accounting archives and the cult inscriptions is as large as the distance to Greek and its causes cannot be separated; twenty names of the Haghia Triada archive survive in Knossian Linear B under an explicit rule; three suffixes and one prefix have measurable distributions; vocabulary sharing at Haghia Triada is explained by scribal hand rather than by document type; sound-based matching does not discriminate among candidate languages; and two-syllable form matches carry no signal in either Aegean script. The same procedure produced, and then corrected, one lexical proposal, reported elsewhere.

**Keywords:** Linear A, Etruscan, permutation tests, null models, calibration, confounders, undeciphered scripts, computational epigraphy.

## 1. La necesidad

El Lineal A tiene unos siete mil signos repartidos en 1.719 documentos, la mayoría tablillas de contabilidad de Hagia Triada y Chania, sin bilingüe y sin pariente lingüístico conocido. Los intentos de lectura, desde Gordon a Georgiev y desde Palmer a Finkelberg, han seguido el mismo camino: asignar a los signos los valores del Lineal B, buscar en una lengua conocida palabras parecidas y encontrarlas, porque un silabario de noventa signos y palabras de dos o tres sílabas producen coincidencias con cualquier léxico amplio (Duhoux 1989). El estudio computacional reciente de Nepal y Perono Cacciafoco (2024) reconoce tres limitaciones que son las que este trabajo aborda: no filtrar las coincidencias casuales, no distinguir préstamo de azar, y no medir la potencia de un corpus pequeño. Los editores del primer volumen colectivo dedicado a la escritura (Petrakis y Steele 2025) añaden una observación que aquí se toma como punto de partida: el corpus publicado equivale al de un solo escriba de Pilos, y no hay razón para suponer que exista un "punto crítico" de cantidad a partir del cual los resultados se vuelvan fiables; el problema no es solo el tamaño sino la ausencia de un término de comparación.

Lo que aquí se propone no es un método de lectura sino un procedimiento para fijar el mapa de lo afirmable. Sus componentes no son nuevos: el análisis distribucional es el de Duhoux y Davis, los nulos de permutación con márgenes fijos vienen de la ecología de comunidades (Gotelli 2000; Strona et al. 2014), la calibración en un corpus con respuesta conocida es práctica corriente en cualquier instrumento. Lo que no se había hecho en este campo es combinarlos con disciplina y publicar los negativos con número, y eso es lo que sigue.

## 2. Datos y procedimiento

### 2.1 Corpus

Transliteraciones de GORILA (Godart y Olivier 1976-1985) en la forma legible por máquina del LinearA Explorer (Hogan 2022), que conserva subíndices, sitio, soporte, contexto arqueológico, las atribuciones de mano de GORILA V y los comentarios de Younger (2024b) con los datos de sello. Verificación de signos en el conjunto de datos de SigLA (Salgarella y Castellan 2020). Para el Lineal B, la edición del mismo autor sobre las ediciones estándar (5.889 documentos, 5.597 grupos de signos), con las manos de Cnosos de Olivier. Para el etrusco, el corpus de Larth (Vico) con 7.139 registros y el corpus ETP (429 textos con metadatos). Un defecto conocido de los datos del Explorer, la etiqueta de soporte de las tablillas de Zakros, se corrigió desde SigLA; una ligadura de su transliteración (\*304+PA-KU-PA en HT Wa 1020) resultó ser dos signos consecutivos según SigLA, y se registra aquí como advertencia sobre las transliteraciones derivadas.

### 2.2 Unidades y medidas

Las unidades son los grupos de signos (799 tipos, 1.117 tokens en tablillas con dos o más grupos; 76% de hapax), los documentos como conjuntos de grupos, y los perfiles de sílabas iniciales y de esqueletos consonánticos. Las medidas son las habituales: distancia de Jensen-Shannon entre perfiles (ecuación 1), índice de Jaccard entre documentos (ecuación 2), correlación de Mantel entre matrices de distancia (ecuación 3), información mutua entre posiciones (ecuación 4), y el algoritmo curveball para nulos de márgenes fijos en matrices de presencia (ecuación 5, Strona et al. 2014). Cada una se enuncia en el apéndice con su fuente.

### 2.3 Nulos

Cada afirmación lleva el nulo que conserva lo que la afirmación no pretende explicar: para la coocurrencia entre documentos, permutaciones que conservan el número de grupos por documento y el número de documentos por grupo (curveball); para la morfología, permutación de la sílaba afijada entre todas las palabras conservando sus longitudes; para las clases por posición, permutación de etiquetas; para los confusores, permutación dentro de estrato (etiqueta de tipo dentro de mano, o de mano dentro de tipo). El umbral se fijó en p < 0,01 con mil permutaciones para afirmaciones nuevas y p < 0,05 para réplicas; las comparaciones múltiples se corrigen por Bonferroni cuando son menos de diez y por Benjamini-Hochberg cuando son más.

### 2.4 Potencia

Antes de cada test se estimó el efecto mínimo detectable con el n disponible. Dos cifras gobiernan el resto: el suelo de distancia entre dos muestras del mismo corpus a 42 tipos es 0,198 (Jensen-Shannon sobre esqueletos consonánticos), de modo que ninguna diferencia menor es detectable a ese tamaño; y en el etrusco, el test de sibilantes tiene 68 pares utilizables, que es el orden de magnitud de los tests posicionales del Lineal A. Un test cuyo efecto esperado cae bajo el suelo se declara indecidible y no se corre.

## 3. Calibración en etrusco

El etrusco es el control adecuado: alfabeto leído, lengua no indoeuropea entendida a medias, corpus del tamaño del Lineal A y con metadatos de ciudad y de época, y tres hechos gramaticales o sociolingüísticos establecidos que el procedimiento debe recuperar sin que se le digan.

Genitivo ante los términos de filiación. Ante la palabra clan, "hijo", el nombre del padre va en genitivo. Medido sobre el corpus completo de OpenEtruscan (5.941 textos distintos, 5.470 de ellos en calidad limpia), el test posicional aplicado a ciegas encuentra la terminación -l en 11 de las 18 palabras que preceden a clan (61%) frente a 1,4 esperadas por la frecuencia general de esa terminación en el vocabulario, y en 5 de las 13 que preceden a sec, "hija" (38%, esperadas 1,0). Los dos superan el nulo de muestreo del vocabulario (p < 0,0005 y p = 0,0035).

Y lo hace con la especificidad correcta, que es lo que distingue un instrumento de un generador de ruido: ante puia, "esposa", y ante lupu, "murió", que no rigen genitivo, la terminación aparece en 1 de 12 y 1 de 9 casos, dentro de lo esperable (p = 0,63 y p = 0,50). El instrumento ve flexión donde la hay y no la ve donde no la hay.

Síncopa como cambio en el tiempo. La pérdida de vocales interiores se fecha hacia el 500 a.C. El índice de síncopa es 0,28 más alto en los textos tardíos que en los tempranos, y el efecto se mantiene al controlar la ciudad (p < 0,002 dentro de ciudad). El instrumento ve tiempo donde lo hay.

Sibilantes como variación geográfica. La distinción gráfica de sibilantes es un rasgo del norte. La razón norte/sur es 0,6 frente a 0,1 (p = 0,72 dentro de ciudad): el efecto es de ciudad, no de época. El instrumento no confunde geografía con tiempo cuando los metadatos permiten separarlas.

La calibración fija lo que se puede esperar del mismo aparato en el Lineal A: recuperará morfología y estratificación si existen y si hay metadatos para separar los confusores; donde no los haya, dirá "indecidible", y esa respuesta hay que aceptarla.

## 4. Resultados con nulo en el Lineal A: qué hay y dónde está

El procedimiento de las secciones 2 y 3 produjo nueve resultados sobre el Lineal A. Cada uno tiene ahora su artículo, y aquí se resumen en una frase con su cifra y su remisión, para que este texto sea el del método y no el de los resultados.

1. **No es griego, ni en su propio silabario**, y no se parece a ninguna de trece candidatas bajo los valores del B ni bajo cualquier asignación anclada por los topónimos (z máxima 1,7). Artículo de las trece candidatas.
2. **Dos registros** (votivo y administrativo) con causas inseparables por el tamaño del corpus. Artículo de la plantilla.
3. **Nombres que sobreviven en Cnosos**: las coincidencias con el B son topónimos (3 contra 0,24), no lexemas. Artículo de los topónimos.
4. **Morfología situada**: los pares raíz/terminación existen y cinco de seis no cambian nada medible; con solo unidades íntegras quedan -JA, -ME, -TI. Artículo de los topónimos, sección 6 bis.
5. **Vocabulario compartimentado por sitio**, y la aritmética como prueba (KU-RO suma). Artículo del recibo, y el inventario.
6. **Los cribados de forma y su control negativo**: el instrumento no encuentra parentesco donde no lo hay. Artículo de las calibraciones.
7. **La fórmula de libación**: función de los huecos sin lectura, techo de predicción 14,0% con su causa. Artículo de la fórmula.
8. **Un perfil tipológico sin lista de candidatas**: cinco rasgos observables, que no seleccionan (187 de 1.064). Artículo de las trece, sección 6.
9. **Las propuestas de filiación y qué predice cada una**: ninguna predicción se cumple. Artículo de las trece.

Y el décimo, que no estaba: **el inventario funcional**, 56 unidades con evidencia a favor y en contra y condición de refutación, con lo que el corpus no puede fijar. Artículo del inventario.

## 5. Negativos de método

Se informan porque cierran vías que otros volverían a abrir.

Un descriptor estructural por nodo (Omega-N, con el código público de BiomeMakers/OmegaN) aplicado a la alineación de signos A y B por su papel en el grafo de coocurrencia recupera el rango medio 27,4 frente a 32,5 del azar (p = 0,018), exactamente lo que recupera el grado por sí solo (26,8): lo que se transfiere entre escrituras es la cuota de grado, y el rol estructural codifica la lengua, no el signo. Dentro del A, el descriptor no tiene fiabilidad test-retest a estos tamaños (exceso triádico entre dos mitades de Hagia Triada +0,06 y +0,02), por lo que cualquier test de estructura fina es indecidible; se propone una condición de tamaño mínimo para el cribado del método.

Un clasificador de función (49 etiquetas, 25 rasgos de posición y compañía) acierta 0,67 a 0,73 escondiendo una etiqueta cada vez, frente a 0,39 a 0,48 con etiquetas barajadas: distingue la fórmula de libación, y las cabeceras de las entradas, pero clasifica como nombre las dos mercancías conocidas, porque de mercancías hay dos ejemplos. La estructura predice función gruesa, no clase semántica.

Un modelo neuronal de desciframiento con y sin el regularizador Omega-S sobre las veinticinco palabras conocidas queda preregistrado con predicción de cero en ambos brazos; no se ha corrido.

La coexclusión entre palabras no tiene potencia a este tamaño (sección 4.5), y la "receta" de aromáticos (proporciones iguales entre ingredientes) es indecidible con las cantidades legibles (0,26 de pares iguales frente a 0,21 del nulo de fracciones, p = 0,24).

Tres pruebas tomadas de la ecología de redes se declaran no concluyentes o retiradas. La curvatura de Forman sobre el grafo de coocurrencia, con la predicción de que los términos de transacción ocupan los puentes, no separa a esos términos del resto en Susa (p = 0,50) y en Hagia Triada apunta en la dirección predicha sin alcanzar significación (p = 0,12), probablemente porque la curvatura de Forman está dominada por el grado; la prueba requiere la curvatura de Ollivier-Ricci y queda pendiente. El gradiente de "energía" (documentos ordenados por volumen de mercancía) no altera la diversidad del vocabulario en Susa (tasa de hapax 0,40, 0,40, 0,36, 0,42 por cuartiles; p = 0,47), de modo que la analogía con el gradiente de energía externa de los suelos no se traslada. Y la razón ascendencia/capacidad de Ulanowicz, que en una primera pasada situaba a Hagia Triada y a Susa en la ventana de vitalidad (a = 0,41 y 0,39, con F máximo en a = 1/e), es reproducida exactamente por un nulo que conserva las sumas de filas y columnas de la matriz documentos × palabras (0,411 y 0,430 en el nulo), y Uruk y el ibérico ni siquiera caen en la ventana: el índice mide las distribuciones marginales y no la estructura, y el resultado se retira. La lección es general y vale para cualquier índice calculado sobre una matriz de recuentos, dentro y fuera de la epigrafía: si el nulo de márgenes fijos lo reproduce, el índice mide los márgenes.

La ligadura \*304+PA-KU-PA del LinearA Explorer no existe: SigLA lee \*629 seguido de KU-PA. Se informa porque sostuvo durante dos días un argumento de una lectura, y porque las transliteraciones derivadas requieren verificación signo a signo antes de usarse como dato.

Una tercera fuente de error del mismo tipo apareció al examinar las palabras que aparecen a la vez en documentos administrativos y en inscripciones sobre piedra: de las dieciocho que comparten los dos vocabularios, dos (JA-SA e I-TI) resultaron ser el ancla JA-SA-SA-RA-ME partida por un salto de línea que la transliteración convierte en dos entradas. Es el tercer caso de artefacto de la fuente derivada en este trabajo, junto a la ligadura inexistente y a las fracciones transcritas como enteros.

Y una cuarta observación afecta a la clasificación del corpus. Reclasificados los 1.719 documentos por su contenido (presencia de anclas de la fórmula; presencia de cantidades y logogramas de mercancía) en lugar de por el material del soporte, la etiqueta de soporte predice bien el contenido salvo en un caso: de los vasos de piedra, 33 son documentos contables y solo 15 llevan fórmula votiva, y los 33 se concentran casi por completo en Zakros, con hasta doce cantidades en una sola pieza (ZA 10b). El corpus votivo real del Lineal A son diecisiete documentos y no los ciento siete que el soporte sugiere, lo que reduce la potencia de cualquier análisis del vocabulario de culto y explica por qué varias de las pruebas de la sección 4.7 resultan indecidibles. La separación entre administración y culto debe hacerse por contenido; la clasificación de los 1.719 documentos acompaña a este trabajo. La comprobación completa, con las veintitrés series medidas una a una, se presenta aparte (Acedo 2026h); baste aquí con que diecisiete de ellas tienen cohesión de logogramas al menos doble que su entorno, y que las seis restantes no contradicen la clasificación: cuatro pertenecen a la clase que Montecchi define por la AUSENCIA de ideograma, de modo que un índice sobre logogramas no puede verlas; dos son fragmentos sin apenas texto; y la sexta, la serie Ec, no comparte logogramas pero sí el 54,5% de su vocabulario, la cifra más alta del corpus, lo que indica que HT 86 y HT 95 son dos versiones del mismo documento. Merece la pena señalar la dirección del resultado: el mismo tipo de prueba aplicado por Corazza y sus coautores (2022) a la división tripartita del chiprominoico obligó a revisarla, y aquí confirma la clasificación existente. Un procedimiento que solo produjera refutaciones sería sospechoso; que confirme unas clasificaciones y refute otras es lo propio de un instrumento cuyo resultado depende del objeto y no del instrumento.


## 6. Un caso: cómo el procedimiento produjo, y después corrigió, una lectura

El procedimiento se ilustra mejor con el caso en que falló a medias. Buscando los grupos de signos que se comportan como cosas contadas (recurrencia dentro de documento con cantidades distintas, cantidades enteras, ausencia en listas de personal), el cribado aisló KU-PA (AB 81-03): repetido en las dos caras de ZA 11 con 1 y 3, en KH 29 con 2, en HT 110a con 1; con una familia de derivados (KA-KU-PA, KU-PA-ZU, KU-PA-JA, KU-PA-RI) que aparecen junto al logograma \*303 en dos rodeles y en KH 5; y con dos afijos que recurren en el corpus por encima del nulo. Solo entonces se comparó la forma: griego κύπαιρος, pregriego según Frisk y Beekes, micénico ku-pa-ro, que glosa el logograma de la juncia en KN Ga 517. La primera versión leyó la familia como la palabra minoica de la juncia, contra la lectura de Younger, que la tenía por nombre de un contribuyente.

Tres comprobaciones posteriores, todas del mismo procedimiento, cambiaron la lectura sin tocar la etimología. La verificación signo a signo en SigLA mostró que la "ligadura" \*304+PA-KU-PA del nódulo HT Wa 1020, uno de los apoyos, era una secuencia de tres signos sin ligadura. La tabulación de los sellos de todos los rodeles de Hagia Triada (comentarios de Younger, SigLA) mostró dos grupos de sellado: uno en que la palabra va sola, y otro en que la palabra va seguida de un logograma de mercancía, y en ese segundo grupo están KA-KU-PA con \*303 pero también A-RA-TU-ME con ovejas y KU-MI-NA-QE con cabras, palabras que no pueden ser mercancías. Y la estructura de KH 5 (grupo, logograma, cantidad, con WI-SA-SA-NE ante \*626 y KU-PA-ZU ante \*303) resultó ser la de partes ante mercancías. La lectura corregida es la que concilia: la raíz KU-PA es la palabra de la planta; la familia de los archivos es un nombre formado sobre ella, como Kyparissos o Maratón en griego; y dos casos más del mismo tipo (KU-MI-NA-QE y el comino; KI-KI-RA-JA sobre el KI-KI-NA que Neumann identificó con el higo de sicomoro en 1960) sostienen la pauta.

Lo que el caso enseña sobre el método es lo que importa aquí. Primero, que el orden función-forma no protege por sí solo de un error de función: la recurrencia con cantidades, tomada como firma de mercancía, era compatible con una parte a la que se asigna dos veces, y solo un dato externo a la tablilla (los sellos) lo decidió. Segundo, que cada apoyo debe verificarse en la fuente primaria y no en una transliteración derivada, por buena que sea. Tercero, que la corrección no destruyó el resultado sino que lo situó: la etimología, que era lo único que no dependía de la función, sobrevivió intacta, y la pauta de nombres formados sobre plantas es más defendible y más general que la lectura inicial. El artículo que presenta el caso (Acedo 2026, en evaluación) lleva dentro esa historia porque la historia es parte de la evidencia.

## 7. Discusión

El procedimiento no descifra, y conviene decirlo con las cifras de este trabajo: sobre 7.000 signos produjo dos raíces con significado propuesto, dos nombres descompuestos, dos afijos con función situada, y la plantilla de una fórmula. Lo que produjo con más abundancia son negativos con número, y ese es su valor: cada uno cierra una vía que la bibliografía ha reabierto durante un siglo. La comparación por sonido no discrimina entre lenguas candidatas (todas a 1,3-1,7 sobre su nulo), ni en el Lineal A ni en el Lineal B (383 falsos con la misma regla); la diferencia entre archivos y santuarios no es de tipo administrativo; la coexclusión no es medible a 224 muestras; un descriptor de red no es fiable a este tamaño; un clasificador no aprende una clase de dos ejemplos.

Que los negativos son de tamaño y no de método lo demuestra la calibración cruzada. El mismo aparato, sobre el proto-elamita (1.594 tablillas, 8.282 entradas), recupera en una sesión la clasificación de los signos por sistema numeral, la cabecera institucional y la partición entre nombres y mercancías que el campo estableció en veinte años, y encuentra además el marco de las cadenas largas, 24 monopolios del grano y 13 pares de coexclusión con nulo curveball, que en el Lineal A no tenían potencia. Sobre Uruk (6.387 tablillas), recupera tres de las cuatro predicciones sobre la herencia de los sistemas numerales y refuta la cuarta por ausencia. Sobre el eteochipriota, con 21 inscripciones, el test de perfil se declara sin potencia y el posicional separa las dos lenguas por sus terminaciones (p < 10⁻¹⁶). Sobre el ibérico, con 1.919 textos y solo la provincia como metadato, recupera los formantes onomásticos de Untermann (295 frente a 11 del nulo) y las dos isoglosas gráfico-morfológicas conocidas (el signo S56 final meridional, p = 3·10⁻⁹; el sufijo -ḿi nororiental, p = 3·10⁻⁵). Sobre el chiprominoico, donde no hay respuesta conocida con la que calibrar, el mismo aparato encuentra estructura donde el nulo no la produce: en las 183 inscripciones del conjunto de datos publicado por Corazza, Tamburini, Valério y Ferrara (2022), las secuencias de tres y cuatro signos que se repiten al menos tres veces son 19 y 6, frente a 0,9 y 0 al barajar los signos dentro de cada inscripción conservando longitudes y frecuencias (p < 0,005), de modo que la escritura combina signos en unidades recurrentes; el corpus no permite en cambio el análisis de archivo, porque solo seis de sus inscripciones son tablillas. En cada corpus el instrumento dice lo mismo: lo que hay, lo que no hay, y lo que no puede decirse con ese n. Un trabajo independiente y contemporáneo permite calibrar mejor esa afirmación y conviene citarlo. Briakos (2026), en una tesis de máster en informática sobre el mismo corpus, mide con un corpus sintético del Lineal B fiel a las distribuciones publicadas que el emparejamiento por rango de frecuencia acierta el 13% con los 2.481 tokens disponibles, seis veces el azar pero por debajo del 21% que sería útil, y sitúa el umbral en unos 10.000 tokens, es decir, siete mil quinientos más de los que hay. Ese número es más preciso que nuestra curva de potencia para esa pregunta concreta, y las dos medidas se complementan: la suya dice a qué tamaño empieza a servir el reconocimiento de frecuencias, la nuestra a qué tamaño empieza a ver cada instrumento distribucional. Sus resultados sobre la divergencia entre registros (p = 0,018 por permutación) y sobre las huellas de escriba (veintitrés manos con preferencias de bigramas distintivas) coinciden con los nuestros por vías distintas, lo que refuerza ambos. Y su trabajo aporta dos prácticas que hemos adoptado: etiquetar cada estadístico según su procedencia (calculado del corpus con el hash del fichero registrado, tomado de la literatura con cita, o meramente ilustrativo), y comprobar si una diferencia aparente entre grupos no rastrea las condiciones de registro del dato en lugar del dato; él encontró que una separación geográfica aparente en un análisis visual seguía al brillo fotográfico con r = 0,990.

Aplicado ese último control a nuestro corpus, el resultado obliga a una cautela que no habíamos declarado: la longitud media de documento varía un 311% entre yacimientos y un 274% entre soportes, y la proporción de signos dañados varía todavía más. Cualquier comparación de perfiles entre grupos debe emparejarse por longitud antes de interpretarse, cosa que hicimos en la sección 4.2 al fijar el tamaño de muestra, pero que no habíamos justificado con esta medida.

![](fig_curva_potencia.png)

*Fig. 1. A qué tamaño de corpus empieza a ver cada instrumento. Círculo lleno: detecta la estructura; aspa: no la detecta, o el nulo de márgenes la reproduce; raya: no aplicable. La coexclusión, el marco de las cadenas largas y el perfil por subcorpus aparecen entre 800 y 1.600 documentos; los afijos y la aritmética funcionan ya a 224; el control de mano solo donde hay atribución de escribas.*


Una nota sobre el procedimiento, para que las cifras anteriores se lean bien. El trabajo tuvo una fase exploratoria, sin hipótesis previa, de la que no se afirma nada por sí solo: sus resultados se trataron como hipótesis y solo se conservan los que se replicaron con un nulo específico o se confirmaron en otro corpus. Las afirmaciones nuevas proceden de la fase preregistrada, en la que cada hipótesis llevaba su nulo, su umbral y su regla de parada antes de correrse. Dentro de cada familia de pruebas se corrige por comparaciones múltiples (Bonferroni en los once sufijos, donde ninguno sobrevive al umbral corregido, y en las sesenta terminaciones ibéricas; Benjamini-Hochberg en las asociaciones de signo y sistema), y las pruebas de una sola hipótesis preregistrada se informan con su p exacta. Tres resultados de la fase exploratoria no sobrevivieron y se declaran retirados en la sección 5.

El origen del aparato es la ecología de comunidades, y la analogía merece una frase, no más: los documentos son muestras, las palabras taxones, y las preguntas sobre coocurrencia, coexclusión, especificidad y recambio son las mismas que se hacen a una comunidad microbiana, con los mismos nulos (Gotelli 2000; Strona et al. 2014) y con el mismo requisito de fiabilidad test-retest que exige cualquier índice de estructura (Acedo 2026b). Lo que la epigrafía añade a la ecología es un confusor que en las muestras biológicas se llama lote y aquí se llama escriba: en Hagia Triada el vocabulario compartido lo explica la mano y no el tipo de documento (p = 0,002 frente a 0,21), y un índice de nicho que no lo controlara mediría carteras de escriba. Lo que la ecología añade a la epigrafía es la costumbre de preguntar, antes de leer, si el corpus tiene tamaño para responder. Un caso reciente ilustra el rendimiento de esa manera de mirar. La frecuencia de un producto en un archivo mide su importancia económica local y no su importancia en la receta: la juncia aparece 84 veces en 61 documentos del Lineal A y es la tercera mercancía del archivo, mientras que en el corpus micénico, cinco veces mayor, aparece tres veces, y dos en el asirio medio. La inversión no es de muestreo: indica que Creta producía lo que Mesopotamia importaba. Y el criterio inverso también informa: lo que un archivo no registra puede ser tan revelador como lo que registra, porque un inventario solo contiene lo que se almacena y solo se almacena lo que dura y lo que vale. Eso explica que no haya logograma de agua en ninguna de las dos escrituras egeas, y que las flores, cuyos perfumes duraban dos meses según Teofrasto, no aparezcan donde sí aparecen las raíces y las resinas.

Hacia dónde sigue esto no es hacia la lectura. Es hacia los anclajes: cada palabra pregriega cuya raíz aparece en las tablillas con la función correcta es una línea de una bilingüe sintética, y con treinta de esas líneas el minoico tendría vocabulario, morfología sobre ese vocabulario y una fórmula con partes, aunque no se pronunciara. El procedimiento descrito aquí es la fábrica de esos anclajes, y la garantía de que cada uno lleva su nulo, su calibración y su corrección cuando toca.

## Declaración de asistencia

El procesamiento de los corpus, las pruebas de permutación y los borradores de este texto se produjeron con la asistencia de un modelo de lenguaje (Claude, Anthropic) bajo la dirección del autor, responsable de todas las afirmaciones.

## Apéndice: ecuaciones

(1) Distancia de Jensen-Shannon: JSD(P,Q) = ½ D(P‖M) + ½ D(Q‖M), M = (P+Q)/2, D la divergencia de Kullback-Leibler en base 2 (Lin 1991).
(2) Índice de Jaccard: J(A,B) = |A ∩ B| / |A ∪ B| (Jaccard 1901).
(3) Correlación de Mantel entre matrices de distancia, con permutación de filas y columnas (Mantel 1967).
(4) Información mutua entre posiciones: I(X;Y) = Σ p(x,y) log₂ [p(x,y) / p(x)p(y)] (Shannon 1948).
(5) Nulo de márgenes fijos por el algoritmo curveball (Strona et al. 2014), que conserva las sumas de filas y columnas de la matriz documentos × palabras.

## Referencias (provisionales)

Acedo, A. 2026. Nombres minoicos formados sobre fitónimos: KU-PA y la juncia, KU-MI-NA-QE y KI-KI-RA-JA en los archivos del Lineal A. Borrador en evaluación.

Acedo, A. 2026b. Mensurabilidad del FSRI: condiciones de tamaño y fiabilidad test-retest. Borrador.

Acedo, A. 2026f. La fórmula de libación del Lineal A: función de los huecos y frases candidatas. Borrador.

Acedo, A. 2026g. Registro de pruebas y preregistro del procedimiento (documento de acompañamiento).

Best, J. and F. Woudhuizen 1989. Lost Languages from the Mediterranean. Leiden.

Chadwick, J. The classification of the Knossos tablets.

Corazza, M., F. Tamburini, M. Valério and S. Ferrara 2022. Unsupervised deep learning supports reclassification of Bronze Age Cypriot writing system. PLOS ONE 17(7), e0269544.

Acedo, A. 2026h. Una clasificación de 2010 puesta a prueba: las clases y series de Hagia Triada bajo permutación. Borrador.

Briakos, N. 2026. An Undeciphered Script in the Age of AI: A Corpus-Constrained Computational Analysis of Linear A. Tesis de máster, Universidad del Pireo.

Dahl, J. L. 2019. Tablettes et fragments proto-élamites / Proto-Elamite Tablets and Fragments (MDP 32). Paris.

Damerow, P. and R. K. Englund 1989. The Proto-Elamite Texts from Tepe Yahya. Cambridge, MA.

Davis, B. 2018. The Phaistos Disk: a new way of viewing the language behind the script. OJA 37, 373-410.

Duhoux, Y. 1989. Le linéaire A: problèmes de déchiffrement. In Problems in Decipherment, Louvain-la-Neuve, 59-119.

Georgiev, V. 1963. Les deux langues des inscriptions crétoises en linéaire A. Sofia.

Godart, L. and J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A, I-V. Paris.

Gordeziani, R. 2007. Mediterranean-Kartvelian Structural Parallels. Tbilisi.

Gordon, C. H. 1966. Evidence for the Minoan Language. Ventnor.

Gotelli, N. J. 2000. Null model analysis of species co-occurrence patterns. Ecology 81, 2606-2621.

Hogan, R. 2022. Linear A Explorer. https://lineara.xyz

Jaccard, P. 1901. Étude comparative de la distribution florale dans une portion des Alpes et du Jura. Bulletin de la Société Vaudoise des Sciences Naturelles 37, 547-579.

Lin, J. 1991. Divergence measures based on the Shannon entropy. IEEE Transactions on Information Theory 37, 145-151.

Mantel, N. 1967. The detection of disease clustering and a generalized regression approach. Cancer Research 27, 209-220.

Montecchi, B. 2019. Contare a Haghia Triada. Incunabula Graeca CVII. Roma.

Montecchi, B. 2009. Le frazioni, gli errori di calcolo e le unità di misura nella documentazione in lineare A. Annali dell'Istituto Italiano di Numismatica 55, 29-52.

Montecchi, B. 2010. A classification proposal of Linear A tablets from Haghia Triada in classes and series. Kadmos 49, 11-38.

Nepal, A. and F. Perono Cacciafoco 2024. Minoan cryptanalysis. Information 15(2), 73.

Owens, G. 1999. The structure of the Minoan language. Journal of Indo-European Studies 27, 15-56.

Palmer, L. R. 1958. Luvian and Linear A. Transactions of the Philological Society 57, 75-100.

Petrakis, V. and P. M. Steele 2025. The Wor(l)ds of Linear A: some concluding thoughts. In The Wor(l)ds of Linear A, Athens, 167-176.

Salgarella, E. and S. Castellan 2020. SigLA. https://sigla.phis.me

Shannon, C. E. 1948. A mathematical theory of communication. Bell System Technical Journal 27, 379-423.

Steele, P. M. 2013. A Linguistic History of Ancient Cyprus. Cambridge.

Strona, G., D. Nappo, F. Boccacci, S. Fattorini and J. San-Miguel-Ayanz 2014. A fast and unbiased procedure to randomize ecological binary matrices with fixed row and column totals. Nature Communications 5, 4114.

Untermann, J. 1990. Monumenta Linguarum Hispanicarum III. Die iberischen Inschriften aus Spanien. Wiesbaden.

Vico, G. 2023. Larth: Etruscan NLP corpus. https://github.com/GianlucaVico/Larth-Etruscan-NLP

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos y N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Younger, J. G. 2024a-b. Linear A Lexicon; Linear A Texts in Phonetic Transcription. https://kansas.academia.edu/JYounger

# Qué debe declarar una propuesta de lectura de una escritura no descifrada, cómo se mide, y qué ve el instrumento donde la respuesta se conoce

**Alberto Acedo**
Biome Makers Inc. Versión de envío v1.0, 11 de septiembre de 2026 (funde el protocolo v0.2, el método v0.3 y las calibraciones v0.2). No circular.

## Resumen

Las propuestas de lectura de escrituras no descifradas rara vez declaran qué dato las refutaría, con qué nulo se han contrastado y cuántas pruebas se hicieron antes de encontrar la que se publica. Este artículo hace tres cosas. Primero, fija ocho requisitos mínimos que una propuesta debería cumplir para poder discutirse (verificación del dato en la edición, nulo declarado y conservador, tasa de error del instrumento, recuento de pruebas, confusores de sitio y soporte, condición de refutación, prior art con su medida, y separación entre función y significado), y los aplica a dos propuestas ajenas y a una generada con un modelo de lenguaje. Segundo, describe el procedimiento que los implementa (el paquete kuro: nulos de permutación que conservan lo que la afirmación no explica, calibración en etrusco, doce instrumentos con tasa de error, un ciclo con puerta de novedad y corrección por lote, y dos etapas con un modelo en el bucle cuya tasa de invención se mide), con sus negativos de método y un caso en que produjo y después corrigió una lectura. Tercero, lo calibra en cuatro corpus donde parte de la respuesta se conoce (etrusco, ibérico, chiprominoico, y los archivos de Susa y Uruk), y reporta en cada uno qué recupera de lo sabido, qué contradice y a qué tamaño deja de ver. La conclusión que sirve al Lineal A es la del contraste: el ibérico, con dos docenas de nombres en una bilingüe, se ancla; el minoico, con seis topónimos consonánticos, no; mismo instrumento, datos distintos.

**Palabras clave:** desciframiento, modelos nulos, calibración, tasa de error, protocolo, Lineal A, etrusco, ibérico, chiprominoico, protoelamita.

# Parte 1. El protocolo

## 1.1. El problema

Las propuestas de lectura aparecen más deprisa de lo que el campo puede evaluarlas, y el premio de un millón de dólares para el índico (2025) ha acelerado el ritmo. El problema no es la falta de competencia: es que no hay un mínimo común de lo que una propuesta debe declarar para que otro pueda juzgarla. Sin ese mínimo, la discusión se resuelve por autoridad o por cansancio, y una propuesta refutada reaparece cinco años después con otro nombre.

Este texto no propone un método ni evalúa propuestas ajenas. Propone ocho requisitos, todos elementales en otras ciencias empíricas, y muestra para cada uno un caso en que su ausencia produjo un falso positivo. Tres de los casos son nuestros, y están ahí a propósito: quien propone un protocolo debe mostrar primero dónde ha fallado él.

## 1.2. Los ocho requisitos

### 1.2.1 Un modelo nulo para cada afirmación distribucional
Toda afirmación del tipo "esta palabra aparece con esta otra", "este afijo es productivo", "estas dos clases de documento difieren" necesita la permutación que conserve lo que la afirmación no pretende explicar y destruya solo lo que sí. No basta un nulo cualquiera: el nulo equivocado produce positivos.
Caso propio: medimos la razón ascendencia/capacidad de la red documentos-palabras en Hagia Triada y en Susa y las dos caían en la "ventana de vitalidad" de Ulanowicz, un resultado atractivo. Con un nulo que conserva las sumas de filas y columnas, el nulo reproduce el valor observado con tres decimales. El índice medía las distribuciones marginales. Retirado.
Caso propio 2: medimos la composicionalidad del léxico minoico (si las palabras largas se descomponen en elementos recurrentes) y salía 0,12 frente a 0,02 del nulo de sílabas barajadas, y por encima del griego a igual tamaño. Con un nulo que conserva las transiciones entre sílabas, el valor observado queda dentro del nulo (p = 0,60): era la fonotaxis del silabario. Retirado.
Regla: el nulo debe conservar todo lo que no es la hipótesis. A este requisito hay que añadirle una segunda parte, que la aplicación del protocolo a una propuesta ajena ha mostrado necesaria. No basta con declarar el nulo: hay que declarar **qué afirmación queda cubierta por él y cuál no**. Un nulo sobre un conjunto no cubre a sus miembros, y es un caso frecuente: en el trabajo compañero sobre topónimos, quince casos superan juntos el nulo y ninguno se sostiene por separado, cosa que allí se escribe expresamente. Y un nulo de coincidencia, por bien construido que esté, mide cuán improbable sería lo observado si no hubiera efecto; no convierte una propuesta en certeza ni elimina la apofenia, que es el sesgo de ver estructura donde no la hay y que ningún cálculo interno al propio material puede descartar. La distancia entre lo que un nulo mide y lo que se concluye de él es un fallo tan real como no correrlo.

### 1.2.2 Un control positivo en un corpus con respuesta conocida
Antes de aplicar un instrumento a lo desconocido hay que comprobar que recupera lo conocido en un corpus comparable. Si no lo recupera, el silencio del instrumento no es información.
Nuestro uso: calibramos en etrusco (recupera el genitivo ante clan, la cronología de la síncopa y la geografía de las sibilantes), en eteochipriota frente a griego chipriota (separa las dos lenguas por sus terminaciones), en proto-elamita (recupera la clasificación de los sistemas numerales de Dahl, la cabecera institucional y la partición nombres/mercancías) y en el ibérico (recupera los formantes de Untermann y dos isoglosas conocidas).
Contraejemplo del campo: la mayoría de las propuestas de lectura del Lineal A y del índico no informan de ningún control positivo, de modo que no se sabe si su método vería la respuesta si estuviera delante.

### 1.2.3 Una predicción sobre texto no visto
Una lectura que solo explica los textos ya conocidos no se puede evaluar. La propuesta debe decir qué espera encontrar en la siguiente inscripción y qué la refutaría.
Nuestro uso: la lectura de la familia KU-PA predice que sus miembros seguirán apareciendo con el logograma de la juncia y con mercancías secas, que un rodel nuevo con KA-KU-PA llevará ese logograma o una ligadura suya, y que la familia no aparecerá como recipiente de líquidos. El protocolo de lo que se hará con el cetro de Cnosos cuando se publique está preregistrado antes de conocer el texto.
Nota: la predicción no exige que aparezca el texto; exige que esté escrita antes.

### 1.2.4 Cuántas pruebas se corrieron, y corrección por comparaciones múltiples
Un procedimiento que prueba cuarenta hipótesis encuentra dos por debajo de 0,05 por azar. La propuesta debe declarar el denominador y corregir dentro de cada familia de pruebas.
Caso propio: de once sufijos probados en el Lineal A, tres superan el umbral sin corregir y ninguno lo supera tras Bonferroni; lo informamos así, y el resultado que sostenemos no es "estos tres sufijos son productivos" sino "hay señal de morfología por posición que ninguno de los sufijos alcanza a demostrar por separado".
Contraejemplo del campo: los cribados de coincidencia léxica entre una escritura no leída y un diccionario extenso, que son de hecho miles de pruebas simultáneas, casi nunca declaran ese número.

### 1.2.5 Verificar el dato en la edición primaria
Las transliteraciones derivadas, incluidas las excelentes, introducen errores que se propagan.
Caso propio: uno de nuestros apoyos para leer KU-PA como mercancía era una ligadura, \*304+PA-KU-PA, en un nódulo de Hagia Triada. La base de datos paleográfica lee ahí tres signos consecutivos: la ligadura no existe. Sostuvo un argumento durante dos días.
Caso propio 2: la misma fuente transcribe algunos signos de fracción como números enteros, lo que hacía fallar la aritmética de varias tablillas.
Regla: cada dato que sostiene una afirmación se comprueba en la edición o en la base paleográfica, y se declara qué versión se ha usado.

### 1.2.6 Publicar los negativos con su número
Un negativo sin número no es información: "no encontramos coexclusión" puede significar que no la hay o que el corpus es pequeño. Con número, el negativo es una medida de potencia y ahorra el trabajo a los siguientes.
Nuestro uso: no hay coexclusión medible entre palabras del Lineal A (cero pares con esperado mayor que uno en 224 documentos), y sí la hay en el proto-elamita con 830 tablillas (13 pares); un descriptor de red no tiene fiabilidad test-retest a estos tamaños; la comparación por sonido no discrimina entre lenguas candidatas (todas entre 1,3 y 1,7 sobre su propio nulo) ni en el Lineal A ni en el Lineal B, donde la misma regla produce 383 falsos.

### 1.2.7 Explicar la terminación, o declararla sin explicar

Cuando una propuesta identifica un grupo de signos con una palabra conocida de otra lengua, la comparación suele apoyarse en la raíz y dejar el final sin tratar. Ese es el punto por donde se cuela la mayor parte de los falsos positivos, porque una raíz de dos o tres sílabas coincide con facilidad y una terminación no explicada puede estar ocultando morfología, una partícula o un límite de palabra mal situado.

El requisito es barato: **decir qué se propone que sea la terminación, o declarar expresamente que no se explica**. No exige acertar; exige no callar.

Un caso propio lo ilustra, y por eso se incluye aquí. En el trabajo compañero sobre nombres formados sobre nombres de planta (Acedo 2026a) se propuso KU-MI-NA-QE como formado sobre el comino (micénico ku-mi-no, griego κύμινον, préstamo semítico), sobre la base de la raíz compartida y de su distribución en un rodel sellado, donde el grupo de signos es la parte y el logograma la mercancía. La vocal -a frente al micénico -o no es objeción, porque responde a la regla de correspondencia medida sobre 46 pares (la vocal final minoica pasa a -o en griego y la -a nunca se conserva). **Pero la terminación -QE quedó sin tratar**, y una consulta a J. M. Jiménez Delgado (Universidad de Sevilla) la señaló como el problema del caso.

Comprobada en el corpus, la objeción se sostiene. Hay siete grupos de signos terminados en -qe sobre 782 tipos (0,9%), y solo dos tienen su raíz atestiguada por separado; frente al nulo de sílabas barajadas conservando longitudes, dos pares dan p = 0,086, de modo que -qe no se sostiene como sufijo productivo, a diferencia de -ja, que sí lo hace con siete pares. Y KA-PA-QE es revelador: su raíz KA-PA es un topónimo cretense (Uchitel 2002-2003) que encabeza seis tablillas de Hagia Triada, de modo que KA-PA-QE se lee con naturalidad como "y KA-PA". En micénico, -qe es el enclítico copulativo. Si el minoico tuviera un enclítico comparable, KU-MI-NA-QE no sería un nombre sino la palabra ku-mi-na con una partícula pegada, y sus dos contextos lo permiten.

El caso no queda refutado, queda **abierto**: cumple dos de las tres condiciones y la tercera está en discusión. Escribirlo así es lo que este requisito pide, y es lo que la propuesta original no hacía. El caso tiene además un interlocutor reciente. Davis (2025), en su balance de los avances lingüísticos en el estudio del Lineal A, recuerda que Duhoux estableció que un afijo resulta creíble cuando las palabras que lo muestran comparten cuatro o más silabogramas consecutivos, y advierte que no todos los ejemplos que él mismo reúne cumplen ese criterio. Es un requisito del mismo tipo que los de esta nota: no exige acertar, exige declarar en qué condiciones la propuesta se sostiene.

### 1.2.8 Antes de interpretar una ausencia, comprobar que el instrumento podía haberla visto

Un cero es la observación más tentadora de un corpus pequeño y la más fácil de leer mal. Cuando algo no aparece, hay dos explicaciones posibles y sólo una es interesante: que no esté porque el objeto no lo tenía, o que no esté porque el instrumento no podía verlo. El requisito consiste en descartar la segunda antes de afirmar la primera.

Dos ejemplos propios lo ilustran, y los dos se detectaron al aplicar este requisito de forma retroactiva.

**Primero.** Se afirmó que ningún grupo de signos del Lineal A termina en -so, y se contrastó con el hecho de que los topónimos cretenses terminan en -so en griego (Cnosos, Tilisos, Amnisos). Medida la distribución completa de sílabas, resulta que **la sílaba so no aparece nunca en el corpus, en ninguna posición**, y con ella otras siete de la columna en -o (do, jo, mo, no, qo, wo, zo). La ausencia al final de palabra no era un rasgo fonotáctico del minoico: era una laguna del silabario transliterado. La afirmación se retiró y se sustituyó por la comparación de cada sílaba con su propia frecuencia general, que sí mide una preferencia posicional y no depende de qué signos tengan valor asignado.

**Segundo.** Al aplicar por campos semánticos el criterio funcional de un trabajo compañero (Acedo 2026a), los nombres formados sobre nombres de animal dieron cero coincidencias frente a nueve del campo vegetal. La lectura inmediata era que la onomástica minoica no formaba nombres sobre animales, lo que sería un rasgo cultural con contenido. Pero la búsqueda se hace necesariamente con raíces micénicas, y en Creta el ganado se escribe siempre con logograma y nunca con sílabas: no existen las palabras minoicas de los animales con que buscar. El cero medía la ausencia de vocabulario disponible, no la ausencia de la pauta.

**La comprobación es barata en los dos casos y consiste en la misma pregunta**: ¿qué tendría que haber en el corpus para que el instrumento pudiera detectar lo que digo que falta? Si esa condición previa no se cumple, la ausencia no es un dato sobre la lengua.

El requisito se enuncia, por tanto, así: **toda afirmación de la forma "X no aparece" debe ir acompañada de la comprobación de que X podría haber aparecido**, es decir, de que el signo, la palabra o la categoría estaban disponibles para el instrumento en el material y en la transliteración empleados. Cuando esa comprobación no se puede hacer, la ausencia se informa como propiedad del corpus disponible y no de la lengua.

## 1.3. Lo que el protocolo no exige

No exige métodos computacionales: una propuesta hecha a mano puede cumplir los ocho requisitos, y muchas propuestas computacionales no cumplen ninguno. No exige renunciar a la intuición, que es el origen de casi todas las lecturas buenas; exige separar el momento de la intuición del momento de la comprobación. Y no exige que una propuesta sea correcta para ser publicable: exige que sea evaluable.

## 1.3 bis. El protocolo aplicado a dos propuestas ajenas, y calibrado en una lengua con anclaje

El protocolo se ha aplicado a dos propuestas de lectura del Lineal A que no son nuestras, sin nombrar a sus autores, porque lo que importa es el patrón y no la firma.

La primera es un texto de desciframiento con siete afirmaciones. Una cumple parcialmente los requisitos; dos son medibles y caen al medirse: la ley de potencias que se ofrece como prueba de "lenguaje natural" la cumple mejor el corpus barajado (R² 0,95) que el real (0,81), y los cortes de palabra que se dan por acertados aciertan un 88,5% sobre una tasa base del 86,5%. Las otras cuatro no declaran nulo ni pueden tenerlo.

La segunda es un repositorio público generado con un modelo de lenguaje que declara el Lineal A "resuelto en cinco minutos" con un 92% de confianza. Contrastado con el corpus: da 1.450 inscripciones con Cnosos 450 y Hagia Triada 300 (el corpus tiene 1.720, con Cnosos 59 y Hagia Triada 1.108); lee "YA-NE" como vino con confianza 0,90, y la unidad no existe; propone "fórmulas" (aceite + 10 + destinatario) que aparecen cuatro veces en 89; y asigna a sílabas sueltas significados como "invocación divina". Lo único correcto (KU-RO total, PA-I-TO Festos, VIN vino) es lo que ya estaba publicado. Es el caso extremo de una propuesta que no declara nada verificable, y muestra por qué dos de los ocho requisitos, verificar el dato en la edición y contar las pruebas, tienen que ir antes que cualquier nulo: un nulo sobre una unidad que no existe es un cálculo sin objeto.

El mismo procedimiento, aplicado a una lengua que sí tiene anclaje, sirve de calibración. El ibérico se lee y no se entiende, y dispone de una bilingüe parcial, los nombres latinizados de la Turma Salluitana en el bronce de Ascoli. Sus elementos, escritos en la ortografía ibérica (que no distingue sordas y sonoras: Adingibas es atin-kibas), aparecen en el corpus de Hesperia por encima de un nulo de cadenas de igual longitud en 8 de 23 casos (1,2 esperados), cinco tras corrección; los treinta formantes onomásticos de Untermann, en 15 de 24 probados. Con la ortografía latina, sin la correspondencia, 1 de 16. El mismo instrumento aplicado a la única fuente casi bilingüe del minoico, los seis topónimos cretenses de las listas egipcias, no ancla nada (1 de 9, y ese es artefacto de un esqueleto frecuente). La diferencia entre las dos lenguas es de dato, no de método: dos docenas de nombres frente a seis, y el instrumento lo dice con una p en cada caso. Es lo que el protocolo pide de cualquier propuesta: que diga cuánto anclaje tiene, medido, antes de decir qué lee.

## 1.4. Por qué ahora

Tres razones. El volumen de propuestas ha crecido con la disponibilidad de herramientas y de premios. Los corpus están digitalizados, de modo que los ocho requisitos son hoy baratos: un nulo son diez líneas de código. Y el campo ha producido, en los últimos años, ejemplos de cómo se hace bien: la puesta a prueba con nulos de la división tripartita del chiprominoico, la validación de Ithaca con un experimento entre historiadores, y las advertencias explícitas sobre el poder discriminante de las coincidencias en corpus pequeños. Este texto solo ordena lo que esos trabajos ya practican.



# Parte 2. El procedimiento

## 2.2. Datos y procedimiento

### 2.2.1 Corpus

Transliteraciones de GORILA (Godart y Olivier 1976-1985) en la forma legible por máquina del LinearA Explorer (Hogan 2022), que conserva subíndices, sitio, soporte, contexto arqueológico, las atribuciones de mano de GORILA V y los comentarios de Younger (2024b) con los datos de sello. Verificación de signos en el conjunto de datos de SigLA (Salgarella y Castellan 2020). Para el Lineal B, la edición del mismo autor sobre las ediciones estándar (5.889 documentos, 5.597 grupos de signos), con las manos de Cnosos de Olivier. Para el etrusco, el corpus de Larth (Vico) con 7.139 registros y el corpus ETP (429 textos con metadatos). Un defecto conocido de los datos del Explorer, la etiqueta de soporte de las tablillas de Zakros, se corrigió desde SigLA; una ligadura de su transliteración (\*304+PA-KU-PA en HT Wa 1020) resultó ser dos signos consecutivos según SigLA, y se registra aquí como advertencia sobre las transliteraciones derivadas.

### 2.2.2 Unidades y medidas

Las unidades son los grupos de signos (799 tipos, 1.117 tokens en tablillas con dos o más grupos; 76% de hapax), los documentos como conjuntos de grupos, y los perfiles de sílabas iniciales y de esqueletos consonánticos. Las medidas son las habituales: distancia de Jensen-Shannon entre perfiles (ecuación 1), índice de Jaccard entre documentos (ecuación 2), correlación de Mantel entre matrices de distancia (ecuación 3), información mutua entre posiciones (ecuación 4), y el algoritmo curveball para nulos de márgenes fijos en matrices de presencia (ecuación 5, Strona et al. 2014). Cada una se enuncia en el apéndice con su fuente.

### 2.2.3 Nulos

Cada afirmación lleva el nulo que conserva lo que la afirmación no pretende explicar: para la coocurrencia entre documentos, permutaciones que conservan el número de grupos por documento y el número de documentos por grupo (curveball); para la morfología, permutación de la sílaba afijada entre todas las palabras conservando sus longitudes; para las clases por posición, permutación de etiquetas; para los confusores, permutación dentro de estrato (etiqueta de tipo dentro de mano, o de mano dentro de tipo). El umbral se fijó en p < 0,01 con mil permutaciones para afirmaciones nuevas y p < 0,05 para réplicas; las comparaciones múltiples se corrigen por Bonferroni cuando son menos de diez y por Benjamini-Hochberg cuando son más.

### 2.2.4 Potencia

Antes de cada test se estimó el efecto mínimo detectable con el n disponible. Dos cifras gobiernan el resto: el suelo de distancia entre dos muestras del mismo corpus a 42 tipos es 0,198 (Jensen-Shannon sobre esqueletos consonánticos), de modo que ninguna diferencia menor es detectable a ese tamaño; y en el etrusco, el test de sibilantes tiene 68 pares utilizables, que es el orden de magnitud de los tests posicionales del Lineal A. Un test cuyo efecto esperado cae bajo el suelo se declara indecidible y no se corre.

## 2.3. Calibración en etrusco

El etrusco es el control adecuado: alfabeto leído, lengua no indoeuropea entendida a medias, corpus del tamaño del Lineal A y con metadatos de ciudad y de época, y tres hechos gramaticales o sociolingüísticos establecidos que el procedimiento debe recuperar sin que se le digan.

Genitivo ante los términos de filiación. Ante la palabra clan, "hijo", el nombre del padre va en genitivo. Medido sobre el corpus completo de OpenEtruscan (5.941 textos distintos, 5.470 de ellos en calidad limpia), el test posicional aplicado a ciegas encuentra la terminación -l en 11 de las 18 palabras que preceden a clan (61%) frente a 1,4 esperadas por la frecuencia general de esa terminación en el vocabulario, y en 5 de las 13 que preceden a sec, "hija" (38%, esperadas 1,0). Los dos superan el nulo de muestreo del vocabulario (p < 0,0005 y p = 0,0035).

Y lo hace con la especificidad correcta, que es lo que distingue un instrumento de un generador de ruido: ante puia, "esposa", y ante lupu, "murió", que no rigen genitivo, la terminación aparece en 1 de 12 y 1 de 9 casos, dentro de lo esperable (p = 0,63 y p = 0,50). El instrumento ve flexión donde la hay y no la ve donde no la hay.

Síncopa como cambio en el tiempo. La pérdida de vocales interiores se fecha hacia el 500 a.C. El índice de síncopa es 0,28 más alto en los textos tardíos que en los tempranos, y el efecto se mantiene al controlar la ciudad (p < 0,002 dentro de ciudad). El instrumento ve tiempo donde lo hay.

Sibilantes como variación geográfica. La distinción gráfica de sibilantes es un rasgo del norte. La razón norte/sur es 0,6 frente a 0,1 (p = 0,72 dentro de ciudad): el efecto es de ciudad, no de época. El instrumento no confunde geografía con tiempo cuando los metadatos permiten separarlas.

La calibración fija lo que se puede esperar del mismo aparato en el Lineal A: recuperará morfología y estratificación si existen y si hay metadatos para separar los confusores; donde no los haya, dirá "indecidible", y esa respuesta hay que aceptarla.



## 2.4. Negativos de método

Se informan porque cierran vías que otros volverían a abrir.

Un descriptor estructural por nodo (Omega-N, con el código público de BiomeMakers/OmegaN) aplicado a la alineación de signos A y B por su papel en el grafo de coocurrencia recupera el rango medio 27,4 frente a 32,5 del azar (p = 0,018), exactamente lo que recupera el grado por sí solo (26,8): lo que se transfiere entre escrituras es la cuota de grado, y el rol estructural codifica la lengua, no el signo. Dentro del A, el descriptor no tiene fiabilidad test-retest a estos tamaños (exceso triádico entre dos mitades de Hagia Triada +0,06 y +0,02), por lo que cualquier test de estructura fina es indecidible; se propone una condición de tamaño mínimo para el cribado del método.

Un clasificador de función (49 etiquetas, 25 rasgos de posición y compañía) acierta 0,67 a 0,73 escondiendo una etiqueta cada vez, frente a 0,39 a 0,48 con etiquetas barajadas: distingue la fórmula de libación, y las cabeceras de las entradas, pero clasifica como nombre las dos mercancías conocidas, porque de mercancías hay dos ejemplos. La estructura predice función gruesa, no clase semántica.

Un modelo neuronal de desciframiento con y sin el regularizador Omega-S sobre las veinticinco palabras conocidas queda preregistrado con predicción de cero en ambos brazos; no se ha corrido.

La coexclusión entre palabras no tiene potencia a este tamaño (sección 4.5), y la "receta" de aromáticos (proporciones iguales entre ingredientes) es indecidible con las cantidades legibles (0,26 de pares iguales frente a 0,21 del nulo de fracciones, p = 0,24).

Tres pruebas tomadas de la ecología de redes se declaran no concluyentes o retiradas. La curvatura de Forman sobre el grafo de coocurrencia, con la predicción de que los términos de transacción ocupan los puentes, no separa a esos términos del resto en Susa (p = 0,50) y en Hagia Triada apunta en la dirección predicha sin alcanzar significación (p = 0,12), probablemente porque la curvatura de Forman está dominada por el grado; la prueba requiere la curvatura de Ollivier-Ricci y queda pendiente. El gradiente de "energía" (documentos ordenados por volumen de mercancía) no altera la diversidad del vocabulario en Susa (tasa de hapax 0,40, 0,40, 0,36, 0,42 por cuartiles; p = 0,47), de modo que la analogía con el gradiente de energía externa de los suelos no se traslada. Y la razón ascendencia/capacidad de Ulanowicz, que en una primera pasada situaba a Hagia Triada y a Susa en la ventana de vitalidad (a = 0,41 y 0,39, con F máximo en a = 1/e), es reproducida exactamente por un nulo que conserva las sumas de filas y columnas de la matriz documentos × palabras (0,411 y 0,430 en el nulo), y Uruk y el ibérico ni siquiera caen en la ventana: el índice mide las distribuciones marginales y no la estructura, y el resultado se retira. La lección es general y vale para cualquier índice calculado sobre una matriz de recuentos, dentro y fuera de la epigrafía: si el nulo de márgenes fijos lo reproduce, el índice mide los márgenes.

La ligadura \*304+PA-KU-PA del LinearA Explorer no existe: SigLA lee \*629 seguido de KU-PA. Se informa porque sostuvo durante dos días un argumento de una lectura, y porque las transliteraciones derivadas requieren verificación signo a signo antes de usarse como dato.

Una tercera fuente de error del mismo tipo apareció al examinar las palabras que aparecen a la vez en documentos administrativos y en inscripciones sobre piedra: de las dieciocho que comparten los dos vocabularios, dos (JA-SA e I-TI) resultaron ser el ancla JA-SA-SA-RA-ME partida por un salto de línea que la transliteración convierte en dos entradas. Es el tercer caso de artefacto de la fuente derivada en este trabajo, junto a la ligadura inexistente y a las fracciones transcritas como enteros.

Y una cuarta observación afecta a la clasificación del corpus. Reclasificados los 1.719 documentos por su contenido (presencia de anclas de la fórmula; presencia de cantidades y logogramas de mercancía) en lugar de por el material del soporte, la etiqueta de soporte predice bien el contenido salvo en un caso: de los vasos de piedra, 33 son documentos contables y solo 15 llevan fórmula votiva, y los 33 se concentran casi por completo en Zakros, con hasta doce cantidades en una sola pieza (ZA 10b). El corpus votivo real del Lineal A son diecisiete documentos y no los ciento siete que el soporte sugiere, lo que reduce la potencia de cualquier análisis del vocabulario de culto y explica por qué varias de las pruebas de la sección 4.7 resultan indecidibles. La separación entre administración y culto debe hacerse por contenido; la clasificación de los 1.719 documentos acompaña a este trabajo. La comprobación completa, con las veintitrés series medidas una a una, se presenta aparte (Acedo 2026h); baste aquí con que diecisiete de ellas tienen cohesión de logogramas al menos doble que su entorno, y que las seis restantes no contradicen la clasificación: cuatro pertenecen a la clase que Montecchi define por la AUSENCIA de ideograma, de modo que un índice sobre logogramas no puede verlas; dos son fragmentos sin apenas texto; y la sexta, la serie Ec, no comparte logogramas pero sí el 54,5% de su vocabulario, la cifra más alta del corpus, lo que indica que HT 86 y HT 95 son dos versiones del mismo documento. Merece la pena señalar la dirección del resultado: el mismo tipo de prueba aplicado por Corazza y sus coautores (2022) a la división tripartita del chiprominoico obligó a revisarla, y aquí confirma la clasificación existente. Un procedimiento que solo produjera refutaciones sería sospechoso; que confirme unas clasificaciones y refute otras es lo propio de un instrumento cuyo resultado depende del objeto y no del instrumento.


## 2.5. Un caso: cómo el procedimiento produjo, y después corrigió, una lectura

El procedimiento se ilustra mejor con el caso en que falló a medias. Buscando los grupos de signos que se comportan como cosas contadas (recurrencia dentro de documento con cantidades distintas, cantidades enteras, ausencia en listas de personal), el cribado aisló KU-PA (AB 81-03): repetido en las dos caras de ZA 11 con 1 y 3, en KH 29 con 2, en HT 110a con 1; con una familia de derivados (KA-KU-PA, KU-PA-ZU, KU-PA-JA, KU-PA-RI) que aparecen junto al logograma \*303 en dos rodeles y en KH 5; y con dos afijos que recurren en el corpus por encima del nulo. Solo entonces se comparó la forma: griego κύπαιρος, pregriego según Frisk y Beekes, micénico ku-pa-ro, que glosa el logograma de la juncia en KN Ga 517. La primera versión leyó la familia como la palabra minoica de la juncia, contra la lectura de Younger, que la tenía por nombre de un contribuyente.

Tres comprobaciones posteriores, todas del mismo procedimiento, cambiaron la lectura sin tocar la etimología. La verificación signo a signo en SigLA mostró que la "ligadura" \*304+PA-KU-PA del nódulo HT Wa 1020, uno de los apoyos, era una secuencia de tres signos sin ligadura. La tabulación de los sellos de todos los rodeles de Hagia Triada (comentarios de Younger, SigLA) mostró dos grupos de sellado: uno en que la palabra va sola, y otro en que la palabra va seguida de un logograma de mercancía, y en ese segundo grupo están KA-KU-PA con \*303 pero también A-RA-TU-ME con ovejas y KU-MI-NA-QE con cabras, palabras que no pueden ser mercancías. Y la estructura de KH 5 (grupo, logograma, cantidad, con WI-SA-SA-NE ante \*626 y KU-PA-ZU ante \*303) resultó ser la de partes ante mercancías. La lectura corregida es la que concilia: la raíz KU-PA es la palabra de la planta; la familia de los archivos es un nombre formado sobre ella, como Kyparissos o Maratón en griego; y dos casos más del mismo tipo (KU-MI-NA-QE y el comino; KI-KI-RA-JA sobre el KI-KI-NA que Neumann identificó con el higo de sicomoro en 1960) sostienen la pauta.

Lo que el caso enseña sobre el método es lo que importa aquí. Primero, que el orden función-forma no protege por sí solo de un error de función: la recurrencia con cantidades, tomada como firma de mercancía, era compatible con una parte a la que se asigna dos veces, y solo un dato externo a la tablilla (los sellos) lo decidió. Segundo, que cada apoyo debe verificarse en la fuente primaria y no en una transliteración derivada, por buena que sea. Tercero, que la corrección no destruyó el resultado sino que lo situó: la etimología, que era lo único que no dependía de la función, sobrevivió intacta, y la pauta de nombres formados sobre plantas es más defendible y más general que la lectura inicial. El artículo que presenta el caso (Acedo 2026, en evaluación) lleva dentro esa historia porque la historia es parte de la evidencia.



# Parte 3. Las calibraciones

## 3.2.1 Estado de la cuestión

La lectura del etrusco es completa y su comprensión, parcial: el vocabulario con significado establecido ronda las mil entradas (Bonfante y Bonfante 2002; Wallace 2008; ETP), y de los textos, la inmensa mayoría son inscripciones funerarias breves cuyo contenido es onomástico. Los textos largos (Liber Linteus, Tabula Capuana, Tabula Cortonensis, Cippus Perusinus) contienen el vocabulario no onomástico que el campo discute, y es allí donde los editores marcan sus dudas. La pregunta que aquí se plantea no es qué significan esas palabras, sino qué clase de palabra son, que es una cuestión decidible por distribución.

## 3.2.2 Datos y método

Corpus Larth (Vico 2023): 7.139 registros con ciudad, fecha y traducción cuando la hay, del que se apartan 26 textos umbros (Tablas Iguvinas) detectados por vocabulario; léxico ETP_POS (Wallace y colaboradores) con 1.122 entradas y categoría gramatical. Normalización ortográfica (th → θ, ch → χ, ph → φ, ś → σ, c y q → k), que sube de 316 a 349 las palabras conocidas presentes en los textos. Etiquetas: nombre propio, sustantivo o adjetivo, verbo, partícula. Rasgos: posición inicial y final en la inscripción, inscripción de una sola palabra, vecinos por clase conocida, sufijos (-s, -l, -si, -ke, -χe, -θ, -al, -as, -ia, -u), frecuencia, dispersión por ciudad, y posición contigua a un praenomen conocido. Validación cruzada de cinco pliegues y nulo de etiquetas barajadas.

## 3.2.3 Resultados

### 3.2.3.1 El clasificador aprende la función
Acierto 0,70 (0,26 con etiquetas barajadas); recall por clase 0,78 (nombre), 0,54 (sustantivo), 0,67 (verbo), 0,83 (partícula). Los rasgos de mayor peso son la posición en la fórmula onomástica y los sufijos verbales en -ke/-χe.

### 3.2.3.2 Validación involuntaria sobre palabras conocidas
El fichero de trabajo omite palabras corrientes, de modo que aparecen como "desconocidas" términos cuyo significado el campo sí tiene. El clasificador, sin saberlo, acierta en ocho de diez comprobables: teke (verbo, 0,98), larke y fulnike (verbos, pasados en -ke), ein (partícula, 0,75), θui (partícula), suθi y zilaθ (sustantivos), mlaχ (sustantivo o adjetivo); falla en mulu "dio" y lupu "murió", participios en -u, cuyo sufijo no figuraba entre los rasgos. Esa es la corrección más inmediata del modelo.

### 3.2.3.3 Los candidatos
De 154 palabras desconocidas para el campo con frecuencia ≥ 3, nueve no son nombres. Tres merecen examen: θapikun (Populonia, Po 4.4), en posición de predicado tras la partícula relativa inpa y con un derivado en la misma inscripción, θapintaś, lo que satisface dos de las tres condiciones del procedimiento; fanu (Cippus Perusinus), entre la partícula eθ "así" y el sujeto lautn "familia", con la comparación clásica con el latín fanum "santuario" pero sin derivado y sin bilingüe que la contraste, una condición y media; y aknanasa, que el examen retira: es el participio acnanasa "habiendo engendrado" de la inscripción de los Alethnas, con traducción en el propio corpus, y su clasificación como sustantivo es un error del modelo por el mismo motivo que mulu y lupu.

### 3.2.3.4 Dónde están las dudas de los editores
El minado de las traducciones localiza las dudas de contenido en los textos largos: θelu y parχ (Alethnas), munis (dedicatoria a Hercle), θlu, θup y sela (Volterra), iluku y cuieskhu (Tabula Capuana). Cada una tiene entre una y tres atestaciones en el corpus disponible, insuficientes para el procedimiento; son el objetivo natural cuando se disponga de la edición completa.

## 3.2.4 Discusión y límites

El resultado es de método: en un corpus con vocabulario glosado suficiente, la función de una palabra no glosada es predecible por distribución con acierto medible, y el propio modelo señala qué rasgo morfológico le falta cuando falla. El límite es de datos: el corpus abierto es ruidoso (OCR, umbro, glosas de nombres en lugar de traducciones) y la edición de referencia no está disponible en forma tabulada. Con ella, el mismo procedimiento se aplicaría a las dudas de los editores en los textos largos, que es donde el vocabulario no onomástico del etrusco espera.



## 3.3.1 Estado de la cuestión

El semisilabario ibérico se lee desde Gómez-Moreno, y la lengua sigue sin entenderse. Lo que sí está establecido es un conjunto de regularidades: un repertorio de formantes que se combinan de dos en dos para formar antropónimos (Untermann 1990), un puñado de sufijos recurrentes (-en, -ar, -ka, -te), un sistema numeral reconocido por comparación con el vasco (Orduña 2005; Ferrer i Jané 2009), y diferencias gráficas entre el ibérico nororiental, el levantino y el meridional que Hesperia recoge en sus mapas de isoglosas. Estas regularidades se han obtenido por inspección de un corpus grande y por comparación interna, no por contraste con modelos nulos, de modo que no se conoce su tamaño de efecto ni la probabilidad de obtenerlas por azar.

## 3.3.2 Datos y método

Corpus: 2.094 textos ibéricos derivados del Banco de Datos Hesperia (UCM) en la versión publicada por Luo et al. (2021), con la referencia Hesperia de cada texto, que contiene el código de provincia. De ellos, 1.919 tienen texto utilizable tras apartar los fragmentos y los signos de lectura dudosa: 2.677 palabras, 2.359 tipos. Zonas: nororiental (Cataluña, Aragón, Castellón, sur de Francia), 1.644 textos; levantino-meridional (Valencia, Alicante, Albacete, Murcia, Andalucía), 269. Faltan la cronología y el soporte, que están en Hesperia y no en esta copia; su ausencia impide separar el registro y la época, y así se declara.

Método: el de Acedo (2026c). Para los formantes, nulo de letras barajadas entre palabras conservando longitudes; para las terminaciones por zona, test exacto de Fisher con corrección de Bonferroni sobre las sesenta terminaciones probadas (umbral p < 8·10⁻⁴).

## 3.3.3 Resultados

### 3.3.3.1 Los formantes de Untermann son el repertorio que el nulo señala
Los treinta formantes buscados como subcadenas aparecen 295 veces; el nulo da 11,1 de media (máximo 20 en 100 permutaciones). Los más frecuentes son taŕ (62), biuŕ (37), atin (33), iltiŕ (31), śalir (26), bilos y beleś (24 cada uno), unin (15), aŕbi (13), baise (12). El resultado no es trivial: dice que las secuencias que Untermann aisló no son arbitrarias respecto a la fonotaxis del corpus.

### 3.3.3.2 Dos isoglosas se separan con nulo, una tercera es un artefacto
Con las terminaciones de dos y tres signos, y sobre 2.090 palabras del norte y 574 del sur: -kí (el signo S56 en posición final) 28,6‰ en el sur frente a 1,2‰ en el norte (p = 3·10⁻⁸), y 30,9‰ frente a 0 en las de tres signos (p = 3·10⁻⁹); -ḿi 40,5‰ en el norte frente a 7,6‰ en el sur (p = 3·10⁻⁵). Ambas son las isoglosas que Hesperia describe en su mapa 2. La tercera diferencia detectada, la terminación -n (21‰ sur frente a 2,3‰ norte), corresponde a una convención de transcripción del separador y no a un hecho de la lengua; se informa para que no se cuente como resultado.

### 3.3.3.3 Lo que no puede hacerse todavía
Sin cronología no puede separarse el cambio en el tiempo del cambio en el espacio, que es precisamente el confusor que la calibración etrusca del procedimiento sabe separar cuando hay fechas. Sin soporte no puede compararse el registro de los plomos con el de la cerámica y el de las monedas. Los dos análisis están preparados y se aplicarán cuando el Banco de Datos facilite esos campos.



### 3.3.4 Discusión de la calibración ibérica

Lo que este trabajo añade no es un hallazgo sino una medida: el repertorio onomástico y las dos isoglosas principales del ibérico tienen ahora tamaño de efecto y probabilidad bajo un nulo explícito. Eso importa por dos razones. Primera, porque el ibérico es el corpus paleohispánico con más textos y mejores metadatos, y cualquier afirmación futura sobre su morfología debería medirse igual. Segunda, porque el mismo procedimiento, aplicado a corpus mucho menores (Lineal A, proto-elamita), declara sin potencia lo que aquí sí se mide: la comparación entre corpus fija el tamaño a partir del cual cada instrumento empieza a ver.



### 3.3.5 El anclaje bilingüe, medido: el bronce de Ascoli

Los nombres latinizados de la Turma Salluitana (bronce de Ascoli, 89 a. C.) son la única bilingüe real de una lengua paleohispánica. La prueba: para cada elemento onomástico, cuántas formas del corpus de Hesperia (2.906 íntegras) lo contienen, contra 1.000 cadenas de la misma longitud generadas por el modelo de bigramas de letras del propio corpus. En ortografía latina (adin, gibas, bilus, balci, urgi) supera el nulo 1 de 16: la escritura ibérica no distingue sordas de sonoras, y Adingibas se escribe atin-kibas. En ortografía ibérica, con la correspondencia establecida del campo, 8 de 23 superan el nulo (1,2 esperados; p binomial 10⁻⁵) y cinco sobreviven a Bonferroni: bilos, sosin, biuŕ, balke, tautin. De la lista de formantes de Untermann, 15 de 24. El sistema onomástico que la bilingüe deja ver está en el corpus, con una p por elemento, y coincide con lo que Untermann aisló a mano.

### 3.3.6 El perfil de terminaciones, con la unidad declarada

Raíces atestiguadas desnudas y con una terminación compartida por tres o más raíces, contra un nulo que baraja las terminaciones entre formas. Por letra, el ibérico da 46 terminaciones contra 10 esperadas (4,5 veces), y las más compartidas son las que el campo lee: -te, -ka/-ke, -ḿi, -ar, -en. Con unidad semisilábica (oclusiva + vocal como una unidad), 24 contra 17 (1,4 veces). El Lineal A por sílaba, todas las unidades, 14 contra 6 (2,3 veces); solo las íntegras, 3 contra 1 (-JA, -ME, -TI). Dos lecciones: la razón depende de la unidad, y hay que declararla; y parte de las alternancias publicadas del Lineal A descansa en unidades rotas.

### 3.3.7 Cuatro afirmaciones del campo ibérico contra nulo

Los numerales vascoides (Orduña 2005; Ferrer 2009: ban, bin, irur, laur, borste, śei, sisbi, sorse, abaŕ, oŕkei) deberían componerse entre sí como en vasco: formas con dos numerales distintos, 7 observadas contra 0,7 esperadas con diez formas al azar de las mismas longitudes (p=0,014; oŕkei-irur, oŕkei-abaŕ-ban, oŕkei-ke-laur). Śalir como plata (Orduña): con marcas metrológicas en 7 de 13 inscripciones contra 28% de base (p=0,046). Ekiar como firma de artesano tras un nombre: 1 de 8 como token aparte y 1 de 13 dentro de la misma forma; no se sostiene con este corpus. La fórmula funeraria aŕe take: dos inscripciones, sin nulo posible. La proporción (una resiste, dos al borde, una cae) es la misma que da el procedimiento sobre las lecturas de Younger en el Lineal A.

## 3.4. Chiprominoico: unidades léxicas recurrentes en 183 secuencias

Del conjunto de datos publicado por Corazza, Tamburini, Valério y Ferrara (2022; repositorio sign2vec_d) se reconstruyen 183 inscripciones con su secuencia de signos, sitio y soporte: 1.386 signos, 155 tipos. Contra un nulo de unigramas (mismos signos, orden barajado), las secuencias repetidas están muy por encima del azar: 2-gramas 83 contra 43,9; 3-gramas 19 contra 0,9; 4-gramas 6 contra 0. El corpus tiene unidades léxicas recurrentes, que es la condición mínima para que cualquier método de emparejamiento tenga con qué trabajar. El contraste entre tablillas y otros soportes no tiene potencia (6 tablillas, todas de Ugarit). Es la calibración más cercana al Lineal A en tamaño, escritura y época, y la que más se parece a él en lo que no puede hacer.

## 3.5.1 Por qué comparar tres archivos que no se leen

Los tres corpus comparten la condición que los hace difíciles y la que los hace comparables. Ninguno tiene bilingüe: el Lineal A no se lee; el proto-elamita no se lee y su lengua es desconocida; el proto-cuneiforme se lee a medias, por la continuidad de sus logogramas y sus numerales en el cuneiforme sumerio (Nissen, Damerow y Englund 1993; Englund 1998). Los tres son, en cambio, archivos contables de palacio o de institución, con el mismo tipo de documento: la tablilla que registra entradas de una cantidad de algo asociada a alguien, con cabecera y a veces con total. La bibliografía de cada uno ha descrito esa anatomía por separado (Schoep 2002 y Montecchi 2010 para Hagia Triada; Dahl 2005, 2019 y Damerow y Englund 1989 para Susa; Englund 1998 para Uruk), pero no se ha medido con el mismo instrumento en los tres, y por tanto no se sabe qué rasgos son de la contabilidad temprana en general y cuáles de cada tradición.

La comparación tiene además un valor de método. El aparato usado aquí (Acedo 2026c) produce en el Lineal A una serie de resultados negativos que se atribuyeron al tamaño del corpus: sin coexclusión medible, sin fiabilidad de los descriptores de red, sin potencia para separar tipos de documento. Aplicado a corpus hermanos cinco y veinte veces mayores, permite decir para cada instrumento a qué tamaño empieza a ver, y por tanto convertir esos negativos en una curva de potencia.

## 3.5.1 bis. Los tres archivos

Hagia Triada, hacia 1450 a.C. Villa de la llanura de la Mesará, en la Creta neopalacial; su archivo, unas 150 tablillas y 150 nódulos y rodeles, se conserva porque el edificio ardió en las destrucciones del Minoico Reciente IB, y registra el último año de una administración que asignaba grano, aceite, vino, higos, ganado y aromáticos, con veintiún escribas trabajando a la vez (Schoep 2002; Montecchi 2010). No hay estratificación temporal: es una foto fija.

Susa, hacia 3100-2900 a.C. Capital de la llanura de Juzestán, en contacto con Uruk y a la vez independiente de ella; sus 1.500 tablillas proto-elamitas son cuentas de grano, ganado, personal y productos derivados, con sistemas numerales propios y una cabecera institucional recurrente, y son casi todo lo que se conserva de esa administración; la periferia (Malyan, Tepe Yahya, Sialk, Sofalin) aporta unas cincuenta más (Damerow y Englund 1989; Dahl 2005, 2019).

Uruk IV-III, hacia 3350-3000 a.C. La primera administración escrita conocida, en la Baja Mesopotamia; unas 5.000 tablillas de la ciudad y sus alrededores, con los sistemas numerales de los que derivan los de Susa, y con un repertorio de logogramas cuyo significado se conoce en parte por su continuidad en el cuneiforme sumerio (Nissen, Damerow y Englund 1993; Englund 1998). Es el único de los tres cuyo contenido se entiende a medias.

## 3.5.2 Datos e instrumentos

Lineal A: GORILA (Godart y Olivier 1976-1985) en la forma del LinearA Explorer (Hogan 2022), con las manos de GORILA V y los comentarios de Younger (2024); verificación en SigLA (Salgarella y Castellan 2020). Proto-elamita y proto-cuneiforme: las transliteraciones y el catálogo de CDLI (exportación de septiembre de 2026), con los sistemas numerales según Damerow y Englund (1989) y Dahl (2019). En los tres, la unidad es la entrada (línea numerada con cadena de signos y cantidad); la cadena de signos del Lineal A es el grupo de signos silábicos, la del proto-elamita y el proto-cuneiforme la secuencia de signos no numerales de la entrada.

Instrumentos, en el mismo orden en los tres corpus: (1) tamaño y tasa de hapax de las cadenas; (2) hapax por longitud de cadena; (3) recurrencia dentro de documento con cantidades distintas por clase de longitud; (4) cabeceras (primera entrada) y totales; (5) monopolios de vocabulario por tipo de documento o por sistema numeral; (6) coocurrencia y coexclusión con nulo curveball (Strona et al. 2014) sobre la matriz documentos × cadenas frecuentes; (7) sistemas numerales por clase de objeto; (8) manos, donde las hay. Los nulos y umbrales son los descritos en Acedo (2026c): permutación con conservación de márgenes o de longitudes, p < 0,01 con mil permutaciones para afirmaciones nuevas.

## 3.5.3 Resultados

### 3.5.3.1 La anatomía es la misma

Los tres archivos escriben la entrada como cadena de signos más cantidad, abren con cabecera (SA-RA₂ y los topónimos en Hagia Triada; M157, el signo de institución, en 278 tablillas de Susa; los signos de institución y de oficio en Uruk) y cierran con total en una parte de las tablillas (KU-RO en Hagia Triada; los totales de Susa y Uruk marcados por posición). La proporción de entradas con cantidad difiere entre los tres (0,60, 0,75 y 0,80; χ² = 121, p < 10⁻²⁶ sobre 8.282 y 23.272 entradas), pero el orden de magnitud es el mismo y la diferencia se explica por la proporción de cabeceras y de líneas rotas en cada corpus; lo comparable es la anatomía, no la tasa.

### 3.5.3.1 bis Tabla comparativa

| instrumento | Hagia Triada (224 doc.) | Susa (1.594 tabl.) | Uruk (6.387 tabl.) |
|---|---|---|---|
| entradas con cantidad | 0,60 | 0,75 | 0,80 |
| hapax de la cadena (1 signo / 3+ signos) | 0,03 / 0,76 | 0,03 / 0,87-0,99 | 0,03 / 0,9 |
| repetición dentro del documento con cantidad distinta (cadenas cortas / largas) | 0,13 / 0,02 | 0,13 / 0,002 | comparable a Susa |
| cabecera institucional | SA-RA₂ (20 doc.), topónimos | M157 (278 tabl.) | signos de institución y oficio |
| total | KU-RO (37), PO-TO-KU-RO, DA-I | por posición | por posición |
| monopolios de vocabulario | 6 (cuentas) + 3 (asignaciones) | 24 (capacidad), 3 (decimal) | pendiente |
| coexclusión con nulo curveball | 0 pares (sin potencia) | 13 pares | pendiente |
| marco de las cadenas largas | KA- 17% en rodeles; -JA 7 pares | M288 final (lift 3,8); M124 inicial | pendiente |
| sistemas numerales por clase | fracciones propias (Corazza et al. 2021) | 4 sistemas, decimal propio | 5 sistemas, origen de los de Susa |
| manos atribuidas | 21 (73 tabl.) | ninguna en el catálogo | ninguna |

### 3.5.3.2 La partición del léxico es la misma, y se ve mejor con más datos

En los tres corpus las cadenas cortas son pocas, frecuentes y repetidas, y las largas son muchas, únicas y no se repiten. En Susa la gradación es limpia: las cadenas de un signo son hapax en el 3% de los casos y se repiten dentro de la tablilla con cantidades distintas en el 13%; las de tres o más signos son hapax en el 87-99% y se repiten en el 0,2%. En Hagia Triada la misma partición existe (los términos de mercancía y transacción se repiten, los nombres son hapax al 76%) pero se ve con menos definición porque la clase corta es en su mayoría logográfica. Uruk se comporta como Susa. La partición entre lo contado y quien lo entrega o recibe es, por tanto, un rasgo de la contabilidad temprana y no de una tradición, y el criterio conductual (repetición con cantidades distintas) la recupera sin lectura en los tres.

### 3.5.3.3 Los compartimentos, y quién los hace

En Hagia Triada, las cuentas con total tienen seis palabras de monopolio y las asignaciones tres (p < 0,01 en ambos casos); en Susa, el sistema de capacidad (grano) tiene 24 cadenas de monopolio, el decimal 3, el sexagesimal ninguna. La coexclusión, que en Hagia Triada no es medible (cero pares con esperado ≥ 1 en 224 documentos), aparece en Susa con 830 tablillas: 13 pares nunca coocurren cuando deberían (la cabecera M157 con M371, M370, M373, M046, M367; el producto de grano M297 con M376, M124, M003, M032, M009), lo que separa las cuentas de grano de las de ganado y personal. Solo Hagia Triada permite el control de mano: con 73 tablillas atribuidas a 21 escribas, el vocabulario compartido lo explica la mano (efecto 0,032, p = 0,002 controlando el tipo) y no el tipo de documento (0,025, p = 0,21): los compartimentos minoicos son, al menos en parte, carteras de escriba. Susa y Uruk no tienen manos atribuidas en el catálogo, y su compartimentación no puede descomponerse así; se declara.

### 3.5.3.4 Las cadenas largas tienen marco

En Susa, las 1.296 cadenas de tres o más signos con cantidad tienen un signo de institución u objeto en posición final por encima del azar (M288 231 veces, lift 3,8, p < 10⁻⁶; también M263, M297, M346) y un signo de clase en posición inicial (M124, M305, M157). Los "nombres" llevan marco: clasificador delante, núcleo variable, institución u objeto detrás. En Hagia Triada el marco existe con menos potencia: el prefijo KA- (17% de los grupos de rodel frente a 4% de los de tablilla) y el sufijo -JA (siete pares raíz/derivado frente a 3,1 esperados). Es el mismo fenómeno a dos escalas de datos.

### 3.5.3.5 Los numerales

Susa hereda de Uruk el sistema sexagesimal (cadena N45 → N34 → N14 → N01 idéntica, mismos acarreos), adapta el de capacidad (mismo tramo alto N01 → N39 → N24, tramo de fracciones propio N30C, N30D, N39C), inventa el decimal (N23 y la cadena N23 → N14 → N01 no existen en Uruk; N51 cambia de valor, de 120 bisexagesimal a 1.000 decimal) y no toma el bisexagesimal (la cadena N19 → N04 de Uruk, 231 casos, ausente en Susa). Es la descripción de Damerow y Englund y de Dahl, recuperada por estructura, con la corrección de que la herencia bisexagesimal no se confirma. El Lineal A no tiene con quién compararse por este lado: sus fracciones (Corazza et al. 2021) son un sistema propio.

### 3.5.3.6 La periferia

En Susa la cabecera institucional M157 es exclusiva del centro (278 tablillas, 0 en Malyan, Yahya, Sialk o Sofalin); Yahya escribe casi solo cuentas de grano y tiene seis signos propios; Malyan usa el inventario de Susa sin signo ajeno. En Creta, Hagia Triada frente a Chania y Zakros muestra una diferencia de repertorio del mismo tipo (los monopolios de HT no aparecen fuera), con la misma limitación de tamaño de la periferia. En los dos casos la diferencia centro/periferia es de género administrativo antes que de escritura.

### 3.5.3.7 Nota sobre el alcance de este trabajo

La comparación de las funciones administrativas que cada archivo pone en palabras (totales, transferencia, sello, fecha, medida) y sus consecuencias para la cuestión de si la forma del recibo minoico es propia o aprendida se tratan en un trabajo aparte (Acedo 2026g), que añade a estos tres archivos los textos administrativos asirios medios, las cartas de Amarna y los registros neoasirios. Aquí el objeto es otro: qué instrumento distributivo empieza a ver a qué tamaño de corpus.

## 3.5.4 Discusión

Qué es común. La contabilidad temprana de tres regiones sin contacto directo (Uruk y Susa lo tuvieron; Creta con ninguna de las dos) tiene la misma anatomía y la misma partición del léxico, y en los tres casos la parte que registra a las personas y los lugares es la clase abierta de cadenas largas y únicas, y la que registra lo contado es la clase cerrada de signos cortos y repetidos. Eso no es lingüística: es la forma que toma un registro de entregas cuando se escribe, y se ve en las tres escrituras porque las tres nacieron para eso.

Qué es propio. Susa inventa un sistema decimal para personas y animales y no toma el bisexagesimal; Creta escribe la mercancía casi siempre con logograma y la parte con sílabas, y separa recibos (rodeles) de listas (tablillas) con un prefijo; Uruk tiene los sistemas de tiempo, raciones y superficie que los otros dos no necesitan. Cada archivo muestra su economía en lo que decidió contar y en cómo decidió contarlo.

Un negativo que conviene registrar. Ordenadas las tablillas de Susa por el volumen de mercancía que registran, la diversidad del vocabulario no cambia (tasa de hapax 0,40, 0,40, 0,36 y 0,42 por cuartiles; p = 0,47): lo que crece con el volumen es la repetición dentro de la tablilla (de 0,08 a 0,49), no la dominancia léxica. La analogía con los gradientes de energía de los sistemas ecológicos, que predice menos diversidad a más entrada, no se traslada al archivo.

Qué enseña sobre el instrumento. La coexclusión, el marco de los nombres y la partición nítida por longitud aparecen con claridad en Susa y Uruk y no en Hagia Triada, cuyo tamaño es una quinta parte y cuyo léxico es mayormente logográfico. El control de mano, en cambio, solo es posible en Hagia Triada, porque solo allí hay atribución de escribas. Cada corpus responde a los instrumentos que su tamaño y sus metadatos le permiten, y la comparación fija por primera vez, con número, el orden de magnitud en que cada instrumento empieza a ver: coexclusión, en torno a ochocientas muestras con vocabulario mixto; marco de nombres, en torno a mil cadenas largas; control de mano, con veinte manos y setenta documentos.

Una asimetría que condiciona todo lo anterior. Los tres corpus no ofrecen los mismos metadatos: solo Hagia Triada tiene manos atribuidas, de modo que el confusor del escriba únicamente puede medirse allí; solo Susa y Uruk comparten un sistema numeral comparable, de modo que la herencia solo puede probarse entre ellos; y solo Susa y Uruk tienen tamaño para la coexclusión. Cada afirmación comparativa de este trabajo vale para los corpus en que el instrumento correspondiente tiene datos, y no más. Qué no dice. Nada sobre las lenguas, que siguen siendo tres desconocidas, ni sobre parentesco entre las escrituras, que no lo tienen salvo Uruk-Susa. Lo que dice es dónde está cada archivo en la tipología de la administración escrita temprana, y que el Lineal A, el más pequeño de los tres, es un archivo normal de esa tipología, medido con la vara que sus hermanos mayores permiten calibrar.




## 3.5 Lo que las cuatro calibraciones dicen del Lineal A

Leídas juntas, dicen tres cosas.

**El instrumento ve.** En cada corpus recupera lo sabido sin que se le diga: la función de las palabras etruscas glosadas, los formantes de Untermann, los numerales compuestos, las unidades léxicas del chiprominoico, la anatomía contable de Susa y Uruk. Donde contradice lo sabido (ekiar sin nombre delante; una isoglosa ibérica que es artefacto de recogida), dice por qué y con qué número.

**Así es "aislado".** La fonotaxis del ibérico, lengua aislada con transcripción fiable, sale con p≈1 contra las trece candidatas del Lineal A, exactamente como el minoico. El instrumento no distingue "aislado" de "filtro de transcripción", y esa es una limitación que hay que declarar; pero fija qué aspecto tiene una lengua sin pariente en este instrumento, y el minoico tiene ese aspecto.

**Así es "con anclaje".** El ibérico, con dos docenas de nombres en una bilingüe latina, ancla ocho elementos con una p por cada uno. El Lineal A, con los seis topónimos cretenses de las listas egipcias, escritos solo en consonantes, ancla uno de nueve, y ese es artefacto de un esqueleto frecuente. Mismo instrumento, misma prueba, datos distintos. La distancia entre las dos lenguas no es de método.

Eso es lo que este artículo aporta al problema del Lineal A: no una lectura, sino la medida de por qué no la hay, en cuatro corpus donde se puede comprobar que la medida funciona.



## Datos y reproducibilidad

Código, tablas derivadas, tasas de error y manifiesto de cifras en kuro (github.com/BiomeMakers/kuro). Los corpus de terceros no se redistribuyen y se reconstruyen con los scripts del paquete; ver data/README.md.

## Declaración de asistencia

El procesamiento de los corpus, las pruebas y la redacción de este texto se produjeron con la asistencia de un modelo de lenguaje (Claude, Anthropic) bajo la dirección del autor, que es responsable de todas las afirmaciones aquí hechas. Dos etapas del procedimiento usan el modelo en el bucle; sus tasas de invención (22% y 1%) se declaran en la Parte 2.

## Referencias

Acedo, A. 2026. Nombres minoicos formados sobre fitónimos: KU-PA y la juncia, KU-MI-NA-QE y KI-KI-RA-JA en los archivos del Lineal A. Borrador en evaluación.

Acedo, A. 2026. Qué puede afirmarse de un corpus de siete mil signos. Borrador.

Acedo, A. 2026b. Mensurabilidad del FSRI: condiciones de tamaño y fiabilidad test-retest. Borrador.

Acedo, A. 2026c. Qué puede afirmarse de un corpus de siete mil signos. Borrador.

Acedo, A. 2026c. What can be claimed about a corpus of seven thousand signs: null tests, calibration and confounders in Linear A, with Etruscan as control. Draft.

Acedo, A. 2026d. kuro. Software.

Acedo, A. 2026d. kuro: modelos nulos, calibración y confusores para corpus epigráficos pequeños. Software.

Acedo, A. 2026f. La fórmula de libación del Lineal A: función de los huecos y frases candidatas. Borrador.

Acedo, A. 2026g. Registro de pruebas y preregistro del procedimiento (documento de acompañamiento).

Acedo, A. 2026g. The Minoan receipt is native: the form of bookkeeping in six Bronze Age administrations. Draft.

Acedo, A. 2026h. Una clasificación de 2010 puesta a prueba: las clases y series de Hagia Triada bajo permutación. Borrador.

Agostiniani, L. y F. Nicosia 2000. Tabula Cortonensis. Roma.

Assael, Y., T. Sommerschield, A. Cooley et al. 2025. Contextualizing ancient texts with generative neural networks. Nature 643.

Assael, Y., T. Sommerschield, B. Shillingford et al. 2022. Restoring and attributing ancient texts using deep neural networks. Nature 603, 280-283.

Best, J. and F. Woudhuizen 1989. Lost Languages from the Mediterranean. Leiden.

Bonfante, G. y L. Bonfante 2002. The Etruscan Language: An Introduction. 2ª ed. Manchester.

Briakos, N. 2026. An Undeciphered Script in the Age of AI: A Corpus-Constrained Computational Analysis of Linear A. Tesis de máster, Universidad del Pireo.

Chadwick, J. The classification of the Knossos tablets.

Corazza, M., F. Tamburini, M. Valério and S. Ferrara 2022. Unsupervised deep learning supports reclassification of Bronze Age Cypriot writing system. PLOS ONE 17(7), e0269544.

Corazza, M., F. Tamburini, M. Valério y S. Ferrara 2022. Unsupervised deep learning supports reclassification of Bronze Age Cypriot writing system. PLOS ONE 17(7): e0269544.

Corazza, M., S. Ferrara, B. Montecchi, F. Tamburini and M. Valério 2021. The mathematical values of fraction signs in the Linear A script. Journal of Archaeological Science 125, 105214.

Dahl, J. L. 2005. Complex graphemes in Proto-Elamite. Cuneiform Digital Library Journal 2005:3.

Dahl, J. L. 2019. Tablettes et fragments proto-élamites / Proto-Elamite Tablets and Fragments (MDP 32). Paris.

Damerow, P. and R. K. Englund 1989. The Proto-Elamite Texts from Tepe Yahya. Cambridge, MA.

Davis, B. 2018. The Phaistos Disk: a new way of viewing the language behind the script. OJA 37, 373-410.

Duhoux, Y. 1989. Le linéaire A: problèmes de déchiffrement. In Problems in Decipherment, Louvain-la-Neuve, 59-119.

Englund, R. K. 1998. Texts from the Late Uruk period. In J. Bauer, R. K. Englund and M. Krebernik, Mesopotamien: Späturuk-Zeit und Frühdynastische Zeit (OBO 160/1), Freiburg, 15-233.

Ferrer i Jané, J. 2009. El sistema de numerales ibérico: avances en su conocimiento. Palaeohispanica 9, 451-479.

Georgiev, V. 1963. Les deux langues des inscriptions crétoises en linéaire A. Sofia.

Godart, L. and J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A, I-V. Paris.

Gordeziani, R. 2007. Mediterranean-Kartvelian Structural Parallels. Tbilisi.

Gordon, C. H. 1966. Evidence for the Minoan Language. Ventnor.

Gotelli, N. J. 2000. Null model analysis of species co-occurrence patterns. Ecology 81, 2606-2621.

Hogan, R. 2022. Linear A Explorer. https://lineara.xyz

Jaccard, P. 1901. Étude comparative de la distribution florale dans une portion des Alpes et du Jura. Bulletin de la Société Vaudoise des Sciences Naturelles 37, 547-579.

Lin, J. 1991. Divergence measures based on the Shannon entropy. IEEE Transactions on Information Theory 37, 145-151.

Luo, J., F. Hartmann, E. Santus, R. Barzilay and Y. Cao 2021. Deciphering undersegmented ancient scripts using phonetic prior. Transactions of the ACL 9, 69-81.

Mantel, N. 1967. The detection of disease clustering and a generalized regression approach. Cancer Research 27, 209-220.

Montecchi, B. 2009. Le frazioni, gli errori di calcolo e le unità di misura nella documentazione in lineare A. Annali dell'Istituto Italiano di Numismatica 55, 29-52.

Montecchi, B. 2010. A classification proposal of Linear A tablets from Haghia Triada in classes and series. Kadmos 49, 11-38.

Montecchi, B. 2019. Contare a Haghia Triada. Incunabula Graeca CVII. Roma.

Nepal, A. and F. Perono Cacciafoco 2024. Minoan cryptanalysis. Information 15(2), 73.

Nissen, H. J., P. Damerow and R. K. Englund 1993. Archaic Bookkeeping: Early Writing and Techniques of Economic Administration in the Ancient Near East. Chicago.

Orduña, E. 2005. Sobre algunos posibles numerales en textos ibéricos. Palaeohispanica 5, 491-506.

Owens, G. 1999. The structure of the Minoan language. Journal of Indo-European Studies 27, 15-56.

Palmer, L. R. 1958. Luvian and Linear A. Transactions of the Philological Society 57, 75-100.

Petrakis, V. and P. M. Steele 2025. The Wor(l)ds of Linear A: some concluding thoughts. In The Wor(l)ds of Linear A, Athens, 167-176.

Rix, H. 1991. Etruskische Texte. Editio minor. Tübingen.

Salgarella, E. 2022. Linear A. Oxford Research Encyclopedia of Classics.

Salgarella, E. and S. Castellan 2020. SigLA. The Signs of Linear A: a palaeographical database. https://sigla.phis.me

Salgarella, E. and S. Castellan 2020. SigLA. https://sigla.phis.me

Schoep, I. 2002. The Administration of Neopalatial Crete. Salamanca.

Shannon, C. E. 1948. A mathematical theory of communication. Bell System Technical Journal 27, 379-423.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos and N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos y N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Steele, P. M. 2013. A Linguistic History of Ancient Cyprus. Cambridge.

Strona, G., D. Nappo, F. Boccacci, S. Fattorini and J. San-Miguel-Ayanz 2014. A fast and unbiased procedure to randomize ecological binary matrices with fixed row and column totals. Nature Communications 5, 4114.

Uchitel, A. 2002-2003. HT 94. Minos 37-38, 81-88.

Untermann, J. 1990. Monumenta Linguarum Hispanicarum III. Die iberischen Inschriften aus Spanien. Wiesbaden.

Velaza, J. 1996. Epigrafía y lengua ibéricas. Madrid.

Vico, G. 2023. Larth: Etruscan NLP corpus. https://github.com/GianlucaVico/Larth-Etruscan-NLP

Wallace, R. E. 2008. Zikh Rasna: A Manual of the Etruscan Language and Inscriptions. Ann Arbor.

Younger, J. G. 2024. Linear A Texts in Phonetic Transcription. https://kansas.academia.edu/JYounger

Younger, J. G. 2024a-b. Linear A Lexicon; Linear A Texts in Phonetic Transcription. https://kansas.academia.edu/JYounger

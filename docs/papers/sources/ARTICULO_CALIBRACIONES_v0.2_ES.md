# El mismo instrumento en cuatro corpus con respuesta parcial: etrusco, ibérico, chiprominoico, y los archivos de Susa y Uruk

**Alberto Acedo**
Biome Makers Inc. Borrador v0.2, 11 de septiembre de 2026. Funde tres notas anteriores (v0.2: sección 5 en español) (etrusco v0.1, ibérico v0.1, tres archivos v0.1) y añade el anclaje del bronce de Ascoli, el perfil de terminaciones y el chiprominoico. No circular.

## Resumen

Un instrumento que solo se ha aplicado a una escritura no descifrada no puede saber si ve algo. Este artículo aplica el mismo procedimiento (nulos de permutación que conservan lo que la afirmación no explica, tasas de error medidas, condición de refutación por entrada) a cuatro corpus donde la respuesta se conoce en parte, y reporta en cada uno qué recupera de lo sabido, qué contradice, y a qué tamaño deja de ver. En etrusco, un clasificador distribucional aprende la función de las palabras glosadas y la asigna a las no glosadas, con validación involuntaria sobre formas conocidas. En ibérico, el nulo señala los treinta formantes onomásticos que Untermann aisló a mano (295 apariciones contra 11 esperadas), separa dos isoglosas y desmonta una tercera; y con la única bilingüe paleohispánica, el bronce de Ascoli, ancla 8 de 23 elementos (1,2 esperados; cinco tras corrección) siempre que se escriban en la ortografía del silabario, que no distingue sordas de sonoras (en ortografía latina, 1 de 16). En chiprominoico, 183 secuencias reconstruidas del conjunto de datos de Corazza y otros (2022) muestran unidades léxicas recurrentes muy por encima del nulo (3-gramas 19 contra 0,9) y un contraste entre soportes sin potencia. En los archivos protoelamita de Susa y protocuneiforme de Uruk, comparados con Hagia Triada, la anatomía contable es la misma y cada instrumento tiene un tamaño mínimo a partir del cual ve. La conclusión transversal es la que sirve al Lineal A: **lo que separa una lengua con anclaje de una sin él es el dato, no el método**, y el instrumento lo dice con una p en cada caso. El ibérico se ancla con dos docenas de nombres; el minoico, con los seis topónimos consonánticos de las listas egipcias, no.

**Palabras clave:** calibración, modelos nulos, etrusco, ibérico, chiprominoico, protoelamita, protocuneiforme, bronce de Ascoli, Lineal A.

## 1. Para qué calibrar

Un método para escrituras no descifradas tiene un problema que no tiene ningún otro: no puede comprobarse sobre su objeto. Si dice que una unidad del Lineal A es un calificador, nadie puede decirle que no. La única forma de saber qué ve es aplicarlo a corpus donde parte de la respuesta se conoce: lenguas que se leen y no se entienden (etrusco, ibérico), o archivos contables de escrituras primitivas cuya lógica se conoce por otros medios (Susa, Uruk), o una escritura hermana del Lineal A con más texto corrido (chiprominoico). En cada caso el instrumento debe recuperar lo sabido sin que se le diga, y donde contradiga lo sabido debe poder decirse por qué.

Las cuatro calibraciones que siguen se hicieron con el mismo paquete (kuro) y sin cambiar una línea del método entre corpus. Cada sección reporta qué recupera, qué contradice, y a qué tamaño el instrumento deja de tener potencia. La sección 6 dice qué significa todo esto para el Lineal A.

## 2.1 Estado de la cuestión

La lectura del etrusco es completa y su comprensión, parcial: el vocabulario con significado establecido ronda las mil entradas (Bonfante y Bonfante 2002; Wallace 2008; ETP), y de los textos, la inmensa mayoría son inscripciones funerarias breves cuyo contenido es onomástico. Los textos largos (Liber Linteus, Tabula Capuana, Tabula Cortonensis, Cippus Perusinus) contienen el vocabulario no onomástico que el campo discute, y es allí donde los editores marcan sus dudas. La pregunta que aquí se plantea no es qué significan esas palabras, sino qué clase de palabra son, que es una cuestión decidible por distribución.

## 2.2 Datos y método

Corpus Larth (Vico 2023): 7.139 registros con ciudad, fecha y traducción cuando la hay, del que se apartan 26 textos umbros (Tablas Iguvinas) detectados por vocabulario; léxico ETP_POS (Wallace y colaboradores) con 1.122 entradas y categoría gramatical. Normalización ortográfica (th → θ, ch → χ, ph → φ, ś → σ, c y q → k), que sube de 316 a 349 las palabras conocidas presentes en los textos. Etiquetas: nombre propio, sustantivo o adjetivo, verbo, partícula. Rasgos: posición inicial y final en la inscripción, inscripción de una sola palabra, vecinos por clase conocida, sufijos (-s, -l, -si, -ke, -χe, -θ, -al, -as, -ia, -u), frecuencia, dispersión por ciudad, y posición contigua a un praenomen conocido. Validación cruzada de cinco pliegues y nulo de etiquetas barajadas.

## 2.3 Resultados

### 2.3.1 El clasificador aprende la función
Acierto 0,70 (0,26 con etiquetas barajadas); recall por clase 0,78 (nombre), 0,54 (sustantivo), 0,67 (verbo), 0,83 (partícula). Los rasgos de mayor peso son la posición en la fórmula onomástica y los sufijos verbales en -ke/-χe.

### 2.3.2 Validación involuntaria sobre palabras conocidas
El fichero de trabajo omite palabras corrientes, de modo que aparecen como "desconocidas" términos cuyo significado el campo sí tiene. El clasificador, sin saberlo, acierta en ocho de diez comprobables: teke (verbo, 0,98), larke y fulnike (verbos, pasados en -ke), ein (partícula, 0,75), θui (partícula), suθi y zilaθ (sustantivos), mlaχ (sustantivo o adjetivo); falla en mulu "dio" y lupu "murió", participios en -u, cuyo sufijo no figuraba entre los rasgos. Esa es la corrección más inmediata del modelo.

### 2.3.3 Los candidatos
De 154 palabras desconocidas para el campo con frecuencia ≥ 3, nueve no son nombres. Tres merecen examen: θapikun (Populonia, Po 4.4), en posición de predicado tras la partícula relativa inpa y con un derivado en la misma inscripción, θapintaś, lo que satisface dos de las tres condiciones del procedimiento; fanu (Cippus Perusinus), entre la partícula eθ "así" y el sujeto lautn "familia", con la comparación clásica con el latín fanum "santuario" pero sin derivado y sin bilingüe que la contraste, una condición y media; y aknanasa, que el examen retira: es el participio acnanasa "habiendo engendrado" de la inscripción de los Alethnas, con traducción en el propio corpus, y su clasificación como sustantivo es un error del modelo por el mismo motivo que mulu y lupu.

### 2.3.4 Dónde están las dudas de los editores
El minado de las traducciones localiza las dudas de contenido en los textos largos: θelu y parχ (Alethnas), munis (dedicatoria a Hercle), θlu, θup y sela (Volterra), iluku y cuieskhu (Tabula Capuana). Cada una tiene entre una y tres atestaciones en el corpus disponible, insuficientes para el procedimiento; son el objetivo natural cuando se disponga de la edición completa.

## 2.4 Discusión y límites

El resultado es de método: en un corpus con vocabulario glosado suficiente, la función de una palabra no glosada es predecible por distribución con acierto medible, y el propio modelo señala qué rasgo morfológico le falta cuando falla. El límite es de datos: el corpus abierto es ruidoso (OCR, umbro, glosas de nombres en lugar de traducciones) y la edición de referencia no está disponible en forma tabulada. Con ella, el mismo procedimiento se aplicaría a las dudas de los editores en los textos largos, que es donde el vocabulario no onomástico del etrusco espera.



## 3.1 Estado de la cuestión

El semisilabario ibérico se lee desde Gómez-Moreno, y la lengua sigue sin entenderse. Lo que sí está establecido es un conjunto de regularidades: un repertorio de formantes que se combinan de dos en dos para formar antropónimos (Untermann 1990), un puñado de sufijos recurrentes (-en, -ar, -ka, -te), un sistema numeral reconocido por comparación con el vasco (Orduña 2005; Ferrer i Jané 2009), y diferencias gráficas entre el ibérico nororiental, el levantino y el meridional que Hesperia recoge en sus mapas de isoglosas. Estas regularidades se han obtenido por inspección de un corpus grande y por comparación interna, no por contraste con modelos nulos, de modo que no se conoce su tamaño de efecto ni la probabilidad de obtenerlas por azar.

## 3.2 Datos y método

Corpus: 2.094 textos ibéricos derivados del Banco de Datos Hesperia (UCM) en la versión publicada por Luo et al. (2021), con la referencia Hesperia de cada texto, que contiene el código de provincia. De ellos, 1.919 tienen texto utilizable tras apartar los fragmentos y los signos de lectura dudosa: 2.677 palabras, 2.359 tipos. Zonas: nororiental (Cataluña, Aragón, Castellón, sur de Francia), 1.644 textos; levantino-meridional (Valencia, Alicante, Albacete, Murcia, Andalucía), 269. Faltan la cronología y el soporte, que están en Hesperia y no en esta copia; su ausencia impide separar el registro y la época, y así se declara.

Método: el de Acedo (2026c). Para los formantes, nulo de letras barajadas entre palabras conservando longitudes; para las terminaciones por zona, test exacto de Fisher con corrección de Bonferroni sobre las sesenta terminaciones probadas (umbral p < 8·10⁻⁴).

## 3.3 Resultados

### 3.3.1 Los formantes de Untermann son el repertorio que el nulo señala
Los treinta formantes buscados como subcadenas aparecen 295 veces; el nulo da 11,1 de media (máximo 20 en 100 permutaciones). Los más frecuentes son taŕ (62), biuŕ (37), atin (33), iltiŕ (31), śalir (26), bilos y beleś (24 cada uno), unin (15), aŕbi (13), baise (12). El resultado no es trivial: dice que las secuencias que Untermann aisló no son arbitrarias respecto a la fonotaxis del corpus.

### 3.3.2 Dos isoglosas se separan con nulo, una tercera es un artefacto
Con las terminaciones de dos y tres signos, y sobre 2.090 palabras del norte y 574 del sur: -kí (el signo S56 en posición final) 28,6‰ en el sur frente a 1,2‰ en el norte (p = 3·10⁻⁸), y 30,9‰ frente a 0 en las de tres signos (p = 3·10⁻⁹); -ḿi 40,5‰ en el norte frente a 7,6‰ en el sur (p = 3·10⁻⁵). Ambas son las isoglosas que Hesperia describe en su mapa 2. La tercera diferencia detectada, la terminación -n (21‰ sur frente a 2,3‰ norte), corresponde a una convención de transcripción del separador y no a un hecho de la lengua; se informa para que no se cuente como resultado.

### 3.3.3 Lo que no puede hacerse todavía
Sin cronología no puede separarse el cambio en el tiempo del cambio en el espacio, que es precisamente el confusor que la calibración etrusca del procedimiento sabe separar cuando hay fechas. Sin soporte no puede compararse el registro de los plomos con el de la cerámica y el de las monedas. Los dos análisis están preparados y se aplicarán cuando el Banco de Datos facilite esos campos.



### 3.4 Discusión de la calibración ibérica

Lo que este trabajo añade no es un hallazgo sino una medida: el repertorio onomástico y las dos isoglosas principales del ibérico tienen ahora tamaño de efecto y probabilidad bajo un nulo explícito. Eso importa por dos razones. Primera, porque el ibérico es el corpus paleohispánico con más textos y mejores metadatos, y cualquier afirmación futura sobre su morfología debería medirse igual. Segunda, porque el mismo procedimiento, aplicado a corpus mucho menores (Lineal A, proto-elamita), declara sin potencia lo que aquí sí se mide: la comparación entre corpus fija el tamaño a partir del cual cada instrumento empieza a ver.



### 3.5 El anclaje bilingüe, medido: el bronce de Ascoli

Los nombres latinizados de la Turma Salluitana (bronce de Ascoli, 89 a. C.) son la única bilingüe real de una lengua paleohispánica. La prueba: para cada elemento onomástico, cuántas formas del corpus de Hesperia (2.906 íntegras) lo contienen, contra 1.000 cadenas de la misma longitud generadas por el modelo de bigramas de letras del propio corpus. En ortografía latina (adin, gibas, bilus, balci, urgi) supera el nulo 1 de 16: la escritura ibérica no distingue sordas de sonoras, y Adingibas se escribe atin-kibas. En ortografía ibérica, con la correspondencia establecida del campo, 8 de 23 superan el nulo (1,2 esperados; p binomial 10⁻⁵) y cinco sobreviven a Bonferroni: bilos, sosin, biuŕ, balke, tautin. De la lista de formantes de Untermann, 15 de 24. El sistema onomástico que la bilingüe deja ver está en el corpus, con una p por elemento, y coincide con lo que Untermann aisló a mano.

### 3.6 El perfil de terminaciones, con la unidad declarada

Raíces atestiguadas desnudas y con una terminación compartida por tres o más raíces, contra un nulo que baraja las terminaciones entre formas. Por letra, el ibérico da 46 terminaciones contra 10 esperadas (4,5 veces), y las más compartidas son las que el campo lee: -te, -ka/-ke, -ḿi, -ar, -en. Con unidad semisilábica (oclusiva + vocal como una unidad), 24 contra 17 (1,4 veces). El Lineal A por sílaba, todas las unidades, 14 contra 6 (2,3 veces); solo las íntegras, 3 contra 1 (-JA, -ME, -TI). Dos lecciones: la razón depende de la unidad, y hay que declararla; y parte de las alternancias publicadas del Lineal A descansa en unidades rotas.

### 3.7 Cuatro afirmaciones del campo ibérico contra nulo

Los numerales vascoides (Orduña 2005; Ferrer 2009: ban, bin, irur, laur, borste, śei, sisbi, sorse, abaŕ, oŕkei) deberían componerse entre sí como en vasco: formas con dos numerales distintos, 7 observadas contra 0,7 esperadas con diez formas al azar de las mismas longitudes (p=0,014; oŕkei-irur, oŕkei-abaŕ-ban, oŕkei-ke-laur). Śalir como plata (Orduña): con marcas metrológicas en 7 de 13 inscripciones contra 28% de base (p=0,046). Ekiar como firma de artesano tras un nombre: 1 de 8 como token aparte y 1 de 13 dentro de la misma forma; no se sostiene con este corpus. La fórmula funeraria aŕe take: dos inscripciones, sin nulo posible. La proporción (una resiste, dos al borde, una cae) es la misma que da el procedimiento sobre las lecturas de Younger en el Lineal A.

## 4. Chiprominoico: unidades léxicas recurrentes en 183 secuencias

Del conjunto de datos publicado por Corazza, Tamburini, Valério y Ferrara (2022; repositorio sign2vec_d) se reconstruyen 183 inscripciones con su secuencia de signos, sitio y soporte: 1.386 signos, 155 tipos. Contra un nulo de unigramas (mismos signos, orden barajado), las secuencias repetidas están muy por encima del azar: 2-gramas 83 contra 43,9; 3-gramas 19 contra 0,9; 4-gramas 6 contra 0. El corpus tiene unidades léxicas recurrentes, que es la condición mínima para que cualquier método de emparejamiento tenga con qué trabajar. El contraste entre tablillas y otros soportes no tiene potencia (6 tablillas, todas de Ugarit). Es la calibración más cercana al Lineal A en tamaño, escritura y época, y la que más se parece a él en lo que no puede hacer.

## 5.1 Por qué comparar tres archivos que no se leen

Los tres corpus comparten la condición que los hace difíciles y la que los hace comparables. Ninguno tiene bilingüe: el Lineal A no se lee; el proto-elamita no se lee y su lengua es desconocida; el proto-cuneiforme se lee a medias, por la continuidad de sus logogramas y sus numerales en el cuneiforme sumerio (Nissen, Damerow y Englund 1993; Englund 1998). Los tres son, en cambio, archivos contables de palacio o de institución, con el mismo tipo de documento: la tablilla que registra entradas de una cantidad de algo asociada a alguien, con cabecera y a veces con total. La bibliografía de cada uno ha descrito esa anatomía por separado (Schoep 2002 y Montecchi 2010 para Hagia Triada; Dahl 2005, 2019 y Damerow y Englund 1989 para Susa; Englund 1998 para Uruk), pero no se ha medido con el mismo instrumento en los tres, y por tanto no se sabe qué rasgos son de la contabilidad temprana en general y cuáles de cada tradición.

La comparación tiene además un valor de método. El aparato usado aquí (Acedo 2026c) produce en el Lineal A una serie de resultados negativos que se atribuyeron al tamaño del corpus: sin coexclusión medible, sin fiabilidad de los descriptores de red, sin potencia para separar tipos de documento. Aplicado a corpus hermanos cinco y veinte veces mayores, permite decir para cada instrumento a qué tamaño empieza a ver, y por tanto convertir esos negativos en una curva de potencia.

## 5.1 bis. Los tres archivos

Hagia Triada, hacia 1450 a.C. Villa de la llanura de la Mesará, en la Creta neopalacial; su archivo, unas 150 tablillas y 150 nódulos y rodeles, se conserva porque el edificio ardió en las destrucciones del Minoico Reciente IB, y registra el último año de una administración que asignaba grano, aceite, vino, higos, ganado y aromáticos, con veintiún escribas trabajando a la vez (Schoep 2002; Montecchi 2010). No hay estratificación temporal: es una foto fija.

Susa, hacia 3100-2900 a.C. Capital de la llanura de Juzestán, en contacto con Uruk y a la vez independiente de ella; sus 1.500 tablillas proto-elamitas son cuentas de grano, ganado, personal y productos derivados, con sistemas numerales propios y una cabecera institucional recurrente, y son casi todo lo que se conserva de esa administración; la periferia (Malyan, Tepe Yahya, Sialk, Sofalin) aporta unas cincuenta más (Damerow y Englund 1989; Dahl 2005, 2019).

Uruk IV-III, hacia 3350-3000 a.C. La primera administración escrita conocida, en la Baja Mesopotamia; unas 5.000 tablillas de la ciudad y sus alrededores, con los sistemas numerales de los que derivan los de Susa, y con un repertorio de logogramas cuyo significado se conoce en parte por su continuidad en el cuneiforme sumerio (Nissen, Damerow y Englund 1993; Englund 1998). Es el único de los tres cuyo contenido se entiende a medias.

## 5.2 Datos e instrumentos

Lineal A: GORILA (Godart y Olivier 1976-1985) en la forma del LinearA Explorer (Hogan 2022), con las manos de GORILA V y los comentarios de Younger (2024); verificación en SigLA (Salgarella y Castellan 2020). Proto-elamita y proto-cuneiforme: las transliteraciones y el catálogo de CDLI (exportación de septiembre de 2026), con los sistemas numerales según Damerow y Englund (1989) y Dahl (2019). En los tres, la unidad es la entrada (línea numerada con cadena de signos y cantidad); la cadena de signos del Lineal A es el grupo de signos silábicos, la del proto-elamita y el proto-cuneiforme la secuencia de signos no numerales de la entrada.

Instrumentos, en el mismo orden en los tres corpus: (1) tamaño y tasa de hapax de las cadenas; (2) hapax por longitud de cadena; (3) recurrencia dentro de documento con cantidades distintas por clase de longitud; (4) cabeceras (primera entrada) y totales; (5) monopolios de vocabulario por tipo de documento o por sistema numeral; (6) coocurrencia y coexclusión con nulo curveball (Strona et al. 2014) sobre la matriz documentos × cadenas frecuentes; (7) sistemas numerales por clase de objeto; (8) manos, donde las hay. Los nulos y umbrales son los descritos en Acedo (2026c): permutación con conservación de márgenes o de longitudes, p < 0,01 con mil permutaciones para afirmaciones nuevas.

## 5.3 Resultados

### 5.3.1 La anatomía es la misma

Los tres archivos escriben la entrada como cadena de signos más cantidad, abren con cabecera (SA-RA₂ y los topónimos en Hagia Triada; M157, el signo de institución, en 278 tablillas de Susa; los signos de institución y de oficio en Uruk) y cierran con total en una parte de las tablillas (KU-RO en Hagia Triada; los totales de Susa y Uruk marcados por posición). La proporción de entradas con cantidad difiere entre los tres (0,60, 0,75 y 0,80; χ² = 121, p < 10⁻²⁶ sobre 8.282 y 23.272 entradas), pero el orden de magnitud es el mismo y la diferencia se explica por la proporción de cabeceras y de líneas rotas en cada corpus; lo comparable es la anatomía, no la tasa.

### 5.3.1 bis Tabla comparativa

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

### 5.3.2 La partición del léxico es la misma, y se ve mejor con más datos

En los tres corpus las cadenas cortas son pocas, frecuentes y repetidas, y las largas son muchas, únicas y no se repiten. En Susa la gradación es limpia: las cadenas de un signo son hapax en el 3% de los casos y se repiten dentro de la tablilla con cantidades distintas en el 13%; las de tres o más signos son hapax en el 87-99% y se repiten en el 0,2%. En Hagia Triada la misma partición existe (los términos de mercancía y transacción se repiten, los nombres son hapax al 76%) pero se ve con menos definición porque la clase corta es en su mayoría logográfica. Uruk se comporta como Susa. La partición entre lo contado y quien lo entrega o recibe es, por tanto, un rasgo de la contabilidad temprana y no de una tradición, y el criterio conductual (repetición con cantidades distintas) la recupera sin lectura en los tres.

### 5.3.3 Los compartimentos, y quién los hace

En Hagia Triada, las cuentas con total tienen seis palabras de monopolio y las asignaciones tres (p < 0,01 en ambos casos); en Susa, el sistema de capacidad (grano) tiene 24 cadenas de monopolio, el decimal 3, el sexagesimal ninguna. La coexclusión, que en Hagia Triada no es medible (cero pares con esperado ≥ 1 en 224 documentos), aparece en Susa con 830 tablillas: 13 pares nunca coocurren cuando deberían (la cabecera M157 con M371, M370, M373, M046, M367; el producto de grano M297 con M376, M124, M003, M032, M009), lo que separa las cuentas de grano de las de ganado y personal. Solo Hagia Triada permite el control de mano: con 73 tablillas atribuidas a 21 escribas, el vocabulario compartido lo explica la mano (efecto 0,032, p = 0,002 controlando el tipo) y no el tipo de documento (0,025, p = 0,21): los compartimentos minoicos son, al menos en parte, carteras de escriba. Susa y Uruk no tienen manos atribuidas en el catálogo, y su compartimentación no puede descomponerse así; se declara.

### 5.3.4 Las cadenas largas tienen marco

En Susa, las 1.296 cadenas de tres o más signos con cantidad tienen un signo de institución u objeto en posición final por encima del azar (M288 231 veces, lift 3,8, p < 10⁻⁶; también M263, M297, M346) y un signo de clase en posición inicial (M124, M305, M157). Los "nombres" llevan marco: clasificador delante, núcleo variable, institución u objeto detrás. En Hagia Triada el marco existe con menos potencia: el prefijo KA- (17% de los grupos de rodel frente a 4% de los de tablilla) y el sufijo -JA (siete pares raíz/derivado frente a 3,1 esperados). Es el mismo fenómeno a dos escalas de datos.

### 5.3.5 Los numerales

Susa hereda de Uruk el sistema sexagesimal (cadena N45 → N34 → N14 → N01 idéntica, mismos acarreos), adapta el de capacidad (mismo tramo alto N01 → N39 → N24, tramo de fracciones propio N30C, N30D, N39C), inventa el decimal (N23 y la cadena N23 → N14 → N01 no existen en Uruk; N51 cambia de valor, de 120 bisexagesimal a 1.000 decimal) y no toma el bisexagesimal (la cadena N19 → N04 de Uruk, 231 casos, ausente en Susa). Es la descripción de Damerow y Englund y de Dahl, recuperada por estructura, con la corrección de que la herencia bisexagesimal no se confirma. El Lineal A no tiene con quién compararse por este lado: sus fracciones (Corazza et al. 2021) son un sistema propio.

### 5.3.6 La periferia

En Susa la cabecera institucional M157 es exclusiva del centro (278 tablillas, 0 en Malyan, Yahya, Sialk o Sofalin); Yahya escribe casi solo cuentas de grano y tiene seis signos propios; Malyan usa el inventario de Susa sin signo ajeno. En Creta, Hagia Triada frente a Chania y Zakros muestra una diferencia de repertorio del mismo tipo (los monopolios de HT no aparecen fuera), con la misma limitación de tamaño de la periferia. En los dos casos la diferencia centro/periferia es de género administrativo antes que de escritura.

### 5.3.7 Nota sobre el alcance de este trabajo

La comparación de las funciones administrativas que cada archivo pone en palabras (totales, transferencia, sello, fecha, medida) y sus consecuencias para la cuestión de si la forma del recibo minoico es propia o aprendida se tratan en un trabajo aparte (Acedo 2026g), que añade a estos tres archivos los textos administrativos asirios medios, las cartas de Amarna y los registros neoasirios. Aquí el objeto es otro: qué instrumento distributivo empieza a ver a qué tamaño de corpus.

## 5.4 Discusión

Qué es común. La contabilidad temprana de tres regiones sin contacto directo (Uruk y Susa lo tuvieron; Creta con ninguna de las dos) tiene la misma anatomía y la misma partición del léxico, y en los tres casos la parte que registra a las personas y los lugares es la clase abierta de cadenas largas y únicas, y la que registra lo contado es la clase cerrada de signos cortos y repetidos. Eso no es lingüística: es la forma que toma un registro de entregas cuando se escribe, y se ve en las tres escrituras porque las tres nacieron para eso.

Qué es propio. Susa inventa un sistema decimal para personas y animales y no toma el bisexagesimal; Creta escribe la mercancía casi siempre con logograma y la parte con sílabas, y separa recibos (rodeles) de listas (tablillas) con un prefijo; Uruk tiene los sistemas de tiempo, raciones y superficie que los otros dos no necesitan. Cada archivo muestra su economía en lo que decidió contar y en cómo decidió contarlo.

Un negativo que conviene registrar. Ordenadas las tablillas de Susa por el volumen de mercancía que registran, la diversidad del vocabulario no cambia (tasa de hapax 0,40, 0,40, 0,36 y 0,42 por cuartiles; p = 0,47): lo que crece con el volumen es la repetición dentro de la tablilla (de 0,08 a 0,49), no la dominancia léxica. La analogía con los gradientes de energía de los sistemas ecológicos, que predice menos diversidad a más entrada, no se traslada al archivo.

Qué enseña sobre el instrumento. La coexclusión, el marco de los nombres y la partición nítida por longitud aparecen con claridad en Susa y Uruk y no en Hagia Triada, cuyo tamaño es una quinta parte y cuyo léxico es mayormente logográfico. El control de mano, en cambio, solo es posible en Hagia Triada, porque solo allí hay atribución de escribas. Cada corpus responde a los instrumentos que su tamaño y sus metadatos le permiten, y la comparación fija por primera vez, con número, el orden de magnitud en que cada instrumento empieza a ver: coexclusión, en torno a ochocientas muestras con vocabulario mixto; marco de nombres, en torno a mil cadenas largas; control de mano, con veinte manos y setenta documentos.

Una asimetría que condiciona todo lo anterior. Los tres corpus no ofrecen los mismos metadatos: solo Hagia Triada tiene manos atribuidas, de modo que el confusor del escriba únicamente puede medirse allí; solo Susa y Uruk comparten un sistema numeral comparable, de modo que la herencia solo puede probarse entre ellos; y solo Susa y Uruk tienen tamaño para la coexclusión. Cada afirmación comparativa de este trabajo vale para los corpus en que el instrumento correspondiente tiene datos, y no más. Qué no dice. Nada sobre las lenguas, que siguen siendo tres desconocidas, ni sobre parentesco entre las escrituras, que no lo tienen salvo Uruk-Susa. Lo que dice es dónde está cada archivo en la tipología de la administración escrita temprana, y que el Lineal A, el más pequeño de los tres, es un archivo normal de esa tipología, medido con la vara que sus hermanos mayores permiten calibrar.


## 6. Lo que las cuatro calibraciones dicen del Lineal A

Leídas juntas, dicen tres cosas.

**El instrumento ve.** En cada corpus recupera lo sabido sin que se le diga: la función de las palabras etruscas glosadas, los formantes de Untermann, los numerales compuestos, las unidades léxicas del chiprominoico, la anatomía contable de Susa y Uruk. Donde contradice lo sabido (ekiar sin nombre delante; una isoglosa ibérica que es artefacto de recogida), dice por qué y con qué número.

**Así es "aislado".** La fonotaxis del ibérico, lengua aislada con transcripción fiable, sale con p≈1 contra las trece candidatas del Lineal A, exactamente como el minoico. El instrumento no distingue "aislado" de "filtro de transcripción", y esa es una limitación que hay que declarar; pero fija qué aspecto tiene una lengua sin pariente en este instrumento, y el minoico tiene ese aspecto.

**Así es "con anclaje".** El ibérico, con dos docenas de nombres en una bilingüe latina, ancla ocho elementos con una p por cada uno. El Lineal A, con los seis topónimos cretenses de las listas egipcias, escritos solo en consonantes, ancla uno de nueve, y ese es artefacto de un esqueleto frecuente. Mismo instrumento, misma prueba, datos distintos. La distancia entre las dos lenguas no es de método.

Eso es lo que este artículo aporta al problema del Lineal A: no una lectura, sino la medida de por qué no la hay, en cuatro corpus donde se puede comprobar que la medida funciona.

## Datos y reproducibilidad

Etrusco: OpenEtruscan y Larth/ETP. Ibérico: Banco de Datos Hesperia vía Luo y otros 2021 (solo consulta; no se redistribuye). Chiprominoico: Corazza y otros 2022 (sign2vec_d). Susa y Uruk: CDLI. Código y tablas derivadas en kuro (github.com/BiomeMakers/kuro).

## Declaración de asistencia

El procesamiento de los corpus, las pruebas y la redacción de este texto se produjeron con la asistencia de un modelo de lenguaje (Claude, Anthropic) bajo la dirección del autor, que es responsable de todas las afirmaciones aquí hechas.

## Referencias

Corazza, M., F. Tamburini, M. Valério y S. Ferrara 2022. Unsupervised deep learning supports reclassification of Bronze Age Cypriot writing system. PLOS ONE 17(7): e0269544.

Ferrer i Jané, J. 2009. El sistema de numerales ibérico: avances en su conocimiento. Palaeohispanica 9, 451-479.

Orduña, E. 2005. Sobre algunos posibles numerales en textos ibéricos. Palaeohispanica 5, 491-506.

Acedo, A. 2026c. Qué puede afirmarse de un corpus de siete mil signos. Borrador.

Acedo, A. 2026c. What can be claimed about a corpus of seven thousand signs: null tests, calibration and confounders in Linear A, with Etruscan as control. Draft.

Acedo, A. 2026d. kuro. Software.

Acedo, A. 2026d. kuro: modelos nulos, calibración y confusores para corpus epigráficos pequeños. Software.

Acedo, A. 2026g. The Minoan receipt is native: the form of bookkeeping in six Bronze Age administrations. Draft.

Agostiniani, L. y F. Nicosia 2000. Tabula Cortonensis. Roma.

Bonfante, G. y L. Bonfante 2002. The Etruscan Language: An Introduction. 2ª ed. Manchester.

Corazza, M., S. Ferrara, B. Montecchi, F. Tamburini and M. Valério 2021. The mathematical values of fraction signs in the Linear A script. Journal of Archaeological Science 125, 105214.

Dahl, J. L. 2005. Complex graphemes in Proto-Elamite. Cuneiform Digital Library Journal 2005:3.

Dahl, J. L. 2019. Tablettes et fragments proto-élamites / Proto-Elamite Tablets and Fragments (MDP 32). Paris.

Damerow, P. and R. K. Englund 1989. The Proto-Elamite Texts from Tepe Yahya. Cambridge, MA.

Englund, R. K. 1998. Texts from the Late Uruk period. In J. Bauer, R. K. Englund and M. Krebernik, Mesopotamien: Späturuk-Zeit und Frühdynastische Zeit (OBO 160/1), Freiburg, 15-233.

Ferrer i Jané, J. 2009. El sistema de numerales ibérico: avances en su conocimiento. Palaeohispanica 9, 451-479.

Godart, L. and J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A, I-V. Paris.

Hogan, R. 2022. Linear A Explorer. https://lineara.xyz

Luo, J., F. Hartmann, E. Santus, R. Barzilay and Y. Cao 2021. Deciphering undersegmented ancient scripts using phonetic prior. Transactions of the ACL 9, 69-81.

Montecchi, B. 2010. A classification proposal of Linear A tablets from Haghia Triada in classes and series. Kadmos 49, 11-38.

Nissen, H. J., P. Damerow and R. K. Englund 1993. Archaic Bookkeeping: Early Writing and Techniques of Economic Administration in the Ancient Near East. Chicago.

Orduña, E. 2005. Sobre algunos posibles numerales en textos ibéricos. Palaeohispanica 5, 491-506.

Rix, H. 1991. Etruskische Texte. Editio minor. Tübingen.

Salgarella, E. and S. Castellan 2020. SigLA. The Signs of Linear A: a palaeographical database. https://sigla.phis.me

Schoep, I. 2002. The Administration of Neopalatial Crete. Salamanca.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos and N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Strona, G., D. Nappo, F. Boccacci, S. Fattorini and J. San-Miguel-Ayanz 2014. A fast and unbiased procedure to randomize ecological binary matrices with fixed row and column totals. Nature Communications 5, 4114.

Untermann, J. 1990. Monumenta Linguarum Hispanicarum III. Die iberischen Inschriften aus Spanien. Wiesbaden.

Velaza, J. 1996. Epigrafía y lengua ibéricas. Madrid.

Vico, G. 2023. Larth: Etruscan NLP corpus. https://github.com/GianlucaVico/Larth-Etruscan-NLP

Wallace, R. E. 2008. Zikh Rasna: A Manual of the Etruscan Language and Inscriptions. Ann Arbor.

Younger, J. G. 2024. Linear A Texts in Phonetic Transcription. https://kansas.academia.edu/JYounger

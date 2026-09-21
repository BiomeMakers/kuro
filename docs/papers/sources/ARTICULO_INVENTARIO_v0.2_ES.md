# El inventario funcional del Lineal A: cincuenta y seis unidades con función fijada por distribución, y lo que el corpus no puede fijar

**Alberto Acedo**
Biome Makers Inc. Borrador v0.2, 11 de septiembre de 2026. No circular.

## Resumen

Un siglo de propuestas de lectura del Lineal A no ha producido un inventario que diga, unidad por unidad, qué se sabe, con qué evidencia, y qué observación lo refutaría. Este artículo lo construye para las 156 unidades del corpus con tres o más atestaciones íntegras. Cada lectura se fija por la distribución de la unidad en el corpus (posición, cifras y fracciones, compañía, sitio y sello) contra un nulo de permutación con tasa de error medida, y se archiva con la evidencia a favor, la evidencia en contra, y una condición de refutación. El resultado son 56 unidades con función: cuatro términos aritméticos, ocho encabezados y términos de transacción, dieciséis signos de mercancía, ganado y personas, dieciséis calificadores y grados, ocho topónimos y nombres compartidos con el Lineal B, y cuatro funciones sueltas. Catorce no tienen fuente previa; las otras 42 tienen prior art y llevan aquí por primera vez una medida. Ninguna es una palabra con significado léxico: los logogramas son dibujos, y los grupos de signos silábicos tienen función, no traducción. El inventario trae además tres hechos del corpus que las ediciones no declaran: 276 de las 783 unidades silábicas están rotas en todas sus atestaciones (35%), lo que invalida parte de las alternancias morfológicas publicadas; los 801 nódulos sellados de Hagia Triada forman dos circuitos de sellos que no comparten signos, y el signo no identifica al sellador; y el archivo no registra metal, miel ni pescado, presentes en la cultura material. Se declara el techo: con este corpus, el método interno fija funciones y no palabras, y el número no se mueve con más corridas sino con dato nuevo.

**Palabras clave:** Lineal A, Hagia Triada, inventario, modelos nulos, logogramas, calificadores, nódulos, tasa de error.

## 1. Por qué un inventario y no una lectura más

Quien busca en el Lineal A qué se sabe de una unidad concreta encuentra el lexicón de Younger, que lo recoge casi todo y no distingue lo medido de lo conjeturado, y una bibliografía de propuestas que rara vez declara qué dato la refutaría. Lo que no hay es una tabla con tres columnas: qué se afirma, qué lo apoya, qué lo tumbaría. Este artículo es esa tabla, construida con un solo procedimiento y publicada con su código.

El procedimiento no lee. Fija qué **hace** una unidad en la cuenta a partir de cómo la trata el escriba: si abre el documento, si lleva cifra, si esa cifra admite fracciones, si va después de una mercancía con una cifra menor, si se le añade una sílaba o si es la sílaba añadida, con qué otras unidades comparte documento, y en los nódulos, con qué sello. Cada una de esas observaciones tiene un nulo que conserva lo que la afirmación no explica, y cada instrumento tiene una tasa de error medida sobre material donde no debería encontrar nada.

## 2. El corpus y lo que las ediciones no dicen de él

El corpus es GORILA a través del LinearA Explorer: 1.720 documentos y 1.007 unidades distintas, de las que 156 tienen tres o más atestaciones y al menos una íntegra. Ese es el techo del inventario: por debajo de tres atestaciones no hay perfil que medir.

**Las unidades rotas.** El campo `words` de la edición conserva el signo de rotura y la transliteración lo pierde. Recuperado, 276 de las 783 unidades silábicas (35%) están rotas en todas sus atestaciones: ]MA-TE-RE no es MA-TE-RE. Tres de las ocho coincidencias léxicas con el Lineal B de un primer cotejo eran fragmentos, y de los pares raíz/terminación de Davis, cinco de ocho terminaciones bajan de tres raíces cuando solo cuentan las íntegras (quedan -JA, -ME, -TI). Todo el inventario se calcula sobre unidades íntegras.

**Los nódulos.** Los comentarios de Younger dan, para 801 nódulos de Hagia Triada, el signo inscrito y el sello (número CMS II,6 y motivo). Signo y sello van ligados (información mutua 0,88 contra 0,19 en 500 permutaciones), pero no uno a uno: los sellos forman dos bloques que no comparten signos (AT 13, 99, 45, 9, 17, 38 solo con *301 y ZE; AT 125, 105, 19, 95, 79 con KU, KA, SI, RO, I y TA y nunca *301), y dentro de un bloque un mismo sello usa seis signos. El signo no identifica al sellador; identifica lo sellado. AT 19 usa KU en 42 de 44 nódulos: un funcionario para un solo tipo. Lo que falta para leer esos signos es el tipo de nódulo por documento (Hallager 1996, vol. II), que no está en fuente abierta.

**Los huecos.** La cultura material de Hagia Triada tiene lingotes de cobre, miel y pescado. Ningún signo con cifra tiene el perfil de esas cosas (enteros bajos o peso para el metal, fracción de líquido para la miel), *118 es la unidad de peso y acompaña a cyperus y sésamo, y el lexicón de Younger no las menciona. El archivo de tablillas no las registra.

## 3. Los instrumentos y su tasa de error

Doce instrumentos, cada uno con su nulo y su tasa medida (data/derived/error_rates.json). Los que sostienen el inventario:

| instrumento | qué mide | nulo | tasa de error a 0,05 |
|---|---|---|---|
| perfil de cantidades | fracción de las cifras de un logograma contra la base (27%), en la dirección que predice la clase; tamaño de las cifras | fracciones a la tasa base | 4,6% (peor caso, dirección a posteriori) |
| encabezado | primera posición en tablilla contra la base (11,8%) | binomial | posicional: 3-5% |
| subrecuento | cifra menor que la de la mercancía precedente contra la base (52%) | binomial | (dentro de posicional) |
| calificador | sílaba añadida a dos o más signos de mercancía distintos | regla, no prueba | — |
| coocurrencia estratificada | dos unidades en el mismo documento, conservando sitio y márgenes | bipartito por sitio | 5,5% |
| adyacencia | dos unidades contiguas, sobre pares elegibles | permutación | 2,5% |
| cotejo de nombres | coincidencia exacta con el léxico del B por longitud | bigramas de sílabas del propio corpus | (por longitud; 2 sílabas = azar) |
| aritmética | la cifra tras la unidad iguala la suma de las anteriores | permutación | 2,5% |

Un instrumento se calibra sobre el material al que se aplica: la tasa del perfil se midió barajando las fracciones de logogramas ya leídos a la tasa base; la de coocurrencia, sobre palabras y logogramas del propio corpus (8,0% sin estratificar, 5,5% estratificando por sitio: el sitio era el confusor).

## 4. El inventario

Cincuenta y seis unidades: 25 establecidas (consenso del campo confirmado por nuestra prueba), 27 propuestas (nuestra prueba sin consenso previo, o prior art sin prueba propia hasta ahora), 4 disputadas (fuente en contra). Estado, atestaciones, lectura, fuente previa a favor y número de evidencias en contra:

| unidad | estado | atest. | lectura | fuente previa | contra |
|---|---|---|---|---|---|
| **Aritmética** | | | | | |
| KU-RO | established | 37 | total | Godart & Olivier / field consensus, Scho |  |
| KI-RO | established | 16 | deficit | Schoep, Uchitel |  |
| DA-I | proposed | 2 | a total, of a kind distinct from KU-RO | — |  |
| PO-TO-KU-RO | established | 2 | grand total | Schoep |  |
| **Calificadores y grados** | | | | | |
| KU | established | 170 | as an added syllable, a qualifier of four commodities (GRA+KU, TELA+KU, *188+KU, | — |  |
| KA | proposed | 169 | as an added syllable, a qualifier of wine and of persons (VIN+KA, VIR+KA); alone | — |  |
| OLE+MI | proposed | 19 | a grade of oil; listed together with OLE+DI in every document where it carries a | Younger | 1 |
| KI | established | 19 | as an added syllable, a qualifier of oil and *316 (OLE+KI, *316+KI) and of wool  | Del Freo, via Nosch and Weilhartner |  |
| CYP+D | proposed | 19 | a grade of cyperus recorded in the smallest amounts (fractions in 13 of 16, maxi | — |  |
| PA | proposed | 16 | qualifier (a grade or type) shared by grain, cyperus and *304: GRA+PA, CYP+PA, * | — |  |
| OLE+DI | proposed | 12 | a grade of oil; listed together with OLE+MI in every document where it carries a | Younger | 1 |
| TU | established | 11 | qualifier (a grade or type) restricted to the olive family: OLE+TU and OLIV+TU | Younger |  |
| RA | proposed | 9 | as an added syllable, a qualifier of oil and wine (OLE+RA, VIN+RA) | — |  |
| OLE+TA | proposed | 8 | a grade of oil recorded in small fractional amounts | Younger |  |
| GRA+KU | proposed | 7 | GRA with the qualifier KU (a grade or type) | — |  |
| VIN+RA | proposed | 4 | wine with the qualifier RA (a grade or type), parallel to OLE+RA | — |  |
| MA-RU-ME | proposed | 3 | wool with the qualifier ME (a type or grade) | Del Freo, via Nosch and Weilhartner |  |
| *188+KU | proposed | 2 | *188 with the qualifier KU (a grade or type) | — |  |
| KI-MA-RU | proposed | 1 | wool with the qualifier KI | Del Freo, via Nosch and Weilhartner |  |
| TELA+KU | proposed | 1 | TELA with the qualifier KU (a grade or type) | — |  |
| **Encabezados y transacción** | | | | | |
| TE | established | 58 | transaction term set between a party and the commodity ("X 𐄁 TE 𐄁 VIN"); also th | Schoep, Younger |  |
| SA-RA₂ | disputed | 20 | transaction term, Haghia Triada only; possibly the ethnic of the site | Schoep, Uchitel | 1 |
| A-DU | established | 10 | heading term (record label) of HT tablets; heads the lists of HT 86 and HT 95 am | Younger |  |
| KA-PA | established | 6 | heading term of HT tablets (HT only); KA-PA-QE is its extended form (Salgarella  | Salgarella |  |
| JE-DI | proposed | 4 | heading term (first position in 3 of 4 tablet attestations) | — |  |
| A-KA-RU | established | 3 | heading term of HT tablets (HT 2.1, HT 86a.1, HT 86b.1 as second heading) | Younger |  |
| DA-QE-RA | proposed | 3 | heading term of HT tablets (HT 6a.6 as a second heading, HT 120.1) | Younger |  |
| KI-RI-TA₂ | proposed | 2 | heading term (first position in both attestations) | — |  |
| **Mercancías, ganado y personas** | | | | | |
| NI | established | 76 | figs (the logogram NI; ni- as the first syllable of the Minoan word) | Neumann; Salgarella and Petrakis (eds.), |  |
| GRA | established | 62 | grain (cereal), the bulk dry commodity | Ventris and Chadwick |  |
| VIN | established | 53 | wine, a liquid commodity | Ventris and Chadwick |  |
| CYP | established | 52 | cyperus (*303), a fine commodity measured in small fractional amounts | Ventris and Chadwick |  |
| OLIV | established | 24 | olives, the fruit as distinct from its oil | Ventris and Chadwick |  |
| OLE+U | proposed | 22 | a type of oil counted in whole units (or a counted unit of oil: whole numbers, s | — | 1 |
| OLE | established | 22 | olive oil, a liquid commodity | Ventris and Chadwick |  |
| *22F | established | 14 | goat, female; Linear B CAPf | GORILA / Ventris and Chadwick |  |
| *308 | proposed | 12 | fatty product derived from the olive | Koh & Birney, Younger |  |
| *305 | proposed | 12 | a category of persons | Younger |  |
| *21M | established | 8 | sheep, male (ram); Linear B OVISm | GORILA / Ventris and Chadwick |  |
| *23M | established | 7 | ox/bull; Linear B BOSm | GORILA / Ventris and Chadwick |  |
| *21F | established | 4 | sheep, female (ewe); Linear B OVISf | GORILA / Ventris and Chadwick |  |
| *131B | proposed | 4 | a variant of the wine sign (AB 131b), a type of wine | GORILA |  |
| *22M | established | 3 | goat, male; Linear B CAPm | GORILA / Ventris and Chadwick |  |
| VIR | established | 0 | person (man), the unit counted in personnel lists | Ventris and Chadwick |  |
| **Otras funciones** | | | | | |
| JA-SA-SA-RA-ME | proposed | 7 | does not designate the offering or the object | — |  |
| *306 | disputed | 7 | possibly the sign for woman | Uchitel | 2 |
| KU-NI-SU | disputed | 5 | first name in a list; the Semitic reading as emmer is proposed and contested | Younger, various, cited by Younger | 1 |
| SU-KI-RI-TE-I-JA | proposed | 1 | formed on the stem of Sybrita, or sharing its lexicon | Davis |  |
| **Topónimos y nombres** | | | | | |
| KI-DA-RO | proposed | 2 | a personal name shared with the Linear B tablets of Knossos (Godart 1984) | Godart |  |
| PA-I-TO | established | 2 | Phaistos, the place name (Linear B pa-i-to) | Godart |  |
| DA-I-PI-TA | proposed | 2 | a personal name shared with the Linear B tablets of Knossos (Godart 1984) | Godart |  |
| I-TA-JA | proposed | 1 | a personal name shared with the Linear B tablets of Knossos (Godart 1984) | Godart |  |
| DA-MA-TE | disputed | 1 | coincides with Linear B da-ma-te; read as Demeter by some, contested | Owens | 2 |
| SU-KI-RI-TA | established | 1 | Sybrita, the place name (Linear B su-ki-ri-ta) | Godart |  |
| I-JA-TE | proposed | 1 | coincides with Linear B i-ja-te (PY Eq 146); Younger: "of/from I-JA" | Godart, Younger |  |
| SE-TO-I-JA | established | 1 | Setoia, the place name (Linear B se-to-i-ja; Archanes or Iouktas?) | Godart |  |

Cuatro cosas se ven en la tabla entera.

**Catorce sin fuente previa.** DA-I como total de otra clase; KI-RI-TA₂ y JE-DI como encabezados; VIN+RA paralelo a OLE+RA; KU como calificador de cuatro mercancías y PA de tres; KA de vino y de personas; CYP+D como cyperus en cantidades mínimas; OLE+TA como aceite fino; OLE+DI y OLE+MI como grados emparejados; JA-SA-SA-RA-ME como lo que no es. Son funciones, y varias son el mismo hallazgo visto en varias unidades (KU en cuatro ligaduras).

**Cuarenta y dos con prior art, y la medida es lo nuevo.** VIR solo en enteros (2 de 36 con fracción, p=0,0008); GRA en enteros grandes (12 de 90, máximo 976); CYP casi siempre en fracciones y en cantidades pequeñas (39 de 64, máximo 23); TE en el patrón separador-TE-separador-mercancía en 10 de 24 contra 2,5% (p=10⁻¹⁰); el ganado con marca de sexo en enteros (2 de 28, p=0,007) y PH 31 como lista por especie y sexo; A-DU en primera posición en 7 de 10 (p<0,0001). Y en la otra dirección: seis "encabezados" de Younger con cero en primera posición, KU-NI-SU como emmer disputada, y "*304 siempre entre OLE y OLIV" falso como está dicho (6 de 25).

**Ninguna palabra.** Las 56 son función: qué hace la unidad en la cuenta. De los 16 signos de mercancía, ganado y personas, la lectura viene de la identidad pictográfica con el Lineal B (OLE es aceite porque el signo es el mismo y en el B está fijado por contexto griego), y nuestra prueba dice que la administración los contaba como esa clase de cosa se cuenta. Ningún grupo silábico tiene traducción: KU-RO es "total" porque suma, no porque sepamos cómo se decía "total" en minoico.

**Lo que se probó y no se fijó.** Los nombres de lista (la clase más numerosa) solo se juzgan por exclusión: sin fracciones propias, sin sílaba añadida, no encabezado, no total; y esa exclusión deja igual a un nombre de persona y a una mercancía escrita en sílabas. Sin fuente externa no hay juez positivo, y la categoría "entrada de lista" no se cuenta como lectura. Los signos de nódulo (*301, KU, KA, SI, RO, ZE) tienen fijada su estructura (los dos circuitos) y no su lectura. Las cinco unidades al borde de dos corridas (VIR+[?], QA2+[?]+PU, SA-RU, A-SE, JE-DI parcialmente) no se archivan: p de 0,01 a 0,04 a secas con 50-80 pruebas es lo que el azar produce.

## 4 bis. El alcance del inventario: qué archivo fijó cada función

Las 56 entradas no se fijaron sobre "el Lineal A" sino sobre los archivos que tienen material suficiente, y eso es casi siempre Hagia Triada (64% del corpus). La distinción no es formal. El segundo archivo, Khania (227 documentos, 105 tablillas), **no usa términos de suma en ninguna de sus tablillas**, frente a 41 de 205 en Hagia Triada: bajo la tasa de Hagia Triada, la probabilidad de ese cero es 7·10⁻¹¹. KU-RO, KI-RO, PO-TO-KU-RO y DA-I son funciones del archivo de Hagia Triada, y en Khania no hay con qué comprobarlas.

Khania tampoco es el mismo tipo de archivo: sus tablillas tienen la mitad de unidades (7,4 frente a 13,8) y la cuarta parte de grupos silábicos (0,8 frente a 3,1), sus cifras son menores (mediana 3 frente a 5), el 36% llevan fracción frente al 17%, y su mercancía dominante es el cyperus (65 apariciones frente a 14), con el 68% de sus registros en fracciones. Es distribución menuda de un producto fino, no almacén de graneles.

Aplicados los instrumentos con las tasas base del propio archivo, Khania no produce encabezados ni calificadores propios, y produce una lectura que Hagia Triada no puede dar: **CYP+D lleva la cantidad ½ en 12 de sus 16 atestaciones con cifra** contra una base del 22% (p=10⁻⁵), y se emite tras entradas de personas (KH 7a: VIR+*313b 10 y CYP+D ½; VIR+*313b 4 y CYP+D ⅓). Ninguna mercancía de Hagia Triada tiene una cantidad dominante a ese nivel. Es la única candidata del corpus a asignación de cantidad fija.

El inventario, por tanto, se lee con esta restricción: **es el inventario funcional del archivo de Hagia Triada, con adiciones de Khania y de los vasos votivos.** El corpus del Lineal A no tiene un formato contable sino al menos dos.

## 5. Cómo se llegó, y por qué el número se para

El inventario pasó de 18 a 56 en dos días de trabajo con el mismo procedimiento sobre las mismas unidades: el paralelo con el Lineal B (ganado, mercancías, NI, TE), la extrapolación de estructuras (calificador, subrecuento, encabezado), el cotejo de nombres con nulo, y dos etapas con un modelo de lenguaje en el bucle. Esas dos etapas se midieron: leyendo pasajes de la literatura, el modelo inventa unidades inexistentes en el 22% de los casos; proponiendo una lectura a partir del dosier de cada unidad (cifras, posición, compañía, sello), en el 1%. Su aporte fue el enrutado a escala, no la idea: las tres lecturas nuevas que trajo salieron de reglas mecánicas aplicadas a unidades que nadie había mirado con ellas. La segunda vuelta del mismo procedimiento sobre las 117 unidades restantes no encontró nada.

Ese es el techo, y conviene decirlo con precisión. No es el techo del problema: es el techo de lo que se puede **verificar** con este corpus. Las cuentas tienen pocas funciones y están casi todas fijadas; las que quedan (unos veinte signos de nódulo) esperan un dato externo; y el paso de función a palabra exige un juez que el corpus no contiene, porque nada en él puede decir que "KU-NI-SU significa emmer" es falso. Ese juez lo darían una bilingüe o texto corrido nuevo, y salen de excavación.

## 6. Discusión

Lo que este inventario cambia no es el número de lecturas sino su estatuto. Cada una de las 56 lleva escrito qué observación la refutaría, y el diccionario se niega a archivar una entrada sin esa línea. Cada instrumento lleva su tasa de error, y una tasa que salió mal (el nulo uniforme de las fracciones, 16,5%) se conserva como registro de por qué se cambió el nulo y no el instrumento. Cada afirmación con prior art lleva la cita y la medida juntas, y las que caen se archivan como caídas, con la fuente en contra. Es lo que el campo pide de un desciframiento y no ha pedido de un lexicón: que se pueda saber, de cada línea, cuánto vale.

Y lo que el inventario dice del Lineal A, leído entero, es una cosa que un siglo de propuestas no había dicho con esta forma: **sabemos qué se contaba y cómo se organizaba la cuenta, sabemos tres lugares, y no sabemos ninguna palabra**. La distancia entre un archivo entendido y una lengua leída es exactamente esa, y no la cierra ningún método interno.

## Datos y reproducibilidad

Corpus GORILA vía LinearA Explorer (R. Hogan); sellos de los nódulos de los comentarios de J. Younger; Lineal B de linearb.xyz. Diccionario, tasas de error, tabla signo × sello y corridas en data/derived/ del paquete kuro (github.com/BiomeMakers/kuro), con los scripts que reconstruyen cada fuente no redistribuible.

## Declaración de asistencia

El procesamiento del corpus, las pruebas y la redacción de este texto se produjeron con la asistencia de un modelo de lenguaje (Claude, Anthropic) bajo la dirección del autor, que es responsable de todas las afirmaciones aquí hechas. Dos etapas del procedimiento usan el modelo en el bucle; sus tasas de invención se declaran en la sección 5.

## Referencias

Davis, B. 2024. Minoan Linear A: the state of the question. AURA Supplement 15.

Godart, L. 1984. Du linéaire A au linéaire B. En Aux origines de l'hellénisme: la Crète et la Grèce. Hommage à Henri van Effenterre. París, 121-128.

Godart, L. y J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A (GORILA), 5 vols. París: École française d'Athènes.

Hallager, E. 1996. The Minoan Roundel and Other Sealed Documents in the Neopalatial Linear A Administration. Aegaeum 14, 2 vols. Lieja.

Salgarella, E. 2019. Non-administrative Linear A? SMEA NS 5.

Schoep, I. 2002. The Administration of Neopalatial Crete. Minos Suppl. 17. Salamanca.

Ventris, M. y J. Chadwick 1973. Documents in Mycenaean Greek, 2ª ed. Cambridge.

Younger, J. G. 2024. Linear A Texts and Inscriptions in Phonetic Transcription (en línea).

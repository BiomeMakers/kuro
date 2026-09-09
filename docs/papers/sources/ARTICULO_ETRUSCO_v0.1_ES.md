# Función sin significado: un clasificador distribucional para el vocabulario no glosado del etrusco

**Alberto Acedo**
Biome Makers Inc. Borrador preliminar v0.1, 6 de septiembre de 2026. Trabajo en curso: pendiente de la edición de referencia (Rix, Etruskische Texte, o el ETP completo) en forma tabulada.

## Resumen

El etrusco se lee y se entiende a medias: unas mil palabras tienen significado establecido y el resto del vocabulario, en su mayoría onomástico, no. Este trabajo pregunta qué puede decirse de una palabra etrusca no glosada sin proponerle significado: si es nombre propio, sustantivo, verbo o partícula. Un clasificador entrenado sobre 374 palabras con categoría conocida (léxico ETP más el vocabulario nuclear del campo), con rasgos de posición en la frase, vecinos de clase conocida, sufijos y posición en la fórmula onomástica, alcanza un acierto de 0,70 en validación cruzada frente a 0,26 con las etiquetas barajadas, con recuperación pareja por clase (nombre 0,78, sustantivo 0,54, verbo 0,67, partícula 0,83). Aplicado al vocabulario no glosado, el clasificador recupera sin conocerlas las categorías de palabras que el campo sí conoce y que el fichero de trabajo omitía (teke "colocó" como verbo con 0,98; ein "no" como partícula; suθi "tumba" y mlaχ como sustantivos; los pasados en -ke), y falla sistemáticamente en los participios en -u (mulu, lupu), lo que identifica el rasgo que falta. Entre las palabras desconocidas para el campo con frecuencia igual o superior a tres, nueve no son nombres, y una de ellas, θapikun (Populonia), reúne dos de las tres condiciones exigidas para una propuesta léxica: distribución de predicado tras la partícula relativa inpa y un derivado en la misma inscripción (θapintaś). El trabajo no propone lecturas; ofrece una lista ordenada de candidatos con su función y el criterio para cerrarlos.

**Palabras clave:** etrusco, clasificación funcional, análisis distribucional, modelos nulos, onomástica, Tabula Cortonensis, Cippus Perusinus.

## 1. Estado de la cuestión

La lectura del etrusco es completa y su comprensión, parcial: el vocabulario con significado establecido ronda las mil entradas (Bonfante y Bonfante 2002; Wallace 2008; ETP), y de los textos, la inmensa mayoría son inscripciones funerarias breves cuyo contenido es onomástico. Los textos largos (Liber Linteus, Tabula Capuana, Tabula Cortonensis, Cippus Perusinus) contienen el vocabulario no onomástico que el campo discute, y es allí donde los editores marcan sus dudas. La pregunta que aquí se plantea no es qué significan esas palabras, sino qué clase de palabra son, que es una cuestión decidible por distribución.

## 2. Datos y método

Corpus Larth (Vico 2023): 7.139 registros con ciudad, fecha y traducción cuando la hay, del que se apartan 26 textos umbros (Tablas Iguvinas) detectados por vocabulario; léxico ETP_POS (Wallace y colaboradores) con 1.122 entradas y categoría gramatical. Normalización ortográfica (th → θ, ch → χ, ph → φ, ś → σ, c y q → k), que sube de 316 a 349 las palabras conocidas presentes en los textos. Etiquetas: nombre propio, sustantivo o adjetivo, verbo, partícula. Rasgos: posición inicial y final en la inscripción, inscripción de una sola palabra, vecinos por clase conocida, sufijos (-s, -l, -si, -ke, -χe, -θ, -al, -as, -ia, -u), frecuencia, dispersión por ciudad, y posición contigua a un praenomen conocido. Validación cruzada de cinco pliegues y nulo de etiquetas barajadas.

## 3. Resultados

### 3.1 El clasificador aprende la función
Acierto 0,70 (0,26 con etiquetas barajadas); recall por clase 0,78 (nombre), 0,54 (sustantivo), 0,67 (verbo), 0,83 (partícula). Los rasgos de mayor peso son la posición en la fórmula onomástica y los sufijos verbales en -ke/-χe.

### 3.2 Validación involuntaria sobre palabras conocidas
El fichero de trabajo omite palabras corrientes, de modo que aparecen como "desconocidas" términos cuyo significado el campo sí tiene. El clasificador, sin saberlo, acierta en ocho de diez comprobables: teke (verbo, 0,98), larke y fulnike (verbos, pasados en -ke), ein (partícula, 0,75), θui (partícula), suθi y zilaθ (sustantivos), mlaχ (sustantivo o adjetivo); falla en mulu "dio" y lupu "murió", participios en -u, cuyo sufijo no figuraba entre los rasgos. Esa es la corrección más inmediata del modelo.

### 3.3 Los candidatos
De 154 palabras desconocidas para el campo con frecuencia ≥ 3, nueve no son nombres. Tres merecen examen: θapikun (Populonia, Po 4.4), en posición de predicado tras la partícula relativa inpa y con un derivado en la misma inscripción, θapintaś, lo que satisface dos de las tres condiciones del procedimiento; fanu (Cippus Perusinus), entre la partícula eθ "así" y el sujeto lautn "familia", con la comparación clásica con el latín fanum "santuario" pero sin derivado y sin bilingüe que la contraste, una condición y media; y aknanasa, que el examen retira: es el participio acnanasa "habiendo engendrado" de la inscripción de los Alethnas, con traducción en el propio corpus, y su clasificación como sustantivo es un error del modelo por el mismo motivo que mulu y lupu.

### 3.4 Dónde están las dudas de los editores
El minado de las traducciones localiza las dudas de contenido en los textos largos: θelu y parχ (Alethnas), munis (dedicatoria a Hercle), θlu, θup y sela (Volterra), iluku y cuieskhu (Tabula Capuana). Cada una tiene entre una y tres atestaciones en el corpus disponible, insuficientes para el procedimiento; son el objetivo natural cuando se disponga de la edición completa.

## 4. Discusión y límites

El resultado es de método: en un corpus con vocabulario glosado suficiente, la función de una palabra no glosada es predecible por distribución con acierto medible, y el propio modelo señala qué rasgo morfológico le falta cuando falla. El límite es de datos: el corpus abierto es ruidoso (OCR, umbro, glosas de nombres en lugar de traducciones) y la edición de referencia no está disponible en forma tabulada. Con ella, el mismo procedimiento se aplicaría a las dudas de los editores en los textos largos, que es donde el vocabulario no onomástico del etrusco espera.

## Datos

Larth (Vico 2023), ETP (Wallace y colaboradores). Scripts: paquete kuro (Acedo 2026d).

## Declaración de asistencia

El procesamiento del corpus, el entrenamiento del clasificador y el primer borrador de este texto se produjeron con la asistencia de un modelo de lenguaje (Claude, Anthropic) bajo la dirección del autor, responsable de todas las afirmaciones.

## Referencias

Acedo, A. 2026c. Qué puede afirmarse de un corpus de siete mil signos. Borrador.
Acedo, A. 2026d. kuro. Software.
Agostiniani, L. y F. Nicosia 2000. Tabula Cortonensis. Roma.
Bonfante, G. y L. Bonfante 2002. The Etruscan Language: An Introduction. 2ª ed. Manchester.
Rix, H. 1991. Etruskische Texte. Editio minor. Tübingen.
Vico, G. 2023. Larth: Etruscan NLP corpus. https://github.com/GianlucaVico/Larth-Etruscan-NLP
Wallace, R. E. 2008. Zikh Rasna: A Manual of the Etruscan Language and Inscriptions. Ann Arbor.

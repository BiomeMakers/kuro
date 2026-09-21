# Lo publicado en desciframiento y lectura de lenguas antiguas, 2022-2026, y qué nos sirve

Revisión hecha el 12 de septiembre de 2026.

## 1. Lo que nos afecta directamente: una reclamación sobre el Lineal A, de hace tres meses

**Tom Di Mino**, ingeniero de IA sin formación académica en lenguas antiguas (Hudson Valley, Nueva York), anunció en **junio de 2026** haber descifrado el Lineal A. Su tesis: el minoico es una lengua **semítica extinta**, antecesora del hebreo bíblico, el arameo y el árabe.

**Su pivote es exactamente nuestro objeto de estudio: la fórmula de libación.** Propone que el signo *301, que no tiene valor fonético asignado, vale *na*; con eso, la secuencia de la fórmula contiene la raíz semítica n-w-y, *nawaya*, "morar, habitar", atestiguada en hebreo y acadio. De ahí deriva el resto.

Cifras declaradas: en junio, 40 signos con valor propuesto (13 sin valor previo), léxico de 408 palabras y un borrador de nueve páginas, *Ya Diktu: Grammar of the Minoan Peak Sanctuary Libation Formula*. En agosto, ampliado a 42 signos, 508 entradas y 443 traducciones, 41 páginas. Usó Python con Claude Code sobre GORILA y SigLA, **las mismas dos fuentes que nosotros**. Está en revisión en Rutgers y Cambridge. La metodología completa no es pública y nadie ha replicado las asignaciones.

**Precedente:** Cyrus Gordon propuso el vínculo semítico en 1957 (*Antiquity*) y el campo no lo aceptó.

**Qué tenemos nosotros que tenga que ver con esto**, y hay que decirlo con cuidado porque su trabajo está en revisión y puede ser correcto:
- El ugarítico (semítico) está entre las trece candidatas probadas. Bajo los valores del Lineal B, su distancia fonotáctica al minoico no se distingue de la del minoico barajado.
- La búsqueda anclada de valores optimiza los valores de los signos no anclados, que incluyen *301, con recocido simulado y control. **Ninguna candidata semítica baja por debajo de su control** (máximo z de toda la tabla: 1,7, y es del luvita, no del semítico).
- Sobre la misma fórmula medimos que los rellenos son hapax en 32 de 32, que A-TA-I-*301-WA-JA abre en 8 de 8, que U-NA-KA-NA-SI es el término de la ofrenda por el logograma que lo sigue en SY Za 2, y que JA-SA-SA-RA-ME nunca lleva logograma en trece apariciones.
- Y que la arquitectura de la fórmula es la de la fórmula de ofrenda egipcia, medida contra 1.357 ejemplares reales.

**Lo que esto NO demuestra**, y el artículo debe decirlo: nuestra prueba mide la fonotaxis del corpus entero, no si un texto concreto admite una lectura. Una fórmula votiva podría contener préstamos semíticos sin que la lengua lo sea (es lo que hemos medido con las palabras viajeras), y una lectura correcta de un texto no obliga a que el corpus se parezca a esa lengua. Lo que sí se puede afirmar: **bajo ninguna asignación de valores compatible con los topónimos compartidos con el Lineal B, el corpus del Lineal A se parece a una lengua semítica más de lo que se le parece un corpus sin lengua.**

## 2. Restauración de texto: el listón está alto y no es nuestro problema
**Aeneas** (Assael, Sommerschield y otros, *Nature*, julio de 2025; DeepMind con Nottingham, Oxford, Warwick y AUEB) restaura, data y localiza inscripciones latinas, y además devuelve paralelos de entre 150.000 inscripciones. Sucede a **Ithaca** (2022), que hacía lo propio con el griego. Código y modelo son públicos (github.com/google-deepmind/predictingthepast).

Nos sirve como referencia de evaluación: nuestra prueba de predicción sobre la fórmula se evalúa como se evalúa la restauración textual en ese campo, y el techo del 14% se lee contra ese listón. No nos sirve como herramienta: Aeneas necesita una lengua conocida y decenas de miles de ejemplos.

## 3. Leer sin descifrar: el problema puede ser físico, no lingüístico
El **Vesuvius Challenge** lee los rollos carbonizados de Herculano sin abrirlos, con tomografía y aprendizaje automático. En 2023 se recuperaron 2.000 caracteres; **en 2026, PHerc. 1667 fue el primer rollo desenrollado virtualmente y leído de principio a fin**. El gran premio de 2027 (un millón de dólares) es leer varios rollos completos.

La lección para nosotros es la que ya está escrita en todos nuestros artículos, con un ejemplo caro: cuando el problema es de datos y no de método, lo resuelve una tecnología de adquisición, no un algoritmo de análisis. Su equivalente para el Lineal A es la excavación.

## 4. Pocos datos y una bilingüe mínima: cuánta hace falta
**NüshuRescue** (Yang, Ma y Vosoughi, Dartmouth, 2024-2025): marco con un modelo de lenguaje para escrituras con muy pocos datos digitales, aplicado al nüshu, la escritura de mujeres de Hunan. Partió de **35 traducciones verificadas chino-nüshu** más una descripción de la estructura de la escritura, y con eso tradujo frases nuevas.

No es desciframiento (la lengua subyacente se conoce y hay bilingüe), pero da la única cifra empírica reciente sobre **cuánta bilingüe hace falta**: del orden de unas decenas de pares verificados, con la lengua conocida. Es la referencia para la frase de nuestros artículos donde decimos qué hallazgo decidiría entre lecturas, que hasta ahora decía "una bilingüe" sin cuantificar. Y su otra observación coincide con lo que medimos en el hipotetizador: el prior estructural compensa la falta de datos.

## 5. El estado del arte en emparejamiento de cognados
**Tamburini 2025** (*Frontiers in AI* 8:1581129), ya incorporado: optimización combinatoria con recocido simulado acoplado, k-permutaciones, comodines para signos ilegibles y conocimiento parcial fijado. Supera a NeuroDecipher en seis de siete bancos de prueba, y documenta que los resultados publicados de NeuroDecipher no se reproducen sin reinicios múltiples.

**Evaluación de modelos de lenguaje sobre escrituras raras** (arXiv 2501.17785, enero de 2025): mide qué hacen los modelos multimodales con escrituras poco expuestas. Confirma lo que medimos por nuestra cuenta: útiles como enrutadores, no como descifradores.

## 6. Lo que no ha pasado
No ha habido ningún desciframiento consumado y aceptado desde el elamita lineal (Desset y otros, 2022). El Indo, el rongorongo, el disco de Festos y el jeroglífico cretense siguen sin leer. El resumen de 2025 del campo lo dice sin rodeos: no hay ningún caso confirmado de una IA que descifre por sí sola una lengua completamente desconocida sin guía humana ni contexto lingüístico previo.

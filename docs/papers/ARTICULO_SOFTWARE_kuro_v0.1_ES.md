# kuro (KU-RO, "total"): modelos nulos, calibración y confusores para corpus epigráficos pequeños

**Alberto Acedo**, Biome Makers Inc.
Borrador v0.1, 6 de septiembre de 2026. Destino: Journal of Open Source Software (artículo corto más revisión del repositorio). Versión española del texto inglés.

## Resumen

kuro es un paquete de Python para el análisis estadístico de corpus epigráficos demasiado pequeños, fragmentarios o mal entendidos como para leerse: Lineal A, proto-elamita, proto-cuneiforme, ibérico, etrusco. No descifra. Responde, con un nulo de permutación detrás de cada afirmación, qué puede sostener un corpus y qué no: si dos grupos de documentos difieren en registro por encima del suelo de muestreo, si un afijo forma pares raíz/derivado por encima del azar, si las cadenas de signos coocurren o se excluyen frente a un nulo de márgenes fijos, si un vocabulario está compartimentado por tipo de documento o por mano de escriba, si los totales suman, y si las coincidencias de forma con un léxico externo superan lo que producen las sílabas barajadas. También mina los comentarios de los expertos en busca de expresiones de duda, para dirigir los tests a donde los especialistas se detuvieron.

## Necesidad

El trabajo estadístico sobre escrituras no descifradas ha producido lecturas por coincidencia de sonido que cualquier léxico amplio suministra (Duhoux 1989; Nepal y Perono Cacciafoco 2024) y, en el extremo opuesto, la idea de que nada en esos corpus es contrastable (Petrakis y Steele 2025). Lo que falta es una caja de herramientas común en la que cada afirmación distribucional vaya unida al modelo nulo que conserva lo que la afirmación no explica, y en la que los instrumentos se calibren en corpus con respuesta conocida antes de aplicarse a los desconocidos. kuro ofrece cargadores para los formatos que la comunidad ya usa (el JSON del LinearA Explorer, las exportaciones ATF de CDLI, las tablas de signos tipo SigLA, tablas CSV de textos) y los tests, de modo que un epigrafista pueda correr un análisis calibrado en unas líneas y publicar sus negativos con número.

## Funcionalidad

- Modelo de corpus: documentos con sitio, soporte, fecha, mano y tokens en orden de lectura.
- Modelos nulos: barajado de etiquetas, barajado dentro de estrato, aleatorización curveball de márgenes fijos (Strona et al. 2014), y barajado de sílabas con longitudes conservadas.
- Tests: distancia de perfil (Jensen-Shannon) con suelo de muestreo y nulo a nivel de documento; pares raíz/derivado por afijo; marco posicional de las cadenas largas; coocurrencia y coexclusión de metacomunidad; monopolios por tipo de documento; análisis de confusor (mano frente a tipo) con permutación dentro de estrato; aritmética de totales con fracciones; cribado de forma contra un catálogo externo; tasa de hapax por longitud de cadena.
- Minado de dudas sobre comentarios.

## Validación

El paquete reproduce, en etrusco, el genitivo ante clan, la cronología de la síncopa y la geografía de las sibilantes; en eteochipriota frente a griego chipriota, la separación por sílabas finales; en proto-elamita, los sistemas numerales por clase de objeto de Dahl, la cabecera institucional y la partición nombres/mercancías; en Uruk frente a Susa, la herencia del sistema sexagesimal, la adaptación del de capacidad y la invención del decimal; en ibérico, los formantes onomásticos de Untermann y las isoglosas del S56 meridional y del -ḿi nororiental. Su uso en el Lineal A se describe en Acedo (2026a, 2026b, 2026c).

Más allá de reproducir resultados publicados, tres comprobaciones cuantifican lo que el paquete aporta en una tarea con respuesta conocida (clasificar un grupo de signos del Lineal B como nombre de persona o término, solo por distribución, sobre 64 palabras cuyo significado el campo tiene establecido). Un decisor de reglas escrito a partir de la bibliografía alcanza 0,63 de acierto balanceado; el modelo distribucional, 0,77; y seguir al modelo donde está seguro y a las reglas en el resto, 0,80 de acierto simple. Una curva de aprendizaje muestra que veinte palabras anotadas bastan para tres aciertos de cada cuatro (0,74), con mejora lenta después. Y en la tarea que un investigador hace de verdad, priorizar qué revisar, ordenar por la probabilidad del modelo encuentra la mitad de los términos tras 22 revisiones en lugar de 32 al azar, alrededor de un tercio menos de trabajo. Las tres se informan con sus límites: se hacen sobre el Lineal B, las reglas son nuestras y el conjunto etiquetado es pequeño. Un estudio con expertos humanos, diseñado según Assael et al. (2022), está preparado y se añadirá cuando haya participantes.

## Agradecimientos

Datos: LinearA Explorer (R. Hogan), SigLA (E. Salgarella y S. Castellan), CDLI, Hesperia (vía Luo et al. 2021), Larth (G. Vico), ETP (R. Wallace y colaboradores).

## Referencias

(Las del texto inglés.)

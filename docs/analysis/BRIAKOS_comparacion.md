# Briakos frente a nosotros: la comparación honesta (7 de septiembre de 2026)

Nikolaos Briakos, *An Undeciphered Script in the Age of AI: A Corpus-Constrained Computational Analysis of Linear A*, tesis de máster en Informática, Universidad del Pireo, mayo de 2026. Dirigida por Ioannis Venetis, con tribunal de tres.

## Lo que coincide, y es mucho

| resultado | él | nosotros |
|---|---|---|
| divergencia entre registros | JSD 0,0944, permutación p = 0,018 | JSD 0,193 con otra medida, p < 0,005 |
| huellas de escriba | 23 escribas con preferencias de bigramas | confusor mano por serie, con interacción medida |
| variación entre yacimientos | d de Cohen 0,623 (Festos frente a Chania) | perfiles por sitio y por soporte |
| detección de la fórmula | algoritmo no supervisado, recupera 5 de 9 elementos sin conocerla | plantilla completa por distribución, con los 32 hapax |
| límite del corpus | umbral útil en unos 10.000 tokens, 7.500 más de los que hay | curva de potencia: la coexclusión aparece a 800 documentos y no a 224 |
| conclusión de fondo | el corpus no da para la asignación fonética | la comparación por sonido no discrimina lenguas |

Dos personas que no se conocen, con métodos distintos, llegando a las mismas conclusiones sobre los mismos datos. Es lo mejor que le puede pasar a un resultado.

## Lo que él hace y nosotros no

**La parte de aprendizaje automático, y la hace bien.** Entrena un transformador pequeño (cuatro capas, 800.000 parámetros) con GPU, mide la caída de pérdida de validación (de 2,82 a 0,65 en cien épocas) y comprueba que reconstruye KU-RO en posiciones enmascaradas. Nosotros no hemos entrenado nada.

**La calibración cuantitativa del límite.** Construye un corpus sintético del Lineal B fiel a las distribuciones publicadas y mide que el emparejamiento por rango de frecuencia acierta el 13% con 2.481 tokens, seis veces el azar pero por debajo del 21% que haría falta. De ahí sale el umbral de 10.000 tokens. Es más preciso que nuestra curva de potencia.

**Y el análisis multimodal, con un resultado que hay que aplaudir:** combina rasgos visuales con incrustaciones distribucionales y encuentra que la aparente separación geográfica es un artefacto de la exposición fotográfica (correlación de 0,990 entre la primera componente visual y el brillo de la imagen). Es el mismo tipo de negativo que nosotros publicamos, y muy bien hallado.

**Y una práctica de rigor que nosotros NO tenemos:** etiqueta cada estadístico según su procedencia (calculado del corpus con hash SHA256 registrado; tomado de la literatura con cita; o meramente ilustrativo). Es mejor que lo nuestro y deberíamos copiarlo.

## Lo que nosotros hacemos y él no

**Los nulos de márgenes fijos.** Él usa permutaciones, pero no aparece el curveball ni ningún nulo que conserve las sumas de filas y columnas. Ese es el nulo que nos hizo retirar la ventana de dos lados; sin él, ese resultado habría quedado publicado como positivo.

**La calibración en corpus reales con respuesta conocida.** La suya es un corpus sintético del Lineal B. La nuestra son cinco corpus reales (etrusco, eteochipriota, proto-elamita, Uruk, ibérico) donde el instrumento tiene que recuperar lo que el campo ya sabe. Son cosas distintas: la suya mide el límite estadístico; la nuestra comprueba que el instrumento ve lo que hay.

**La retirada de resultados propios.** En su tesis no aparecen las expresiones "negative result" ni "withdraw". Nosotros hemos retirado dos índices que ya teníamos escritos y lo hemos publicado con sus números. No es un defecto suyo (una tesis no suele contener el cementerio de su autor), pero es una diferencia de práctica.

**Y sobre todo, el contenido de los documentos.** Su pregunta es "¿puede la inteligencia artificial descifrar el Lineal A?", y la responde con honestidad: todavía no. La nuestra es "¿qué dicen estos documentos y qué puede afirmarse?", y de ahí salen DA-I, \*308, el expediente de aromáticos, la estructura de la receta, la forma del recibo comparada con seis administraciones y el canal minoico medido. Nada de eso está en su tesis, y nada de su tesis contradice lo nuestro.

## La respuesta a la pregunta

Él ha hecho una tesis de máster; nosotros seis días. La diferencia no es de calidad ni de cantidad, sino **de objeto**: él estudia qué puede hacer un método con esta escritura, y nosotros qué dicen estos documentos. Su trabajo es informática aplicada a la epigrafía; el nuestro es epigrafía con instrumentos de otro campo.

Dos cosas conviene decírselas uno en voz alta. La primera: un estudiante solo, con dirección académica y unos meses, alcanzó por su cuenta la mitad de nuestras conclusiones metodológicas. Eso mide lo asequible que es hoy esta clase de análisis y rebaja cualquier tentación de creer que hemos hecho algo excepcional en lo técnico. La segunda: su rigor documental es superior al nuestro y hay que adoptarlo.

Lo que sí es nuestro y no está en ningún sitio: el cruce con las recetas de Assur, con el kyphi, con las Un de Pilos y con la química de Chamalevri; la comparación de la forma del recibo entre seis administraciones; y el expediente de aromáticos leído hasta donde el corpus permite. Eso no lo hace un método: lo hacen las preguntas.

## Consecuencias prácticas
1. Citarlo en el artículo de método, en trabajos previos, diciendo que coincidimos por vías distintas.
2. Incorporar su umbral de 10.000 tokens a nuestra curva de potencia: es mejor dato que el nuestro para esa afirmación.
3. Adoptar su etiquetado de procedencia de los estadísticos.
4. Y escribirle. Es la persona viva que más se parece a lo que hacemos, está empezando, y no tiene ningún motivo para vernos como competencia.

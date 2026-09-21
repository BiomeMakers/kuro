# Las escrituras no descifradas, con sus cifras publicadas (13-sep)

Cifras de las ediciones y de la bibliografía. No hay ninguna estimación propia en esta tabla.

| escritura | signos | corpus (signos) | unidades | ¿rejilla de valores? | fuente |
|---|---|---|---|---|---|
| **Lineal A** | 110 | 7.147 | 552 | **sí**, heredada del Lineal B | GORILA |
| **Elamita lineal**, antes de 2020 | 77 | 1.731 | — | no | OCLEI supl. 2020: 25 inscripciones |
| **Elamita lineal**, hoy | 77 | ~2.000 | — | **sí**, Desset 2022 | Hatamti (Lieja): 45 textos |
| **Chiprominoico** | 155 | 1.378 | 300 | no (8 de 155) | Corazza et al. 2022 |
| **Jeroglífico cretense** | 96 | 1.555 | 581 | no | Olivier 1990: 270 docs, 581 grupos |
| **Disco de Festos** | 45 | 241 | — | no | un solo objeto |
| **Índico** | 417 | ~5.000 inscripciones | — | no | Mahadevan 1977 (386 Parpola, 694 Wells) |
| **Protoelamita** | ~1.200 | ~1.700 tablillas | — | no | Dahl |

Las unidades del chiprominoico se midieron aquí sobre el corpus reconstruido del repositorio público de Corazza y colaboradores: 1.378 signos, 155 tipos, 182 documentos, 300 secuencias distintas de dos o más signos entre divisores, de 3,51 signos de media.

## El coste, que sí se calcula para todas

El coste en bits de especificar una asignación solo necesita el número de signos libres:

| escritura | signos libres | coste en bits |
|---|---|---|
| Disco de Festos | 37 | 206 |
| Elamita lineal (hoy) | 57 | 360 |
| Elamita lineal (2020) | 69 | 435 |
| Jeroglífico cretense | 88 | 582 |
| Lineal A | 94 | 640 |
| Chiprominoico | 147 | 1.072 |
| Índico | 409 | 3.563 |
| Protoelamita | 1.192 | 12.196 |

## Y lo que no se puede calcular, que es la mitad de la cuenta

**Lo que un corpus aporta depende de cuántas veces una lectura acierta por azar, y esa tasa solo se puede medir si ya existe una rejilla de valores.** Sin valores, no hay lecturas que contar; y sin lecturas, el término de aporte no se puede evaluar.

De las ocho escrituras de la tabla, **dos tienen rejilla**: el Lineal A, que hereda la del Lineal B, y el elamita lineal desde 2022. Las otras seis no.

Eso invierte una intuición cómoda. **La cuenta no sirve para decidir si una escritura sin valores se puede descifrar**, porque el dato que hace falta es consecuencia de haber empezado a descifrarla. Sirve para lo contrario: para decir, cuando ya hay una rejilla propuesta, cuánto falta para que la propuesta esté determinada.

## Las dos que tienen los cuatro números

| | coste | aporta | déficit | anclas |
|---|---|---|---|---|
| **Lineal A**, con su tasa medida de 0,738 | 587 | 242 | **345** | 56 |
| **Chiprominoico**, suponiéndole la misma | 1.073 | 131 | **941** | 130 |

La segunda línea es conservadora y hay que leerla como cota inferior: **el chiprominoico, sin rejilla, tendría una tasa de encaje peor que la del Lineal A, no mejor**. Su déficit real es mayor que 941.

Y con eso queda dicho lo que este cálculo puede decir del pariente más cercano del Lineal A: **está casi el triple de lejos**, con siete veces menos texto y cuarenta y cinco signos más. Cualquier proyecto que se proponga leer el chiprominoico por método interno trabaja con una fracción de la información que el Lineal A tiene, y el Lineal A no basta.

## Lo que haría falta para completar la tabla

Para el índico y el protoelamita falta el recuento de unidades, que es extraíble de sus corpus digitales (CDLI para el protoelamita; los corpus de Mahadevan y Wells para el índico). Para el jeroglífico cretense, el CHIC de Olivier y Godart da los 581 grupos y habría que contarlos por separado.

Ninguna de las tres daría un veredicto de descifrabilidad, por la razón del apartado anterior. Darían el coste, que ya está arriba, y la escala del corpus. **Eso es todo lo que se puede saber antes de tener valores, y decirlo es parte del resultado.**

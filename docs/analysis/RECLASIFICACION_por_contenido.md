# Reclasificación del corpus por contenido, no por soporte (7 de septiembre de 2026)

El hallazgo de que los vasos de piedra de Zakros son cuentas y no exvotos obliga a comprobar el resto del corpus. Se reclasifican los 1.720 documentos por lo que CONTIENEN y no por el material del que están hechos.

## Criterio
- **VOTIVO**: contiene al menos un ancla de la fórmula de libación (las doce formas conocidas de las cinco anclas).
- **CONTABLE**: dos o más cantidades, o al menos un logograma de mercancía con cantidad.
- **ETIQUETA**: uno o más logogramas sin cantidades (nódulos, rodeles).
- **INDETERMINADO**: ni lo uno ni lo otro (fragmentos, inscripciones de una palabra).

## El resultado

| soporte | contable | votivo | etiqueta | indeterminado |
|---|---|---|---|---|
| Nódulo | 1 | 0 | 810 | 75 |
| Tablilla | 260 | 0 | 52 | 80 |
| Rodel | 3 | 0 | 76 | 72 |
| **Vaso de piedra** | **33** | **15** | 15 | 44 |
| Vasija de arcilla | 3 | 1 | 19 | 51 |
| Objeto de metal | 0 | 1 | 7 | 15 |
| Barra de cuatro caras | 4 | 0 | 1 | 0 |

Dos lecturas de la tabla.

**Primera: el soporte predice bien salvo en un caso.** Nódulos y rodeles son etiquetas, las tablillas son cuentas, y ninguna tablilla del corpus lleva fórmula votiva. Ahí la etiqueta de soporte y el contenido coinciden.

**Segunda, y es la corrección: los vasos de piedra son de todo.** Treinta y tres son cuentas, quince son votivos, quince son etiquetas y cuarenta y cuatro son ilegibles. Es decir, **más del doble de los vasos de piedra son documentos contables que exvotos**, al revés de lo que la clasificación por soporte induce a pensar. Y esos treinta y tres se concentran en Zakros: ZA 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, casi todo el corpus de vasos de ese yacimiento, con hasta doce cantidades en una sola pieza (ZA 10b).

## Consecuencias

1. **Zakros tenía un archivo escrito sobre piedra.** No es una anomalía de una pieza: son treinta y tres documentos contables sobre vasos, en un solo yacimiento. Eso es un hecho arqueológico que la clasificación por material oscurece, y merece comprobarse con la bibliografía (Platon y sus sucesores) porque puede ser conocido y estar mal reflejado en la base de datos.

2. **Cualquier análisis que separe "administración" de "culto" por el soporte está contaminado.** Los nuestros no lo estaban, porque usábamos yacimientos de culto explícitos (Iouktas, Petsofás, Syme, Kophinás) y no el material, pero el criterio queda ahora escrito y el fichero de clasificación acompaña al trabajo (03_lineal_a/datos/clasificacion_por_contenido.json, con la clase de cada uno de los 1.720 documentos).

3. **El corpus votivo real es más pequeño de lo que parece:** quince vasos de piedra, una vasija de arcilla y un objeto de metal con anclas de la fórmula, más las inscripciones que contienen la apertura sin anclas. Diecisiete documentos, no ciento siete. Eso reduce todavía más la potencia de cualquier análisis sobre el vocabulario de culto, y explica por qué tantas de nuestras pruebas sobre la fórmula son indecidibles.

## Lo que aporta al campo
Un fichero con la clase de contenido de cada documento del corpus, obtenido con un criterio explícito y reproducible, que cualquiera puede usar para no repetir el error. Y la observación de que Zakros escribía cuentas en vasos de piedra, que si no está en la bibliografía es un hallazgo y si lo está es una corrección a la base de datos que el campo utiliza.

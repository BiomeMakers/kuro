# La mitad generativa: construida, conectada, corrida y medida (15-sep)

## El error de planteamiento

Este trabajo construyó durante un mes **un instrumento de rechazo**: nulos, análisis de potencia, un protocolo de diez requisitos, una función de descifrabilidad. Todo sirve para decir que no. Es una máquina de arbitrar, no de jugar.

Y la asimetría se notaba: una hipótesis se tumba en diez minutos, y no había **ninguna forma sistemática de producir una**. Las once que cayeron el 14 y el 15 de septiembre se generaron por corazonada, con un juez implacable detrás.

Peor aún: **la mitad generativa estaba construida y nunca se había ejecutado.** El alineador de `kuro/aligner.py`, escrito desde Luo y colaboradores (2021) y validado en el Lineal B, se dio por inútil porque la curva de anclas decía que hace falta más anclaje del que hay. Se midió que no iba a funcionar y no se corrió.

## Primera corrida: el generador desnudo

Corrido sobre el Lineal A con doce anclas y seis léxicos candidatos, **ordenó las lenguas por el tamaño de su vocabulario**: micénico (3.000 palabras, objetivo −28,58), acadio (2.987, −33,06), luvita (2.097, −36,81), hitita (868, −39,72), ugarítico (26, −50,41).

Y el primero era el micénico, **que sabemos que no es la lengua del Lineal A**. El generador reproducía el artefacto que el artículo 02 documenta en el criterio del campo.

## El puente que faltaba

El generador no conocía **nada** de lo medido: ni las 151 lecturas funcionales, ni el perfil vocálico, ni la ausencia de armonía, ni las casillas sintácticas, ni la lista de logogramas, ni las siete sílabas que probablemente no existen.

Se escribió `kuro/measured.py` (cuatro tests) para conectarlos: penaliza sílabas ausentes, distancia al perfil vocálico medido, y armonía vocálica creada. Con él, la mejor asignación **no propone ni una sílaba ausente**.

## Segunda corrida: con restricciones, vocabulario igualado y formato igualado

Con las restricciones puestas y el vocabulario a 2.000, el micénico seguía ganando. La razón resultó ser otro artefacto: **su vocabulario está escrito con el mismo silabario**, de modo que ya venía en la forma que el modelo espera, mientras las demás se silabificaron con una función tosca. No se comparaban lenguas sino formatos.

Pasadas **todas** por la misma función, incluido el micénico:

| lengua | vocab | total |
|---|---|---|
| **hitita** | 868 | **−39,46** |
| acadio | 1.500 | −42,89 |
| micénico | 1.422 | −43,02 |
| luvita | 1.498 | −44,56 |
| hurrita | 1.500 | −44,84 |

El micénico cae al tercer puesto, que es lo que debía pasar. Y el hitita gana **con el vocabulario más pequeño**, que es lo contrario del artefacto de tamaño.

## Y el nulo lo cierra

Contra treinta vocabularios falsos construidos con las sílabas del propio hitita y sus mismas longitudes: media −43,57, desviación 1,56, mejor −40,09. **El hitita real da −41,76: z = +1,16, p = 0,100.**

**No se separa.** El orden anterior no significa nada.

## El segundo intento: la rejilla al modo de Kober

Ventris no buscó la lengua, buscó **la rejilla**: construyó la tabla de consonantes y vocales por distribución interna y solo al final vio que salía griego. Este trabajo nunca lo había intentado.

Medido sobre los 48 signos con ocho o más apariciones, comparando los contextos de cada par:

| pares | parecido medio | nulo | p |
|---|---|---|---|
| **misma consonante** (65) | **0,7150** | 0,6335 | **< 0,0005** |
| misma vocal (235) | 0,6523 | 0,6343 | 0,045 |
| ninguna de las dos (828) | 0,6226 | — | — |

**La estructura de la rejilla está en el corpus**, y la consonante la organiza mucho más que la vocal.

**Pero no alcanza para levantarla.** Agrupados los signos por parecido de contexto en trece grupos, las series consonánticas no emergen: el grupo mayor mezcla erres, eses, tes, enes y emes. Un efecto de 0,715 contra 0,633 se detecta con mil pares y no basta para decidir a qué grupo va cada signo.

## Lo que queda establecido

**La mitad generativa existe, está conectada con lo medido, se ha corrido con nulo, y no discrimina.** Eso ya no es una suposición basada en la curva de anclas: es una medida.

**Y la rejilla es recuperable en principio y no en la práctica**, con este corpus. Kober tenía miles de formas del Lineal B; aquí hay 501 unidades. Es el mismo techo de potencia que el análisis del 14 de septiembre estableció por el lado crítico, ahora confirmado por el generativo.

**El planteamiento no era erróneo: era incompleto.** Faltaba esta corrida, y su resultado es que ambas mitades, la que rechaza y la que propone, dan lo mismo.

# Grambank como selector de candidatas: lo que se puede codificar y lo que acota (10 de septiembre de 2026)

La idea del usuario: en vez de partir de las candidatas que un siglo propuso, **codificar el
minoico en los rasgos tipológicos que sí observamos y dejar que las 2.467 lenguas de Grambank digan
cuáles se parecen.** Selección de candidatas por datos.

Grambank v1.0 (Skirgård y otros 2023, *Science Advances*): 195 rasgos, 2.467 lenguas, CC BY.
Descargado entero desde su repositorio de GitHub.

## 1. Lo que se puede codificar sin leer

De los 195 rasgos, cincuenta y seis tienen nombres que sugieren observabilidad. Leídos uno a uno,
**los que de verdad se pueden codificar sin leer el minoico son tres:**

| rasgo | lo que dice el corpus | código |
|---|---|---|
| GB024, orden numeral-nombre | el número sigue a lo contado 1.020 veces, lo precede 744 | N-Num |
| GB159, reduplicación en nombres | 33 de 782 palabras tienen sílaba repetida (a-sa-sa-ra, di-di, da-da) | sí |
| GB136, orden de constituyentes fijo | la fórmula tiene siete posiciones fijas | sí, en el votivo |

Y un cuarto que Grambank no codifica como rasgo simple: **hay prefijos y sufijos** (I-, A-, JA-;
-ja, -na, -te, -ti, -qe).

**Los otros 192 exigen saber qué es un verbo, un caso, un artículo o un poseedor**, y eso es leer.

## 2. Cuánto acotan tres rasgos

**272 lenguas de 2.330 codificadas coinciden en los tres.** Por familia:

| familia | lenguas |
|---|---|
| austronesio | 87 |
| atlántico-congo | 60 |
| sino-tibetano | 31 |
| afroasiático | 15 |
| trans-neoguineano | 9 |
| ... | |

**No acota.** Tres rasgos binarios dejan más de una de cada nueve lenguas del mundo, y las familias
que dominan son las que dominan Grambank por número. **El afroasiático, que incluye el semítico,
queda con quince, y ninguna anatolia ni tirsénica aparece porque Grambank casi no las tiene**: son
lenguas muertas y la base codifica sobre todo lenguas vivas o bien descritas.

## 3. Lo que esto enseña, y no es que la idea sea mala

**La idea es correcta y el instrumento es el adecuado; lo que falta son rasgos.** Con tres, el
espacio no se estrecha. Con diez o quince, sí lo haría: cada rasgo binario independiente divide el
espacio por dos, y quince lo dividirían por miles.

**Y los rasgos que faltan no son imposibles, son costosos.** Cada uno exige una medida distribucional
que sustituya a la lectura: por ejemplo, GB044 (marca de plural) se podría aproximar buscando si las
palabras que preceden a cantidades mayores que uno llevan una terminación que las que preceden a uno
no llevan. Eso es un análisis por rasgo, y hay quizá diez que se pueden atacar así.

**Y el segundo límite es de Grambank:** las candidatas históricas del minoico (hitita, luvita,
hurrita, etrusco, eteocretense) apenas están codificadas, porque son lenguas muertas. Para que la
selección sirviera habría que **codificarlas nosotros** en los mismos rasgos, lo que es factible
porque sus gramáticas están publicadas, pero es trabajo.

## 4. Lo que queda hecho
Grambank entero en el paquete, tres rasgos del minoico codificados con su medida, y la ruta clara:
**un análisis distribucional por rasgo para llegar a diez o quince, y la codificación manual de las
cinco candidatas muertas.** Es la versión tipológica del mismo obstáculo que la comparación
fonológica: el método está, y falta poner los datos en el mismo formato.


---

## 5. CON LA ACOTACIÓN ESPACIAL, que propuso el usuario

Filtradas las 272 por geografía (Mediterráneo, Anatolia, Oriente Próximo, Cáucaso: latitud 20-50,
longitud −10 a 60), **quedan dos: sumerio y abjasio.**

Y antes de leer eso, lo que Grambank tiene de la zona y cómo puntúa:

| lengua | familia | GB024 numeral | GB159 redupl. | GB136 orden fijo | coincide |
|---|---|---|---|---|---|
| **sumerio** | aislada | N-Num | sí | sí | **3/3** |
| **abjasio** | abjaso-adigué | ambos | sí | sí | **3/3** |
| hebreo antiguo | semítico | ambos | sí | ? | 2/3 |
| fenicio | semítico | ambos | no | sí | 2/3 |
| kabardiano | abjaso-adigué | ambos | no | sí | 2/3 |
| griego antiguo | indoeuropeo | ambos | no | no | 1/3 |
| hurrita | hurro-urartiano | Num-N | ? | sí | 1/3 |
| latín, checheno, lezguiano | | | | | 1/3 |
| **acadio** | semítico | Num-N | ? | no | **0/3** |
| **luvita jeroglífico** | anatolio | Num-N | no | no | **0/3** |
| ugarítico | semítico | Num-N | ? | no | 0/3 |
| **etrusco** | | ? | ? | ? | sin codificar |
| hitita, elamita, hático, licio, lidio, cario, eblaíta | | | | | **no están** |

## 6. Lo que se puede decir y lo que no

**Lo que se puede decir con tres rasgos, y es más de lo que esperaba:**

- **El luvita jeroglífico puntúa 0 de 3.** La candidata anatolia clásica, la de Palmer y Finkelberg,
  no coincide en ninguno de los tres rasgos observables. Su numeral precede al nombre y el minoico
  lo sigue.
- **El acadio y el ugarítico, 0 de 3.** El semítico oriental y occidental cuneiforme tampoco.
- **El griego antiguo, 1 de 3**, coherente con nuestra distancia de 0,104.
- **Los que coinciden en los tres son el sumerio y el abjasio.** Y en 2 de 3, el hebreo antiguo, el
  fenicio y el kabardiano.

**Lo que no se puede decir:** que el minoico sea pariente del sumerio o del abjasio. Tres rasgos
binarios son tres bits, y con tres bits cualquier lengua tiene una probabilidad de 1/8 de coincidir
por azar. **Que dos coincidan entre dieciocho de la zona es exactamente lo que el azar daría** (18/8
= 2,25). Lo que separa a las que puntúan 0 de las que puntúan 3 es real, pero débil.

**Y hay un sesgo declarable:** hitita, elamita, hático y las anatolias menores **no están en
Grambank**. No puntúan 0; no puntúan nada. Y el etrusco está pero sin codificar en estos tres.

## 7. Lo que esto vale

**La dirección del resultado es informativa aunque su fuerza no lo sea.** Las candidatas
indoeuropeas y semíticas cuneiformes puntúan bajo en los tres rasgos que el corpus permite ver; las
aisladas y caucásicas puntúan alto. Eso es coherente con la hipótesis de sustrato no indoeuropeo, y
es coherente también con que el abjasio aparezca: el noroeste caucásico se ha propuesto varias veces
como pariente del sustrato pregriego, aunque nunca con evidencia.

**Y da el orden de trabajo:** cada rasgo nuevo que se codifique en el minoico multiplica por dos la
resolución. Con diez, las dieciocho lenguas de la zona quedarían separadas de verdad. Y hay que
codificar hitita, elamita y etrusco a mano, porque sin ellas la comparación está sesgada hacia lo que
Grambank tiene.

**Y una pieza encaja sola:** el sumerio es una de las cuatro lenguas que bajamos hoy de CDLI, con
4,6 millones de palabras. Es la candidata con más corpus y la que mejor puntúa en lo poco que
podemos medir. Cuando pase por el formato común, es la primera que hay que comparar.

## 5. Segundo intento (10-sep, tarde): seis rasgos, luego cinco

**Añadidos:** GB333 decimal (sí: unidades, decenas, centenas y millares en el corpus), GB334 quinario (no), GB335 vigesimal (no). Los tres se leen directamente del sistema numeral.

**Probado y no codificable:** GB044 (plural morfológico). Prueba: entradas silábicas con cantidad 1 (149) frente a mayor que 1 (327). Reduplicación 1,3% frente a 1,5%: nada. Distribución de la última sílaba: distancia 0,356 contra 0,306 en el nulo (p=0,052), pero el exceso es -RO, que son KU-RO y KI-RO (los totales, siempre con cifras grandes): confusor de formato, no plural. No se codifica.

**Retirado:** GB024 (orden nombre-numeral). En el Lineal B, que escribe griego (numeral antes del nombre en la lengua), las tablillas ponen igualmente la palabra y luego la cifra. Lo medido es la convención contable del escriba, no la sintaxis. Con él, 103 lenguas de 1.531 coincidían en 6/6, ninguna mediterránea; sin él:

**Cinco rasgos (GB136, GB159, GB333, GB334, GB335): 187 de 1.064 lenguas coinciden en todos (18%).** Austronesio 77, sino-tibetano 28, atlántico-congo 26, afroasiático 15. Candidatas: hurrita 4 de 4 codificados (GB159 sin codificar), abjasio 4 de 5 (vigesimal), sumerio 3 de 5 (quinario y vigesimal por el sexagesimal), griego antiguo 3 de 5, acadio 3 de 4, etrusco sin codificar. Hitita, luvita, elamita y hático no están en Grambank.

**Veredicto:** con un corpus contable, los rasgos observables sin leer son cinco, y cinco no seleccionan. Los rasgos que sí seleccionarían (orden de constituyentes en la oración, marcas verbales, caso, posesión) exigen texto corrido, y el único texto corrido del Lineal A es la fórmula votiva, que ya dio el que podía dar (orden fijo). Codificar a mano las candidatas muertas no cambia esto: cinco rasgos las dejan a todas en 3-4 de 5 junto a un quinto de las lenguas del mundo. La vía queda abierta en principio y cerrada en la práctica hasta que haya más texto corrido o una lectura.

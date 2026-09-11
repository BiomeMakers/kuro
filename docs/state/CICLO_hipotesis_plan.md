# El ciclo de hipótesis: qué hemos dicho, qué falta, y cómo construirlo

9 de septiembre de 2026. Nace de la conversación sobre la noticia del enjambre de agentes de OpenAI
y de la pregunta de si eso abre una perspectiva nueva para el Lineal A.

---

## PARTE 1. LO QUE SE DIJO, ORDENADO

### 1.1 Por qué el enjambre no transfiere tal cual
El enjambre resolvió un problema matemático porque **en matemáticas existe un verificador**: una
demostración correcta se comprueba mecánicamente, así que se pueden generar millones de caminos y
dejar que el juez decida. En el Lineal A no hay verificador: si un modelo propone que KU-NI-SU es la
escanda, nada dice sí o no. Es la razón de que un siglo de propuestas no se haya podido decidir, y
está medida en nuestro propio trabajo: el cribado por sonido produce **383 falsos positivos** en el
Lineal B, donde sabemos la respuesta.

### 1.2 Pero sí hay un juez, aunque no sea el de las matemáticas
El nulo, el control de confusor, la comprobación bibliográfica y la condición de refutación no dicen
si algo es verdad, pero **dicen si algo se sostiene**. Eso basta para filtrar mil candidatos a diez.

### 1.3 Dónde está el cuello de botella, medido con lo de hoy
No en generar hipótesis. Hoy generamos cinco en veinte minutos y tardamos horas en descartarlas:

| hipótesis | tiempo hasta el descarte | qué la mató |
|---|---|---|
| cuatro variedades de cereal | 20 minutos | el Lexicon de Younger |
| campos con fonología distinta | 1 hora | el control de escriba |
| los afijos cambian el comportamiento | 1 sesión | el nulo y la corrección múltiple |

**El coste está en el descarte.** Por eso el ciclo, no la generación, es lo que hay que
industrializar.

### 1.4 El género acota más que cualquier método (aportación del usuario)
Un recibo admite muy poco: quién entrega, quién recibe, qué, cuánto, un total. No caben verbos
abstractos ni sintaxis compleja. **Y esa acotación ya está medida por nosotros**, dispersa en noventa
y siete análisis: las personas no llevan fracción; los aromáticos sí; el 47% de las series economizan
la mención del producto; ciertos signos son locales de un yacimiento; el orden de mercancías es fijo
en cuatro de cuatro tablillas.

Cada una de esas medidas es una restricción sobre lo que una unidad puede significar. **Aplicadas
juntas, muchas unidades quedarían con una sola categoría posible.**

### 1.5 La franja intermedia es donde se puede medir (aportación del usuario)
Lo frecuente está gramaticalizado y aparece con todo, de modo que no discrimina. Lo raro es hapax:
596 unidades aparecen una sola vez y no tienen distribución. **La franja de tres a quince
apariciones es la única con casos suficientes y especificidad suficiente**, y es donde está todo lo
que hemos encontrado (\*305 con doce, \*308 con doce, KI-RE-TA-NA con cuatro).

### 1.6 Coocurrencia de distintos órdenes (aportación del usuario)
Hasta ahora hemos medido solo el orden cero, estar en el mismo documento. Faltan:

- **orden 1, adyacencia**: ir pegados, que es lo que reveló el principio de continuidad;
- **orden 2, separación fija**: estar siempre a la misma distancia, que delataría una plantilla;
- **coexclusión**: pares frecuentes que nunca coinciden, que marca categorías incompatibles y que
  medimos para palabras (sin potencia) pero no para logogramas, que son más frecuentes.

### 1.7 Creatividad y filtro van juntos, en ese orden
El filtro sin ocurrencia produce una tabla que no dice nada. La ocurrencia sin filtro produce lo que
el campo lleva un siglo produciendo. Las dos mejores cosas del proyecto (el expediente de aromáticos,
la comparación con Assur por lo que **no** dicen) nacieron de una ocurrencia, no de un cálculo.

---

## PARTE 2. EL PLAN, POR PUNTOS

### Fase 0. Lo que ya existe y no hay que construir
El índice de referencia (`kuro.Reference`), el diccionario con evidencia tipada y fechada
(`kuro.Dictionary`), el manifiesto con las retiradas y el prior art, los diez instrumentos de medida,
los cinco corpus de calibración, y 39 tests.

### Fase 1. El objeto Hipótesis
Una clase que atraviese el ciclo entero y deje registro en cada paso.

**Nace con dos campos obligatorios**: la afirmación y **qué la refutaría**. Sin el segundo no se
construye; es el tercer requisito del protocolo hecho código.

**Pasos que ejecuta sola:**
1. consulta el índice de referencia y **se detiene si está publicada**, informando de dónde;
2. elige el nulo según el tipo de afirmación (distribucional, aritmética, posicional, de ausencia);
3. **aplica los confusores que le tocan por tipo**: escriba para afirmaciones sobre vocabulario,
   captura para las que vienen de imagen, disponibilidad del instrumento para las de ausencia,
   soporte y yacimiento para las de distribución;
4. corrige por el número de pruebas de su familia;
5. y se archiva: al diccionario si sobrevive, al manifiesto como retirada si no.

**Control de la fase:** correrla sobre las tres hipótesis de hoy y comprobar que **las tres mueren en
el paso donde murieron a mano**, y por la misma razón. Si una sobrevive, el ciclo es más débil que
nosotros y no sirve.

### Fase 2. Las restricciones del género
Extraer de los noventa y siete análisis las reglas ya medidas, cada una con su fuente, su cifra y su
tasa de excepción conocida. Formuladas siempre como **eliminación de categorías**, nunca como
asignación: "no puede ser una persona", no "es una mercancía".

**Control de la fase, y es el que decide si vale:** aplicarlas a las unidades cuya categoría ya
conocemos (KU-RO, VIR, los logogramas heredados, los términos de transacción de Schoep). **Si el
sistema no recupera lo que sabemos, no vale para lo que no sabemos.** Se mide como recuperación y
como falsos positivos, y se publica esa tasa junto a cualquier resultado que produzca.

### Fase 3. Los órdenes de coocurrencia
Implementar adyacencia, separación fija y coexclusión de logogramas, cada uno con su nulo propio.

**Control de la fase:** cada orden debe recuperar en el Lineal B lo que allí se sabe (que los
calificadores van pegados al logograma, que las fórmulas tienen separación fija). Un orden que no
recupere lo conocido en el corpus conocido no se aplica al desconocido.

### Fase 4. Las lenguas como medida del error
Cada corpus con respuesta conocida no es un dato más: **es una medida de la tasa de error del
instrumento**. Con cinco sabemos que recupera el genitivo etrusco, la clasificación proto-elamita y
las fórmulas ibéricas. Cada corpus nuevo estrecha el intervalo.

El objetivo es poder escribir, junto a cada resultado: "sale p = 0,01, **y en corpus con respuesta
conocida este instrumento se equivoca el N% de las veces**". Eso es lo que ninguna propuesta de
lectura del campo puede decir hoy.

**Candidatos a sexto corpus:** los cifrados del proyecto Descrypt, que son un caso límite que ninguno
de los cinco cubre (lengua conocida, longitud conocida, respuesta verificable).

### Fase 5. La capa de iteración sobre lo que sobrevive
Y aquí está lo que faltaba en lo dicho hasta ahora.

**Una hipótesis que sobrevive no es un resultado: es una restricción nueva.** Si se establece que
\*305 cuenta personas, eso restringe todo documento donde aparezca, y por tanto **cambia el espacio
de las demás unidades de esos documentos**.

De modo que el ciclo no termina en el archivo: **cada supervivencia dispara una segunda vuelta** sobre
las unidades que comparten documento con ella, ahora con una restricción más. Eso es lo que convierte
un filtro en un sistema que aprende.

**Y tiene un peligro que hay que controlar desde el diseño:** si la hipótesis A se usa para restringir
la B, y luego la B para reforzar la A, se construye un castillo de naipes. **Regla:** una hipótesis
solo puede usar como restricción a otra si esa otra sobrevivió **sin usarla a ella**. El diccionario
ya registra la evidencia con su procedencia, así que la dependencia es rastreable y se puede prohibir
por código.

**Control de la fase:** un test que falle si existe un ciclo de dependencias entre hipótesis.

---

## PARTE 3. EL ORDEN, Y POR QUÉ

| fase | qué da | coste |
|---|---|---|
| 1. objeto Hipótesis | baja el coste del descarte de horas a segundos | alto |
| 2. restricciones del género | reduce el espacio de las 752 unidades sin asignar | medio |
| 3. órdenes de coocurrencia | tres medidas nuevas que nadie ha aplicado aquí | medio |
| 4. corpus como tasa de error | convierte cada p en un p con error conocido | bajo por corpus |
| 5. capa de iteración | convierte el filtro en sistema | bajo, si 1 está bien hecha |

**Empezar por la 1**, porque las demás la usan y porque es la que ataca el cuello de botella medido.

**Y una regla para todo el desarrollo, que sale de esta semana:** cada fase se valida recuperando lo
que ya se sabe antes de aplicarse a lo que no se sabe. Es el segundo requisito del protocolo, y es lo
único que separa esto de un generador de propuestas.


---

## PARTE 4. CONSTRUIDO (9 de septiembre de 2026, misma sesión)

Las cinco fases están implementadas, con sus controles pasados. Cuarenta y siete tests.

| fase | módulo | control | resultado |
|---|---|---|---|
| 1 | `kuro.Hypothesis` | correrla sobre las tres hipótesis de hoy | **pasa**: las tres mueren en el mismo paso que a mano (bibliografía, escriba, corrección múltiple) |
| 2 | `kuro.Constraints` | aplicar las reglas a las categorías conocidas | **pasa tras corregir**: dos de las cinco reglas fueron retiradas por la validación |
| 3 | `kuro.Orders` | recuperar lo conocido y declarar la ceguera | **pasa**: recupera CYP→NI y NI→VIN como adyacencia real |
| 4 | corpus como error | pendiente | — |
| 5 | `kuro.Iteration` | construir un ciclo y comprobar que falla | **pasa**: la guarda lo detecta |

### Lo que la validación de la fase 2 encontró, y es la mejor prueba de que sirve

De las cinco reglas escritas, **la validación eliminó dos**:

- `single_site` decía que un término de transacción no puede ser exclusivo de un yacimiento.
  Eliminó **KI-RO**, que es un término de transacción y solo aparece en Hagia Triada, como SA-RA₂.
- `carries_logogram` decía que un término de transacción no va seguido de logograma de mercancía.
  Eliminó **KU-RO**, que sí lo lleva en las tablillas de mercancías mixtas.

Las dos quedan en el código **como comentario y no borradas**, porque una regla que falló es
información y alguien volverá a escribirlas. Con las tres restantes, la recuperación es del 100% y
las eliminaciones falsas, cero.

### Y lo que la fase 3 encontró en su primer uso

**La coexclusión sobre logogramas da veintitrés pares** con esperanza mayor que tres y cero
coincidencias. Pero al comprobar el confusor de soporte, **\*301 vive en nódulos (230 de 238
apariciones) y KA, SI y ZE también**, de modo que la coexclusión estaba midiendo el género del
documento.

Repetida solo dentro de tablillas: **de veintitrés pares queda uno**, TE con \*303 (esperados 3,3,
p = 0,031). Y con dieciocho pares contrastables en total, la corrección múltiple lo deja fuera.

**La adyacencia, en cambio, sí da resultado limpio**: CYP → NI aparece quince veces contra 5,6 del
nulo (p < 0,001) y NI → VIN dieciséis contra 4,1 (p < 0,001), mientras GRA → NI y OLE → VIN no
superan el nulo. Eso confirma como adyacencia lo que habíamos medido como orden: la secuencia
\*303 > higos > vino es real y no un artefacto de coocurrencia.

### Lo que queda
La fase 4, que es barata: para cada instrumento, su tasa de falsos positivos en los cinco corpus con
respuesta conocida, de modo que todo resultado futuro pueda escribirse como "p = X, con un
instrumento que se equivoca el N% de las veces en corpus donde la respuesta se conoce".

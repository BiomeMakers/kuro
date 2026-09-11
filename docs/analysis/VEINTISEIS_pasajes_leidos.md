# Los 26 pasajes, leídos uno a uno: un hilo real y una propuesta de generador (10 de septiembre de 2026)

## 1. Lo que hay de verdad en los 26

Leídos con su contexto completo. **Siete contienen una afirmación contrastable con nuestro corpus;
diecinueve son bibliografía, pies de figura, discusión de otro corpus o cosas ya medidas.**

| # | afirmación | fuente | resultado |
|---|---|---|---|
| H1 | OLIV+TU aparece siempre justo después de OLIV | Younger | **no medible**: nuestra fuente no escribe OLIV+TU |
| H2 | la variante 131c del vino solo está en Chania | Judson | **no medible**: la fuente no distingue variantes |
| H3 | \*306 solo en Chania y Hagia Triada | Judson | confirmada trivialmente (6 en Chania, 0 en otros) |
| H4 | \*164 silabograma en HT, logograma en Chania | Nosch y Weilhartner | no se ve con nuestra transcripción |
| H5 | **en HT 24, KI y ME abrevian tipos de lana** | Del Freo | **el único hilo real** |
| H6 | grano, higos, vino en el mismo orden en la parte baja | Hogan | ya medida por nosotros, 4 de 4 |
| H7 | que A-DU empiece por A- puede ser casual | Davis | confirmada: el 12,4% de las palabras empiezan por A- |

**Tres no medibles por la transcripción, una ya medida, dos confirmaciones triviales, y una que
abre algo.** Ese es el rendimiento real de 26 candidatos: uno.

## 2. El hilo: MA-RU-ME, que era uno de nuestros siete huecos

Del Freo, citado por Nosch y Weilhartner, dice que en HT 24 las sílabas KI y ME abrevian tipos o
calidades de lana. MA-RU es el logograma de la lana. Y en HT 24a están, **en la misma tablilla**:

| forma | estructura | apariciones |
|---|---|---|
| KI-MA-RU | KI + lana | 1 |
| MA-RU-ME | lana + ME | 3 |
| MA-RU | lana sola | (en HT 117a) |

**Es exactamente la estructura de los aceites cualificados** (OLE+KI, OLE+MI, OLE+U) que trabajamos
en el expediente de aromáticos: mercancía más calificador.

**Y la prueba que lo sostiene:** si KI y ME son calificadores de tipo, deberían aparecer con otras
mercancías. Lo hacen:

- **KI** califica el aceite (OLE+KI, 21 veces), la lana (KI-MA-RU) y \*316 (\*316+KI);
- **ME** califica la lana (MA-RU-ME) y SI (SI+ME, que está en HT 23a, el expediente).

**Un calificador que aparece con dos o tres mercancías distintas se comporta como un tipo o calidad,
no como un nombre.** Eso es lo que Del Freo propone para la lana y lo que nosotros medimos para el
aceite sin haberlos conectado.

**Hipótesis, con su condición:** MA-RU-ME es lana de calidad ME y KI-MA-RU lana de calidad KI, del
mismo modo que OLE+KI es aceite de calidad KI. La refutaría que KI o ME aparecieran con cantidades o
posiciones incompatibles con un calificador, por ejemplo encabezando documentos o llevando su propio
total.

**Y el inventario sube en una unidad**, de 53 a 54: MA-RU-ME pasa de hueco a "lana con calificador",
con Del Freo como fuente y nuestra medida de que KI se reparte entre mercancías como apoyo.

---

## 3. CÓMO HACER EL GENERADOR, DICHO SIN ADORNOS

El generador bibliográfico actual es una expresión regular que busca "in proportion to", "always
followed by" y cosas así, y luego coge el nombre de unidad más cercano. **Eso extrae punteros a
pasajes, no afirmaciones**, y por eso 26 candidatos dieron cuatro "supervivientes" que no eran nada.

**Lo que ha funcionado hoy es lo que he hecho a mano: leer el pasaje y escribir la proposición.** Y
eso sí se puede automatizar, pero no con expresiones regulares: **con un modelo de lenguaje en el
bucle**, que es precisamente lo que yo soy.

### El diseño, en tres piezas

**Uno: el filtro barato sigue siendo la expresión regular.** No para extraer afirmaciones, sino para
señalar qué pasajes merecen lectura. De cien mil palabras señala treinta pasajes, y eso ya es útil.

**Dos: cada pasaje señalado se lee con un modelo y se convierte en una proposición estructurada, o en
"ninguna".** La salida tiene un formato fijo que el ciclo ya entiende: unidades, tipo de afirmación
(distribucional, posicional, aritmética, predictiva, de ausencia), la afirmación en una frase, y
**qué observación la refutaría**. Si el modelo no puede rellenar los cuatro campos, el pasaje se
descarta.

**Tres: la proposición entra al ciclo tal cual.** Con la bibliografía comprobada, el nulo de su tipo,
los confusores que las lecciones programen, y su archivo.

### Por qué esto sí y lo anterior no

Porque **la parte que falla es entender el texto, y eso es lo que un modelo hace y una expresión
regular no.** Hoy lo he hecho con veintiséis pasajes y ha tardado minutos; la pieza que lo hace
automático es una llamada por pasaje con el formato fijo.

### Lo que no resuelve
Que **las fuentes se sigan consiguiendo a mano**. Y que **un pasaje mal leído produzca una proposición
falsa**: por eso la salida exige la condición de refutación, que es el filtro que hoy nos ha salvado
siete veces.

### Cuánto costaría
El código de la pieza dos es corto, porque la interfaz ya existe: `Hypothesis` acepta exactamente
esos cuatro campos. Lo que hay que escribir es la llamada al modelo con el formato y el descarte de lo
que no lo cumpla. **Es una tarde**, y se puede probar con los mismos 26 pasajes de hoy, cuya respuesta
correcta ahora conocemos: siete proposiciones de veintiséis, una útil.

# Los seis trabajos nuevos: qué aportan y qué nos obligan a cambiar (7 de septiembre de 2026)

Seis textos recibidos hoy. Tres son relevantes para lo que hacemos, uno mucho, y dos poco.

---

## 1. Briakos, N. (2026), *An Undeciphered Script in the Age of AI*, tesis de máster, Universidad del Pireo (mayo 2026)

**Es el trabajo que más se parece al nuestro, y hay que citarlo.** Un estudiante de informática hace, con 419 tablillas de lineara.xyz, buena parte de lo que hemos hecho: distribuciones zipfianas, sesgos posicionales, divergencia entre registros (JSD = 0,0944, p = 0,018 por permutación), variación de longitud de palabra entre yacimientos (d de Cohen 0,623, Festos frente a Chania), 23 huellas de escriba con preferencias de bigramas, y un detector no supervisado de fórmula que recupera cinco de los nueve elementos de la fórmula de libación sin conocerla de antemano.

Y hace algo que nosotros no: entrena un transformador pequeño y calibra con un corpus sintético del Lineal B para estimar **a qué tamaño el reconocimiento de frecuencias empieza a ser útil: unos 10.000 tokens, siete mil quinientos más de los que hay.** Es exactamente nuestra curva de potencia, obtenida por otro camino y con otro método.

**Coincidencias con nuestros resultados, y son tranquilizadoras:** la divergencia entre registros (nosotros 0,193 con otra medida; él 0,0944 con la suya, los dos significativos), las huellas de escriba (él 23, nosotros el confusor mano-serie), y sobre todo la conclusión de fondo: el corpus no da para la asignación fonética.

**Lo que nos obliga a hacer:** citarlo en el artículo de método, y revisar dos afirmaciones nuestras a la luz de las suyas (la de las huellas de escriba y la de la separación de registros). Y decir con honestidad que no somos los primeros en aplicar este tipo de análisis, aunque nuestro aparato de nulos y calibración sea distinto.

---

## 2. Halloub, M. R. (2026), *A Multi-Layer Operator Grammar for Linear A Accounting Texts*

Propone una gramática formal de cuatro niveles para la contabilidad del Lineal A, sobre nueve tablillas de Hagia Triada. Su hallazgo central es que **la familia ku- es heterogénea y contiene tres clases funcionalmente distintas**: marcadores de estado contable (ku-ro, ki-ro, po-to-ku-ro), marcadores de proceso (\*308, GRA+KU, \*188) y formas léxicas o toponímicas (KU-PA₃-NU, KU-PA₃-NA-TU), y sostiene que tratarlas como un sistema único es el error principal a evitar.

**Coincide con nosotros en tres puntos y en uno nos precede:** que \*188 no pertenece al bloque de aromáticos (nosotros lo retiramos por su distribución; él por su papel en la aritmética), que la familia KU-PA₃ es toponímica y distinta de la nuestra (que es lo que Jiménez Delgado también sostiene), y que \*308 tiene un papel de transformación aritmética y no de mercancía ordinaria.

**Y aporta algo que no teníamos:** la clase de ligaduras +KU (GRA+KU y compañía) como categoría con función propia. Nosotros vimos GRA+KU en HT 16 y HT 20 sin darle papel.

**Cautela:** es de un investigador independiente en física teórica, no del campo, y trabaja sobre nueve tablillas. Sus resultados hay que tratarlos como los nuestros: propuestas con evidencia, no lecturas establecidas.

---

## 3. Schümann, M. (2026), *The Linear A Inscription IO Za 2*, con DOI de Zenodo (junio 2026)

Nueva edición y reconstrucción de IO Za 2, la mesa de libación del Juktas, con lectura de A-TA-I-JO-WA-JA, JA-SA-SA-RA-ŽA, U-NA-KA-NA-SI, I-PI-NA-MA y SI-RU-TE, y reconstrucción del final como TA-NA-RA-TE-U-TI-NU I-DA[-MA-TE-QE]. Interpreta TA-NA-RA como "santuario", TE-U como "del dios", TI-NU como nombre divino comparable al micénico di-wo-nu-so, e I-DA-MA-TE como la divinidad del Ida.

**Toca directamente nuestro trabajo:** i-da-ma-te es uno de los ocho pares del prefijo I- que medimos (i-da-ma-te en Arkalochori frente a da-ma-te en Kythera), y su lectura de TI-NU como teónimo afectaría a nuestra plantilla de la fórmula.

**Pero hay que ser prudentes:** es un trabajo de autopublicación en Zenodo, con lecturas etimológicas que son justamente el tipo de propuesta que nuestro protocolo pide contrastar. Lo citaría como propuesta reciente, no como apoyo.

---

## 4. Chiapello, D. (s.f.), *Grain management in Linear A accounting tablets*

Defiende la hipótesis del "minoico griego": que a-du equivale al micénico a-pu-do-si ("entrega") y da-du-ma-ta a otra forma griega, con argumentos de apócope de preposiciones y paralelos dialectales tesalios y macedonios.

**Es directamente contrario a nuestro resultado.** Nosotros medimos que el Lineal A leído con valores del Lineal B está más lejos del griego micénico que el griego micénico barajado (0,104 frente a 0,092 del nulo), y que el conversor recupera el 36-47% donde la identidad de lengua exigiría el 85%.

**Lo útil:** es un ejemplo perfecto para el protocolo de mínimos. Su propuesta no declara nulo, no tiene control positivo, y no predice texto no visto. Sin descalificar a nadie, es el tipo de argumento que el protocolo pide formular de otro modo para que se pueda evaluar.

---

## 5-6. El volumen *The Wor(l)ds of Linear A* (Salgarella y Petrakis, eds., AURA Supplement 15, 2025) y Minoans1

El volumen completo, que ya citábamos por el capítulo final de Petrakis y Steele. Comprobado: **no menciona ni la juncia, ni los aromáticos, ni el perfume, ni las fracciones, ni HT 23a**. Es decir, el expediente que hemos descrito no está tratado en la publicación más reciente y completa del campo. Eso es una buena noticia para el artículo de aromáticos y conviene decirlo con cautela: significa que nadie lo ha publicado, no que nadie lo haya visto.

---

## Consecuencias, por orden

1. **Citar a Briakos en el artículo de método**, y decir que sus resultados sobre registro y escribas coinciden con los nuestros por otra vía. Su umbral de 10.000 tokens es un dato que refuerza nuestra curva de potencia y hay que incorporarlo.
2. **Citar a Halloub** en el artículo de aromáticos, por \*188 y por \*308, y reconocer que la clase +KU es suya.
3. **Mencionar a Schümann** al hablar del prefijo I- y de i-da-ma-te, como propuesta reciente.
4. **Usar a Chiapello como ejemplo en el protocolo de mínimos**, con respeto y sin nombres si es posible.
5. Y anotar que el volumen de 2025 no trata el expediente de aromáticos, lo que sitúa nuestro artículo.

# Métodos de otros campos aplicables al Lineal A, y lo que ya se ha probado (12-sep-2026)

## Parte A. Casos de desciframiento con condiciones parecidas

Los cinco desciframientos consumados se resumen en el documento OPCIONES_desde_la_bibliografia.md. Lo que importa aquí es cuál se parece a nuestra situación, que es la de **Tipo II: escritura conocida, lengua desconocida**, de la que la literatura dice que "estrictamente no es desciframiento sino análisis lingüístico" y que es extremadamente difícil solo con información interna.

| caso | condición que compartimos | lo que a ellos les faltaba y consiguieron | ¿podemos? |
|---|---|---|---|
| **Elamita lineal** (Desset y otros 2022) | sin bilingüe estricta; corpus de 40 inscripciones | "bilingüismo parcial": dos grupos de textos muy formularios del mismo tipo en dos escrituras, correlacionados por nombres propios y títulos | **el más parecido**; nuestro equivalente ya hecho: las fórmulas de ofrenda egipcias alineadas posición a posición |
| **Maya** (Proskouriakoff 1960) | sin lengua candidata al principio | el patrón de fechas revela el contenido (intervalos que caben en una vida) | probado 12-sep: no hay equivalente, porque nuestras tablillas no registran juntos beneficiario y asignación |
| **Ibérico** (Gómez-Moreno 1922) | escritura conocida, lengua no | valores de signo por monedas bilingües; la lengua sigue sin entenderse cien años después | es nuestro espejo, no nuestra salida |
| **Lineal B** (Ventris 1952) | rejilla estructural disponible | una lengua candidata que resistiera la prueba | cerrado por tres vías (fonotaxis, valores libres, cognados) |
| **Cario** | valores erróneos asumidos durante décadas | tomar en serio las bilingües egipcio-carias que ya existían | no hay bilingües que estemos ignorando; las egipcias ya están probadas |

**Conclusión de la parte A:** el único camino con precedente real para nuestra situación es el de Desset, y consiste en explotar un género muy formulario contra su equivalente en una escritura leída. Eso ya está iniciado (fórmula votiva contra fórmula de ofrenda egipcia) y su límite ya está medido: la arquitectura coincide, el contenido de las posiciones no.

## Parte B. Métodos de fuera del campo, y cuál es transferible

### B.1 Descubrimiento de motivos (bioinformática) — PROBADO HOY, FUNCIONA

En bioinformática, MEME (Bailey y Elkan 1994) y los HMM de perfil (HMMER, Pfam) resuelven exactamente nuestro problema: encontrar patrones conservados con posiciones variables en pocas secuencias, sin saber qué significan. MEME admite alfabetos definidos por el usuario, así que se aplica a cualquier secuencia simbólica.

**Prueba de concepto corrida hoy.** Las 308 tablillas del corpus, convertidas en secuencias de categorías (W palabra, C mercancía, N cifra, f fracción, T total, L logograma, | separador), contra un nulo de Markov de orden 1 que conserva frecuencias y transiciones (60 corridas):

| motivo | observado | nulo | razón | lectura |
|---|---|---|---|---|
| WfWfW | 7 | 0,0 | 14x | palabra + fracción repetido: lista de partidas fraccionarias |
| fCfCf | 8 | 0,4 | 16x | mercancía + fracción repetido |
| WfWf | 10 | 0,3 | 20x | igual que el primero |
| \|L\|C | 12 | 1,5 | 8x | separador, signo suelto, separador, mercancía |
| WCNC | 40 | 9,8 | 4x | parte + mercancía + cifra + mercancía |

**El método se valida solo:** el motivo \|L\|C es el patrón de TE que fijamos a mano el 10 de septiembre (SA-RO 𐄁 TE 𐄁 VIN, HT 6a, 9a, 14, 17, 19). Que el descubrimiento automático lo recupere sin que se lo digan es el control positivo.

**Y encuentra uno que no teníamos:** WfWfW, listas de palabras cada una con su fracción, en HT 8a, HT 98a, PE 2 y HT 23a. Es un formato distinto del expediente de mercancías, y las cuatro tablillas no se habían tratado como un género aparte.

**Qué falta:** aplicarlo con un HMM de perfil de verdad (posiciones con probabilidad, no cadenas exactas), que es lo que permitiría clasificar tablillas por formato y detectar las que no encajan en ninguno. Es media sesión de trabajo y no depende de nadie.

### B.2 Transporte óptimo de Gromov-Wasserstein (aprendizaje automático) — SIN PROBAR, EL MÁS PROMETEDOR DE LOS QUE FALTAN

Alvarez-Melis y Jaakkola (EMNLP 2018) alinean dos espacios de palabras **sin diccionario semilla y sin espacio común**: en vez de comparar posiciones, comparan cómo se relacionan entre sí las distancias dentro de cada espacio. Es decir, alinean por estructura relacional, no por parecido de forma.

**Por qué es distinto de lo que hemos hecho.** NeuroDecipher empareja por distancia de edición de las grafías, y por eso arrastra el filtro de la transcripción. Gromov-Wasserstein no mira las grafías en absoluto: mira si la "geometría" del vocabulario minoico (qué palabras aparecen en contextos parecidos) tiene la misma forma que la de otra lengua. Si el minoico y una candidata tuvieran la misma estructura semántica de un archivo contable, el método lo vería sin depender de los valores del Lineal B, que es nuestro obstáculo declarado.

**Lo que haría falta:** embeddings de contexto para las unidades minoicas (los tenemos implícitos en la coocurrencia) y para las candidatas. Con 800-1.000 unidades el método es aplicable; su limitación conocida es el coste con vocabularios grandes, que no es nuestro caso. El control es el de siempre: el mismo alineamiento contra un minoico barajado.

### B.3 Optimización combinatoria con recocido acoplado (Frontiers in AI 2025)

Un trabajo de este año propone exactamente lo que montamos el 11 de septiembre (recocido simulado sobre asignaciones de valores) pero con permutaciones-k que permiten correspondencias nulas, de uno a muchos y de muchos a uno, y dice superar el estado del arte en identificación de cognados. Nuestra búsqueda de valores es una versión más simple: solo permuta valores uno a uno. Merece leerse y, si su código está disponible, correrlo con nuestro control.

### B.4 Ideas de otros campos, evaluadas y descartadas o aparcadas

- **Factorización de matrices y sistemas de recomendación** (tablilla × mercancía): encontraría "tipos de cuenta" latentes. Aplicable, barato, y probablemente redundante con lo que ya da la comparación entre archivos.
- **Detección de puntos de cambio** (series temporales): para segmentar palabras donde no hay separador. El Lineal A sí tiene separadores, así que no aporta.
- **Distancia por compresión normalizada**: clasificación de lenguas sin modelo. Es una tercera medida de lo mismo que ya hemos cerrado dos veces.
- **Filogenética bayesiana**: exige listas de cognados que no tenemos.
- **Estilometría de autoría**: identificar manos por el texto y no por la paleografía. Aplicable, y con SigLA como verdad para calibrar. Es la línea del trabajo neuronal sobre manos escribales del Lineal B (arXiv 2108.04199).

## Recomendación

1. **HMM de perfil sobre los formatos de tablilla** (B.1). El descubrimiento de motivos ya ha demostrado hoy que funciona y que recupera lo que sabemos. Es lo único de esta lista que amplía el inventario de funciones.
2. **Gromov-Wasserstein contra las candidatas** (B.2), con el control barajado. Es la única prueba de filiación que no pasa por la forma de los signos, y por tanto la única que escapa al filtro que hemos declarado como obstáculo principal.
3. Leer el trabajo de Frontiers 2025 (B.3) antes de escribir la sección de búsqueda de valores del artículo de las candidatas.

---

# Addendum (12-sep, tarde): Tamburini 2025, y lo que obliga a cambiar

**Referencia completa:** Tamburini, F. (2025). "On automatic decipherment of lost ancient scripts relying on combinatorial optimisation and coupled simulated annealing". *Frontiers in Artificial Intelligence* 8:1581129. DOI 10.3389/frai.2025.1581129. Acceso abierto CC BY. Código y datos: github.com/ftamburin/CSA_OptMatcher.

Leído entero. Cinco cosas que nos afectan, en orden de importancia.

## 1. Es el mismo método que nuestra búsqueda de valores, publicado y más completo. Hay que citarlo.
Su sistema plantea el desciframiento como optimización de una función de energía sobre asignaciones de signos, resuelta con recocido simulado acoplado (16 recocedores en paralelo). Codifica las soluciones con k-permutaciones, lo que le permite representar correspondencias nulas, de uno a muchos y de muchos a uno, donde la nuestra solo permuta valores uno a uno. La energía combina en un solo paso la correspondencia de signos y la de léxicos, esta última resuelta con el algoritmo húngaro. **Nuestro artículo de las candidatas no puede enviarse sin citarlo.**

## 2. Y nuestra aportación sigue en pie, porque es justo lo que él no tiene.
Tamburini evalúa sobre listas de cognados conocidos: mide aciertos contra una verdad. Nosotros no tenemos verdad, y por eso usamos un corpus de control (el minoico con las sílabas barajadas) contra el que comparar. Él mismo señala esa carencia en su discusión: probar estos sistemas en casos reales, con escrituras y lenguas desconocidas, "presenta un conjunto de retos completamente distinto y comparanda inciertos". El control es exactamente ese comparandum, y es lo que nosotros aportamos.

## 3. Explica el fracaso de nuestro torneo, y no fue culpa nuestra.
Dice dos cosas sobre NeuroDecipher (Luo y otros 2019), que es el programa que corrimos: que no consiguió reproducir sus resultados publicados, y que estos "parecen ser los valores máximos obtenidos tras numerosos reinicios"; y que tuvo que modificar el código para quitar de la entrada información no disponible en un desciframiento real, como el número esperado de cognados en el conjunto de prueba. Nuestro torneo del 11-sep dio emparejamientos sin sentido y el control positivo no encontró el hebreo. Con esto, ese resultado se explica: el sistema requiere reinicios múltiples y conocimiento que en nuestro caso no existe.

## 4. Su herramienta es mejor que NeuroDecipher para nuestro caso, y está publicada.
Tres razones concretas: admite **comodines para signos ilegibles** (nosotros tenemos 276 de 783 unidades rotas en todas sus atestaciones, el 35%); admite **conocimiento parcial fijado** de la correspondencia de signos (nosotros tenemos dieciséis signos anclados por los topónimos compartidos con el Lineal B); y está pensado para **pocos centenares de palabras por lado**, que es nuestro tamaño, mientras que las redes neuronales necesitan más datos. Sus resultados en Lineal B contra griego micénico son 89,4% frente al 75,8% de NeuroDecipher recalculado en condiciones realistas.

**Acción:** correr CSA_OptMatcher con nuestros datos (minoico contra cada candidata) y con nuestro control barajado, que es la combinación que nadie ha hecho. Sustituye al uno a uno de NeuroDecipher.

## 5. El autor está en el departamento de Silvia Ferrara.
Fabio Tamburini, Dipartimento di Filologia Classica e Italianistica, Universidad de Bolonia. Es coautor de Corazza, Tamburini, Valério y Ferrara (2022) sobre el chiprominoico, y de Corazza y otros (2021) sobre los valores de las fracciones del Lineal A, que es el artículo con el que corregimos nuestras fracciones el 10 de septiembre. Y su trabajo futuro declarado es "aplicar el sistema propuesto a las escrituras no descifradas del área egea". Es decir: acabamos de escribir a Ferrara, y su colaborador más cercano en lo computacional va a hacer lo que estamos haciendo. Conviene escribirle a él también, y pronto, con la parte que nos distingue por delante (el control, las tasas de error, el corpus verificado contra GORILA).

## 6. La controversia del Indo, para el artículo del protocolo
Tamburini resume el caso que más nos sirve como aviso. Rao y otros (2009, *Science*) sostuvieron que la escritura del valle del Indo codifica lengua porque su entropía condicional se parece más a la de las lenguas naturales que a la de sistemas no lingüísticos; Lee, Jonathan y Ziman (2010) hicieron lo propio con los símbolos pictos. Sproat (2010) los refutó con un conjunto mayor de corpus no lingüísticos, mostrando que ninguno de esos métodos distingue de forma fiable escritura de no escritura, y propuso una medida basada en repetición que los clasificaba al revés. Es el precedente exacto de lo que el artículo del protocolo advierte: una medida estadística sin el control adecuado produce la conclusión que se busca, y el campo tarda años en deshacerla. Va citado en el protocolo.

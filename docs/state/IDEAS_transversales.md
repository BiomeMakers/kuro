# Ideas de fuera del campo que sí son transversales a nuestro propósito (12-sep-2026)

Revisada la bibliografía de desciframiento, esto es lo que viene de **fuera** de la epigrafía egea y se puede aplicar. Lo ordeno por lo que ya hemos probado hoy y lo que queda.

## Aplicado hoy
**1. El marcador multimétrico (debate del Indo).** Rao 2009 midió entropía condicional; Sproat 2010 y 2014 demostró que una métrica sola no discrimina y aportó corpus no lingüísticos reales (kudurrus, postes totémicos, piedras pictas, blasones, iconos meteorológicos); Nair 2026 exige coincidencia simultánea en cuatro dimensiones. **Aplicado**: los nódulos del Lineal A no son escritura (entropía condicional 0, repertorio cerrado de 33 signos que satura). Ver SCORECARD_no_linguistico.md. Es el hallazgo transversal del día.

## Pendientes, con lo que hay
**2. Curvas de acumulación y estimadores de riqueza (ecología).** La curva de vocabulario nuevo por documento es una curva de rarefacción, y los estimadores de riqueza (Chao, Jackknife) dicen **cuántas unidades faltan por aparecer** en un corpus. Aplicado al Lineal A daría una cifra defendible para "cuánto del léxico tenemos" y, sobre todo, cuánto corpus nuevo haría falta para llegar a N unidades. Es la respuesta cuantitativa a la pregunta de cuánto falta, y no la hemos dado nunca.

**3. Ley de Heaps y Zipf como diagnóstico por subcorpus.** Nair reporta pendiente de Zipf −1,49 para el Indo; nosotros medimos la ley de potencias una vez (y la usamos para refutar a otro). Medida **por soporte y por archivo** diría si tablillas, nódulos y votivas obedecen la misma ley, que es otra forma de la pregunta semiótica.

**4. Optimización combinatoria para la asignación de valores** (Frontiers 2025, recocido simulado acoplado con k-permutaciones, que admite correspondencias uno a muchos y muchos a uno). Nuestra búsqueda de valores solo permite permutaciones uno a uno; su formulación es más general y tiene código publicado. Es la versión buena de lo que hicimos ayer.

**5. Criptoanálisis con modelos de lenguaje** (Kambhatla 2018; Knight). Los cifrados de sustitución se resuelven con búsqueda guiada por un modelo de lenguaje, y esas técnicas "no se han aplicado con éxito a datos arqueológicos". La razón es la misma de siempre (no hay lengua destino), pero la **maquinaria de búsqueda** sí sirve para el problema de los valores.

**6. Segmentación estadística sin espacios** (Yadav 2008; Luo 2021). El Lineal A tiene separadores, pero los textos votivos y los sellos no siempre; y las unidades "rotas" son un problema de segmentación disfrazado. Los métodos de segmentación con verosimilitud podrían dar una lectura distinta de las alternancias.

**7. Detección de comunidades en el grafo de bigramas** (Nair usa Louvain y encuentra 12 comunidades funcionales). Nosotros tenemos el grafo de coocurrencia y nunca hemos hecho comunidades sobre el grafo de **secuencia**. Daría clases de signos por comportamiento, que es otra vía al inventario de funciones.

**8. Deduplicación como control.** Nair encuentra un 24% de inscripciones duplicadas exactas en el Indo, que infla las métricas de repetición. Nosotros nunca hemos comprobado duplicados exactos en el Lineal A, y con 886 nódulos de un signo es evidente que los hay; afecta a cualquier medida de frecuencia.

## Lo que NO es transversal, aunque lo parezca
- Traducción automática no supervisada (PidginUNMT y similares): exige corpus grandes y una lengua destino.
- Modelos de lenguaje grandes como descifradores: no tienen verdad contra la que comprobarse; su papel medido es leer y enrutar (22% y 1% de invención).
- Más lenguas candidatas: la vía está cerrada por fonotaxis, por valores y por tipología.

## Recomendación
La 2 (estimadores de riqueza) y la 8 (duplicados) son de una tarde y mejoran todo lo demás. La 7 es un instrumento nuevo barato. La 4 es la única que podría mover la aguja en la asignación de valores, y tiene código publicado.

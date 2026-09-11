# El nulo bipartito: el método importado no funcionó, y por qué eso enseña algo (10 de septiembre de 2026)

Primera transferencia deliberada de método desde otro campo, siguiendo el mapa de `kuro.transfer`.
El resultado no es el esperado y es más informativo por eso.

## 1. Qué se importó y por qué

El análisis de redes bipartitas (bibliometría, ecología de redes) usa el **modelo de configuración**:
grafos aleatorios que conservan las dos secuencias de grados, es decir, en cuántos documentos aparece
cada unidad y cuántas unidades tiene cada documento.

La hipótesis era directa: nuestra coocurrencia hipergeométrica da un 8,0% de falsos al umbral del 5%
porque **los documentos no son intercambiables**, y el modelo de configuración conserva por
construcción lo que la hipergeométrica supone.

Implementado con el algoritmo curveball, que intercambia los elementos no compartidos de dos
documentos y por tanto conserva ambos grados exactamente. Comprobado con un test.

## 2. El resultado: no cambia nada

| nulo | falsos positivos al 5% |
|---|---|
| hipergeométrico | 8,0% |
| **bipartito, solo grados** | **8,0%** |

**Idéntico.** El método importado, correctamente implementado y con sus grados verificados, no
mejora nada.

## 3. Por qué, y es lo que enseña

**Porque el grado no era la causa.** La diagnosis de ayer decía que los documentos no son
intercambiables por yacimiento, escriba y género; el modelo de configuración conserva cuántas veces
aparece cada cosa, pero **sigue mezclando documentos de Hagia Triada con los de Zakros**. La
estructura que infla la coocurrencia sobrevive intacta en el nulo.

Es exactamente el error que retiramos dos veces en agosto: **un nulo que no conserva lo que la
afirmación no pretende explicar.** Esta vez lo cometí importando un método sin comprobar que su
supuesto encajaba con la causa diagnosticada.

## 4. La versión que sí funciona

Añadida la estratificación: los intercambios ocurren **solo entre documentos del mismo yacimiento**.

| nulo | 5% | 1% | 0,1% |
|---|---|---|---|
| hipergeométrico | 8,0% | 4,2% | 2,2% |
| bipartito simple | 8,0% | 4,0% | 3,0% |
| **bipartito por yacimiento** | **5,5%** | 4,0% | 4,0% |

**Al umbral del 5% la tasa baja de 8,0% a 5,5%, casi el nominal.** A umbrales más finos no mejora, y
eso hay que decirlo: con doscientos ensayos no se puede resolver por debajo de 0,005, de modo que las
cifras de 4,0% en las columnas de 1% y 0,1% son ruido de resolución y no medidas.

## 5. Lo que hay que hacer con esto

**Usar el nulo estratificado para toda afirmación de coocurrencia del proyecto**, y rehacer con él
el bloque de aromáticos, que se construyó con la hipergeométrica sobre material mayoritariamente de
Hagia Triada.

**Y conservar las dos medidas**, la del método importado tal cual y la de su versión estratificada,
porque el contraste es el resultado: no basta con traer un método de otro campo; hay que comprobar
que **su supuesto ataca la causa que uno ha diagnosticado**, y aquí no lo hacía.

## 6. La regla que sale de esto, para el protocolo de transferencia
`kuro.transfer` ya pregunta, antes de importar un método, qué supone sobre la intercambiabilidad de
los documentos. **Faltaba la pregunta siguiente:** y ese supuesto, ¿coincide con la causa
diagnosticada del problema que quiero arreglar? Aquí no coincidía, y la coincidencia parecía obvia.

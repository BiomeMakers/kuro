# La búsqueda anclada de valores, corregida y definitiva (13-sep)

Este documento reemplaza la tabla de septiembre. Aquella era inservible por dos fallos de montaje, los dos encontrados y corregidos hoy.

## Los dos fallos

**El esqueleto consonántico del minoico llevaba basura.** Los caracteres `+`, `?`, corchetes y dos glifos de uso privado entraban como consonantes. El corpus real podía explotarlos y el control barajado no. Solo eso llevaba al acadio a z = +6,88.

**Y los once blancos no eran objetos del mismo tipo.** El ugarítico venía del DULAT como lista de lemas deduplicada, ratio 1,00. Los de TLHdig eran volcados de tokens: el hático repite *pa-la* 113 veces, el luvita arrastra el sumerograma KI.MIN 94 veces, la entrada más frecuente del hurrita es un signo cuneiforme repetido 1.194 veces, y las cuatro primeras del hitita son clíticos. Además el ibérico, semisilabario cuya transliteración no segmenta como el minoico, tenía esqueletos de hasta 24 consonantes frente a una media minoica de 2,79.

Normalizar (`kuro/targets.py`, ocho tests) deduplica, elimina logogramas y signos, descarta formas de menos de tres letras y acota el esqueleto a seis consonantes. El acadio pasa de 40.000 formas a 3.548 y el sumerio a 2.330: **más del 90% de lo que se usaba como léxico no eran palabras.**

## La tabla definitiva

Recocido simulado sobre los 59 signos libres, 6.000 pasos, **20 controles**, blancos normalizados. El control es un minoico con el orden silábico destruido.

| lengua | z | escritura de transmisión |
|---|---|---|
| etrusco | **+1,75** | alfabeto propio |
| luvita | +1,30 | cuneiforme |
| ugarítico | +1,28 | alfabético consonántico |
| ibérico | +0,99 | semisilabario |
| hitita | +0,22 | cuneiforme |
| palaico | −0,19 | cuneiforme |
| micénico | −0,90 | silabario |
| acadio | −1,15 | cuneiforme |
| sumerio | −2,59 | cuneiforme |
| hático | −3,32 | cuneiforme |
| hurrita | −4,04 | cuneiforme |

**Ninguna alcanza z = 3, y el máximo es +1,75.**

## Lo que esto establece

**La vía fonológica queda cerrada, y esta vez con un instrumento que sabemos calibrado.** Bajo cualquier asignación de valores compatible con los topónimos compartidos, el minoico no se parece a ninguna de las once más de lo que un minoico sin secuencias se deja parecer.

El control implícito lo confirma: **el micénico da −0,90**. Sabemos que el Lineal A no es griego, y el instrumento lo coloca en el grupo sin señal. Si se hubiera disparado, habría invalidado el resto.

Y el dato que explica por qué todo esto ocurre: la columna de valores del Lineal B frente al mejor resultado real. El hitita pasa de 0,296 a 0,193, el ibérico de 0,365 a 0,209, el etrusco de 0,297 a 0,101. **La optimización mejora la distancia entre un tercio y dos tercios en todas las lenguas**, lo que confirma por vía independiente lo medido en agosto: con 59 valores libres, cualquier corpus se acerca a cualquier blanco, y por eso el encaje léxico no discrimina.

## Una limitación que hay que declarar

**Las siete lenguas transmitidas en cuneiforme promedian −1,40 y las cuatro restantes +0,78.** El sesgo no es determinante, ya que el luvita es cuneiforme y queda en +1,30, pero es visible y probablemente refleja convenciones de transliteración que ninguna normalización de nuestro lado corrige.

Los dos valores más negativos, el hurrita y el hático, son las dos lenguas aisladas del conjunto, conocidas solo por textos de archivos hititas y de un único género. Sus vocabularios no son léxicos generales, y sus perfiles no son comparables con el resto ni después de deduplicar. **Un z negativo no es evidencia sobre parentesco**: dice que el minoico barajado conviene a ese blanco más que el real, lo que señala un desajuste de perfiles y no una distancia lingüística.

## Lo que se retira

La tabla de septiembre entera, con sus trece candidatas y sus z sobre cinco controles. En particular: el luvita como la más alta con 2,3, el etrusco a −3,2 y el ugarítico a 0,1. Ninguno de los tres era un valor real, y el del etrusco se comunicó por correo a una especialista antes de descubrirlo.

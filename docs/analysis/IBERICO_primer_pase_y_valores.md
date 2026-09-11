# Ibérico, primer pase, y la búsqueda de valores (10-sep, noche)

## Ibérico (Hesperia vía Luo 2021)
2.094 inscripciones, 4.697 tokens, 3.087 formas (2.906 íntegras). Regiones Hesperia: TE 630, HER 370, V 213, B 212, GI 137. Inscripción media de 2,2 tokens; 300 con tres o más. Formas más frecuentes: ban 33, śalir 14, bil 12, bal 11, iunstir 9, bateba 9. Los elementos formulares del campo (Untermann) se localizan: ban en 158 formas, iuns- 25, ekiar 20, eban 17, baite 16.

**Contra las trece con el mismo instrumento (nulo = consonantes ibéricas barajadas): p≈1 contra todas**, salvo Lineal A p=0,045 con distancia igual al nulo (0,341 vs 0,342): una de trece, no significa nada sola. **Calibración:** una lengua aislada con transcripción fiable sale exactamente como el minoico. Dos lecturas: así es "aislado" en este instrumento, y el instrumento no distingue "aislado" de "filtro".

## Búsqueda de asignaciones de valores (kuro/valuesearch.py)
Recocido simulado sobre intercambios de valores consonánticos entre los 75 signos, objetivo la distancia a la candidata, **control = mismo recocido sobre un minoico con el orden de sílabas destruido**. Prototipo (1.500 pasos, 3 controles):

| candidata | valores del B | mejor real | control (media ± sd) | z |
|---|---|---|---|---|
| micénico | 0,100 | 0,059 | 0,064 ± 0,005 | 1,1 |
| hurrita | 0,198 | 0,121 | 0,108 ± 0,003 | −3,6 |
| etrusco | 0,312 | 0,172 | 0,165 ± 0,005 | −1,2 |

Con 75 valores libres cualquier cosa se acerca a cualquier cosa, y **el corpus real no se acerca más que el control**. La corrida completa (20.000 pasos, 10 controles, 14 lenguas) va en el Mac. Versión restringida pendiente: fijar los signos anclados por los topónimos compartidos (pa-i-to, su-ki-ri-ta, se-to-i-ja) y liberar solo el resto.

## NeuroDecipher
Ficheros .cog preparados (data/derived/nd/, real y control por candidata) y guion en MAC.md. Código de 2019; si no instala en media hora, se deja.

## Corrida completa de la búsqueda anclada (10-sep, noche): 13 lenguas, 6.000 pasos, 5 controles

16 signos fijos (los de pa-i-to, su-ki-ri-ta, se-to-i-ja, da-i-pi-ta, i-ta-ja, ki-da-ro y las vocales), 59 libres.

| lengua | valores del B | mejor real | control | z |
|---|---|---|---|---|
| luvita | 0,220 | 0,113 | 0,120 | 2,3 |
| hitita | 0,181 | 0,105 | 0,110 | 1,5 |
| micénico | 0,100 | 0,053 | 0,054 | 1,3 |
| sumerio | 0,322 | 0,219 | 0,222 | 1,0 |
| acadio | 0,295 | 0,193 | 0,194 | 0,4 |
| ugarítico | 0,257 | 0,171 | 0,172 | 0,1 |
| elamita | 0,275 | 0,200 | 0,200 | 0,1 |
| hático | 0,233 | 0,122 | 0,119 | −1,0 |
| eteocretense | 0,243 | 0,174 | 0,171 | −1,2 |
| palaico | 0,207 | 0,125 | 0,119 | −1,4 |
| hurrita | 0,198 | 0,121 | 0,114 | −2,3 |
| ibérico | 0,341 | 0,246 | 0,239 | −2,5 |
| etrusco | 0,312 | 0,189 | 0,177 | −3,2 |

**Ninguna llega a z=3.** El máximo es el luvita (2,3), la candidata de Palmer y Finkelberg: con cinco controles y una sd de 0,003, no es señal, pero es la única en la dirección correcta por encima de 2 y merece una repetición con 20 controles antes de decir nada. El etrusco, que ayer era la dirección que los valores del B "escondían", aquí sale al revés: el corpus real se deja acercar **menos** que el control (−3,2). Las dos observaciones sobre el etrusco no son contradictorias (ayer se comparaban valores del B contra azar; hoy real contra control bajo optimización), pero juntas dicen que no hay nada ahí.

**Cierre:** bajo cualquier asignación de valores compatible con los topónimos compartidos, el minoico no se parece a ninguna de las trece más de lo que un minoico sin secuencias se deja parecer. La vía fonológica queda cerrada por segunda vez, y de forma más fuerte que con los valores fijos. Pendiente: luvita con 20 controles, y la frase para el artículo de las trece.

## Luvita con 21 controles (10-sep, noche)
Real 0,1131; controles media 0,1191, sd 0,0035; **z=1,70**; un control de 21 queda por debajo del real (0,113). Con 5 controles daba 2,3; con 21 baja a 1,7 y un control lo iguala. **No hay señal luvita.** La vía queda cerrada para las trece sin excepción: ninguna supera z=2 con controles suficientes.

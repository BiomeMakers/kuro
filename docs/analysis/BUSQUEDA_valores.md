# Búsqueda de asignaciones de valores (10-sep, noche)

**Pregunta:** para cada lengua candidata, ¿qué valores consonánticos de los 75 silabogramas acercan más el perfil de bigramas del minoico, y cuánto se acerca en el mejor caso? **Nulo:** la misma optimización sobre minoico con las sílabas barajadas dentro de cada palabra (misma longitud, mismas frecuencias de sílaba, solo se destruye el orden). Solo cuenta la ganancia que supere la de los controles. Implementado en kuro/valuesearch.py (recocido simulado: intercambio de valores entre dos signos o reasignación desde el inventario) y scripts/value_search.py.

**Primera pasada** (2.000 pasos, 5 controles, semilla 0), doce candidatas:

| candidata | inicio (valores del B) | mejor real | controles (media / mín.) | p |
|---|---|---|---|---|
| micénico | 0,100 | 0,071 | 0,074 / 0,062 | 0,60 |
| hitita | 0,181 | 0,108 | 0,109 / 0,104 | 0,40 |
| hurrita | 0,198 | 0,102 | 0,106 / 0,092 | 0,60 |
| luvita | 0,220 | 0,107 | 0,103 / 0,093 | 0,80 |
| hático | 0,233 | 0,092 | 0,104 / 0,091 | 0,20 |
| palaico | 0,207 | 0,111 | 0,120 / 0,117 | 0,00 |
| ugarítico | 0,257 | 0,170 | 0,162 / 0,153 | 1,00 |
| acadio | 0,295 | 0,185 | 0,188 / 0,178 | 0,40 |
| sumerio | 0,322 | 0,195 | 0,212 / 0,195 | 0,00 |
| elamita | 0,275 | 0,179 | 0,190 / 0,188 | 0,00 |
| eteocretense | 0,243 | 0,151 | 0,155 / 0,138 | 0,40 |
| etrusco | 0,360 | 0,235 | 0,222 / 0,212 | 1,00 |

**Réplicas** (10 controles, semilla 1): palaico p=0,70 (no replica; corpus de 883 palabras), sumerio p=0,50 (no replica), **elamita p=0,00** (0,173 contra 0,178 mín. y 0,198 media). Tercera pasada elamita (3.000 pasos, 8 controles, semilla 2): 0,175 contra 0,175 mín. y 0,179 media, p=0,12.

**Lectura:** con 75 valores libres, todo se acerca a todo (ganancias de 0,03 a 0,14), y el minoico real no se acerca más que el barajado a once de doce candidatas. La única excepción es el elamita, que gana en dos pasadas y se estrecha en la tercera cuando el optimizador tiene más presupuesto: compatible con que el orden real converja antes, no más lejos. **No resuelto.** Artefacto posible: el corpus elamita de CDLI es pequeño (1.532 palabras) y formulaico (aquemenida), un objetivo de baja entropía que puede favorecer al orden real, también formulaico, sobre el barajado. Control pendiente: un objetivo ajeno del mismo tamaño y entropía.

**Corrida grande (Mac):** `PYTHONPATH=. python scripts/value_search.py --steps 10000 --controls 20 --seed 3 --only elamite` (unos 20 minutos). Si la ventaja desaparece con presupuesto, se cierra; si se mantiene con 20 controles, es la primera señal fonológica que no pasa por el filtro del B y hay que mirar la asignación que la produce.

**Pidgin:** la marca medible de un pidgin (léxico de varias fuentes) se probó como bimodalidad fonotáctica del léxico: 0,066 observado contra 0,057 de media y 0,069 de máximo en un nulo de una sola población (p=0,05). Sin señal clara de mezcla. La otra marca (morfología reducida) no discrimina en un corpus contable.

**Tipos de nódulo:** la sigla GORILA lleva el tipo principal; 858 de 866 nódulos con signo de HT son Wa (un agujero). El subtipo de Hallager (colgante, cúpula, cono, pirámide) es lo que falta y solo está en el vol. II.

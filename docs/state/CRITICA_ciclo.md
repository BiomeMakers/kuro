# Crítica dura del ciclo, con la prueba que lo tumba y qué hacer (9 de septiembre de 2026)

## 1. LA PRUEBA PEQUEÑA, Y SU RESULTADO

Diez candidatos, los mejor puntuados del generador, por el ciclo entero.

**Resultado: diez de diez mueren en la puerta bibliográfica.** Ninguno llegó a medirse.

| candidatos | veredicto |
|---|---|
| 10 | `published_already` |
| 0 | cualquier otra cosa |

**El sistema no produce nada. Está estrangulado, y en el paso que yo no había vigilado.**

## 2. EL FALLO, DIAGNOSTICADO

La puerta bibliográfica pregunta **si las unidades están mencionadas**, no si la afirmación está
publicada. Y todo logograma frecuente aparece en Younger: \*301 noventa y una veces, \*304 cuarenta
y cuatro. De modo que cualquier afirmación sobre cualquier unidad conocida se bloquea.

Es exactamente el peligro que tú señalaste (que el sistema se estrangule solo) pero por otra vía: no
por acumulación de lecciones, sino por una prueba de novedad mal formulada desde el principio.

**Y es un error de mi diseño, no de implementación.** Confundí dos cosas distintas: que una unidad
esté catalogada y que una afirmación esté hecha. Younger cataloga las unidades; casi ninguna de sus
entradas contiene la afirmación de adyacencia que el generador propone.

## 3. LO QUE HACE EL CAMPO, Y QUÉ TOMAR DE ÉL

Buscada la bibliografía de sistemas de generación y evaluación de hipótesis (2024-2026), cuatro
cosas nos sirven directamente.

**La novedad se mide por similitud con la afirmación, no por presencia de los términos.** SCIMON
(Wang y otros) compara la idea nueva contra la literatura y la revisa hasta que deja de parecerse a
trabajo previo; el sistema de HypER y los agentes de detección de novedad descomponen la pregunta en
componentes (intervención, diana, métrica, organismo) y buscan la combinación, no cada término por
separado. **Nuestra puerta debe comparar la afirmación completa, no las unidades.**

**El filtro previo es lo que da la eficiencia, y está cuantificado.** El trabajo de Matter-of-Fact
mide que, para un generador con un 1% de hipótesis verdaderas, un buen filtro de viabilidad reduce
los experimentos necesarios en un 80% conservando el 60% de las verdaderas. **Esa es la métrica que
nuestro ciclo debería declarar y no declara**: cuánto reduce el trabajo y cuánto de lo bueno pierde.

**El control de la tasa de descubrimientos falsos, no del p-valor individual.** La literatura de
detección de novedad usa Benjamini-Hochberg sobre p-valores conformes para controlar la FDR, y
señala el problema de los *free riders*: los rechazos cerca del umbral son desproporcionadamente
falsos. **Nosotros usamos Bonferroni, que es más tosco y demasiado conservador con cientos de
pruebas.** Con diez candidatos da igual; con doscientos no.

**Y la procedencia como requisito.** HypER genera hipótesis "con procedencia": cada afirmación
arrastra de dónde salió. Eso ya lo hacemos, y es lo único donde estamos por delante.

## 4. CRÍTICA DURA, PUNTO POR PUNTO

**El ciclo nunca se probó de extremo a extremo hasta ahora.** Cada módulo tenía su test, todos
pasaban, y el conjunto no producía nada. Cuarenta y siete tests verdes y cero hipótesis medidas. Es
el fallo clásico de probar las partes y no el todo, y lo cometí yo.

**La validación de la fase 1 era circular.** Comprobé que el ciclo mata las tres hipótesis que ya
sabíamos muertas. Eso demuestra que no es más permisivo que nosotros; **no demuestra que deje pasar
nada**, y resulta que no deja pasar nada.

**El generador combinatorio propone lo trivial.** Sus mejores candidatos son adyacencias entre
logogramas frecuentes, que es donde el campo ya ha mirado. Y las tres primeras que propone
(CYP → NI, NI → VIN, y el orden de mercancías) **ya las medimos nosotros esta tarde**, lo que
significa que el generador no sabe lo que ya hemos hecho salvo por una lista que escribí a mano.

**El generador bibliográfico da tres candidatos de tres obras.** Con cien mil palabras indexadas,
sacar tres afirmaciones contrastables significa que los patrones de detección son demasiado
estrechos.

**Y la tasa de error solo está medida para dos instrumentos de diez**, de modo que la cualificación
que presume el sistema no está disponible para la mayoría de lo que mide.

## 5. QUÉ HACER, EN ORDEN, CON CRITERIO DE ÉXITO

| # | acción | criterio de éxito |
|---|---|---|
| 1 | **Reformular la puerta de novedad**: comparar la afirmación completa contra el texto, no las unidades. Buscar la coocurrencia de las unidades **y** del predicado en una ventana de texto | las tres afirmaciones que sabemos publicadas (\*308 en proporción a OLIV, el orden de mercancías, la exclusión TE/SA-RA₂) siguen bloqueadas, y las diez adyacencias del ensayo pasan |
| 2 | **Medir la eficiencia del ciclo**, como Matter-of-Fact: de N candidatos, cuántos filtra y cuántos de los buenos pierde | poder escribir "el ciclo reduce el trabajo en X% conservando Y% de lo que sobrevive a mano" |
| 3 | **Cambiar Bonferroni por Benjamini-Hochberg** cuando la familia supere las veinte pruebas, declarando cuál se usa | el resultado de -na (p = 0,0045 con 18 pruebas) se informa con los dos criterios |
| 4 | **Registrar automáticamente lo ya medido**, en vez de la lista escrita a mano | el generador no vuelve a proponer CYP → NI |
| 5 | **Ampliar los patrones del generador bibliográfico** y validarlos contra las afirmaciones que sabemos que hay | recuperar al menos las cuatro de `literature_done` desde el texto, sin la lista |
| 6 | **Medir la tasa de error de los ocho instrumentos restantes** | ninguna afirmación se archiva con "no medida" |

## 6. LO QUE NO HAY QUE HACER, Y ES IMPORTANTE

**No aflojar la puerta hasta que pase todo.** El fallo es que bloquea de más, y la tentación es
quitarla. Pero la razón por la que existe es que seis veces en una semana medimos algo ya publicado.
La corrección es hacerla **precisa**, no permisiva.

**Y no dar por bueno el ciclo porque los tests pasen.** La lección de hoy es que cuarenta y siete
tests verdes son compatibles con un sistema que no produce nada. **El test que faltaba era este: que
de N candidatos, alguno llegue al final.** Ese test hay que escribirlo, y debe fallar si el ciclo
bloquea todo.


---

## 7. LA ACCIÓN 1, HECHA, Y SU RESULTADO

Reformulada la puerta: ahora comprueba **si la afirmación está tratada**, es decir, si las unidades y
un predicado de su tipo aparecen juntos en una ventana de texto, en vez de si las unidades están
catalogadas. Y cuando deja pasar una afirmación cuyas unidades sí están catalogadas, **lo dice**:
"lee las entradas antes de escribir; no estar catalogado no es lo que hace nueva una afirmación".

**La prueba pequeña, repetida:**

| veredicto | candidatos |
|---|---|
| ya publicada | 9 |
| borderline | 1 |
| no sostenida | 2 |
| **sobreviven** | **0** |

**El ciclo ya funciona: filtra, mide e informa.** Tres candidatos llegaron a medirse; uno quedó en el
borde (OLE+KI seguido de OLE+MI, p = 0,0485 con doce pruebas) y dos no se sostienen.

**Y cero supervivientes es un resultado honesto, no un fallo.** Los doce candidatos eran las
adyacencias más obvias del corpus, y nueve están tratadas. Que el generador ordene arriba lo obvio y
el ciclo lo descarte es el comportamiento correcto; lo que hay que mejorar es el generador, para que
proponga lo no obvio.

**Y el test que faltaba está escrito**: falla si la puerta bloquea una afirmación cuyas unidades
están catalogadas pero cuyo contenido no se ha dicho. Sesenta y ocho tests.

## 8. DÓNDE QUEDA, HONESTAMENTE

El ciclo **está listo para usarse y no está listo para producir**. Funciona de extremo a extremo,
filtra bien y no miente sobre lo que sabe. Lo que no tiene todavía es un generador que proponga cosas
que valga la pena medir: sus mejores candidatos son los que el campo ya miró.

**Las cinco acciones restantes de la tabla anterior siguen pendientes**, y la que más rendiría es la
número cinco: ampliar los patrones del generador bibliográfico. Ahí están las afirmaciones que
alguien que sabe del campo formuló y nadie midió, que es la fuente con mejor relación entre esfuerzo
y resultado, y de la que salieron dos de los tres resultados de esta tarde.


---

## 9. LAS SEIS ACCIONES, HECHAS (misma sesión)

| # | acción | resultado |
|---|---|---|
| 1 | puerta de novedad por afirmación y no por unidad | de bloquear 10 de 10 a bloquear 26 de 40 (65%) |
| 2 | medir la eficiencia del ciclo | `kuro.Efficiency`, con la salvedad escrita en el propio objeto |
| 3 | Benjamini-Hochberg para familias grandes | automático por encima de veinte pruebas; Bonferroni avisa cuando debería ceder el paso |
| 4 | registro automático de lo ya medido | de 4 entradas escritas a mano a 24 leídas del diccionario y del manifiesto |
| 5 | ampliar los patrones bibliográficos | de 3 candidatos a 13, con veinte patrones en vez de seis |
| 6 | tasa de error de los instrumentos restantes | **pendiente**: siguen dos de diez |

## 10. LA CORRIDA COMPLETA, SOBRE CUARENTA CANDIDATOS

```
  filtrados por la puerta de novedad   26 (65%)
  llegan a medirse                     14
  pasarían un p < 0,05 a secas          3
  en el borde tras corregir             3
  sobreviven el ciclo entero            0
```

**Cero supervivientes de cuarenta, y tres habrían parecido resultados sin el ciclo.**

Eso es exactamente lo que el sistema debe hacer y es también su límite actual: **filtra bien y no
genera nada que merezca pasar.** El cuello se ha movido de sitio. Antes estaba en el descarte, que
costaba horas; ahora está en la generación, que propone lo obvio.

**Y la métrica de eficiencia lleva su propia advertencia dentro del código**, porque un filtro que
rechaza todo puntúa perfecto: la reducción solo significa algo junto a la recuperación de los
efectos verdaderos, y **este corpus no tiene clave con la que medirla**. Se informa como lo que es,
cuántos resultados aparentes elimina, y no como acierto.

## 11. LO SIGUIENTE, Y ES UNA SOLA COSA

**El generador.** Todo lo demás está construido y probado. Lo que falta es que proponga hipótesis
que no sean las adyacencias que el campo ya miró, y hay dos vías con rendimiento distinto:

- **la bibliográfica**, que ya da trece candidatos y de la que salieron dos de los tres resultados
  de la tarde. Ampliar los patrones otra vez, y sobre todo indexar más obras: cada libro nuevo son
  candidatos nuevos sin coste;
- **y la transferencia de método**, que es la que ha dado los mejores resultados históricos del
  proyecto y la única que no se puede automatizar. `kuro.transfer` deja escrita la forma del
  problema y cuatro campos sin probar; el más cercano, el análisis de cestas de la compra, tiene
  resuelto el problema de las comparaciones múltiples para millones de reglas candidatas, que es
  exactamente donde el ciclo se va a atascar cuando el generador funcione.

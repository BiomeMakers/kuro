# Auditoría de soporte estadístico: estado y lo que queda (13-sep)

## Por qué existe este documento

Una cifra calculada sobre **cinco permutaciones** se citó durante tres días como firme, se usó en dos artículos y se envió por correo a una especialista. Rehecha con veinte controles se movió un punto entero: el etrusco de −3,2 a −2,1 y el luvita de 2,3 a 0,7, siendo el luvita el dato que se había dado como favorable a la hipótesis anatolia.

El fallo no fue de la medida sino de la **contabilidad de la medida**: el manifiesto guardaba el p-valor y no lo que lo sostiene. Con 55 p-valores en circulación, nadie podía saber, mirando el manifiesto, cuáles descansaban en cinco muestras y cuáles en dos mil.

## Lo hecho

**Campo nuevo en el manifiesto, `p_value_support`:** para cada p-valor, el n, las repeticiones y qué prueba se aplicó. **Declarados 35 de 55.**

**El comprobador lo exige.** `scripts/check_manifest.py` avisa ahora de los p-valores sin soporte declarado y de los que descansan en menos de quince observaciones o cien repeticiones.

**Los siete frágiles, identificados:**

| p-valor | n | repeticiones |
|---|---|---|
| group_c_quantity_stability | 5 | 5.000 |
| sign_307_header_frame | 5 | — |
| group_c_parties_vs_varieties | 6 | — |
| sign_309_not_bulk | 10 | — |
| tg_stem (dos entradas) | 11 | 400 |
| acronym_hypothesis | 11 | 2.000 |

Comprobado que **los que aparecen en los artículos ya llevan su aviso en el texto**: el tema tG va siempre con "no signal" y el p corregido, el grupo C dice expresamente que no decide, y la estabilidad de cantidades declara que son cinco entradas.

**Marcada como provisional** la tabla de las trece candidatas en los artículos 02 y 07, y corregida la afirmación de que el luvita es la más alta.

## Lo que queda, con su coste

**1. Los veinte p-valores sin soporte declarado.** Hay que ir al código de cada medida y anotar n, repeticiones y prueba. Son: aromatics_capture_correlation, cypd_fixed_quantity, eight_pairs_vs_same_series, entries_ju_ending, los tres etruscan_genitive, los dos montecchi_logograms, no_military_in_linear_a, objects_vs_null, qe_suffix_pairs, room_within_series, series_within_room, shared_units_closer_than_null, star305_capture_correlation, toponyms_span_archives, toponyms_strict_stems, toponyms_vs_null y toponyms_vs_random_mycenaean. **Dos o tres horas.**

**2. El valuesearch completo.** Corriendo con veinte controles. Al terminar, actualizar la tabla en el 02 y el 07 y quitar el aviso de provisionalidad. **Media hora.**

**3. Las 110 cifras del manifiesto que no aparecen en ningún artículo.** Comprobar si es porque se midieron y no se usaron, que es inocuo, o porque se usaron con otra redacción, que impide verificarlas. **Una hora.**

## La regla que este episodio deja

**Cuando un resultado se corrige, hay que rastrear todas sus menciones y no solo el párrafo donde se midió.** Las dos incoherencias internas encontradas hoy en el artículo 07 (la cuenta de bits vieja conviviendo con la nueva, y \*309 descrito como no analizado cuando se había analizado) venían exactamente de no hacerlo.

Y la que debería haber estado desde el principio: **ninguna cifra entra en un artículo sin declarar cuántas observaciones y cuántas repeticiones la sostienen.** Es el requisito 1.2.3 de nuestro propio protocolo, y no lo estábamos cumpliendo.


---

## Resolución de la auditoría (misma noche)

Al leer los artículos uno a uno en lugar de cruzarlos automáticamente, el diagnóstico se invierte.

**Los cincuenta y nueve p-valores que aparecen en los nueve artículos declaran su soporte en el propio texto**, sin excepción: *"12 de 17 atestaciones, tasa base 0,405"*, *"frente a 8,0 esperadas, 500 repeticiones, máximo 14"*, *"16 de 26 casos frente al 25%"*, *"600 repeticiones, máximo del nulo 18"*, *"800 repeticiones, espera 34,4 cruces, mínimo 22"*, *"0 de 105 tablillas frente a 41 de 205"*. Cada cifra publicable lleva su n, su nulo y, donde procede, sus repeticiones y el máximo del nulo.

**Los quince "no recuperables" no corresponden a afirmaciones de ningún artículo.** El manifiesto es el catálogo de todo lo medido en dos meses, incluidas medidas descartadas que nunca llegaron a un texto. Entre ellas el p de 2,5·10⁻⁹⁷ sobre logogramas militares, que me había alarmado y que **no aparece en ninguna parte**.

**El único fallo que sí llegó a los artículos es el del valuesearch**: z calculados sobre cinco controles y citados tres días como firmes. Está marcado como provisional en el 02 y el 07, corregida la afirmación del luvita, y la repetición con veinte controles está corriendo.

### Lo que queda, redimensionado

1. **Limpiar el manifiesto**: retirar las entradas huérfanas o marcarlas como descartadas. Es higiene de un índice interno, no afecta a nada publicable.
2. **Cerrar el valuesearch** cuando termine la corrida.
3. **Las 110 cifras del manifiesto sin aparición en artículos**: misma naturaleza que el punto 1.

### Lo que este episodio deja como regla

El manifiesto guardaba resultados sin guardar lo que los sostiene, y eso hizo imposible distinguir de un vistazo una cifra firme de una frágil. Ahora el campo `p_value_support` existe y el comprobador lo exige. **Pero la lección de fondo es la contraria a la alarma inicial: los artículos estaban bien escritos, y fue el índice el que no permitía verificarlo sin leerlos enteros.**

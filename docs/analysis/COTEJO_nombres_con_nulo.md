# Cotejo de nombres Lineal A / Lineal B con nulo (10-sep, tarde)

**Prior art:** Godart 1984 (vía Younger 2024): nombres presentes en A y en B: A-TI-KA, DA-I-PI-TA, I-JA-TE, I-TA-JA, KI-DA-RO, PA-I-TO, SE-TO-I-JA, SU-KI-RI-TA, quizá A-RA-KO. Sin nulo. Lo nuestro es el nulo.

**Instrumento:** kuro/names.py, NameMatcher. Tres grados (exacta, raíz = palabra del B menos su última sílaba, próxima = una sílaba distinta). Léxico del B: 1.338 palabras de corpus_all (parcial; el léxico completo del B ronda las 5.500 formas).

**Hallazgo previo al resultado:** el campo `words` de lineara.xyz conserva el signo de rotura (𐝫) y `transliteratedWords` lo pierde. **276 de las 783 unidades silábicas están rotas en todas sus atestaciones (35%)**; el diccionario no lo marcaba y ahora lleva `intact`. Tres de las ocho coincidencias del primer pase eran rotas (A-RU-RA-[, ]MA-TE-RE, A-TA-NA-[) y se cayeron.

**Tres nulos**, todos sobre las 507 unidades íntegras: sílabas barajadas, barajadas por posición, y generadas por un modelo de bigramas de sílabas del propio Lineal A (300 repeticiones):

| longitud | exactas observadas | nulo bigramas | p |
|---|---|---|---|
| 2 sílabas | 8 | 6,4 | 0,31 |
| 3 sílabas | 3 | 1,0 | 0,083 |
| 4+ sílabas | 2 | 0,00 (máx 1) | <0,003 |

Raíz y próxima: azar en todas las longitudes. Las coincidencias de dos sílabas son azar puro.

**Las cinco:** SU-KI-RI-TA y SE-TO-I-JA (cuatro sílabas, firmes), PA-I-TO, DA-MA-TE, I-JA-TE (tres sílabas, borde). Archivadas: tres establecidas (topónimos, Godart + nulo), DA-MA-TE disputada (Owens a favor; Duhoux 1997 y Davis 2024 en contra), I-JA-TE propuesta (Younger: I-JA + -TE).

**Observación no medible aún:** de las coincidencias con léxico "griego" del B, Atena, Deméter y arura son palabras que los helenistas sospechan de sustrato; iater y mater no. Con un léxico del B etiquetado por etimología (Beekes) sería una prueba: las coincidencias A/B deberían concentrarse en el sustrato si el minoico no es griego. La lista pregriega del corpus es toponímica y no sirve.

**Pendiente:** el léxico completo del B (DĀMOS / LiBER) subiría observadas y nulo a la vez; el resultado se recalcula, no se extrapola.

## Con el léxico completo del B (linearb.xyz, 5.234 formas), mismo nulo, 300 reps

| longitud | observadas | nulo | p |
|---|---|---|---|
| 2 sílabas | 44 | 55,7 | 0,96 |
| 3 sílabas | 8 | 3,85 | 0,040 |
| 4+ sílabas | 3 | 0,06 | <0,003 |

**Por tipo de la palabra del B (3+ sílabas):** topónimos 3 / 0,24 (p<0,003); nombres de persona 3 / 0,95 (p=0,07); lexemas 2 / 0,54 (p=0,11); sin traducción 3 / 2,1. **El exceso está entero en los topónimos.** Las coincidencias A/B son geografía compartida, no lengua. Recuperada la lista de Godart 1984 completa: da-i-pi-ta, i-ta-ja, ki-da-ro, pa-ra-ne. Archivados los tres primeros como nombres compartidos (propuestos, p=0,07 al nivel del grupo).

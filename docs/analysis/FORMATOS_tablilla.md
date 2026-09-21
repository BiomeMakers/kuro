# Los formatos de tablilla, aprendidos del corpus (12-sep)

**De dónde viene el método.** El descubrimiento de motivos (MEME, Bailey y Elkan 1994; los HMM de perfil de HMMER y Pfam) resuelve en bioinformática el problema que aquí teníamos a mano: encontrar patrones conservados con posiciones variables en pocas secuencias, sin saber qué significan. La fórmula votiva la fijamos leyendo; los formatos administrativos no los había enumerado nadie.

**Cómo.** Cada tablilla pasa a ser una secuencia de categorías funcionales: W palabra silábica, C signo de mercancía, N cifra, f fracción, T término de suma, L signo suelto, | separador. Los n-gramas recurrentes se cuentan contra un nulo de Markov de orden 1 que conserva las frecuencias de categoría y las transiciones entre ellas, de modo que un motivo cuenta solo si el orden lleva información que las transiciones no explican. 308 tablillas, 80 corridas del nulo. Implementado en `kuro/formats.py` con sus tres tests.

**Fallo corregido por el camino:** la edición escribe algunos valores como aproximaciones ("≈ ¹⁄₆") y mi clasificador no los reconocía como fracciones, lo que generaba un motivo espurio (C.C.C sobre HT 23a y HT 91). Arreglado antes de leer nada.

## El control positivo: el procedimiento recupera lo que fijamos a mano

**W | L | C N**, siete apariciones contra 0,48 esperadas, en HT 6a, 14, 17, 19, 21 y más. Es la plantilla de transacción que fijamos el 10 de septiembre leyendo (SA-RO 𐄁 TE 𐄁 VIN), y el procedimiento la encuentra sin que se le diga y **la extiende por los dos lados**: delante la parte (W) y detrás la cantidad (N). La plantilla completa del recibo es *parte, separador, término de transacción, separador, mercancía, cantidad*.

## Cuatro formatos más, ninguno descrito antes como género

| motivo | apariciones | nulo | documentos | qué es |
|---|---|---|---|---|
| **W f W f W f** | 6 | 0,01 | HT 8a, HT 98a, PE 2 | lista de partes, cada una con una cantidad fraccionaria y sin mercancía nombrada: TA-NA-TI ¾, DI-RE-DI-NA ½, TE-*301 ¾, RO-KE ½ |
| **C f C f C f** | 14 | 0,14 | HT 23a, 35, 50a, 91, **KH 8, KH 15** | lista de mercancías, cada una en fracciones: CYP+D ½, NI ½, GRA ½, *304 ¼. Dos de los seis son de Khania, y es el formato que su archivo practica |
| **W N f W N f** | 5 | 0,45 | HT 9a, 19, 36, 104 | lista de partes con cantidad mixta (entero y fracción) |
| **\| W \| W C N** | 5 | 0,19 | HT 28b, 96a, **KH 5, KH 7a** | dos palabras separadas antes de la mercancía: encabezado y parte, o parte y calificativo |

**Lo que esto añade al inventario.** No lecturas nuevas, pero sí lo que faltaba en la parte del archivo: el corpus administrativo tiene al menos cinco plantillas distinguibles, y una de ellas (C f C f C f) es la de Khania, lo que confirma por una segunda vía independiente que ese archivo tiene formato propio. Las tres tablillas del formato W f W f W f (HT 8a, HT 98a, PE 2) son un género que no se había tratado como tal: partes con asignaciones fraccionarias sin mercancía, es decir, el registro más parecido a un reparto de raciones que hay en el corpus, y viene de tres sitios distintos.

**Lo que no hace.** No dice qué significa ninguna posición. Da la plantilla, que es lo que el inventario usa para fijar funciones, y las cinco plantillas son ahora cinco contextos donde buscar, en lugar de uno.

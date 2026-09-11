# Corrida dirigida por unidad (10-sep, tarde; read_units.py en el Mac del usuario)

**Entrada:** 133 unidades sin leer con 3+ atestaciones; 447 pasajes de las 42 obras que las mencionan (4 por unidad como máximo). **Lector:** claude-sonnet-4-6, 447 llamadas.

**Salida del lector:** 196 proposiciones, 154 sin proposición, **97 rechazadas por nombrar unidades que no existen en el corpus (22% de los pasajes).** Esa cifra es la que decide si el modelo puede pasar de leer a proponer: una de cada cinco veces inventa la unidad.

**Ciclo (cycle_units.py):** puerta de novedad, enrutado (perfil / adyacencia / coocurrencia), corrección por lote.
- Prior art (ya publicado, a archivar con cita): la mayoría. Casi todas son constataciones ("A-KA-RU aparece como encabezado en HT 2.1"), no lecturas. El lector convierte cualquier frase en proposición aunque no afirme nada contrastable.
- Sin instrumento: 60 ("aparece solo en HT", "aparece una vez").
- Medidas: 11. **Sobreviven 4** (OLE+DI con OLE+MI, tres veces la misma afirmación, p<0,001; *131B compatible con líquido). Fallan 7 (coocurrencias y adyacencias de nombres que la fuente dice y el corpus no sostiene; QA2+[?]+PU no es agrícola por perfil).

**Fallo del ciclo corregido:** las hipótesis con p=0 salían como "fail" porque Lessons exige controles (baseline, leakage, genre) que el script no anotaba. Ahora se anotan con su nota honesta.

## Archivado a partir del prior art, con prueba propia
Encabezados (primera posición contra base 11,8%, 14 candidatos, Bonferroni 0,0036): **A-DU** 7/10 (p<0,0001), **A-KA-RU** 3/3 (0,0016), **KA-PA** 4/6 (0,0024) establecidos; DA-QE-RA 2/3 (0,039) y KI-RI-TA₂ 2/2 (0,014) propuestos al borde. No pasan: *560, SI+SE, *326, PA-DE, TA-NA-TI, DA-RE (0 en primera posición: la fuente los llama encabezado por otra razón o en otro sentido).
**TU** calificador de la familia del olivo (OLE 3, OLIV 3: dos mercancías, la regla). **OLE+TA** grado de aceite fino (5/5 fracciones, p=0,0008). **OLE+DI y OLE+MI** grados de aceite emparejados (coocurrencia p<0,001). ***131B** variante del vino.
No fijados: KI+MU (3 apariciones), "*304 siempre entre OLE y OLIV" (6 de 25: falso como está dicho).

**Recuento: 48 leídas** (18 al empezar la tarde).

## Lo que enseña sobre el enjambre
El lector no propone; constata. Para que el modelo proponga hace falta un prompt distinto (dado el perfil de la unidad y sus paralelos, formular una lectura con refutación) y un filtro de unidades inventadas antes del ciclo, que ya existe (los 97 rechazos). La tasa de invención del 22% con el prompt de lectura es el número de partida.

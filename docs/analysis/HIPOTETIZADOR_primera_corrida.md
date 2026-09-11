# El modelo propone: primera corrida (10-sep, noche; propose_units.py en el Mac del usuario)

**Entrada:** 124 unidades sin leer (3+ atestaciones, íntegras), un dosier por unidad (cifras y fracciones contra la base, posición, compañeros ya leídos, sitios, soportes, sello y motivo en nódulos, en qué mercancías va como sílaba añadida, paralelo en el B). **Modelo:** claude-sonnet-4-6, 124 llamadas, una por unidad.

**Salida:** 108 propuestas, 15 "no lo sé", **1 unidad inventada (0,8%)**. Con el dosier delante, la invención cae del 22% del lector al 1%: el dato principal de la corrida. Clases propuestas: calificador 40, encabezado 17, total 12, básico 9, nombre 9, fina 8, líquido 4, tela 4, grano 3, personas 2. Confianza: baja 53, media 51, alta 4.

**Juez (cycle_proposals.py), corrección por 84 pruebas direccionales:** sobreviven 6, compatibles 13 (perfil en la base: no es evidencia), al borde 5, fallan 73, sin instrumento 11 (los nombres).

**Fallo corregido en el juez:** la regla del calificador contaba como mercancía cualquier signo delante del "+"; con eso KA "calificaba" a E, MI y RO-VIR (monogramas). Restringido a signos de mercancía, de 15 supervivientes quedan 6.

**Archivado:** PA (califica GRA, CYP, *304: nuevo), KA (VIN+KA, VIR+KA: nuevo), CYP+D (cyperus en cantidades mínimas: nuevo), y las sílabas KU, KI, RA con su función de calificador, que estaba en las ligaduras y no en la sílaba. JE-DI encabezado al borde. **55 leídas.**

**Lo que enseña:** las propuestas del modelo son genéricas ("X es un alimento básico, probablemente higos, aceitunas o..."): encaja cada unidad en la descripción de clase más parecida al dosier. Confunde la ligadura con el calificador (propone "OLE+U es un calificador" cuando el calificador es U). Donde acierta es donde la regla es mecánica y el dosier ya la contiene. Su aporte real ha sido **el enrutado a escala**: elegir una clase por unidad para 124 unidades en ocho minutos, con un 1% de invención, y dejar que el juez haga el resto. No ha propuesto nada que el proposer determinista no hubiera encontrado con las mismas reglas; ha encontrado tres cosas que el proposer determinista no tenía codificadas (PA, KA, CYP+D) porque nadie había mirado.

## Segunda corrida (10-sep, noche; dosier con posición, prompt corregido)
117 unidades; 102 propuestas, 14 "no lo sé", 1 inventada. Clases: básico 24, encabezado 19, líquido 12, nombre 12, fina 8, total 8, calificador 7, grano 6, tela 4, personas 2. La corrección del prompt funcionó: "calificador" cae de 40 a 7 y ya no se propone para ligaduras.

**Juez (52 pruebas direccionales, umbral 0,0010): sobreviven 0.** Compatibles 30 (no es evidencia), al borde 4 (VIR+[?] como categoría de personas 1/20 fracciones; QA2+[?]+PU fina 4/5; SA-RU total 1/2; A-SE encabezado 2/3), fallan 48, categoría "entrada de lista" 4 (MA-DI, DA-ME, PA-DE, DI-DE-RU), sin instrumento 16.

**Lo que dice:** con las mismas reglas y las mismas unidades, la segunda vuelta no encuentra nada. Las seis de la primera eran lo que quedaba. **El inventario interno está en su techo práctico: 56 leídas**, y no se mueve sin dato nuevo (tipos de nódulo, corpus ibérico, léxico externo) o sin instrumento nuevo. Las cuatro al borde no se archivan: 0,01-0,04 a secas con 52 pruebas es lo que el azar produce.

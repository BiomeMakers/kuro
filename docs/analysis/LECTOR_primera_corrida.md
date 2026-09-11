# Primera corrida real del lector con modelo (10-sep, tarde, en el Mac del usuario)

48 pasajes del regex en 42 obras; claude-sonnet-4-6; 48 llamadas. Resultado del lector: 4 proposiciones, 38 sin proposición, 6 rechazadas. Las cuatro las paró la puerta de novedad (ya publicadas o afirmaciones documentales no contrastables con nulo: "atestiguado solo en Chania"). Cero llegaron a un nulo. Cero supervivientes, como se esperaba (a mano esta mañana: 26 pasajes, 7 proposiciones, 1 útil).

**Lo que se probó:** el ciclo funciona de punta a punta sin persona en medio: regex → lector → puerta de novedad → nulo → corrección → archivo, con JSON auditable (data/derived/literature_run.json).

**Fallo encontrado, de dos capas:** el regex tomó "301" de "Weilhartner 2014, 301–2" (una página) por el signo *301, y el lector convirtió "el logograma del azafrán no está documentado en Lineal A" en "*301 (crocus)". Corregido: los números de signo exigen asterisco o prefijo AB/A; los pasajes bajan de 48 a 35. Registrado en manifest.json (reader_failures).

**Lo que sí dio el pasaje, leído a mano:** NI es el logograma de los higos en el B porque ni- es la primera sílaba de la palabra no griega, presumiblemente minoica, con la glosa de Ateneo (νικύλεον, "higo" en cretense: Neumann 1962). NI estaba sin leer en el diccionario; archivado como establecido, con perfil (34% fracción, máximo 62) paralelo al NI del B. **38 leídas.** Y el mismo pasaje cierra *904 como azafrán: el campo dice que el logograma del azafrán no está en Lineal A.

**Escala:** el regex es estrecho (35 pasajes en 1,7 millones de palabras). Con el lector validado, el siguiente paso es abrir el regex a los comentarios por tablilla de Ventris y Chadwick, el Companion y los New Documents, que es donde hoy ha rendido el paralelo con el B (ganado, mercancías, NI, TE).

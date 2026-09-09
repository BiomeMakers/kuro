# Cómo hacer el inventario comparado con los archivos coetáneos (plan operativo, 6 de septiembre de 2026)

Objetivo: aplicar el inventario de clase cerrada (el mismo de PROTOTIPO_recibo_comparado.md) a los archivos administrativos que Creta pudo conocer por el comercio en los siglos XV-XIII: Ugarit, Alalakh, Nuzi, Hattusa, más Mari y las cartas de Amarna como contexto. La pregunta que decide: ¿verbalizan la transferencia ("recibió", "por mano de") y la fecha, como Ur III, o las delegan en sellos, como Creta?

## Qué se puede descargar hoy, y qué no

| fuente | qué contiene | estado |
|---|---|---|
| BDTNS | 101.389 tablillas administrativas de Ur III, transliteradas | YA DESCARGADO (vía el repositorio COMPASS de N. Veldhuis, GitHub) y ya analizado |
| MTAAC gold corpus (cdli-gh) | tablillas de Ur III anotadas morfológicamente en CoNLL | descargable desde GitHub; útil para separar lemas de nombres propios |
| CDLI | catálogo y transliteraciones de todos los periodos, incluidos Alalakh, Nuzi y Amarna | descargable con el script que ya usamos (data/fetch.py de kuro), cambiando el filtro de periodo |
| ORACC (json de cada proyecto) | corpus editados con lematización: SAAO, RINAP, DCCLT, y para nuestro caso el proyecto de textos de Ugarit y los de Nuzi si existen | el servidor build-oracc no está en la lista de dominios permitidos de esta máquina; SÍ se descarga desde un navegador normal |
| Textos de Ugarit (RS, alfabéticos y acadios) | ediciones en KTU/CAT y en PRU; digitalizados parcialmente en ORACC y en el proyecto de Wilfried Watson | requiere petición o conversión manual |
| Archivo de Hattusa (CTH) | catálogo Konkordanz de Maguncia, transliteraciones en línea | descargable página a página; hay un volcado en el proyecto hethiter.net |

## El camino más corto, en tres pasos

1. **Alalakh y Nuzi desde CDLI, con el script que ya tienes.** Son los dos archivos administrativos coetáneos de Creta que están en CDLI con transliteración. Basta cambiar el periodo en `data/fetch.py`: "Middle Babylonian (ca. 1400-1100 BC)" para Alalakh IV y Nuzi, y filtrar por procedencia en el catálogo (`provenience` contiene "Alalakh" o "Nuzi"). Son unos pocos miles de tablillas, y salen en el mismo formato ATF que ya sabemos leer. Esto lo puedes hacer en diez minutos y yo lo analizo igual que Ur III.
2. **ORACC desde tu navegador.** Entra en oracc.museum.upenn.edu/doc/opendata, descarga el zip JSON del proyecto que interese y me lo subes; el parser está escrito en los cuadernos de Veldhuis que ya tengo aquí y lo adapto. Lo más valioso sería un proyecto con lematización, porque da los lemas y separa los nombres propios, que es justo el trabajo que en Ur III tuve que hacer a mano.
3. **Hattusa y Ugarit, por petición.** Los dos tienen equipos activos (hethiter.net en Maguncia; el proyecto de Ugarit en varias sedes). Es el mismo tipo de correo que el de Hesperia: quién eres, qué mides, qué ofreces. No urge: con Alalakh y Nuzi ya tendríamos dos archivos del Bronce Reciente en el área de contacto.

## Qué mediría exactamente

Para cada archivo, lo mismo que en los cuatro que ya tenemos: número de tokens y de tipos, tasa de hapax, clase cerrada (palabras en N o más documentos), cobertura de esa clase, y presencia o ausencia de las cinco funciones (total, transferencia, responsabilidad, fecha, medida). El resultado va a una tabla de seis o siete columnas que es, en sí misma, el artículo: la primera tipología comparada de la forma del recibo en el Mediterráneo oriental del Bronce, medida y no descrita.

## Y la predicción, escrita antes
Si Creta adoptó el modelo de la práctica levantina, Alalakh y Nuzi deberían mostrar la transferencia y la fecha delegadas en sellos o poco verbalizadas, como Creta. Si, como espero, las verbalizan igual que Ur III, la conclusión es que el modelo minoico es propio y que lo que Creta tomó del Oriente fueron mercancías y palabras de mercancía (sésamo, comino), no la forma de la contabilidad.

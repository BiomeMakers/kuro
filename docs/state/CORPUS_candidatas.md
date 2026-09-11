# Corpus de las lenguas candidatas: qué se puede bajar y de dónde (10 de septiembre de 2026)

Para la comparación sistemática del minoico contra todas las candidatas, con mezclas. El formato
común ya existe (`kuro.Normalizer`, esqueleto consonántico con pérdida declarada); esto es la lista
de lo que hay que meter en él.

---

## 1. LAS CUATRO DE CDLI: un script las baja

`scripts/fetch_candidates.py` descarga el volcado ATF completo de CDLI (github.com/cdli-gh/data, CC
BY 4.0) y filtra por lengua:

| lengua | código CDLI | familia | por qué candidata |
|---|---|---|---|
| **sumerio** | sux | aislada | corpus enorme; una propuesta reciente lo defiende |
| **acadio** | akk | semítico oriental | más cercano en el tiempo a Creta que el ugarítico |
| **elamita** | elx | aislada | la otra gran aislada de la zona |
| **hurrita** | xhu | hurro-urartiano | la propuesta de van Soesbergen, el libro que tienes |

```
PYTHONPATH=. python scripts/fetch_candidates.py            # las cuatro
PYTHONPATH=. python scripts/fetch_candidates.py hurrian    # una
```

Van a `data/raw/candidates/`, que está en `.gitignore`. El script tarda uno o dos minutos por el
tamaño del volcado, y deja escrita la procedencia junto a cada fichero.

**Aviso:** la URL del volcado es la documentada hoy; si CDLI la mueve, cdli.earth/downloads tiene la
vigente. El script lo dice al fallar.

---

## 2. LUVITA: hay corpus y es de calidad, pero no se descarga en bloque

**ACLT2, Annotated Corpus of Luwian Texts** (luwian.web-corpora.net), de Ilya Yakubovich y Timofey
Arkhangelskiy. Contiene los textos jeroglíficos de la edición de Hawkins (CHLI) y los cuneiformes de
Starke (StBoT 30), es decir, **todo el luvita conocido**, con transcripción y transliteración en
paralelo.

**Es un corpus de consulta, no de descarga.** El propio sitio desaconseja citarlo directamente y
remite a **eDiAna** (ediana.gwi.uni-muenchen.de, Universidad de Múnich), que es el diccionario
etimológico de las lenguas anatolias menores y tiene los mismos textos enlazados a sus atestaciones.

**Cómo conseguirlo:** escribir a Yakubovich (el correo está en la página del corpus) explicando el
uso, que es exactamente lo que el proyecto quiere fomentar. O extraer las formas desde eDiAna, que
además cubre **licio, cario, sidético y pisidio**, cuatro anatolias menores que también son candidatas
por geografía.

---

## 3. HÁTICO: el corpus es mínimo y está en Hittite

El hático es el sustrato preindoeuropeo de Anatolia central, y es candidato por lógica: si el
minoico es un sustrato egeo, el hático es el sustrato anatolio vecino. **Pero su corpus es pequeño**
(unos cuantos cientos de palabras en textos bilingües hático-hitita) y **no tiene edición digital
propia**: está dentro del corpus hitita de Mainz (hethiter.net, el Hethitologie-Portal), marcado
como lengua.

**Cómo conseguirlo:** el portal de Mainz permite buscar por lengua; los textos háticos salen con la
etiqueta correspondiente. Es trabajo de extracción manual, unas horas, y merece la pena solo si la
comparación con las candidatas grandes deja abierta la vía del sustrato.

---

## 4. LAS QUE FALTAN Y SU ESTADO

| lengua | familia | corpus | acceso |
|---|---|---|---|
| eblaíta | semítico oriental | en CDLI, dentro del acadio (Ebla) | con el script, filtrando por sitio |
| egipcio | afroasiático | TLA, Thesaurus Linguae Aegyptiae, Berlín | consulta; hay volcados por petición |
| chipro-minoico | sin descifrar | corpus de Olivier 2007 y Ferrara | pequeño; ya hay un trabajo de 2022 que lo reclasifica |
| licio, cario, sidético, pisidio | anatolio menor | eDiAna | consulta; pedir a Múnich |
| urartiano | hurro-urartiano | CDLI tiene algo; ECUT en Múnich | con el script si está etiquetado |

---

## 5. EL ORDEN

**Primero las cuatro de CDLI**, que son un comando y dan los corpus grandes. **Luego el luvita por
correo**, que es la candidata clásica y la que más veces se ha propuesto. El hático y el resto,
cuando las primeras seis hayan pasado por el formato común y la comparación diga si la vía del
sustrato sigue abierta.

Con las cuatro de CDLI más las seis que ya tenemos son **diez lenguas en el mismo formato**, y eso
basta para la primera comparación sistemática y para la mezcla.

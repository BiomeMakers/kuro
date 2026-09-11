# Luo y Barzilay: el código de desciframiento y el corpus ibérico, gratis (10-sep, noche)

**Lo que el usuario buscaba (PidginUNMT)** no sirve: traducción no supervisada que exige corpus grandes, una lengua destino conocida y una semilla bilingüe. dfhoughton/pidgin es una librería de Rust sin relación.

**Lo que sí sirve, de la misma búsqueda:**

1. **j-luo93/NeuroDecipher** (ACL 2019, "Neural Decipherment via Minimum-Cost Flow: from Ugaritic to Linear B"). Código completo y datos: 920 pares cognados Lineal B–griego (`linear_b-greek.cog`, y la versión solo con nombres), 43.952 ugarítico–hebreo, y dos ficheros crudos: `linear_b.el.raw` (1.398 formas del B con su griego) y `linear_b.minoan.raw` (1.344 formas del B en transliteración). Es el instrumento de afinidad por cognados que el campo tiene validado (Ugaritico→hebreo, B→griego), y con nuestro nulo delante sería el segundo juez, independiente de la fonotaxis, para las trece candidatas.

2. **j-luo93/DecipherUnsegmented** (TACL 2021, "Deciphering undersegmented ancient scripts using phonetic prior"). Código parcial (los módulos centrales sin limpiar), pero con lo importante: **`data/iberian.csv`, 2.094 inscripciones ibéricas de Hesperia, limpias, con referencia Hesperia por inscripción**: 2.378 formas distintas, 3.779 apariciones. Es el corpus que se le pidió a Orduña el 10-sep. Copiado a data/raw/iberian/ con el cuaderno de limpieza del autor.

**Estado:** datos guardados en data/raw/neurodecipher/ y data/raw/iberian/. Nada corrido todavía. NeuroDecipher exige PyTorch y tres paquetes propios del autor; se instala y se corre en el Mac, no aquí.

**Lo que abre:**
- Ibérico: kuro entero se puede aplicar (aplicó ya al etrusco): frecuencias, plantilla, fórmula de los plomos, nulos, y el mismo cotejo de nombres contra el vasco y contra los antropónimos de la Turma Salluitana (bilingüe latina real). Es un tercer corpus de prueba del protocolo, con una bilingüe parcial que el Lineal A no tiene.
- Lineal A: correr NeuroDecipher A→cada candidata (con el B→griego como calibración de lo que "funcionar" significa) y un nulo (A barajado → candidata). Si el B→griego da X y A→todas da lo que el nulo, la vía por cognados queda cerrada como la fonotáctica; si alguna sale, es señal nueva.

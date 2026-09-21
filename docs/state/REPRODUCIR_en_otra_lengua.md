# Cómo repetir todo esto en otra lengua en horas (12-sep)

## Lo que había y lo que faltaba
El paquete tenía los instrumentos sueltos y una clase `Document` con tres cargadores, pero cada análisis leía el corpus crudo a su manera. Aplicarlo a una lengua nueva era rehacer el pegamento. Ahora hay un guion que encadena los siete pasos en el orden que el trabajo sobre el Lineal A tardó dos semanas en encontrar.

## El uso
```
python scripts/survey.py linear_a
python scripts/survey.py iberian
```
Cinco minutos por corpus. La salida es un informe con todas las cifras y sus nulos, y un JSON en `data/derived/surveys/`.

Añadir una lengua es una entrada en `CORPORA`: un cargador que devuelva documentos y un `CorpusProfile` con los hechos propios de esa lengua (qué signos son mercancías, cuáles son términos de suma, cuál es el separador, qué unidades están rotas, qué lista de nombres externa hay, qué corpus candidatos). Todo es opcional: el paso que no tiene su material se salta y lo dice, en vez de adivinar.

## Los siete pasos, y por qué ese orden
1. **Inventario e integridad.** Qué hay, y cuánto está roto. Va primero porque todo lo demás se calcula sobre unidades íntegras: en el Lineal A, 306 de 1.305 unidades están rotas en todas sus atestaciones, y no verlo invalida las alternancias morfológicas.
2. **Géneros.** Qué soporte lleva plantilla rígida, contra la tasa base del propio corpus.
3. **Formatos.** Motivos de categorías funcionales contra un nulo de Markov, que es el descubrimiento de motivos de la bioinformática aplicado aquí.
4. **Funciones.** Encabezados, calificadores, totales, subrecuentos.
5. **Morfología.** Terminaciones compartidas por varias raíces, contra un nulo que baraja las terminaciones.
6. **Anclaje.** Una lista de nombres externa (una bilingüe) contra un nulo de bigramas del propio corpus.
7. **Filiación.** Fonotaxis contra lenguas candidatas, con control barajado.

Los pasos 6 y 7 necesitan material de fuera y se saltan si no lo hay. Eso no es un fallo: es la diferencia entre una lengua con anclaje y una sin él, que es el resultado central de este trabajo.

## Las lecciones van dentro del código, no en la documentación
Tres errores nos costaron días y ahora los evita el guion:
- **Documentos de un solo signo fabrican encabezados.** El corpus del Lineal A tiene 886 nódulos con un signo cada uno, y sin filtrar daban ocho encabezados falsos con p=0. El paso 4 excluye documentos con menos de tres unidades, y lo dice en su propio docstring con la fecha.
- **Las marcas de edición no son unidades.** El signo de rotura entraba como la unidad más frecuente del corpus.
- **La unidad decide la razón.** El sistema de terminaciones del ibérico da 4,5 veces el nulo por letra y 1,4 por unidad semisilábica. El informe declara siempre qué unidad usó.

## Verificación: reproduce lo que hicimos a mano
Sobre el Lineal A, el guion recupera sin que se le diga: A-TA-I-*301-WA-JA, A-DU, A-KA-RU, KA-PA y JE-DI como encabezados; los calificadores E, KI, KU, PA, RA, KA y D; las terminaciones -JA, -ME y -TI con razón 3,2; los formatos fCfCf y WfWfW; y la rigidez del soporte votivo. Sobre el ibérico recupera el anclaje del bronce de Ascoli (10 de 23 elementos por encima del nulo, con 1,2 esperados: atin, biuŕ, bilos, sosin, balke, tautin, taker, uŕke), y encuentra encabezados que no habíamos buscado (ŕuba 4 de 4, anbi 3 de 3, ka 8 de 19).

## Lo que el guion no hace
No decide qué pregunta tiene sentido en un corpus nuevo, no elige qué conserva cada nulo, y no ve que un archivo domine el corpus y arrastre una prueba (Hagia Triada es el 64% del Lineal A). Eso sigue siendo trabajo de quien lo usa. El guion ahorra las semanas de pegamento, no el juicio.

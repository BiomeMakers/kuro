# Instrucciones del proyecto Lineal A

Este texto va en las instrucciones del proyecto de Claude, y gobierna cualquier sesión sobre el Lineal A.

## Qué es este trabajo

Medir el Lineal A con nulos explícitos y declarar qué no se puede saber. **No es un intento de desciframiento.** El resultado a 14-sep-2026: 151 lecturas funcionales, cero valores fonéticos nuevos, 30 vías cerradas, 21 retiradas, diez artículos.

## Las ocho reglas, en orden de importancia

**1. Comprobar la bibliografía ANTES de medir, no después.** El 14 de septiembre nueve hallazgos aparentes resultaron estar publicados, y las nueve veces bastó una búsqueda de tres minutos para verlo. Antes de escribir que algo es nuevo, buscar en NESTOR (`scripts/nestor_index.py`), en el léxico de Younger y en `manifest.json > prior_art`. **Que una búsqueda no devuelva nada no significa que sea nuevo: significa que no se ha encontrado con esos términos.**

**2. Todo positivo necesita un control que sepamos que debe dar cero.** Los nulos no bastan: el acadio dio z = +6,88 bajo tres nulos distintos y era basura de transliteración; el eteocretense dio p = 0,0000 bajo tres nulos y lo tumbó comparar contra el griego. El control que funciona es una lengua, un corpus o un caso donde la respuesta se conoce. **El Lineal B es el control por defecto**, porque es el mismo sistema con la lengua conocida.

**3. Un método que no recupera la respuesta conocida donde se conoce no se aplica al Lineal A.** Esa es la regla que cerró el conversor alfabético (85% exigido, 47% obtenido), la ligadura acrofónica (falla en el Lineal B) y el alineador. Se valida primero, se aplica después.

**4. Antes de interpretar una ausencia, comprobar que el instrumento podía haberla visto.** Cuatro estadísticos de flexión detectan la del griego en el 0% de los casos cuando se les dan las 501 unidades que el Lineal A tiene. Un negativo sin potencia no dice nada. Se comprueba submuestreando el Lineal B al tamaño del Lineal A.

**5. Cada afirmación lleva su condición de refutación escrita, o "ninguna".** Es campo obligatorio en el diccionario, y lo que no la cumple no entra. Una afirmación que no se puede refutar no se archiva como resultado.

**6. Toda prueba lleva su regla de parada fijada ANTES de correrla.** Sin ella, la exploración se convierte en buscar hasta encontrar algo, que es exactamente lo que este trabajo mide en las propuestas ajenas: con dos mil hipótesis formulables y un umbral de 0,05, salen cien positivos por azar.

**7. Nada entra en el mapa sin medirse aquí.** Las afirmaciones del campo se citan con su veredicto medido, o se marcan expresamente como no verificadas. Doce medidas hasta hoy: tres confirmadas, tres matizadas, una refutada, una cierta solo para un signo.

**8. Registrar cada retirada con su fecha y su motivo.** Veintiuna hasta hoy, seis de ellas positivos propios que un control destruyó. El registro es lo que hace creíble el resto.

## Lo que está prohibido

Afirmar una lectura fonética. **Usar listas de comparación escritas de memoria** (el 14-sep eso produjo un p = 0,033 que desapareció al usar el corpus). **Dividir por soporte cuando se quiere dividir por género** (los vasos de piedra de Zakros llevan cuentas, no fórmulas). Citar a un autor sin medir su afirmación. Tratar como fuente los blogs que traducen el corpus entero al griego o al semítico. **Reimplementar un método de la casa que ya tiene código**: se usa el del repositorio.

## Los documentos del proyecto

| fichero | qué es |
|---|---|
| `MAPA_DEL_MINOICO.md` | el estado entero, once bloques, cada celda con su medida, su control y su potencia |
| `REGISTRO_cambios.md` | el diario, 122 entradas, con cada retirada fechada |
| `manifest.json` | 560 cifras, 74 p-valores con su soporte declarado, 45 entradas de prior art, 30 vías cerradas, 21 retiradas |
| `PROTOCOL_minimums_v1.0_EN.md` | los diez requisitos mínimos, calibrados en cuatro corpus |
| `nestor_index.json` | la bibliografía egea indexada y clasificada por fiabilidad (pendiente de generar) |

## El estado, en una línea

**Faltan 345 bits, que son 56 anclas o 788 unidades más de texto, y ninguno de los siete muros se quita computando.** La única vía abierta que puede añadir anclas está en manos de un especialista: las ligaduras TELA+KU, OLE+RA y CYP+PA, preguntadas a Palaima el 14-sep.

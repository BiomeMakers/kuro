# Plan de acción (12-sep, tarde), tras leer Tamburini 2025

## Decisión: se para NeuroDecipher y se pasa a CSA_OptMatcher
El uno a uno que corre en el Mac se cancela. Razón: Tamburini (2025) no pudo reproducir los resultados publicados de NeuroDecipher, reporta que parecen máximos tras muchos reinicios, y tuvo que quitar de su entrada información que en un desciframiento real no existe. Nuestro torneo del 11-sep falló por lo mismo. Seguir diez horas más con esa herramienta no producirá un negativo interpretable.

Se sustituye por CSA_OptMatcher, del mismo autor, que para nuestro caso tiene tres ventajas concretas: admite comodines para signos ilegibles (35% de nuestras unidades), admite conocimiento parcial fijado (nuestros dieciséis signos anclados) y está pensado para pocos centenares de palabras por lado.

## Qué corre, y en qué orden (paquete csa_kuro.zip, instrucciones en CORRER.md)

**1. Control positivo sobre nuestros datos.** Lineal A contra micénico, con las anclas fijadas. Sabemos la respuesta. Si el instrumento no converge aquí, se para y se cierra la vía de cognados con ese hecho declarado. Es lo que al torneo le faltó y por lo que su negativo no valía.

**2. El experimento.** Seis candidatas (hitita, luvita, hurrita, ugarítico, etrusco, egipcio), cada una con el minoico real y con el control barajado. Doce corridas. Lo que se compara es la energía final: real contra control, mismos tamaños y mismas longitudes.

**Lo nuestro en todo esto** es el control. Tamburini evalúa contra listas de cognados conocidos; nosotros no tenemos verdad, y el corpus barajado es el comparandum que él mismo echa en falta para los casos reales.

## Lo demás que queda, por quién lo hace

### Mío, escritura
- Citar a Tamburini 2025 en el artículo de las candidatas, y decir en qué se diferencia lo nuestro (el control). Es obligado antes de enviar.
- Citar la controversia Rao / Sproat sobre la escritura del Indo en el artículo del protocolo: es el precedente exacto de una medida estadística sin control que el campo tardó años en deshacer.
- Versiones inglesas de los artículos de envío 02, 03 y 04.
- Recortar nueve palabras del resumen de SMEA (309, el máximo es 300).

### Mío, medida
- HMM de perfil sobre los formatos de tablilla, a partir del descubrimiento de motivos que hoy ha recuperado el patrón de TE y encontrado WfWfW. Es lo único de la lista que puede ampliar el inventario.
- Khania sin terminar: 105 tablillas con repertorio propio que solo han pasado por cuatro pruebas.

### Tuyo
- Correr CSA_OptMatcher (paquete listo).
- **Al terminar el bucle: correr el banco de pruebas de Tamburini** (`-c data/linear_b-greek.cog`), sin el cual el resultado de las candidatas no es interpretable. Ver PENDIENTE_banco_de_pruebas_CSA.md.
- Contestar a Hogan (borrador escrito, con la retirada del punto de las fracciones).
- Escribir a Fabio Tamburini (Bolonia, mismo departamento que Ferrara, fabio.tamburini@unibo.it). Va después de tener el control positivo corrido: se le escribe con un resultado, no con una intención.
- Subir el repositorio (kuro_github_12sep.zip) y hacer el Zenodo.
- Elegir si la fórmula sale a SMEA con el plazo de junio.

## Lo que NO se hace
Más lenguas, más rasgos tipológicos, más corridas del lector o del hipotetizador sobre las mismas unidades, y el torneo. Todo eso está medido y cerrado.

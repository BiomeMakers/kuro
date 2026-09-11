# El survey del campo, leído: dónde encaja nuestro trabajo y qué le falta (10 de septiembre de 2026)

Sommerschield, T., Assael, Y., Pavlopoulos, J. y otros (2023), "Machine Learning for Ancient
Languages: A Survey", *Computational Linguistics* 49, 1-44, doi 10.1162/coli_a_00481.

Con su taxonomía de 253 trabajos clasificados. Es el mapa del campo que nos faltaba, y lo primero
que hace es situarnos.

---

## 1. DÓNDE ENCAJA LO NUESTRO, EN SU VOCABULARIO

Su taxonomía tiene ocho categorías. Nuestro trabajo cae en tres, y **no en la que pensábamos**:

| lo que hacemos | su categoría | trabajos en esa categoría |
|---|---|---|
| la predicción de la fórmula | **Textual restoration** | 13 |
| el perfil de plantilla, la clasificación por contenido | **Word segmentation / Representation learning** | 14 |
| el protocolo de mínimos | **Decipherment** (como crítica) | 16 |

**No estamos en "Decipherment", estamos en "Textual restoration"**, y eso importa porque es la
categoría con evaluación más madura: trece trabajos que se comparan contra líneas base y contra
humanos.

## 2. LO QUE HAY SOBRE LINEAL A EN 253 TRABAJOS: TRES

- **Computational Pattern Recognition in Linear A** (2021), en dos categorías;
- y un trabajo de 2022 sobre cypro-minoico que reclasifica por aprendizaje no supervisado.

**Tres de doscientos cincuenta y tres.** El Lineal A está casi vacío en la literatura de aprendizaje
automático, frente a diez trabajos sobre el Indo y dieciséis sobre desciframiento en general. **Eso
es un hueco real y medido**, y sirve para escribir la introducción de cualquiera de nuestros
artículos.

## 3. CÓMO EVALÚA EL CAMPO LA RESTAURACIÓN, Y ES LO QUE NECESITÁBAMOS

Cuatro prácticas que el survey documenta y que nosotros hacemos a medias:

**La línea base humana.** Pythia da un 30% de error de carácter **frente al 57% de dos especialistas
evaluados**. Ithaca hace lo mismo. Nosotros comparamos contra la tasa base estadística y contra un
nulo, pero **nunca contra un humano**, y ese es el patrón del campo.

**El Top-k, no solo el Top-1.** Pythia informa que en tres de cada cuatro casos la respuesta correcta
está **entre sus veinte primeras propuestas**; Latin BERT da 33% de acierto exacto y muchas más
aciertan en el Top-10. **Nosotros solo informamos el acierto exacto**, que es la métrica más dura y
la que peor nos deja: nuestro 12,1% es un Top-1.

**Las líneas base de n-gramas.** Todos los trabajos se comparan contra un modelo de n-gramas, que es
la línea base estándar de la restauración. La nuestra es "adivinar el elemento más frecuente", que es
más débil y por tanto más fácil de batir.

**Y la escala de dificultad por número de signos perdidos.** Lazar y otros informan que los
anotadores aceptan las restauraciones cuando faltan hasta dos caracteres y solo la mitad cuando
faltan tres. **Nuestro experimento no distingue** entre predecir un hueco fácil y uno difícil.

## 4. LO QUE EL SURVEY PIDE Y NOSOTROS SÍ HACEMOS

Su preámbulo metodológico enumera tres cosas que subraya: la correlación entre dataset y rendimiento;
**la partición en entrenamiento, validación y prueba o el remuestreo**; y **el valor de las pruebas
de significación estadística**, que aseguren que las diferencias observadas no son azar.

**Eso es exactamente nuestro protocolo**, escrito por el campo en 2023 y para el aprendizaje
automático. Y el survey señala que **la falta de "ground truths" hace la evaluación extremadamente
difícil**, que es nuestra tesis central dicha por otros.

## 5. QUÉ HAY QUE HACER CON ESTO, EN ORDEN

**Uno, y es barato: informar Top-k además de Top-1.** Nuestro predictor de la fórmula da 12,1% en
Top-1; ver cuánto da en Top-3 y Top-5 es media hora y es la métrica que el campo espera.

**Dos: añadir una línea base de n-gramas.** Es la línea base estándar de la restauración y es más
exigente que la nuestra. Si nuestro predictor la bate, el resultado vale mucho más; si no la bate,
lo hemos sabido antes que un revisor.

**Tres: separar los huecos por dificultad**, al menos entre los que tienen vecinos conocidos y los
que no.

**Y cuatro, más ambicioso: la línea base humana.** No es imposible: se puede pedir a un especialista
que restaure diez huecos y comparar. Es lo que hicieron Pythia e Ithaca, y es lo que convierte un
resultado estadístico en uno defendible ante el campo.

## 6. Y LA CITA QUE CAMBIA LA INTRODUCCIÓN DE NUESTROS ARTÍCULOS
El survey es de 2023, está en acceso abierto, lo firman diez autores entre ellos DeepMind y Oxford,
y es la referencia obligada del campo. **Ninguno de nuestros artículos lo cita**, y los trece
deberían: sitúa lo que hacemos, nombra la tarea con el término estándar, y documenta que el Lineal A
está casi ausente de esta literatura.

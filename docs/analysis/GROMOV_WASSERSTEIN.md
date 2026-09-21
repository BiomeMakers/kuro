# Alineamiento por estructura relacional (Gromov-Wasserstein): medido y cerrado (12-sep)

**Por qué se probó.** Todas nuestras comparaciones del minoico con otras lenguas pasan por la forma de los signos: la fonotaxis usa los valores del Lineal B, y el emparejamiento de cognados usa distancias de edición entre transliteraciones. Las dos heredan la transcripción, que es el obstáculo declarado en todos los artículos. El transporte óptimo de Gromov-Wasserstein (Alvarez-Melis y Jaakkola, EMNLP 2018) no mira los signos: compara cómo se relacionan entre sí las distancias dentro de un inventario con las distancias dentro del otro. Dos inventarios se alinean si su geometría interna tiene la misma forma, se llamen los signos como se llamen. Era la única vía que escapaba al filtro.

**Cómo.** Perfil distribucional de cada signo (qué lo precede, qué lo sigue, dónde está en la palabra), distancia coseno dentro de cada inventario, y acoplamiento por Gromov-Wasserstein entrópico con proyecciones de Sinkhorn, implementado en `kuro/relational.py` para no añadir dependencias. Tres tests.

**El control positivo es gratis:** el Lineal A y el Lineal B se transliteran con los mismos nombres de signo, así que la correspondencia correcta es la identidad sobre los nombres compartidos y la exactitud se mide sin que nadie dé la respuesta.

## Resultado: el instrumento no tiene potencia a nuestro tamaño

Lineal A (455 palabras íntegras de solo silabogramas) contra el léxico del Lineal B: **2 de 50 signos compartidos correctos (4%)**, lo mismo que el control barajado y lo mismo que el azar (1/50 = 2%). El coste del acoplamiento sí distingue el corpus real del barajado (0,0093 frente a 0,0458), pero eso solo dice que el Lineal A tiene estructura de secuencia, cosa que ya sabíamos y que daría igual contra cualquier lengua real.

**El diagnóstico decide el asunto.** Partiendo el Lineal B en dos mitades, donde la respuesta correcta también es la identidad y las dos mitades son la misma lengua:

| palabras por mitad | aciertos | azar |
|---|---|---|
| 455 (nuestro tamaño) | 10% | 1,5% |
| 1.000 | 15% | 1,5% |
| 2.000 | 23% | 1,4% |
| 2.486 | 25% | 1,4% |

Con el tamaño del corpus del Lineal A, el método **no alinea una lengua consigo misma**: recupera uno de cada diez signos. Y aun con cinco veces más material se queda en uno de cada cuatro. El negativo contra el Lineal B, por tanto, no es interpretable: no dice que no haya relación, dice que el instrumento no ve a esta escala.

## Vía cerrada, con su número
Gromov-Wasserstein a nivel de signo queda cerrado para el Lineal A por falta de potencia, no por resultado. Lo que haría falta para reabrirlo: perfiles más ricos que los de vecino inmediato (contextos de documento, no de palabra), o un corpus cinco veces mayor, que no existe. Se declara aquí con la curva de potencia para que nadie lo repita a ciegas, que es exactamente lo que el artículo del protocolo pide de cualquier procedimiento: medir si el instrumento ve antes de interpretar lo que dice.

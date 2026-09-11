# La tasa de error de nuestros propios instrumentos, y una consecuencia incómoda (9 de septiembre de 2026)

Un p-valor dice cuán sorprendente sería un resultado bajo el nulo. No dice **con qué frecuencia este
instrumento, sobre este material, informa de algo que no está**. Ese segundo número se puede medir,
porque tenemos corpus con respuesta conocida, y es lo que permite escribir un resultado como
"p = 0,01, con un instrumento que da un falso positivo el N% de las veces".

Ninguna propuesta de lectura del Lineal A puede decir eso hoy.

## 1. El método

Correr el instrumento en condiciones donde **no debería encontrar nada** (anclas y terminaciones
tomadas al azar, pares de unidades tomados al azar) y contar cuántas veces encuentra algo igualmente.
Doscientas o cuatrocientas repeticiones por corpus.

## 2. Los resultados

| instrumento | corpus | falsos positivos al 5% |
|---|---|---|
| prueba posicional | etrusco (5.470 textos) | 0,5% |
| prueba posicional | Lineal A | 0,0% |
| **coocurrencia hipergeométrica** | **etrusco** | **1,5%** |
| **coocurrencia hipergeométrica** | **Lineal A** | **9,2%** |

**La prueba posicional es conservadora**: por debajo del 5% nominal en los dos corpus. Cuando dice
que ha encontrado algo, se le puede creer.

**La coocurrencia hipergeométrica, en el Lineal A, es casi el doble de anticonservadora que su valor
nominal.** Al 5% nominal produce un 9,2% de falsos.

## 3. Por qué, y es diagnosticable

La prueba hipergeométrica supone que los documentos son **intercambiables**. En etrusco casi lo son:
5.470 textos cortos y homogéneos. En el Lineal A no: hay yacimientos, géneros y escribas, y dos
palabras del mismo yacimiento coinciden más de lo que la hipergeométrica espera.

Medido directamente:

| pares | falsos positivos al 5% |
|---|---|
| ambas palabras de un solo yacimiento, el mismo | **11,9%** |
| palabras de yacimientos distintos | 6,2% |

**La estructura por yacimiento es la causa**, y explica casi toda la diferencia.

## 4. La consecuencia incómoda, y hay que escribirla

**El bloque de aromáticos se construyó con coocurrencia hipergeométrica**, y sus miembros son en
buena parte de Hagia Triada. Es decir, está construido con el instrumento y sobre el material donde
ese instrumento es menos fiable.

Eso **no invalida el bloque**, por dos razones que conviene decir con precisión:

- las asociaciones del bloque tienen p muy por debajo del umbral (varias por debajo de 0,0001), y un
  instrumento que falla al 9% cuando el umbral es 0,05 no falla al 9% cuando el valor observado es
  0,0001;
- y el bloque tiene apoyos que no vienen de la coocurrencia: la igualdad de fracción entre entradas
  (p < 0,00005), la razón astringente-aceite, la comparación con KAR 220 y el descarte químico de la
  tintorería.

**Pero obliga a dos cosas.** Declarar la tasa junto a las cifras de coocurrencia del artículo. Y
rehacer el bloque con un nulo que conserve el yacimiento, para ver cuáles de sus miembros sobreviven.

## 5. Lo que esto vale como aportación
Es la primera vez que este proyecto puede acompañar un p-valor de la tasa de error del instrumento
que lo produjo, medida y no supuesta. **Y la primera aplicación ha encontrado un problema en nuestro
propio trabajo**, que es exactamente para lo que sirve.

La formulación que ahora se puede usar, y que antes no:

> La asociación entre X e Y da p = 0,0001 con una prueba hipergeométrica que, sobre este corpus y en
> condiciones donde no hay efecto, informa de un falso positivo el 9,2% de las veces al umbral del
> 5%; la anticonservadurismo procede de la estructura por yacimiento, y el nulo emparejado por
> yacimiento se informa aparte.

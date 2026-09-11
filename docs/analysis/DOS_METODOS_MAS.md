# Dos métodos más traídos de fuera: la partición jerárquica y Westfall-Young (10 de septiembre de 2026)

Segunda y tercera transferencia. Las dos funcionan, y las dos han obligado a corregir mi primera
implementación.

---

## 1. La partición jerárquica (genética de poblaciones)

**Qué resuelve.** Ayer el resultado de los campos semánticos murió con un nulo emparejado: barajar
la etiqueta de campo dentro de cada escriba, p = 0,117, retirado. Eso responde **si** el efecto
sobrevive al confusor; no dice **cuánta** variación explica cada nivel.

Los estadísticos F de Wright reparten la variación entre niveles anidados desde 1951. Nuestra
estructura tiene la misma forma: documento dentro de escriba dentro de yacimiento.

**Aplicado al perfil de sílabas de los 462 documentos con palabras:**

| nivel | variación explicada | grupos |
|---|---|---|
| yacimiento | **12,1%** | 42 |
| escriba (dentro de yacimiento) | **13,6%** | 85 |
| **campo semántico** (dentro de escriba) | **4,8%** | 112 |
| dentro del grupo más fino | 69,4% | |

**Y esto dice mucho más que el p = 0,117 de ayer.**

El campo semántico explica el **4,8%** de la variación. El escriba, casi el triple. Y el yacimiento,
dos veces y media. Es decir: **la hipótesis del usuario sobre las herencias del léxico no es que
fuera falsa, es que el efecto que buscábamos es tres veces menor que el del escriba y está anidado
dentro de él.**

Y el dato que enmarca todo lo demás: **el 69,4% de la variación está dentro del grupo más fino**, es
decir, entre documentos del mismo campo, del mismo escriba y del mismo yacimiento. La mayor parte de
la variación de este corpus no la explica ninguna de las tres estructuras que sabemos nombrar.

---

## 2. Westfall-Young, y el fallo que tuve que corregir

**Qué resuelve.** Bonferroni supone pruebas independientes. Las nuestras no lo son: cuarenta
candidatos de adyacencia comparten unidades, de modo que CYP aparece en varios pares. Dividir alfa
entre cuarenta tira potencia que la correlación devolvería.

**Mi primera implementación salió más conservadora que Bonferroni**, lo cual era señal de error.
La causa: usaba el **recuento bruto** como estadístico. Un par que aparece quince veces y otro que
aparece tres no están en la misma escala, así que el máximo de la familia lo fijaban siempre los
pares frecuentes y todo lo demás quedaba aplastado.

**Westfall-Young necesita estadísticos comparables**, es decir, p-valores, cada uno contra su propio
nulo. Corregido con dos pasadas: primero el nulo de cada prueba, luego el mínimo p de la familia en
cada permutación.

**Con la corrección, sobre veinticinco pruebas solapadas:**

| prueba | p bruto | p ajustado | pasa |
|---|---|---|---|
| NI → VIN | < 0,001 | < 0,001 | los dos |
| CYP → NI | < 0,001 | < 0,001 | los dos |
| GRA → OLE | < 0,001 | < 0,001 | los dos |
| **OLE+KI → OLE+U** | 0,0025 | **0,0300** | **solo Westfall-Young** |
| \*304 → OLIV | 0,0100 | 0,1263 | ninguno |

**Una prueba se declara con Westfall-Young y no con Bonferroni:** la adyacencia entre dos aceites
cualificados, OLE+KI seguido de OLE+U. Con Bonferroni el umbral es 0,002 y su p bruto de 0,0025 se
queda fuera por poco; con el ajuste que usa la dependencia entre pruebas, sale.

**Y es un candidato del expediente de aromáticos**, dos calificativos del aceite que van pegados.

---

## 3. Lo que estas dos transferencias enseñan juntas

**Las tres transferencias de hoy han fallado en el primer intento, y por la misma clase de razón:**
importé el método sin comprobar que su supuesto encajaba. El nulo bipartito conservaba grados y el
problema era el yacimiento. Westfall-Young necesitaba estadísticos comparables y le di recuentos.

**Y las tres han funcionado en el segundo**, cuando el supuesto se corrigió.

Eso vale como regla y ya está en el protocolo de transferencia: **un método de otro campo no se
importa, se traduce**, y la traducción falla siempre en el supuesto, no en la fórmula.

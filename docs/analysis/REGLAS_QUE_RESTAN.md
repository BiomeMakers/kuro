# ¿Más reglas cumplidas es más probabilidad? La cuenta dice que depende del tipo de regla (12-sep)

La intuición natural es que cuantas más reglas cumple una lectura, más probable es que sea correcta. Es cierta solo bajo dos condiciones, y conviene separarlas porque en este caso una se cumple y la otra no.

## 1. Una regla suma evidencia solo si prohíbe

Una regla que **prohíbe** posibilidades añade evidencia cuando se cumple: si algo solo podía ocurrir de una manera y ocurrió así, eso es informativo. Una regla que **permite** posibilidades resta evidencia: amplía el conjunto de lecturas que también habrían encajado.

Las reglas de conversión que di Mino declara en §9 son, en su mayoría, permisos. Contadas sobre las 552 unidades silábicas íntegras (1.758 posiciones consonánticas):

| permiso declarado | posiciones afectadas | bits de discriminación que destruye |
|---|---|---|
| la longitud nunca se marca (cada sílaba: larga o breve) | 1.758 | **1.758** |
| las oclusivas no distinguen sonora, sorda ni enfática | 682 | **1.081** |
| las laríngeas a menudo no se escriben | 321 | **745** |
| todas las sibilantes se funden en una serie | 193 | **386** |
| la serie R cubre r y l | 224 | **224** |
| **total** | | **4.194 bits** |

**Cuatro mil ciento noventa y cuatro bits.** Cada uno duplica el número de lecturas semíticas compatibles con el mismo texto minoico. Para poner la cifra en escala: el corpus entero aporta 236 bits de restricción y especificar un desciframiento cuesta 587.

Esto no es un reproche a su método: **es una propiedad del silabario**, y él tiene razón al declararla. Un silabario CV no puede escribir la sonoridad ni el énfasis, y las laríngeas semíticas no tienen signo. Lo que hay que ver es la consecuencia: las reglas no son hallazgos que apoyen la lectura, son el precio que el silabario cobra, y ese precio se paga en evidencia.

## 2. Y las reglas tienen que ser independientes

El segundo requisito es que cumplir una regla no implique cumplir otra. Sus rasgos morfológicos, medidos por separado:

- **mimación**: el Lineal A tiene un 7,1% de finales en m frente al 3,1% del micénico, p = 1,5·10⁻⁷. **Aporta bits de verdad.**
- **conjugación por prefijos**: la medida calibra (semíticas 1,20-1,28; no semíticas 0,89-1,08) y el Lineal A queda en 0,85, pero con un intervalo de 0,54 a 1,16. **Aporta cero bits, o negativos.**
- **encaje léxico**: el 89,1% de las unidades encuentra comparando semítico, y las rejillas ficticias llegan al 97,1%. **Aporta cero bits.**
- **tema tG**: no medible sin presuponer la lectura. **No aporta bits comprobables.**

De los cuatro pilares, **uno aporta evidencia medida y tres no**. Y no se suman: sumar tres ceros al uno que sí cuenta no multiplica nada.

## 3. La respuesta

**No.** Más reglas cumplidas no es más probabilidad, si las reglas son permisivas o dependientes entre sí. Lo que hay que contar no son las reglas sino los **bits**: cuánto más improbable es el conjunto de coincidencias bajo la hipótesis que bajo el azar. Aquí, el balance es 4.194 bits regalados por los permisos del silabario, contra los bits que aporta la mimación, que es el único rasgo con señal medida.

**Y lo que esto no dice.** No dice que su lectura sea falsa. Dice que el número de reglas satisfechas no es el argumento, y que el argumento tiene que estar donde hay bits: en la mimación, y en cualquier otro rasgo que se pueda calibrar contra lenguas de respuesta conocida. Esa es la lista corta, y hoy tiene un elemento.

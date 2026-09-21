# El diseño: qué filtros tenemos, cuánto restringe cada uno, y qué falta para cerrar (12-sep)

Especificar un desciframiento del Lineal A cuesta **587 bits**: 94 signos libres (110 menos los 16 anclados por topónimos) por log₂(74) valores posibles, más la elección de lengua. Todo lo que reduzca el espacio de soluciones se cuenta en la misma moneda. Estos son los filtros que tenemos y lo que vale cada uno.

## Los filtros, medidos

| filtro | qué hace | bits |
|---|---|---|
| **1. Signos anclados** (16, por topónimos compartidos con el Lineal B) | fija valores desde fuera | **ya descontado**: por eso los libres son 94 y no 110 |
| **2a. El corpus con fonología permisiva** (las reglas declaradas por di Mino) | exige que cada unidad encuentre una palabra que le encaje; con esas reglas encaja el 86,4% | **112** |
| **2b. El corpus con fonología estricta** (cada consonante distinta cuenta) | lo mismo, sin regalar las distinciones; encaja el 62,9% | **355** |
| **3. Nuestras 56 funciones** (22 con forma silábica, tocan 29 signos) | exige que la palabra signifique lo que la distribución dice | **146-219** |
| **4. Un léxico glosado** (ORACC: acadio, sumerio, ugarítico) | **no aporta bits**: es el instrumento que permite aplicar el filtro 3 | — |

## Lo que se ve al sumarlos

- **Con su diseño** (fonología permisiva y sin filtro funcional): 112 bits frente a 587. Déficit de 475. Del orden de 2⁴⁷⁵ lecturas compatibles.
- **Con fonología estricta y nuestras funciones**: 355 + 146 = **501 bits** frente a 587. Déficit de **86 bits**: del orden de 2⁸⁶, que sigue siendo enorme pero es 2³⁸⁹ veces menos que lo anterior.
- **Con fonología estricta, funciones y una clase semántica ajustada** (219 bits en vez de 146): 574 frente a 587. Déficit de **13 bits**, es decir, unas ocho mil lecturas.

**Ese es el resultado de diseño.** El problema no se cierra del todo, pero pasa de inabordable a enumerable. Ocho mil candidatas se pueden listar, ordenar y publicar para que otros las examinen; 2⁴⁷⁵ no.

## La decisión que hay detrás, y que hay que declarar

La severidad de la fonología **no es una elección libre**: es una hipótesis sobre la escritura. Si el silabario realmente no distinguía sonoridad, la información no está ahí y ser estricto es hacer trampa. Si sí distinguía y la convención de transliteración la borra, ser permisivo es regalar 243 bits.

Ese es el verdadero punto de decisión de cualquier desciframiento del Lineal A, y hasta hoy nadie lo había puesto en números. Di Mino elige permisivo y lo declara, que es más de lo que hicieron Gordon, Best, Palmer o van Soesbergen. Nosotros podemos correr las dos y publicar ambas, que es lo que el protocolo pide.

## Lo que falta, en orden
1. **Los léxicos glosados de ORACC** (`build-oracc.museum.upenn.edu/json/PROYECTO.zip`, o el paquete `oracc-parser` de PyPI). Sin ellos el filtro 3, que es el nuestro, no se puede aplicar.
2. Correr el cribado con las dos fonologías y las 22 unidades funcionales.
3. Publicar la lista de candidatas que sobreviven, con su cuenta de bits, para que el campo la examine.

Eso no es descifrar. Es convertir un problema con 2⁴⁷⁵ soluciones en una lista que cabe en un apéndice.

# Los campos semánticos tienen perfiles fonológicos distintos: uno de seis pares (9 de septiembre de 2026)

La hipótesis es del usuario: si el léxico minoico tiene herencias distintas, los campos semánticos
deberían sonar distinto, porque un préstamo conserva la fonología de donde viene. Contrastable, y no
publicada hasta donde alcanza el índice de referencia.

## 1. El diseño

Cada grupo de signos se asigna a un campo por los logogramas presentes **en su documento**, no por su
significado, que no conocemos. Cuatro campos con vocabulario suficiente: aromáticos (93 grupos),
personal (91), grano (100) y vino con higos (123). El ganado queda fuera con dos grupos.

Se compara el perfil de sílabas de cada campo con el de los demás por distancia de Jensen-Shannon, y
se contrasta contra un nulo que es lo único que decide: **dos subconjuntos del vocabulario del mismo
tamaño, tomados al azar.** Si dos campos difieren solo por el tamaño de la muestra, el nulo lo
reproduce.

## 2. El resultado

| par | observado | nulo medio | p |
|---|---|---|---|
| **aromáticos vs personal** | **0,1155** | 0,0813 | **0,010** |
| personal vs grano | 0,0932 | 0,0793 | 0,140 |
| personal vs vino/higos | 0,0875 | 0,0715 | 0,110 |
| aromáticos vs grano | 0,0584 | 0,0780 | 0,935 |
| grano vs vino/higos | 0,0458 | 0,0694 | 0,975 |
| aromáticos vs vino/higos | 0,0427 | 0,0708 | 0,995 |

**Un par de seis supera el nulo: aromáticos frente a personal, con p = 0,010.**

Los demás no, y tres de ellos están **por debajo** del nulo, es decir, se parecen más entre sí de lo
que se parecerían dos muestras al azar del mismo vocabulario.

Con corrección de Bonferroni por las seis comparaciones el umbral queda en 0,0083, y el resultado
(0,010) **no lo supera**. Se informa como lo que es: **una diferencia que sobrevive sin corregir y no
con corrección**, en el límite.

## 3. Qué distingue los dos perfiles

| prefiere el vocabulario de aromáticos | prefiere el de personal |
|---|---|
| si, a, ta, ra, i, ne, sa, ki | ti, ni, **pa₃**, ro, ka, di, ru, qe |

El caso más marcado es **pa₃**, que aparece ocho veces en el vocabulario de personal y una en el de
aromáticos. Y conviene notar que pa₃ es precisamente el signo de KU-PA₃-NU y KU-PA₃-NA-TU, los dos
grupos que Younger vincula con antropónimos micénicos (ku-pa₃-no en KN Df 1219B).

**Y el solapamiento es bajo:** de 93 grupos en documentos de aromáticos y 91 en documentos de
personal, solo 22 aparecen en los dos. Setenta y uno son exclusivos de un lado y sesenta y nueve del
otro.

## 4. Cómo hay que leer esto, sin pasarse

**Lo que el resultado no dice.** No dice que el vocabulario de aromáticos sea de origen semítico y el
de personal nativo. La distancia entre perfiles es compatible con eso y con otras tres cosas: que los
antropónimos tengan una fonología propia dentro de la misma lengua (cosa normal en cualquier lengua);
que los dos campos se escribieran en momentos distintos; o que la partición por documento arrastre un
efecto de escriba, ya que los expedientes tienen escribas distintos.

**Ese último confusor es el serio y se puede probar**, porque tenemos las atribuciones de mano de
GORILA V. Si la diferencia desaparece dentro de una misma mano, es efecto de escriba y no de campo.

**Lo que sí dice.** Que de las seis comparaciones posibles, solo una difiere del azar, y es
precisamente la que enfrenta un campo de mercancías con el de personas. Los tres campos de mercancías
(aromáticos, grano, vino) **no se distinguen entre sí en absoluto**, lo que es coherente: si el
vocabulario de mercancías tuviera orígenes distintos por producto, los tres diferirían.

## 5. Qué haría falta para sostenerlo
1. **El control de escriba**, que es la objeción evidente y tenemos los datos.
2. **Repetir con la partición por contenido** en vez de por logograma presente, para que un documento
   mixto no cuente en dos campos.
3. Y declarar la corrección múltiple, como arriba.

Es un resultado de los que hay que publicar con su límite escrito: **una diferencia en el borde de la
significación, con un confusor sin descartar.**

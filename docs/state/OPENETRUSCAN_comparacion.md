# OpenEtruscan frente a nosotros: qué hacen igual, qué hacen mejor, y qué aportamos (9 de septiembre de 2026)

Leídos su sitio, su repositorio y sus notas de versión. Es el proyecto vivo que más se parece al nuestro en método, y conviene situarse con precisión.

---

## LO QUE HACEN IGUAL

**Preregistro de métricas.** Su protocolo de evaluación está preregistrado, con enmiendas documentadas cuando cambia. Nosotros preregistramos el experimento del microbioma, el de RCAEval y el de la fórmula.

**Intervalos de confianza por bootstrap** en todo resultado computacional. Nosotros usamos nulos de permutación, que es el equivalente para nuestro tipo de afirmación.

**Retractación pública de resultados propios.** Retiraron un clasificador que afirmaba un 99% de F1 macro, y la nota de retractación está en la tarjeta del modelo, en el repositorio y en la web; el número retirado no aparece en ninguna superficie salvo dentro de la propia retractación. Nosotros retiramos la ventana de Ulanowicz, la composicionalidad y la afirmación sobre -so.

**Publicación del negativo con su cifra.** Su nota de la versión 1.3.1 dice que la afirmación de que "ninguna arquitectura se separa del campo" quedó invalidada por un resultado posterior, y lo corrigen en el texto en vez de callarlo.

**Y la honestidad sobre lo que no saben.** Documentan que su base desplegada tiene 701 inscripciones menos que la archivada, que la causa no se puede determinar desde el código de aplicación, y lo dejan escrito como abierto en vez de inventar una explicación. Antes habían dado una explicación equivocada y la corrigen nombrándola como equivocada.

---

## LO QUE HACEN MEJOR QUE NOSOTROS, Y HAY QUE COPIARLO

**Un manifiesto único que la integración continua verifica.** Su `release-manifest.json` es la fuente de verdad de toda versión, recuento, licencia, DOI y estado de modelo que el proyecto afirma en público, y `check_release_truth.py` hace fallar la CI cuando cualquier superficie se desvía. Lo montaron porque una auditoría externa encontró **cuatro números de versión distintos en cuatro sitios públicos y tres totales de corpus sin reconciliar**.

Nosotros tenemos exactamente ese problema y no lo hemos resuelto: las cifras de nuestros artículos, del README de kuro, de la base de precedencia y de los ficheros de análisis no están reconciliadas por ninguna comprobación automática. Cuando corregimos un número en un sitio, los demás quedan a nuestra memoria.

**Licencias declaradas por artefacto y no por repositorio:** código MIT, datos de salida CC BY, datos de entrada CC0, pesos Apache, documentación CC BY. Nosotros tenemos una licencia para todo.

**Y el detalle del `dup_group_id`:** publican el corpus sin deduplicar porque las repeticiones son artefactos reales, y añaden una columna que permite agrupar por texto normalizado, de modo que quien lo use pueda decidir. Es una solución elegante a un problema que nosotros hemos tenido con las tablillas en dos caras.

---

## LO QUE HACEMOS NOSOTROS Y ELLOS NO

**Calibración en corpus con respuesta conocida.** Ellos evalúan sus modelos contra etiquetas de plata de su propio corpus, con validación cruzada. Eso mide si el modelo aprende sus etiquetas, no si el instrumento ve lo que hay. Nuestra calibración es distinta: aplicamos el mismo instrumento a cinco corpus donde el campo ya sabe la respuesta (etrusco, eteochipriota, proto-elamita, Uruk, ibérico) y comprobamos que la recupera. **Son dos cosas distintas y la segunda no está en su trabajo.**

**El nulo emparejado por cantidad global.** Su bootstrap da intervalos de confianza sobre una métrica; nuestros nulos preguntan si la estructura observada sobrevive a conservar los márgenes. Son preguntas distintas, y la nuestra es la que nos hizo retirar dos resultados.

**La curva de potencia por tamaño de corpus.** A qué tamaño empieza a ver cada instrumento, medido comparando corpus de tamaños distintos. No está en su trabajo ni, hasta donde alcanza mi conocimiento, en el de nadie.

**El control de artefacto de captura.** Si una señal viene del objeto o de cómo se recogió el dato. Ellos tienen el problema (su nota sobre el brillo fotográfico no existe, pero su gap de 701 filas es de la misma familia) y no tienen el instrumento.

**Y el protocolo de mínimos.** Ellos aplican estas prácticas a su proyecto; nosotros hemos escrito qué debería declarar cualquier propuesta para ser evaluable. Es la diferencia entre hacerlo bien y proponer un estándar, y la segunda es publicable como tal.

---

## LA COMPARACIÓN, EN UNA TABLA

| práctica | OpenEtruscan | nosotros |
|---|---|---|
| preregistro | sí | sí |
| intervalos de confianza / nulos | bootstrap | nulos de permutación con márgenes fijos |
| retractación pública | sí | sí |
| negativos con cifra | sí | sí |
| **manifiesto verificado por CI** | **sí** | **no** |
| licencias por artefacto | sí | no |
| **calibración en corpus con respuesta conocida** | no | **sí** |
| **curva de potencia por tamaño** | no | **sí** |
| **control de artefacto de captura** | no | **sí** |
| **protocolo declarado como estándar** | no | **sí** |
| corpus publicado con DOI | sí | pendiente |

---

## LAS DOS CONSECUENCIAS PRÁCTICAS

**1. Copiar el manifiesto.** Es la mejor idea que hemos visto en semanas y resuelve un problema que tenemos ahora mismo. Un `release-manifest.json` en kuro con las cifras que los artículos afirman, y una comprobación que falle cuando un artículo diga una cosa y el análisis otra. Entra en `docs/IDEAS.md` con condición: hacerlo antes de publicar, no después.

**2. Citarlos en el artículo de método.** No como fuente de datos, que ya lo son, sino como ejemplo de que estas prácticas existen y funcionan en epigrafía computacional. El protocolo de mínimos gana mucho si puede señalar un proyecto que ya cumple seis de sus ocho requisitos, y que lo hace en otro corpus.

**Y una tercera, que es de tono:** conviene escribirles. Es el segundo proyecto que encontramos (con Briakos) donde alguien de fuera del campo aplica método cuantitativo a una escritura, y el primero que ha montado la infraestructura. Un contacto ahí vale más que muchos correos a especialistas, porque hablan nuestro idioma.

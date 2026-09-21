# PENDIENTE: el banco de pruebas de CSA_OptMatcher (anotado el 12-sep, tarde)

## Qué hay que correr, cuando el bucle diga TERMINADO
```
cd ~/Downloads/csa
python3 CSA_OptMatcher.py -c data/linear_b-greek.cog -f data/FixNULL -n 2 -m 1 -d cpu 1> LOG_bench 2> LOGE_bench
```
Una hora aproximadamente. Es el banco de pruebas del propio Tamburini (Lineal B contra griego micénico, 919 pares de cognados), donde su artículo reporta 89,4% de aciertos.

## Por qué, y por qué no puede saltarse
Las doce corridas de candidatas comparan minoico real contra minoico barajado. Esa comparación es válida sin saber si el instrumento acierta, porque trata igual a los dos. Pero **si ninguna candidata baja por debajo de su control, el resultado admite dos lecturas**: que no hay parentesco, o que el instrumento no ve nada a este tamaño de corpus. El banco de pruebas separa las dos:
- si reproduce el 89%, la instalación y los parámetros son correctos y el negativo es del minoico: publicable;
- si sale muy por debajo, el negativo es nuestro y no se reporta.

Es la misma disciplina que cerró Gromov-Wasserstein esta mañana: medir si el instrumento ve antes de interpretar lo que dice.

## Error de diseño que quedó registrado
El 12-sep se corrió como control positivo el Lineal A contra el micénico con dieciséis anclas fijadas, esperando que el sistema recuperara la correspondencia de signos, que es la identidad por construcción de la transliteración. Dio **1 acierto de 38 signos libres (3%, el azar)**. Eso NO mide la potencia del instrumento: el método busca la asignación que hace coincidir los dos léxicos, y si no hay cognados entre los dos corpus (que es lo que cuatro vías ya habían establecido) la correspondencia correcta no produce ninguna ventaja. Es una quinta medición del mismo negativo, no un control. El control tenía que hacerse sobre un par con cognados conocidos, que es exactamente el banco de pruebas.

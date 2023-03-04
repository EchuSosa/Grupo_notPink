# The Picture

MISC, 5 points

## Description

![](../images/description-the-picture.jpeg)

## Solution

Nos brindan una imagen:

![](./recurso/challenge.png)

Aparentemente la imagen no contiene información relevante, por lo tanto suponemos que podría contener un mensaje oculto. Usando el comando zsteg verificamos que hay un mensaje oculto.

![](../images/command-the-picture.png)

Realizamos un script que ejecuta el comando y nos muestra la flag oculta:

![](../images/script-the-picture.png)

Reto completado:

![](../images/congratulations-the-picture.png)

Realizamos un script genérico que se puede utilizar con cualquier archivo png y con un diccionario que incluye las partes de la flag conocidas:

![](../images/script-the-picture-actualizado.png)

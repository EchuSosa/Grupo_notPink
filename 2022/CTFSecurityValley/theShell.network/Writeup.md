# The Shell

NETWORK, 5 points

## Description

![](../images/description-the-shell.jpeg)

## Solution

Nos brindan un archivo que contiene una captura de tráfico de red:

![](../images/pcap-the-shell.png)


Al observarla no notamos nada relevante. Por lo tanto ejecutamos el comando strings sobre el archivo, filtrando con grep "{", ya que sabemos que el formato de la flag contiene "{".

![](../images/command-the-shell.png)


Realizamos un script que ejecuta los comandos y nos muestra la flag oculta en los strings del archivo:

![](../images/script-the-shell.png)


Reto completado:

![](../images/congratulations-the-shell.png)

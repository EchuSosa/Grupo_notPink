# The Data

NETWORK, 10 points

## Description

![](../images/description-the-data.jpeg)


## Solution

Nos brindan una captura de tráfico de red:

![](../images/pcap-the-data.png)


Al observarla notamos que hay un paquete HTTP que hace un GET a una dirección.

![](../images/get-http-the-data.png)


Buscamos la respuesta al GET y notamos que devuelve una imagen PNG:

![](../images/200-ok-the-data.png)


Descargamos la imagen PNG y vemos que contiene la flag:

![](../images/flag.png)


Realizamos un script que ejecuta los comandos necesarios para extraer la imagen PNG desde la captura, obtener la flag que contiene, y abrir la imagen con la aplicación predeterminada por el sistema. El script muestra por consola un aproximado de la flag obtenida desde la imagen:

![](../images/script-the-data.png)


Reto completado:

![](../images/congratulations-the-data.png)

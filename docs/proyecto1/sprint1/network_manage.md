# Configuracion de red

## Metodo 1
Pulsamos en el icono de red.

![01](sources/imagenes/network_manage/1.png)

Pulsamos en el icono de la tuerca.

![02](sources/imagenes/network_manage/2.png)

Otra vez pulsamos en el icono de la tuerca.

![03](sources/imagenes/network_manage/3.png)

Pulsamos en la opción IPV4.

![04](sources/imagenes/network_manage/4.png)

Marcar opción manual para luego asignar IP, máscara de red, puerta de enlace y dns.

![05](sources/imagenes/network_manage/5.png)

Pulsamos en el botón de aplicar por último, activar y desactivar cableado.

![06](sources/imagenes/network_manage/6.png)

Abrir un terminal y escribir ip a para comprobar que ha cambiado.

![07](sources/imagenes/network_manage/7.png)

## Metodo 2

Abrimos un terminal.

![01](sources/imagenes/network_manage/8.png)

Ir al directorio/etc/netplan ejecutando el comando cd /etc/netplan

![02](sources/imagenes/network_manage/9.png)

Ejecutamos ls para listar los archivos y ahora ejecutamos sudo rm -rf 90-NM-1eef7e45-3b9d-3043-bee3-fc5925c90273.yaml

![03](sources/imagenes/network_manage/10.png)

Ahora toca editar el archivo 01-network-manager-all.yaml ejecutando sudo nano 01-network-manager-all.yaml

![04](sources/imagenes/network_manage/11.png)

Editamos para que quede así.

![05](sources/imagenes/network_manage/12.png)

Pulsamos ctrl + x.

![06](sources/imagenes/network_manage/13.png)

Pulsamos la tecla s.

![07](sources/imagenes/network_manage/14.png)

Por ultimo pulsamos enter.

![08](sources/imagenes/network_manage/15.png)

Para aplicar los cambios ejecutamos el comando sudo netplan apply.

![09](sources/imagenes/network_manage/16.png)

Por ultimo ejecutamos ip a.

![10](sources/imagenes/network_manage/17.png)



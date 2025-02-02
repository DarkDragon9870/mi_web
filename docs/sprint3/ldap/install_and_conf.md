# Instalacion y configuracion

LDAP es un servidor que te permite gestionar diversos dispositivos mediante un dominio.

## Instalacion
Abrimos una terminal con ctrl ctrl + alt + t y ejecutamos el comando.
```
ip a
```
![1](sources/imagenes/install_and_conf/1.png)
o en caso de tener instalado net-tools.
```
ifconfig
```
![2](sources/imagenes/install_and_conf/2.png)
Pulsamos en el icono de red.

![3](sources/imagenes/install_and_conf/3.png)

Pulsamos en la flecha al lado de cableado.

![4](sources/imagenes/install_and_conf/4.png)

Pulsamos en configurar de red cableada.

![5](sources/imagenes/install_and_conf/5.png)

Pulsamos en la tuerca.

![6](sources/imagenes/install_and_conf/6.png)

Pulsar en IPV4

![7](sources/imagenes/install_and_conf/7.png)

Pulsamos en manual

![8](sources/imagenes/install_and_conf/8.png)

Asignamos la direccion del ip a o ifconfig, mascara de red, puerto de enalce y DNS

![9](sources/imagenes/install_and_conf/9.png)

Pulsar en aplicar.

![10](sources/imagenes/install_and_conf/10.png)

Desconectar el interruptor y volverlo a conectar. En caso de hacerlo en un server abria que modificar un archivo del /etc/netplan y ejecutar el comando ```sudo netplan apply```

![11](sources/imagenes/install_and_conf/11.gif)

Volvemos abrir el terminal editamos el archivo hostname

![12](sources/imagenes/install_and_conf/12.png)

Guardamos los cambios del archivo.

![13](sources/imagenes/install_and_conf/13.png)

Ahora tocara editar el archivo /etc/hosts.

![14](sources/imagenes/install_and_conf/14.png)

en el 127.0.1.1 cambiamos el hostname antiguo al que hemos puesto tambien agregamos una nueva linea con la ip, dominio y hostname de la maquina.

![15](sources/imagenes/install_and_conf/15.png)

Guardamos el archivo y reiniciamos la maquina.

![16](sources/imagenes/install_and_conf/16.png)

Descargamos el archivo y lo extraemos.

![17](sources/imagenes/install_and_conf/17.png)



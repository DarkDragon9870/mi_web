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

Descargamos el archivo del moodle y lo extraemos.

![17](sources/imagenes/install_and_conf/17.png)

Abrimos la terminal y ejecutamos un update.

![18](sources/imagenes/install_and_conf/18.png)

Ahora instalamos ldap ejecutando el siguiente comando:

```
apt install slapd ldap-utils
```

![19](sources/imagenes/install_and_conf/19.png)

Ponemos la contraseña del administrador.

![20](sources/imagenes/install_and_conf/20.png)

Volvemos a poner la contraseña.

![21](sources/imagenes/install_and_conf/21.png)

Ejecutamos este comando para ver si se instalo bien

```
slapcat
```

![22](sources/imagenes/install_and_conf/22.png)

## Configuracion

Ahora ejecutamos el siguiente comando.

```
dpkg-reconfigure slapd
```

![23](sources/imagenes/install_and_conf/23.png)

Pulsamos no

![24](sources/imagenes/install_and_conf/24.png)

Pulsamos enter y saldra este menu.

![25](sources/imagenes/install_and_conf/25.png)

ponemos el nombre de la organizacion.

![26](sources/imagenes/install_and_conf/26.png)

En el siguiente menu pondremos la contrsae de administrador.

![27](sources/imagenes/install_and_conf/27.png)

Pulsamos enter y en el siguiente menu volvemos a poner la misma contraseña

![28](sources/imagenes/install_and_conf/28.png)

Aparecera el siguiente menu cuando pulsamos enter.

![29](sources/imagenes/install_and_conf/29.png)

Selecionamos en si y pulsamos enter.

![30](sources/imagenes/install_and_conf/30.png)

Pulsamos enter.

![31](sources/imagenes/install_and_conf/31.png)

Ahora ejecutamos ```slapcat``` para comprobar que esta bien configurado.

![32](sources/imagenes/install_and_conf/32.png)

Vamos a los archivos descargados y lo editamos.

![33](sources/imagenes/install_and_conf/33.png)

cambiamos los dc por el nuestro en los archivos siguientes:

uo.ldif:

![34](sources/imagenes/install_and_conf/34.png)

grup.ldif:

![35](sources/imagenes/install_and_conf/35.png)

usu.ldif:

![36](sources/imagenes/install_and_conf/36.png)

Guaradamos y ejecutamos el siguiente comando para añadir los archivos:

```
ldapadd -c -x -D "cn=admin,dc=lo_que_has_puesto,dc=nombre_de_dominio" -W -f nombre_archivo.ldif
```

ou.ldif:

![37](sources/imagenes/install_and_conf/37.png)

grup.ldif:

![38](sources/imagenes/install_and_conf/38.png)

usu.ldif:

![39](sources/imagenes/install_and_conf/39.png)

Para comprobar que todo funciono bien volvemos a ejecutar slapcat.

![40](sources/imagenes/install_and_conf/39.png)

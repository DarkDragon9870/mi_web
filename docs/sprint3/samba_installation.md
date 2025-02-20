# Instalar y configurar samba server

## Instalar

Primero ejecutar un sudo apt update.

![01](sources/imagenes/samba_server/1.png)

Una vez hecho el update instalamos el samba

![02](sources/imagenes/samba_server/2.png)

![03](sources/imagenes/samba_server/3.png)

Una vez instalado vamos a la carpeta raiz, creamos una carpeta y ejecutamos estos comandos

```
sudo mkdir hola

sudo chown nobody:nogroup carpeta que has creado

sudo chmod -R 777 carpeta creada

sudo chmod -R 777 carpeta creada

ls -l | grep carpeta creada
```
![04](sources/imagenes/samba_server/4.png)

## Configuracion

Ahora iremos a editar el archivo smb.conf y agregaremos las siguientes lineas.

![05](sources/imagenes/samba_server/5.png)

Guardamos los cambios y reiniciamos el samba.

![06](sources/imagenes/samba_server/6.png)

Ahora creamos los usuarios y grupo.

![07](sources/imagenes/samba_server/7.png)

Ahora ejecutamos el comando.

![08](sources/imagenes/samba_server/8.png)

Creare un archivo de prueba.

![09](sources/imagenes/samba_server/9.png)

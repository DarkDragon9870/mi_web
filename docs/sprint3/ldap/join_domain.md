# Unir al dominio

Ejecutamos un sudo apt update.

![01](sources/imagenes/join_domain/01.png)

Ahora ejecutamos el comando

```
apt install libnss-ldap libpam-ldap nscd
```
![02](sources/imagenes/join_domain/02.png)

Pulsamos enter y saldra este menu. Tendremos que poner ldap//tu_ip.

![03](sources/imagenes/join_domain/03.png)

Pulsamos enter.

![04](sources/imagenes/join_domain/04.png)

cambiamos el example y el net por lo que hemos puesto.

![05](sources/imagenes/join_domain/05.png)

Pulsamos enter.

![06](sources/imagenes/join_domain/06.png)

Volvemos a pusar enter.

![07](sources/imagenes/join_domain/07.png)

volvemos a puslar enter otra vez

![08](sources/imagenes/join_domain/08.png)

Otra vez enter.

![09](sources/imagenes/join_domain/09.png)

Marcamos si y luego pulsamos enter.

![10](sources/imagenes/join_domain/10.png)

Saldra este menu donde cambiaremos el manager por admin y el dc por lo que hemos puesto.

![11](sources/imagenes/join_domain/11.png)

En el siguiente menu tendremos que poner la contraseña que hemos puesto en ldap.

![12](sources/imagenes/join_domain/12.png)

En el siguiente menu cambiamos toca cambiar el proxyuser por otro usuarios como solo tengo un usuario usare el admin pero en un caso real se tiene que usar otro.

![13](sources/imagenes/join_domain/13.png)

Pulsamos en enter y en el siguiente menu ponemos la contraseña.

![14](sources/imagenes/join_domain/14.png)

Una vez configurado iremos al archivo nsswitch.conf y lo editaremos paraque ubuntu consulte los usuarios de ldap.

![15](sources/imagenes/join_domain/15.png)

Guardamos el archivo y ahora editaremos el archivo common-session.

![16](sources/imagenes/join_domain/16.png)

Por ultimo editaremos el archivo 50-ubuntu.conf para poder iniciar sesion on el usuario de ldap.

![17](sources/imagenes/join_domain/17.png)

Si queremos comprobar que el usuario existe hacemos un getent passwd

![18](sources/imagenes/join_domain/18.png)

Reiniciamos la maquina para aplicar los cambios y ahora podremos iniciar sesion con el usuario tanto desde terminal como interfaz grafica.

Terminal

![19](sources/imagenes/join_domain/19.png)

Interfaz grafica:

Estando en el menu de incio de sesion usaremos la opcion no esta en la lista.

![20](sources/imagenes/join_domain/20.png)

Escribimos el usuario y pulsamos enter.

![21](sources/imagenes/join_domain/21.png)

Escribimos contraseña.

![22](sources/imagenes/join_domain/22.png)

Si todo a salido bien habras accedido al alu1.

![23](sources/imagenes/join_domain/23.png)










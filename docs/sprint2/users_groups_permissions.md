# Gestion de usuarios, grupos y permisos.

## Usuarios

Al ejecutar este comando se abrira el archivo password y podras ver los usuarios.
```
nano /etc/passwd
```
![01](sources/imagenes/users_groups_permissions/1.png)
Al ejecutar este comando podras ver las contraseñas. 
```
nano /etc/shadow
```
![02](sources/imagenes/users_groups_permissions/2.png)
Al ejecutar este comando podras ver las contraseñas de las contraseñas. 
```
nano /etc/gshadow
```
![03](sources/imagenes/users_groups_permissions/3.png)
Este comando permite añadir usuarios.
```
useradd usuario
```
![04](sources/imagenes/users_groups_permissions/4.png)
Con este comando puedes crear un usuario asignandole contraseña.
```
adduser usuario
```
![05](sources/imagenes/users_groups_permissions/5.png)
Este comando sirve para eliminar usuarios.
```
userdel usuario
```
![06](sources/imagenes/users_groups_permissions/6.png)

Este comando sirve para eliminar usuarios y la ruta home del usuario.
```
userdel usuario -r
```
![07](sources/imagenes/users_groups_permissions/7.png)
Este comando sirve para cambiar la contraseña de un usuario.
```
passwd usuario
```
![08](sources/imagenes/users_groups_permissions/8.png)
Este comando sirve para añadir a usaurios a grupos.
```
gpasswd usuario -a
```
![09](sources/imagenes/users_groups_permissions/9.png)

## Usermod

Te permite cambiar el directorio home de un usuario.
```
usermod usuario -d
```
![10](sources/imagenes/users_groups_permissions/10.png)
Sirve para cambiar la shell de inicio de un usuario. Para la demostracion usare zsh.
```
usermod usuario --shell /bin/bash

o

usermod usuario --s /bin/bash
```
![11](sources/imagenes/users_groups_permissions/11.png)
Su funcion es cambiar el nombre de  inicio de usuario.
```
usermod usuario -l
```
![12](sources/imagenes/users_groups_permissions/12.png)
La funcion de este comando es para bloquear usuarios.
```
usermod nuevo nombre usuario   -L
```
![13](sources/imagenes/users_groups_permissions/13.png)
La funcion de este comando es para debloquear usuarios.
```
usermod usuario -U
```
![14](sources/imagenes/users_groups_permissions/14.png)
Con este comando puedes añadir usuarios a grupos.
```
usermod -a -G usuario grupo
```
![15](sources/imagenes/users_groups_permissions/15.png)
Este comando permite cambiar el grupo de un usuario.
```
usermod -g usuario grupo
```
![16](sources/imagenes/users_groups_permissions/16.png)

## Grupos
Con este comando puedes ver en que grupos esta un usuario.
```
groups
```
![17](sources/imagenes/users_groups_permissions/17.png)
Con este comando puedes crear grupos.
```
addgroup grupo
```
![18](sources/imagenes/users_groups_permissions/18.png)
Tambien puede servir para añadir usuarios a un grupo.
```
adduser usuario grupo
```
![19](sources/imagenes/users_groups_permissions/19.png)
Con este comando puedes sacar a usuarios de un grupo.
```
deluser usuario grupo
```
![20](sources/imagenes/users_groups_permissions/20.png)
Con este comando puedes cambiar el nombre a un grupo.
```
groupmod -n nombre del grupo nuevo nombre
```
![21](sources/imagenes/users_groups_permissions/21.png)

## Permisos

## Chmod
Sirve para cambiar los permisos de una carpeta afectando al resto de contenido de la carpeta.
```
chmod -R
```
![22](sources/imagenes/users_groups_permissions/22.png)
```
sticky: chmod +t o tambien o+t
```
![23](sources/imagenes/users_groups_permissions/23.png)
Activa un bit especial que hace que los usuarios puedan ejecutar un archivo con permisos del propietario.
```
suid: chmod numero de permisos luego +s o u+s
```
![24](sources/imagenes/users_groups_permissions/24.png)
```
sgid: chmod numero de permisos o g+s
```

## Chown
Sirve para cambiar el propietario de una carpeta y el resto de cosas que contiene la carpeta.
```
chown -R
```
![25](sources/imagenes/users_groups_permissions/25.png)

## Chgrp
Permite cambiar el grupo de un carpeta de forma recursiva.
```
chgrp -R
```
![26](sources/imagenes/users_groups_permissions/26.png)

## Acl

Te permite ver si una carpeta tiene asignado un acl.
```
getfacl
```
![27](sources/imagenes/users_groups_permissions/27.png)
Con este comando puedes asignar un acl a un usuario a un grupo.
```
setfacl -m user o grup:permiso de la carpeta
```
![28](sources/imagenes/users_groups_permissions/28.png)
Este comando borra todas las acl existentes de una carpeta o un archivo.
```
setfactl -b
```
![29](sources/imagenes/users_groups_permissions/29.png)
Permite eleminar una entrada especifica de acl.
```
setfacl -x usuario o grupo carpeta
```
![30](sources/imagenes/users_groups_permissions/30.png)

## Umask
Te permite asignar los permisos predeterminados de la creacion de archivos y carpetas. siguiendo esta tabla

<table style="border: 1px solid black; border-collapse: collapse; width: 100%; text-align: center;">
  <thead>
    <tr style="background-color: #cce5ff;">
      <th style="border: 1px solid black; padding: 8px;">Octal</th>
      <th style="border: 1px solid black; padding: 8px;">Binary</th>
      <th style="border: 1px solid black; padding: 8px;">Perms</th>
      <th style="border: 1px solid black; padding: 8px;">Octal</th>
      <th style="border: 1px solid black; padding: 8px;">Binary</th>
      <th style="border: 1px solid black; padding: 8px;">Perms</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">0</td>
      <td style="border: 1px solid black; padding: 8px;">000</td>
      <td style="border: 1px solid black; padding: 8px;">rwx</td>
      <td style="border: 1px solid black; padding: 8px;">4</td>
      <td style="border: 1px solid black; padding: 8px;">100</td>
      <td style="border: 1px solid black; padding: 8px;">-wx</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">1</td>
      <td style="border: 1px solid black; padding: 8px;">001</td>
      <td style="border: 1px solid black; padding: 8px;">rw-</td>
      <td style="border: 1px solid black; padding: 8px;">5</td>
      <td style="border: 1px solid black; padding: 8px;">101</td>
      <td style="border: 1px solid black; padding: 8px;">-w-</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">2</td>
      <td style="border: 1px solid black; padding: 8px;">010</td>
      <td style="border: 1px solid black; padding: 8px;">r-x</td>
      <td style="border: 1px solid black; padding: 8px;">6</td>
      <td style="border: 1px solid black; padding: 8px;">110</td>
      <td style="border: 1px solid black; padding: 8px;">--x</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">3</td>
      <td style="border: 1px solid black; padding: 8px;">011</td>
      <td style="border: 1px solid black; padding: 8px;">r--</td>
      <td style="border: 1px solid black; padding: 8px;">7</td>
      <td style="border: 1px solid black; padding: 8px;">111</td>
      <td style="border: 1px solid black; padding: 8px;">---</td>
    </tr>
  </tbody>
</table>

```
umask numero
```
![31](sources/imagenes/users_groups_permissions/31.png)
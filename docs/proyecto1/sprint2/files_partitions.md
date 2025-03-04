# Creacion de particiones y formatos.

## Sistemes de fitxers

La función de los sistemas de ficheros es determinar el cómo se van a guardar los archivos, su organización y el acceso.

Los más que se suelen usar son:

FAT32: es el que tiene más compatibilidad con el resto de sistemas operativos, pero solo permite guardar archivos que no supere los 4GB.

exFAT: Es una version mejorada de FAT32 que permite almacenar archivos mas grandes

NTFS: Es el que suele usar los sistemas operativos Windows más modernos porque soporta tamaños grandes de archivos, entre otras ventajas.

EXT4: es el formato que suele usar los sistemas operativos Linux, también tiene la capacidad de almacenar archivos de grandes tamaños.

## Tamaño sector

Es la unidad mínima física donde se guardan los datos en un disco, el tamaño predeterminado es de 512Bytes

## Tamaño block

Es el tamaño predeterminado con el que trabaja un disco duro.

## Fragmentaciones

Fragmentación interna: Es el espacio que queda desaprovechado en los bloques.

Fragmentación externa: Provoca que al principio vaya todo bien al principio, pero al cabo de un tiempo los archivos ocuparán bloques aleatorios, provocando que el rendimiento empeore.

Las soluciones son: Reducir el tamaño del bloque a cambio de empeorar el rendimiento o aumentar el tamaño del bloque para tener mejor rendimiento a cambio de llegar a poder desaprovechar espacio.

Tipos de formateo:

formateo rápido/formateo mediano: El formateo se puede hacer desde el sistema operativo. No borra los archivos solo el sistema de ficheros, los sectores defectuosos los ignora.


formateo de bajo nivel: Necesitas un programa especial para realizar el formateo, repara los sectores defectuosos y borra los archivos.


## FDISK -l

Lista todos los discos que tengas en el quipo.

```
fdisk -l
```

![1](sources/imagenes/file_partitions/1.png)

## DF -T

Muestra las particiones y sistemas de ficheros.

```
df -T
```

![2](sources/imagenes/file_partitions/2.png)

## DU -B

Muestra el tamaño que ocupa un archivo o carpeta.

```
dub -b
```

![3](sources/imagenes/file_partitions/3.png)

## DU -SH

Muestra el tamaño que ocupa un archivo o carpeta en disco. 

```
du -sh
```

![4](sources/imagenes/file_partitions/4.png)

## E4defrag -C 

Te dice si hay que desfragmentar el disco.

```
e4defrag -c
```

![5](sources/imagenes/file_partitions/5.png)

## Creacion de particiones.

Ejecutamos fdisk -l y localizamos el nombre del disco.

![6](sources/imagenes/file_partitions/6.png)

Una vez encontrado el nombre del disco ejecutaremos el siguiente comando:

````
fdisk /dev/nombre del disco
````
![7](sources/imagenes/file_partitions/7.png)

Escribimos la letra n y pulsamos en enter.

![8](sources/imagenes/file_partitions/8.png)

Volvemos a pulsar enter.

![9](sources/imagenes/file_partitions/9.png)

Volvemos a pulsar otra vez enter.

![10](sources/imagenes/file_partitions/10.png)

Otra vez enter.

![11](sources/imagenes/file_partitions/11.png)

Ponemos el valor que queremos y pulsamos enter.

![12](sources/imagenes/file_partitions/12.png)

Para guardar los cambios escribimos w y pulsamos enter.

![13](sources/imagenes/file_partitions/13.png)

Para comprobar que se ha hecho bien la particion ejecutamos otra vez fdisk -l.

![14](sources/imagenes/file_partitions/14.png)

Ahora le daremos formato a la particion ejecutando el siguiente comando:

```
mkfs.ext4 -b numero de sector /dev/nombre particion
```

![15](sources/imagenes/file_partitions/15.png)

Si queremos ver informacion del bloque podemos ejecutar el comando:

```
tune2fs -l /dev/sdb1 | grep block
```

![16](sources/imagenes/file_partitions/16.png)

Ahora podemos montar la particion donde queramos en mi caso en una carpeta del var.

![17](sources/imagenes/file_partitions/17.png)

Para demostracion creare un archivo de demostracion.

![18](sources/imagenes/file_partitions/18.png)

Para montar la particion tenemos que ejecutar el comando:

```
mount -t ext4 /dev/sdb1 /var/particion1
```

![19](sources/imagenes/file_partitions/19.png)

Si ejecutas este comando podras ver las particion:

```
df -T
```

![20](sources/imagenes/file_partitions/20.png)

Para desmontar la particion utiliza el comando:

```
umount /dev/nombre disco
```

![21](sources/imagenes/file_partitions/21.png)

En caso de que quieras hacer que la particion sea permanente edita fstab con este comando:

```
nano /etc/fstab
```

![22](sources/imagenes/file_partitions/22.png)

Editamos el archivo agregando la siguiente linea.

![23](sources/imagenes/file_partitions/23.png)

Por ultimo guardamos los cambios y reiniciamos la maquina.

![24](sources/imagenes/file_partitions/24.png)
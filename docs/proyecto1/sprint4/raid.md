# Raid

El raid es una tecnologia que permite tener los mismos datos de un disco en otros discos que trabaja a nivel de discos y particiones.

Lo que se recomienda para hacer un raid es que los discos tengan las mismas caracteristicas. Hoy en dia se trabaja con volumenes

| RAID | | Discos | Tolerancia a fallos                      |
| :--: | | :----: | :--------------------------------------- |
| 0    | | 2      | Solo con fallar un disco ya no funciona. |
| 1    | | 2      | Si falla uno seguira funcionando.        |
| 5    | | 4      | Solo puede fallar un disco.              |

## Configuracion de raid

En mi caso creare un raid 5 que neceista como minimo 

Primero crearemos los discos duros pulsando click derecho en la maquina virtual y Configuracion o pulsando Configuracion

![01](sources/raid/1.png)

Vamos a almacenamiento.

![02](sources/raid/2.png)

Pulsamos en el icono de un disco duro con un +.

![03](sources/raid/3.png)

Pulsamos el icono del disco con un ciruclo y le asignamos el espacio.

![04](sources/raid/4.png)

Pulsamos en terminar y los mismos pasos hasta crear la cantidad de disco que queramos.

![05](sources/raid/5.png)

Guardamos los cambios y iniciamos la maquina.

![06](sources/raid/6.png)

Abrimos una terminal pusando click derecho en el escritorio y pulsando abrir un terminal o pulsando ctr + alt + t

![07](sources/raid/7.png)

Ejecutamos primero sudo apt update

![08](sources/raid/8.png)

Y ahora instalamos mdadm

```
sudo apt install mdadm
```

![09](sources/raid/9.png)

Pulsamos enter

![10](sources/raid/10.png)

Una vez instalado hacemos fdisk -l para ver que letra tiene los discos

![11](sources/raid/11.png)

![12](sources/raid/12.png)

Ahora ejecutamos el fdisk indicando el disco para darle formato.

![13](sources/raid/13.png)

Escribimos n y pulsamos enter

![14](sources/raid/14.png)

Seguimos pulsando enter hasta que vuelva a pedir que introduscamos una orden

![15](sources/raid/15.png)

Escribimos t y pulsamos enter

![16](sources/raid/16.png)

ahora escribimos fd y pulsamos enter.

![17](sources/raid/17.png)

Escribimos w para guardar los cambios y repitimos los mismos pasos para la cantidad de discos que tengamos.





## Pruevas de fallos
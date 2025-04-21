Para la gestion de procesos  se puede hacer tanto por interfaz como cmd.

## Adminstrador de tareas.

Si queremos gestionar los procesos desde la interfaz podemos usar el administrador de tareas.

![1](sources/procesos/1.png)

Pulsamos en mas detalles para poder ver el resto de procesos y funciones.

![2](sources/procesos/2.png)

En inicio podemos ver que procesos se ejecutan al encender el pc.

![3](sources/procesos/3.png)

En el apartado de detalles podemos ver mas informacion sobre los procesos como los PID.

![4](sources/procesos/4.png)

## Tasklist.

En el caso que estemos en el terminal y que queramos ver los procesos que se ejecutan al momentos podemos usar el comando tasklist.

![5](sources/procesos/5.png)

Si queremos por algun motivo guardar el resultado podemos usar >.

![6](sources/procesos/6.png)

Tambien podemos filtrar los procesos poniendo despues del comando | findstr y el nombre del proceso

![7](sources/procesos/7.png)

## Taskkill

Si queremos matar un proceso podemos usar taskkill poniendo /IM y en caso que queremos forzar el finalizado de la tarea podemos usar /f

![8](sources/procesos/8.png)
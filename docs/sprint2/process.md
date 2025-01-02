# Gestion de procesos

Los procesos son aquellos programas que se estan ejecutando tanto en primer como segundo plano. 

## top

Te permite ver los procesos que se estan ejecutando desde un terminal.

```
Top
```
![1](sources/imagenes/process/1.png)

## pstree

Te genera un arbol de los procesos.

```
pstree 
```
![0](sources/imagenes/process/0.png)

Puedes usar estos parametros para ordenar o decidir lo que se ve.

## -a o --arguments     

   muestra los argumentos de la línea de órdenes.

![2](sources/imagenes/process/2.png)

## -A o --ascii      

   utiliza characteres de trazado de líneas ASCII.

  ![3](sources/imagenes/process/3.png)

## -c o --compact-not

   no compacta subárboles idénticos.

   ![4](sources/imagenes/process/4.png)

## -C o --color=TIPO    

   colorea proceso por atributo por ejemplo edad.

   ![5](sources/imagenes/process/5.png)

## -g o --show-pgids    

   muestra ids de grupos de procesos; implica -c.

   ![6](sources/imagenes/process/6.png)

## -G o --vt100

   utiliza caracteres de trazzdo de líneas VT100.

   ![7](sources/imagenes/process/7.png)

## -h o --highlight-all 

   resalta el proceso actual y sus ascendientes

   ![8](sources/imagenes/process/8.png)

## -H PID o --highlight-pid=PID 

   resalta este proceso y sus ascendientes

   ![9](sources/imagenes/process/9.png)
                      
## -l o --long

   no trunca las líneas largas

   ![10](sources/imagenes/process/10.png)

## -n o --numeric-sort  
   ordena la salida por PID

   ![11](sources/imagenes/process/11.png)

## -N TYPE o --ns-sort=TYPE

   ordena la salida por este tipo de espacio de nombres (cgroup o ipc o mnt o net o pid o time o user o uts)
    
   ![12](sources/imagenes/process/12.png)

## -p o --show-pids

   muestra PIDs; implica -c

   ![13](sources/imagenes/process/13.png)

## -s o --show-parents  

   muestra los padres del proceso seleccionado
   
   ![14](sources/imagenes/process/14.png)

## -S o --ns-changes 

   muestra las transiciones de espacios de nombres
   
   ![15](sources/imagenes/process/15.png)

## -t o --thread-names  

   muestra los nombres completos de hilos

   ![16](sources/imagenes/process/16.png)

## -T o --hide-threads  

   oculta hilos o muestra solo procesos

   ![17](sources/imagenes/process/17.png)

## -u o --uid-changes    

   muestra transiciones de uid

   ![18](sources/imagenes/process/18.png)

## -U o --unicode    

   utiliza caracteres de trazado de líneas UTF-8 (Unicode)

   ![19](sources/imagenes/process/19.png)

## -V o --version       
  
   muestra información sobre la versión

   ![20](sources/imagenes/process/20.png)

## -Z o --security-context 

   muestra los atributos de seguridad

   ![21](sources/imagenes/process/21.png)

## PID

   inicia en el PID asignado; predeterminado es 1 (init)

   ![22](sources/imagenes/process/22.png)

## USUARIO 

   muestra solo árboles con raíz en los procesos de este usuario

   ![23](sources/imagenes/process/23.png)

## PS AUX

   Muestra los procesos actuales.

   ```
   ps aux
   ```

   ![24](sources/imagenes/process/24.png)

## Ctrl+C y Ctrl+Z

   Ctrl+C Cancela el proceso que se esta ejecuatando.

   ![25](sources/imagenes/process/25.png)

   Ctrl+Z Suspende el proceso que se esta ejecutando.
   
   ![26](sources/imagenes/process/26.png)

## Jobs

   Muestra los procesos que se estan ejecutando en segundo plano o estan detenidos en una sesion de shell.
   
   ```
   jobs
   ```

   ![27](sources/imagenes/process/27.png)

## fg %

   Permite volver abrir el proceso que se ha suspendido.

   ```
   fg %numero
   ```

   ![28](sources/imagenes/process/28.png)

   ![29](sources/imagenes/process/29.png)

## Kill
   
   Sirve para matar procesos

   ```
   kill
   ```

   ![30](sources/imagenes/process/30.png)
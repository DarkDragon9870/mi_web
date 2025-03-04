# Instaladores de paquetes

## Synaptic

![01](sources/imagenes/installer_packages/1.png)

## Apt

apt update

apt upgrade 

apt dist-upgrade

apt build-dep paquete

apt install paquete

apt intall paquete=

apt remove paquete

apt purge paquete

apt autoremove

apt clean

apt-cache depends paquete

apt-rdepends paquete

apt -f install

apt-cache policy paquete

## Aptitude

aptitude remove paquete

aptitude purge paquete

aptitude install paquete

aptitude show paquete

## DPKG

dpkg -r paquete

dpkg -P paquete

dpkg -i archivo.deb

dpkg -s paquete

dpkg –get-selections | grep paquete

## Repositoris

main: programario soportado oficialmente

restricted: programario suportat no disponible bajo licenciamiento completamente libre.

universe: progomario soportado por la comunidad.

multiverse: programario que no es libre

## Copia del archivo

/etc/apt/sources.list: Agregar lineas de repositiorios.

apt-get update

i apt-get install paquete

## Compilar el codigo fuente

Instalar lo necesario apt-get install build-essential 

tar: tar xvf archivo.tar

gz: gunzip archivo.gz o gzip -d archivo.gz

tgz, tar.gz: tar xvzf archivo.tar.gz

bz2: bunzip2 archivo.bz2 o bzip2 -d archivo.bz2

tar.bz2: tar xvjf archivo.tar.bz2

zip: unzip archivo.zip

rar: rar -x archivo.rar

entrar a la carpeta

./configure

make

make install

make uninstall

## binarios

chmod +x arxiu.bin

sudo ./arxiu.bin


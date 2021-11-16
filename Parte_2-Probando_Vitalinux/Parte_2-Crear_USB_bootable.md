## Crear un Live USB Bootable de Vitalinux {#CrearLiveUSBBootable}

De forma similar a un CD/DVD Arrancable, podemos grabar la imagen **ISO de Vitalinux** en una **memoria USB** con la finalidad de poder probar o instalar Vitalinux.  A diferencia de lo que nos ocurre con los CD/DVD, nuestro sistema operativo no siempre integra una aplicación que se encargue de grabar la ISO en una memoria USB, por lo que tendremos que instalar una aplicación expresamente para ello si no existe una alternativa.


### ¿Cómo crear un USB Bootable o Arrancable? {#USBBootable}

En el caso de querer quemar la imagen ISO en una memoria USB para crear un USB bootable de instalación de nuestro Linux preferido tenemos también varias opciones

1.  El sistema Operativo suele traer una aplicación para "quemar" USB. Por ejemplo en Ubuntu se llama **Creador de Discos de Arranque**
1.  Aplicaciones de terceros como unetbootin
Comentar que el software actualmente más afamado por su sencillez y por ser multiplataforma (*disponible tanto para Windows como para Linux*) para realizar dicha tarea es **UnetBootin** ([https://unetbootin.github.io/](https://unetbootin.github.io/)). Una vez instalado **UnetBootin** tan sólo es necesario ejecutarlo, elegir la imagen ISO que previamente hayamos descargado de Internet (p.e. [Área de Descargas]({#areaDescargas})) y seleccionar el dispositivo USB (*drive*) que queramos convertir en USB bootable de instalación (*el dispositivo USB debe estar previamente conectado al equipo antes de iniciar UnetBootin*).

{% notificacion_important title='¡¡Formatear el PenDrive USB en Fat32!!' %}
La <b>BIOS</b> del equipo físico será la encargada de leer la memoria USB y advertir que en ella existe un sistema operativo que puede ser instalado (<i>USB Bootable</i>).  Para asegurarnos de que la <b>BIOS</b> pueda leer su contenido sin problemas, por cuestiones de compatibilidad, se recomienda formatear previamente la memoria USB en <b>FAT32</b>. Una vez que la condición del formato esta garantizada deberemos dejar la <b>memoria vacía de contenido</b> antes de pasar a grabar la imagen ISO en su interior.
{% endnotificacion_important %}

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSvr4JxqRNkTwI0mcFJdfbIe5BtDpSGyLO4ucyAyk65f3zXsFa3zxIyFZiPcqRuv_2YEfrGY39SFVi0/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

En la **Píldora formativa de Descarga de una iso y creación de un usb arrancable** podemos encontrar un ejemplo gráfico de como llevar a cabo éste proceso

{% youtube %}https://youtu.be/ex9G7ZXGEt4{% endyoutube %}
# ¿Cómo Probar Vitalinux?









**¿Donde probar Vitalinux?**</tt></center><p>Una vez hemos descargado la imagen ISO de Vitalinux EDU DGA (*[Área de Descargas de Vitalinux](http://wiki.vitalinux.educa.aragon.es/index.php/Descargar)*) tenemos diferentes posibilidades/opciones para poder **probar Vitalinux** y establecer un primer contacto con él.  Ésta decisión es importante, ya que Vitalinux no es una aplicación sin más que podamos instalar y desinstalar ... sino de un Sistema Operativo completo.  Entre todas las opciones destacaremos tres:</p><ol>-  Puedes hacer las pruebas **en tu propio ordenador** iniciando Vitalinux en **modo Live**.  El **modo Live** es una posibilidad que nos ofrece Linux para probar sus sistema operativos **sin tener que instalarlos en el disco duro de nuestro equipo**. Para ello será necesario pasar el archivo ISO con la imagen de Vitalinux a un DVD o memoria USB, y posteriormente indicarle a nuestro equipo que arranque desde ese DVD o USB (*el DVD o USB hará las veces de disco duro de la máquina*).  Ésta opción es recomendada cuando quieres tener una primera experiencia de uso de un sistema operativo Linux, pero no para un uso habitual del sistema ya que normalmente son sesiones de uso no persistentes (*tras trabajar en modo Live, cuando se apaga el equipo se pierden todos los datos, todos los cambios realizados o personalizaciones realizadas*).-  **Instalar Vitalinux en un equipo**.  Esta es la opción más recomendable cuando tenemos claro que Vitalinux va a ser nuestro sistema operativo de trabajo de ahora en adelante.  Al instalar Vitalinux en el disco duro de tu equipo tendrás la opción de eliminar todo lo que allí exista y hacer una instalación limpia, o hacer una **instalación dual** para tener la opción de poder seguir trabajando tanto con el sistema operativo que ya tengas instalado (p.e. Windows 7) y Vitalinux.  Si deseas hacer uso de esta opción y dudas si usar tu equipo personal, puedes usar **otro ordenador** diferente, puedes usar otro ordenador que tengas de pruebas, alguno del centro educativo en el que trabajas o un equipo antiguo que no sepas que uso darle.-  Usar un [ **software de Virtualización**](http://wiki.vitalinux.educa.aragon.es/index.php/Vitalinux/Vitalinux_con_VirtualBox) como VirtualBox.  Ésta última opción es la más recomendable para tener un primer contacto con Vitalinux, poder probarlo en toda su plenitud e incluso seguir trabajando con él en un futuro.  Este tipo de software (*p.e. Virtualbox*), permite crear dentro de nuestro equipo **Máquinas Virtuales** que posteriormente podemos eliminar, al igual que eliminamos cualquier otro archivo de nuestro sistema, y sobre las cuales podemos instalar el sistema operativo que deseemos probar, en nuestro caso Vitalinux.   En concreto, haciendo uso de estas **máquinas virtuales** tendremos exactamente las mismas posibilidades que tendríamos con un equipo físico: probar Vitalinux en modo live o instalarlo en su disco duro Virtual, y todo ello **sin tener que temer que le ocurra nada a nuestro equipo**.</ol><p>Para llevar a cabo el presente curso de introducción a Vitalinux se va a sugerir el hacer uso de Virtualbox.  Si quieres o deseas hacer uso de alguna otra opción tan sólo tendrás que sugerírsela al tutor. Una vez decidido ésto ... podemos continuar con el curso!!</p></td>







## Contenido

<li class="toclevel-1">[1 Instalación de Vitalinux usando VirtualBox](#Instalaci.C3.B3n_de_Vitalinux_usando_VirtualBox)
<ul>
- [1.1 ¿Qué es VirtualBox?](#.C2.BFQu.C3.A9_es_VirtualBox.3F)
- [1.2 ¿De donde obtener VirtualBox?](#.C2.BFDe_donde_obtener_VirtualBox.3F)
- [1.3 ¿Cómo crear una máquina Virtual e instalar Vitalinux?](#.C2.BFC.C3.B3mo_crear_una_m.C3.A1quina_Virtual_e_instalar_Vitalinux.3F)
- [1.4 Instalar las Guest Additions](#Instalar_las_Guest_Additions)
- [1.5 Utilidades de VirtualBox](#Utilidades_de_VirtualBox)

- [4.1 ¿Cómo crear un USB Bootable o Arrancable?](#.C2.BFC.C3.B3mo_crear_un_USB_Bootable_o_Arrancable.3F)




## Instalación de Vitalinux usando VirtualBox

### ¿Qué es VirtualBox?

Tal cómo lo definen en su página oficial ***VirtualBox es un poderoso software de virtualización tanto para la empresa,  como para el uso doméstico. Además se caracteriza por ser la única solución profesional que está libremente disponible como software de código abierto bajo los términos de la Licencia Pública General de GNU (GPL v2)***.


En definitiva, **VirtualBox** es un software muy interesante que nos va a permitir crear una máquina virtual, para posteriormente sobre ésta instalar y probar un sistema operativo (*p.e. Vitalinux*) y todas sus aplicaciones obteniendo como resultado exactamente lo mismo que si lo hubiéramos hecho directamente sobre el equipo físicamente.

**¿Qué significa que la máquina es Virtual?**</tt></center><p>Virtualbox nos va a permitir crear máquinas virtuales en un sentido metáforico, ya que cuando creamos una máquina en Virtualbox en realidad estamos cediendo parte de los recursos hardware de la máquina física a la máquina creada en Virtualbox.  Es decir, a modo de ejemplo, si disponemos de un equipo físico con 4GB de memoria RAM y creamos una máquina en Virtualbox con 1GB de memoria RAM, ese GigaByte es real (*no es virtual*) ya que se los esta *quitando* a la máquina física dejándola únicamente con 3GB.  Entendido lo que sucede con la memoria RAM de la máquina virtual, exáctamente igual podríamos decir de la CPU, la tarjeta de sonido, las tarjetas de red, etc ...  Por tanto, Virtualbox es un software que tiene la capacidad de hacernos creer que tenemos varias máquinas en una.</p></td>




### ¿De donde obtener VirtualBox?

Para poder descargar Virtualbox deberemos dirigirnos a su página Web, a su área de descargas:

-  [Área de Descargas de Virtualbox](https://www.virtualbox.org/wiki/Downloads)
Una vez allí deberemos descargar dos cosas:

1.  El programa de instalación de **Virtualbox** para el sistema operativo que tengas.  Por ejemplo, para el caso de que tengas Windows: [Instalador de Virtualbox para Windows](http://download.virtualbox.org/virtualbox/5.1.14/VirtualBox-5.1.14-112924-Win.exe)
1.  El [**Extension Pack**](http://download.virtualbox.org/virtualbox/5.1.14/Oracle_VM_VirtualBox_Extension_Pack-5.1.14-112924.vbox-extpack).  Este paquete **debe instalarse una vez se haya instalado el anterior**. No es más que un conjunto de drivers y funcionalidades añadidas para Virtualbox (*soporte para dispositivos USB, carpetas compartidas, etc.*)
### ¿Cómo crear una máquina Virtual e instalar Vitalinux?

Crear una máquina virtual es tan facil como seleccionar la acción de Nueva Máquina Virtual, y seguir los pasos que se indican en el asistente. Si dejamos todo por defecto no tendremos problemas, pero por revisar:

-  **Nombre y Tipo de máquina**. Nombre deseado y tipo Linux (32 o 64, según deseemos)
-  Memoria **RAM** que le asignamos (1GB por ejemplo está bien)
-  Crear un **disco** Virtual (se recomienda cuando lo pida reservar el espacio dinámicamente para que solo ocupe en disco el espacio que gastemos). Tamaño el que queramos.
Una vez creada la máquina, tendremos que ir a configuración antes de poder arrancarla para "introducir" el DVD de Vitalinux. 


Con la finalidad de tratar que sea más comprensible el **proceso de creación de una máquina Virtual en Virtualbox** se ha creado el siguiente videotutorial (*advertir que este videotutorial se realizó con otra ordenación de contenidos del curso diferente al actual, por lo que hace las referencias a una supuesta parte 4 que había entonces habría que omitirlas):*


### Instalar las Guest Additions

Las Guest Additions son un conjunto de librerías y programas que podemos instalar en la máquina virtual (no en la real), para añadir funcionalidades extra, de forma que la experiencia en el manejo resulta mucho más enriquecida. De ésta forma podemos tener características como que la resolución de pantalla se ajusta al tamaño de ventana, mejor interacción entre la máquina virtual y la real...


Para ello debemos tener arrancada la máquina y clickar en la opción que hay en **VirtualBox de Dspositivos-&gt;Insertar Imágen de CD** de las Guest Additions. Éste menú puede cambiar si estamos trabjando en un sistema base de Microsoft


La acción anterior lanzará un proceso en la máquina similar al de insertar un CD, donde tendremos el software a instalar.


Para instalarlo debemos **ejecutar el instalador con privelegios de administrador**. Podríamos hacerlo desde la consola, pero vamos a simplificarlo lanzando el proceso desde el navegador de archivos. Usando el botón derecho sobre el icono del CD de las GuestAdditions clickamos sobre la acción de Abrir como root. 


Ahora podemos ejecutar (con doble click) el archivo que pone **"VBolsLinuxAdditions.run"**. Éste proceso lanzará una terminal que ejecutará lo necesario


Solo nos queda **reiniciar**.


Con la finalidad de tratar que sea más comprensible el **proceso de instalación de las Guest Additions en la máquina Virtual Virtualbox** se ha creado el siguiente videotutorial (*advertir que este videotutorial se realizó con otra ordenación de contenidos del curso diferente al actual, por lo que hace las referencias a una supuesta parte 4 que había entonces habría que omitirlas):*


### Utilidades de VirtualBox

Con la finalidad de sacarle el máximo partido a VirtualBox se sugiere que veáis el [[siguiente videotutorial](https://youtu.be/oj92vB5mFAs%7C)], el cual os mostrará los siguientes aspectos:

-  Cómo **transferir a la máquina virtual un pendrive o memoria USB** conectada a la máquina física
-  Cómo **compartir carpetas** entre las máquinas física y virtual
-  Cómo **crear puntos de restauración** el la máquina virtual con la finalidad de poder retornar a un estado previo
-  Cómo **compartir el portapapeles** entre las máquinas física y virtual
-  Cómo habilitar **la opción de *Arrastrar y Soltar* para copiar archivos** entre las máquinas física y virtual



## Tarea 1.3 Op1: <center>¿Cómo probar Vitalinux mediante Virtualbox?</center>

![](img/arranque-en-modo-live.png)





## Crear un Live DVD Bootable de Vitalinux

Un **Live DVD** nos va a permitir poder probar **Vitalinux** sin necesidad de instalarlo.  Para ello simplemente tendremos que abrir la aplicación que normalmente usemos para grabar CDs/DVDs y buscar una de las opciones que se encuentra disponible en todos los **quemadores de CDs/DVDs** referente a **grabar una imagen existente en un CD/DVD**, la cual nos solicitará la ubicación de la imagen **ISO de Vitalinux** que hayamos descargado previamente para pasarla posteriormente a un DVD Virgen que hayáis insertado en la unidad de CDs/DVDs.
Además, por lo general, si abrimos nuestro explorador de archivos y nos situamos en el directorio donde se encuentran las imágenes ISO, y pinchamos con el botón derecho del ratón sobre la imagen ISO nos debería aparecer una opción que explícitamente nos invite a grabar dicha ISO en un CD/DVD.


## Crear un Live USB Bootable de Vitalinux

De forma similar a un CD/DVD Arrancable, podemos grabar la imagen **ISO de Vitalinux** en una **memoria USB** con la finalidad de poder probar o instalar Vitalinux.  A diferencia de lo que nos ocurre con los CD/DVD, nuestro sistema operativo no siempre integra una aplicación que se encargue de grabar la ISO en una memoria USB, por lo que tendremos que instalar una aplicación expresamente para ello si no existe una alternativa.


### ¿Cómo crear un USB Bootable o Arrancable?

En el caso de querer quemar la imagen ISO en una memoria USB para crear un USB bootable de instalación de nuestro Linux preferido tenemos también varias opciones

1.  El sistema Operativo suele traer una aplicación para "quemar" USB. Por ejemplo en Ubuntu se llama **Creador de Discos de Arranque**
1.  Aplicaciones de terceros como unetbootin
Comentar que el software actualmente más afamado por su sencillez y por ser multiplataforma (*disponible tanto para Windows como para Linux*) para realizar dicha tarea es **UnetBootin** ([https://unetbootin.github.io/](https://unetbootin.github.io/)). Una vez instalado **UnetBootin** tan sólo es necesario ejecutarlo, elegir la imagen ISO que previamente hayamos descargado de Internet (p.e. [ Área de Descargas](http://wiki.vitalinux.educa.aragon.es/index.php/Descargar)) y seleccionar el dispositivo USB (*drive*) que queramos convertir en USB bootable de instalación (*el dispositivo USB debe estar previamente conectado al equipo antes de iniciar UnetBootin*).
***Importante: Se recomienda haber [formateado](http://wiki.vitalinux.educa.aragon.es/index.php/Curso_Aularagon/Sistema_de_Archivos-Montaje_de_Dispositivos_de_Almacenamiento_Externos#Formatear_un_dispositivo) el Pen previamente en FAT***. No es obligatorio que el pen esté formateado, pero a veces da problemas. Nos hemos encontrado incluso algún pen de tipo USB3.0 con problemas de reconocimiento en equipos antiguos








## Tarea 1.3 Op2: ¿Cómo probar Vitalinux en modo Live?

![](img/arranque-live.png)








## ¿Cómo modificar el Boot Order para que arranque el equipo desde DVD o USB?
**¿Cómo modificar el Boot Order para que arranque el equipo desde DVD o USB?**\nPara poder probar o instalar un sistema operativo desde un Live DVD o USB es necesario indicar al **Boot Order del equipo** que en lugar de arrancar desde el disco duro del equipo debe hacerlo desde el dispositivo donde tenemos cargado el sistema Live (*unidad de DVD o memoria USB*). La forma de hacer esto **depende bastante del modelo y fabricante del equipo informático** con el que nos encontremos, aunque podemos generalizar que la modificación de este **Boot Order** siempre es posible desde la configuración de la **BIOS** del equipo, accesible tras encender el equipo pulsando sobre una tecla concreta que a su vez también depende del modelo y marca del equipo.</p><p>Una vez dentro de la **BIOS** habrá que buscar entre los menús que aparezcan la opción de modificación del **Boot Order** con la finalidad de elegir como primer dispositivo de arranque al medio donde hemos volcado la imagen ISO.</p><p>No obstante, a parte de todo lo anterior, cabría decir que en muchos de los equipos no es necesario acceder a la **BIOS** y modificar el **Boot Order** para poder arrancar desde el DVD o memoria USB, ya que disponen de una tecla de acceso directo a un menú de selección de dispositivo de arranque (*en la pantalla que aparece nada más arrancar el equipo se suele informar de esa tecla de acceso al **Boot Order**, en el caso de que exista esta posibilidad*).</p><p>A continuación se muestra una tabla donde poder consultar, sin un 100% de éxito ya que depende del modelo, la supuesta tecla de acceso a la **BIOS** y al **Boot Order** en función de la marca del equipo.</p></td>



<td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **F2**</td><td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **F10**</td><td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:0.05pt solid #000000;padding:0.097cm;"> **Suprimir/Del**</td>
<td style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **Acer Dell Eurocase Intel Lenovo Ollivetti Samsung Sony Vaio **<p>**Toshiba **</p></td><td style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **Compac**<p>**HP**</p><p></p></td><td align="center" style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:0.05pt solid #000000;padding:0.097cm;"> **Asus Biostar Asrock ECS Foxconn Gigabyte MSI Zotac**</td>



<td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **F7**</td><td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **F8**</td><td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **F9**</td><td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **F10**</td><td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **F11**</td><td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **F12**</td><td align="center" style="background-color:#cccccc;border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:0.05pt solid #000000;padding:0.097cm;"> **ESC**</td>
<td align="center" style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **ECS**</td><td align="center" style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **Asus**</td><td style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **Biostar**<p>**HP**</p></td><td style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **Intel**<p>**Samsung**</p></td><td style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **Asrock**<p>**MSI**</p></td><td style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:none;padding:0.097cm;"> **Acer**<p>**Dell**</p><p>**Eurocase**</p><p>**Gigabyte**</p><p>**Toshiba** *(en los modelos Toshiba M200, M400 y M700 se accede mediante la flecha→)*</p><p>**Lenovo**</p><p>**Ollivetti**</p></td><td style="border-top:none;border-bottom:0.05pt solid #000000;border-left:0.05pt solid #000000;border-right:0.05pt solid #000000;padding:0.097cm;"> **Compac**<p>**Zotac**</p></td>











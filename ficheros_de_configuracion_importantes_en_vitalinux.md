# Ficheros de Configuración Importantes en Vitalinux

## <img src="img/Logoalerta.png" width="80"> ¡¡Aviso!! ¡¡Ficheros y Directorios de Configuración!!

Una de las características más importantes de los sistemas operativos Linux es que **la configuración del aspecto y del comportamiento** de casi cualquier cosa que se nos pueda ocurrir esta controlado por el contenido que haya en uno o varios archivos de texto.  Por esta razón, uno de los requisitos necesarios para que un **usuario de Escritorio Linux** pueda pasar a ser un **usuario avanzado de Administración del sistema**  es que se requiere conocer cuales son todos estos ficheros, y que hay que tocar en cada uno de ellos para que el aspecto y comportamiento se vea alterado tal como el usuario deseaVamos a realizar una práctica sencilla de ejemplo para demostralo y luego os dejamos un listado de unos cuantos ficheros más (pero no son todos...) por si os pica la curiosidad.

## <img src="img/Logobombilla.png" width="80"> Tarea 3.6: Personalización de Vitalinux mediante la edición de Archivos de Configuración

Requisitos: Es necesario haber leído todo lo referente a  **Archivos y Directorios de Configuración**

El conocimiento de que archivos hay que modificar para poder personalizar un determinado aspecto de Vitalinux le corresponde a un **usuario avanzado**.  Asumiendo que eres un **usuario iniciado** en Vitalinux la única pretensión de este ejercicio o tarea es lo siguiente:
-  Advertir que aspecto tiene alguno de estos archivos de configuración y como afectaría a Vitalinux su modificación
-  Advertir que cualquier aspecto configurable en Linux (*p.e. cambiar el fondo de Escritorio, el tamaño de los iconos, la forma del puntero del ratón, el tema del entorno de ventanas, ... ¡¡cualquier cosa!!*) puede llevarse a cabo editando el archivo adecuado.

A modo de ejemplo, en la siguiente tarea se propone modificar el archivo **~/.config/pcmanfm/lubuntu/desktop-items-0.conf** encargado de controlar el aspecto del **Entorno de Escritorio del Usuario**.  Para ello seguiremos los siguientes pasos:

-  En primer lugar, nos aseguraremos de que no tenemos el **Escritorio Congelado**.  En caso de que este activado este servicio cualquier intento de personalización del Entorno de Escritorio acabará sin éxito.  Para ello deberemos verificar que etiquetas Migasfree tenemos asignadas (***CONTROL + ESPACIO** y escribir **Información Global del Sistema ...***), y en caso de ser necesario deberemos **Modificar las Etiquetas Migasfree** (***CONTROL + ESPACIO** y escribir **Modificar Etiquetas Migasfree...***) y desmarcar la relativa a este aspecto: **SRV-CONGELARESCRITORIO**.  Además, **para que surta efecto la descongelación será necesario reiniciar Vitalinux**.

![La Información de parámetros de Red nos indicará que Etiquetas Migasfree tiene asignadas actualmente el equipo](img/Informacion-parametros-red-etiquetas-migasfree.png)

-  Abre el Explorador de Archivos **pcmanfm** tecleando el atajo **Tecla de Windows + E**
-  En la barra de direcciones del **pcmanfm** escribe la siguiente ruta: **~/.config/pcmanfm/lubuntu**.  Recuerda que el símbolo **~** hace referencia la directorio raíz del perfil del usuario que ha iniciado sesión (*por ejemplo, si se ha iniciado sesión el usuario **dga**, el símbolo **~** es equivalente a escribir **/home/dga***)
-  Pincha con el botón derecho del ratón sobre el archivo **desktop-items-0.conf** y selecciona la opción de **leafpad**.  Este es un editor de textos similar al **notepad** de Windows

![Mediante leafpad editaremos el archivo de configuración desktop-items-0.conf, el cual nos permitirá personalizar el Entorno de Escritorio el usuario](img/Archivos-configuracion-personalizacion-0.png)

-  Modifica los valores que se indican a continuación, tal como se muestra en la siguiente captura de pantalla:
    -  **show_trash **: Modifica su valor de **1** a **0**. Esta modificación hará que ya no se muestre la **Papelera** en el Escritorio del usuario
    -  **show_documents **: Modifica su valor de **1** a **0**.  Esta modificación provocará que ya nos e muestre el acceso directo al directorio **Documentos** en el Escritorio
    -  **desktop_font**: Modifica su valor de **Ubuntu 11** a **Ubuntu 18**.  Esta modificación alterará el tamaño de las letras de los accesos del Escritorio agrandándolas

![Ajustando los valores de las variables del archivo desktop-items-0.conf nos permite personalizar el Entorno de Escritorio del usuario](img/Archivos-configuracion-personalizacion-1.png)

-  Fíjate en el **Widget** del Escritorio y advierte con que usuario has iniciado sesión, y por tanto, a que usuario le estas personalizando el entorno de Escritorio.  Después **Cierra sesión** (*CONTROL + ESPACIO y escribe **Cerrar Sesión***) e inicia sesión de nuevo con el usuario anterior.  De esta forma comprobaremos que los cambios han surtido efecto

![A través de la información proporcionada por el Widget del Escritorio podemos saber en todo momento el nombre del usuario del sistema que ha iniciado sesión](img/Widget-Escritorio-usuario-del-sistema.png)

> **Formato de Entrega**: Si no encuentras muchos problemas para ello, haz capturas de pantalla de todo lo que vayas haciendo (tecla IMPRIMIR PANTALLA, o **CONTROL + ESPACIO** y escribes **Capturar pantalla**). En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil. Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1_apellido2_nombre_TareaX.pdf**

¡¡Comprueba el efecto de las modificacines anteriores!!

## /etc/fstab

Archivo de configuración del sistema donde se indican los puntos del montaje que se tendrán en cuenta durante el arranque del sistema: particiones boot, /, /home, /var, …, unidades de red NFS, Samba, …


## /etc/init.d/rc.local

Script que se ejecuta tras inciarse el equipo, justo antes de iniciarse la sesión gráfica.


## /etc/lightdm/ /etc/lightdm/lightdm.conf

En el directorio /etc/lightdm podemos encontrar todos los archivos de configuración relacionados con la sesión gráfica. El archivo de configuración del sistema /etc/lightdm/lightdm.conf es donde se especifican aspectos relacionados con el inicio de la sesión gráfica. Por ejemplo, mediante la directiva “autologin-user” podemos indicar la cuenta de usuario con la que deseamos que se inicie automáticamente la sesión gráfica.


## /etc/init.d/lightdm {start|stop|restart|force-reload}

Nos permite gestionar el entorno gráfico. Por ejemplo, con la opción “restart” podríamos reinicar el entorno gráfico.


## /etc/sudoers /etc/sudoers.d/

El archivo /etc/sudoers nos permite configurar permisos o privilegios a usuarios para la ejecución de programas ejecutables. A través del directorio /etc/sudoers.d/ podemos crear archivos con la misma finalidad de una forma más organizada.


## /etc/apt/sources.list /etc/apt/sources.list.d/

El fichero de configuración /etc/apt/sources.list contiene la lista de los repositorios que usará el gestor de paquetes del sistema. En el caso de querer organizar y clasificar los repositorios puede hacerse uso de archivos de configuración *.list específicos dentro del directorio de configuración /etc/apt/sources.list.d/


## /etc/NetworkManager/NetworkManager.conf /etc/NetworkManager/system-connections/ /etc/network/interfaces

Archivos de configuración del entorno de red


## /etc/default/vx-dga-variables/ /etc/default/vx-dga-variables/vx-dga-variables-general.conf

El fichero /etc/default/vx-dga-variables/vx-dga-variables-general.conf contiene las variables que pueden ser usadas por los paquetes vx-dga-l-*. También almacena una lista de variables que nos indica las fallas del servidor migasfree que han sido ejecutadas por el equipo a través del cliente migasfree


## /etc/xdg/menus/applications-merged/ /usr/share/desktop-directories/ /usr/share/applications/ ~/.config/menus, ~/.local/share/applications, ~/.local/share/desktop-directories

En el directorio /etc/xdg/menus/applications-merged/ se definen los archivos *.menu con la estructura de nuevos items de menú que queremos que apararezcan en el menú de aplicaciones.
En el directorio /usr/share/desktop-directories/ se localizan los archivos *.directory a los cuales se hace referencia en los *.menu anteriores.
El directorio /usr/share/applications/ contiene los accesos directos *.desktop a todas las aplicaciones gráficas correctamente instaladas en el sistema. En el menú de aplicaciones aparecerán en el item correspondiente a la categoría que se defina en su campo Categories, correspondiendose está con la definida en el Category del archivo *.menu correspondiente.
Para que afecte a un único usuario del sistema deberemos editar los archivos dentro de los directorios: ~/.config/menus, ~/.local/share/applications, y ~/.local/share/desktop-directories


## /etc/xdg/autostart/ ~/.config/autostart/ ~/.config/lxsession/Lubuntu/autostart

El directorio /etc/xdg/autostart/ contiene los accesos directos *.desktop a las aplicaciones que se ejecutarán al inicio de la sesión gráfica, independientemente del usuario que la inicie.
Por otro lado el directorio oculto personal ~/.config/autostart/ contiene los accesos directos *.desktop a las aplicaciones que se ejecutarán en función del usuario que inicie sesión gráfica.
También existe la posibilidad u opción de editar el archivo personal de configuración ~/.config/lxsession/Lubuntu/autostart donde se pueden indicar en cada una de sus líneas una aplicación a iniciar tras iniciarse la sesión gráfica


## /etc/skel/

Directorio donde se localiza el esqueleto o estructura de los directorios congelados.


## /usr/share/pixmaps/ /usr/share/icons/

Directorios que contienen imágenes e iconos que pueden ser usados por el usuario para la personalización de sus aplicaciones.


## /etc/ssh/sshd_config

Archivo de configuración del servicio SSH.


## ~/.ssh/

Directorio personal oculto del usuario donde se encuentran las claves SSH asimétricas del usuario, las claves SSH autorizadas, y los equipos de confianza


## ~/.conky/ ~/.config/gnome-pie/ ~/.config/plank/

Directorios personales ocultos de los usuarios donde se encuentra la configuración del conky que se muestra en el Escritorio, el lanzador de aplicaciones circular gnome-pie y el dock plank desplegable


## /usr/share/lxpanel/profile/Lubuntu/panels/panel ~/.config/lxpanel/Lubuntu/panels/panel

Ficheros de configuración general y personal que describe el aspecto que tendrá tanto del menú principal desplegable, como la barra inferior de tareas que se muestra junto al Escritorio


## ~/.config/openbox/lubuntu-rc.xml

Archivo personal de configuración donde se configuran ciertos aspectos del gestor de ventanas openbox, tales como las acciones a desencadenar en función de los atajos o combinaciones de teclas usadas o acciones a desencadenar en función del uso del ratón


## ~/.config/pcmanfm/lubuntu/desktop-items-0.conf

Archivo personal de configuración donde se especifican las preferencias deseadas para nuestro entorno de Escritorio: imagen de fondo, accesos visibles en el Escritorio, formato de letra y color, etc.


## /usr/local/share/file-manager/actions/

Directorio global que contiene los action scripts que serán accesibles por todos los usuarios desde su navegador de archivos


## ~/.config/lxsession/Lubuntu/desktop.conf

Fichero personal de configuración del entorno de Escritorio, el ratón, etc.


Por ejmplo:


iGtk/CursorThemeSize= nos permite indicar el tamaño del poiner del ratón
sGtk/CursorThemeName= nos permite indicar un tema para el ratón


## /usr/share/lubuntu/openbox/menu.xml ~/.local/share/lubuntu/openbox/menu.xml

Permiten personalizar el menú de openbox, de manera global o personal respectivamente

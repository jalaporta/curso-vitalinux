# Explorador de Archivos en Vitalinux

## Contenido

- [1 Explorador de Archivos en Vitalinux: Características y Funcionalidades](#ExploradorArchivosVitalinux)
- [2 Tarea 3.4: Características del Explorador de Archivos PCManFM](#Tarea3-4)

## Explorador de Archivos en Vitalinux: Características y Funcionalidades {#ExploradorArchivosVitalinux}

En Linux existen diferentes exploradores de archivos: **Nautilus, konqueror, Thunar**, etc. Vitalinux, al basarse en la versión ligera de Ubuntu, **LUbuntu**, hace uso del que supuestamente del explorador que consume menor cantidad de recursos del sistema, llamado **pcmanfm**.


La forma más rápida y eficiente de lanzar este **Explorador de Archivos** es tecleando el atajo **Tecla de Windows + E** (*la tecla de Windows suele encontrarse en la fila inferior del teclado, a la izquierda de la barra espaciadora y la tecla ALT*), aunque puede lanzarse igualmente mediante el lanzador **Synapse**, tecleando **CONTROL + ESPACIO** y escribiendo **pcmanfm**, o directamente pinchando con el ratón sobre **el icono de la carpeta** que hay en **la barra inferior del Entorno de Escritorio**.


Entre sus características y funcionalidades más destacables podrían destacarse las siguientes:

1. Es software libre. Por esta razón cualquier programador puede reutilizar el código y mejorarlo, haciendo que de ello nos beneficiemos toda la comunidad de usuarios.
2. Permite la apertura de multiples pestañas, lo que facilita el movimiento de archivos entre diferentes directorios (*arrastrar y soltar*).  Para abrir una nueva pestaña puede teclearse la combinación **CONTROL + T**
3. Permite crear **marcadores** para acceder de una manera muy rápida a los directorios que elijamos.  Estos **marcadores** se pueden crear pulsando la combinación de teclas **CONTROL + D** estando situados dentro del directorio al cual queremos crear un acceso rápido

![Pulsando CONTROL+D dentro del directorio deseado podemos crear un marcador asociado a dicho directorio que nos permitirá acceder a su contenido de una manera muy directa](img/Explorador-archivos-marcadores-2.png)

4. Permite trabajar con un **panel doble** facilitando la copia y movimiento de archivos y directorios entre los paneles derecho e izquierdo

![Pulsando F3 en pcmanfm permite trabajar con un panel doble facilitando la copia y movimiento de archivos y directorios](img/Explorador-archivos-panel-doble-2.png)

5. Facilita la desconexión de los dispositivos de almacenamiento externos (*USB, CD/DVD, etc.*)
6. Soporta varios modos de vista de iconos: vista compacta, lista detallada y vista en miniatura. Para poder ver y cambiar entre los diferentes modos o vistas puede pulsarse las combinaciones **"CONTROL + 1"**, **"CONTROL + 2"**, **"CONTROL + 3"** o **"CONTROL + 4"**
7. Permite programar y añadir **Acciones** (*Action Scripts*) muy útiles que aumentan considerablemente las funcionales del navegador.  Esta es una característica es muy importante ya que el **Explorador de Archivos pcmanfm** detecta al vuelo el formato de un archivo (*p.e. PDF, TXT, EXE, etc.*) independientemente de la extensión que se le haya asignado, y en función de este nos muestra todas las **Acciones** que tiene configuradas para su manipulación.  Por ejemplo, en la siguiente figura se muestra como al pinchar con el botón derecho del ratón sobre una imagen de formato **PNG** nos aparecen una serie de funcionalidades (*comprimir imagen PNG, ver detalles de la imagen y crear replica en miniatura*) que no aparecerían si el archivo seleccionado hubiera sido una canción **MP3**. Estas **Acciones** se van añadiendo poco a poco a Vitalinux ya que son desarrolladas y testeadas por el equipo técnico de Vitalinux de manera altruista o a demanda de los centros

![pcmanfm permite añadir pequeños programas que permiten añadir funcionalidades o Acciones al navegador para la manipulación de los archivos en función del tipo que sean, Mime Type](img/Explorador-archivos-actions-archivo.png)

1. Permite suplantar al **root** o **Administrador de máximo rango del sistema**.  Esto puede resultar útil cuando la cuenta de usuario con la que se ha iniciado sesión en Vitalinux no tiene los privilegios/permisos necesarios para la manipulación de determinados ficheros.  Lógicamente, para poder hacer esta suplantación será necesario que la cuenta de usuario sea administrador del sistema (*p.e. **profesor**, pero no **alumno***).  Para hacer uso de esta funcionalidad tan sólo habrá que **pinchar con el botón derecho del ratón** sobre el archivo o directorio que queremos abrir con todos los privilegios y seleccionar la opción **Abrir como Root**

![La funcionalidad Abrir como Root del Explorador de Archivos pcmanfm permite a usuarios con perfil de administrador abrir archivos y directorios con todos los permisos necesarios para su manipulación](img/Explorador-archivos-abrir-como-root.png)

## <img src="img/Logobombilla.png" width="80"> Tarea 3.4: Características del Explorador de Archivos PCManFM {#Tarea3-4}

Requisitos: Es necesario haber leído todo lo referente a el [Explorador de Archivos de Vitalinux](http://wiki.vitalinux.educa.aragon.es/index.php/Vitalinux/Explorador_de_Archivos._Caracter%C3%ADsticas_y_Funcionalidades)

Con la finalidad de familiarizarnos con las características y funcionalidades del **Explorador de Archivos** de Vitalinux **pcmanfm** a continuación se proponen los siguientes casos prácticos:

1.  Lanza el **explorador de archivos** de Vitalinux **pcmanfm** haciendo uso del lanzador de aplicaciones **synapse**: **CONTROL + ESPACIO** y escribe **pcmanfm**, después pulsa la tecla **Intro** para confirmar
1.  Lanza el **explorador de archivos** de Vitalinux **pcmanfm** haciendo uso del atajo de teclado **Tecla de Windows + E**
1.  Comprueba a través del **Widget** del Escritorio el incremento de consumo de los recursos del sistema: cantidad de memoria **RAM** y porcentaje de **CPU**.  Advierte que se trata de un explorador muy ligero
1.  Escribe en la barra de direcciones del **Explorador de Archivos pcmanfm** la siguiente ruta absoluta: **/usr/share/vitalinux/iconos**.  Podrás comprobar que es un directorio que contiene un montón de imágenes PNG que se usan en las aplicaciones que se crean en **Vitalinux**.  Comprueba como cambia el modo de vista de **pcmanfm** al pulsar las combinaciones de teclado **"CONTROL + 1"**, **"CONTROL + 2"**, **"CONTROL + 3"** o **"CONTROL + 4"**
1.  **pcmanfm** presenta la característica de **panel doble** (*pulsando **F3***)  con la finalidad de facilitar la copia y movimiento de archivos y directorios de una ubicación a otra. Para comprobar su funcionamiento copiaremos varias imágenes del directorio **Imágenes** a **Documentos**.  Para ello, haciendo uso de la aplicación de capturas de pantalla (*Tecla IMPRIMIR PANTALLA*) realiza varias capturas de pantalla dejándolas en la carpeta de destino por defecto **Imágenes** con el nombre que les quieras dar.  Después, abre en una pestaña del **Explorador de Archivos pcmanfm** el directorio **Imágenes** que contiene dichas capturas y pulsa **F3** para crear un panel doble.  Para terminar, en el panel de la derecha sitúate en el directorio **Documentos** y mueve las imágenes de un panel a otro
1.  Crea un subdirectorio llamado **curso-aularagon** con algún archivo en su interior (*llámalos como quieras*), dentro del directorio **Documentos** ubicado en tu perfil de usuario (*estando dentro del directorio Documentos tan sólo tendrás que pinchar con el botón derecho del ratón y seleccionar la opción **crear***).  A continuación crea un marcador que apunte a dicho directorio llamado **Curso** (*CONTROL + D*). Comprueba que se ha creado el **marcador** en la parte inferior de la columna de la izquierda del **pcmanfm**
1.  De forma similar a lo anterior, crea otro subdirectorio llamado **musica-rock** con algún archivo en su interior (*llámalos como quieras*), dentro del directorio **Música** ubicado en tu perfil de usuario.  A continuación crea un marcador que apunte a dicho directorio llamado **Mi Rock** (*CONTROL + D*). Comprueba que se ha creado el **marcador** en la parte inferior de la columna de la izquierda del **pcmanfm**
1.  Abre tres nuevas pestañas en el explorador de archivos pulsando la combinación **CONTROL + T**, y abre en cada una de esas tres pestañas lo siguiente: el marcador **Curso**, el directorio **Imágenes** de tu perfil de usuario y el directorio **/usr/share/vitalinux/iconos**.  A continuación selecciona todos los iconos que hay en **/usr/share/vitalinux/iconos** mediante la combinación de teclas **CONTROL+A**, cópialos mediante la combinación **CONTROL+C** y pégalos en **Imágenes** mediante la combinación **CONTROL+V**
1.  Manteniendo abiertas las pestañas anteriores, selecciona todas las imágenes que acabas de copiar en el directorio **Imágenes**, **CONTROL+A** y arrástralas hasta la pestaña asociada al marcador **Curso**.  Comprueba que esto mueve los archivos de un directorio a otro*   Por último, comprueba que si intentas crear un directorio llamado **nuevo** dentro de **/usr/share/vitalinux** no podrás por no tener permisos/privilegios suficientes para ello.  En cambio, si te sitúas en **/usr/share**, pinchas con el botón derecho del ratón sobre el subdirectorio **vitalinux** y seleccionas la **Acción** **Abrir como Root** podrás comprobar que se te abrirá una nueva ventana sobre la cual ya tendrás permisos suficientes para crear el directorio **nuevo**. ¡¡Compruébalo!!!

> **Formato de Entrega:** Si no encuentras muchos problemas para ello, haz capturas de pantalla de todo lo que vayas haciendo (*tecla IMPRIMIR PANTALLA, o **CONTROL + ESPACIO** y escribes **Capturar pantalla***), y almacénalas en una memoria USB o donde creas conveniente. En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil. Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1_apellido2_nombre_TareaX.pdf**. Si lo consideras necesario puedes indicar cualquier comentario a las capturas de pantalla.

> >*Importante entregar al tutor el documento con las imágenes en formato pdf para que no haya problemas de lectura y calificar la tarea*

> Asegúrate que el nombre no contenga la letra ñ, tildes ni caracteres especiales extraños. Así por ejemplo la alumna **Begoña Sánchez Mañas**, debería nombrar esta tarea como: **sanchez_manas_begona_Tarea3.4**

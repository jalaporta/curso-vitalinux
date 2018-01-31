# Propietarios y Permisos

## Contenido

- [1 Usuarios de Vitalinux](#UsuariosdeVitalinux)
- [2 Tarea 3.2: Iniciar sesión con una nueva cuenta de Administrador](#Tarea3-2)
- [3 Perfil del Usuario en Linux. Permisos](#PerfilUsuarioLinuxPermisos)
- [4 Tarea 3.3: Gestión de Permisos en Archivos y Directorios](#Tarea3-3)

## Usuarios de Vitalinux {#UsuariosdeVitalinux}

A diferencia de otros sistemas operativos como Windows, por cuestiones de seguridad, las distribuciones Linux como Ubuntu (y Vitalinux se basa en ella) no permiten iniciar sesión en el sistema con **la cuenta de root o superusuario**.  De esta forma Linux se asegura de que si un **software malicioso** accede al sistema (*virus, gusano, etc.*) no tendrá privilegios en la sesión iniciada para afectar al sistema de ficheros del equipo, pudiendo alterar únicamente a las carpetas y archivos que le pertenecen al usuario que ha iniciado sesión.


En **Vitalinux** por defecto ya vienen preconfiguradas tres cuentas de usuario para poder trabajar con él en los centros educativos:

1.  Usuario **dga**: perfil de usuario con el que se inicia por primera vez Vitalinux y con el que se realiza la post-instalación.  Su **password** por defecto es **careidga**.  Puede realizar tareas administrativas (*p.e. instalar nuevo software, configurar impresoras, etc.*) mediante la previa introducción de su password.
1.  Usuario **profesor**: perfil de usuario recomendado para los **docentes** de los centros.  Su **password** por defecto es **careidga**.  Puede realizar tareas administrativas (*p.e. instalar nuevo software, configurar impresoras, etc.*) mediante la previa introducción de su password.
1.  Usuario **alumno**: perfil de usuario recomendado para los **alumnos** de los centros.  Su **password** por defecto es **alumno**.  **No puede** realizar tareas administrativas.

Éstas tres cuentas se crearon como configuración básica para un centro, pero en cualquier momento **se pueden crear** las cuentas de usuarios que se creen necesarias para poder trabajar con el sistema de forma más personalizada/granular. 
Para ello podemos **crear cuentas**:

-  Del sistema. Similares a la de profesor/alumno/dga y con los permisos necesarios
-  Hacer uso de una Base de Datos de usuarios centralizada tipo **LDAP** (y aconsejable en el caso de querer trabajar con muchas cuentas de usuario).
Cuando marcamos en la post-instalación que un equipo se va a emplear a **casa**, lo primero que se sugiere es crear una cuenta de usuario, ya que se entiende que la figura de alumno/profesor no tiene sentido en un ordenador personal.

## <img src="img/Logolupa.png" width="80"> ¡¡Importante!! ¿Al ser públicas las credenciales de los usuarios no hay problemas de seguridad?

Como es obvio, al ser información pública la password de los usuarios **profesor** y **dga** (*careidga*), si éstas no se cambian existe un riesgo de seguridad muy importante en Vitalinux ya que son cuentas con privilegios de administración.  Para subsanarlo se recomienda lo siguiente:
-  Si va a hacerse uso de los perfiles de los usuarios **profesor** y **alumno** dentro de un **Centro Educativo**, se deberían **modificar las passwords**, al menos de los usuarios **profesor** y **dga**.  Para facilitar esta tarea en los centros, ya que nos podemos encontrar con cientos de equipos donde modificar la contraseña y sería una tarea muy latosa ir uno a uno cambiando las passwords, Vitalinux puede cambiar las **passwords** de manera desatendida y automatizada.  Por esta razón, cuando un centro va a instalar Vitalinux en sus equipos indican previamente a los responsables del programa cuales quieren que sean sus nuevas passwords. Ni que decir tiene que el cambio de passwords general se puede llevar a cabo en cualquier momento, no solo antes de instalar en el centro (por ejemplo para un nuevo curso, cuando la contraseña se ha visto "comprometida", cambio de profesorado...)
-  Si va a hacerse uso de Vitalinux en **Casa**, o fuera de un **Centro Educativo**, conviene en la post-instalación, tal como vimos en la [primera parte del curso](primeras_pruebas_con_vitalinux.md), **crear un nuevo usuario administrador con una password personalizada** y eliminar las cuentas de usuario preconfiguradas que ya existen.</td>

## <img src="img/Logobombilla.png" width="80"> Tarea 3.2: Iniciar sesión con una nueva cuenta de Administrador {#Tarea3-2}

Requisitos: Es necesario haber leído todo lo referente a  [Usuarios de Vitalinux](http://wiki.vitalinux.educa.aragon.es/index.php/Vitalinux/Usuarios)

A menos que estés trabajando con Vitalinux en **modo Live**, pulsa la combinación de teclas **CONTROL + ESPACIO** y escribe **Volver a la post-instalación**.  Tras cerrar sesión o reiniciar Vitalinux debería volver a mostrarse el proceso de post-instalación.  Una vez en la **Post-Instalación** indica que vas a hacer uso del sistema operativo Vitalinux fuera de un **Centro Educativo**.  A continuación crea una nueva cuenta de **Administrador** con el nombre y password que tu decidas.  Una vez termine toda la post-instalación, cierra sesión (*CONTROL + ESPACIO y escribe **Cerrar Sesión***) e inicia sesión con el usuario recién creado.  Después abre la aplicación de gestión de usuarios (*CONTROL + ESPACIO y escribe **Usuarios y Grupos***), y elimina todos los usuarios que existen de manera preconfigurada y que no vayas a usar en el equipo (*alumno*, *profesor* y *dga*) ***Importante: Si los usuarios que vas a borrar contienen datos que quieres guardar puedes conservar los mismos al hacer el borrado para poder recuperarlos. Para acceder a ellos, recuerda lo que vimos en la tarea anterior: El directorio personal del usuario está en /home/nombre_usuario)***.  Advierte que para llevar a cabo esta **tarea administrativa** se te solicitará tu password en algún momento para cerciorarse de que tu cuenta es de **Administrador** del sistema.

**Nota importante: si estás en *modo LIVE* NO te dejará eliminar el usuario dga, ya que en éste modo se abren unas consolas virtuales con éste usuario y no podemos eliminar un usuario con sesiones abiertas**. Lo puedes ver si quieres abriendo una terminal/consola y escribiendo el comando **who** y pulsando enter. Se adjunta una captura para que se observe

![sesiones abiertas en modo live](img/Sesiones-abiertas-live.png)

> **Formato de Entrega:** Si no encuentras muchos problemas para ello, haz capturas de pantalla de todo lo que vayas haciendo (*tecla IMPRIMIR PANTALLA, o **CONTROL + ESPACIO** y escribes **Capturar pantalla***). En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil. Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1_apellido2_nombre_TareaX.pdf**.

## Perfil del Usuario en Linux. Permisos {#PerfilUsuarioLinuxPermisos}

Cada usuario en Vitalinux tan sólo es propietario del **perfil** que le pertenece.  Se entiendo por **perfil** el conjunto de directorios y archivos del cual es el propio usuario el propietario, y que por defecto se corresponde con el contenido del directorio ubicado en **/home/*&lt;nombre-usuario&gt;***.  Por ejemplo, el usuario **profesor** es propietario de todo lo que cuelga de **/home/profesor** y el usuario **alumno** de lo que hay en **/home/alumno**.

![El perfil de un usuario esta compuesto por un conjunto de directorios visibles que le pertenecen y que puede modificar](img/Sistema-archivos-perfis-usuario-sin-ocultos.png)

![El perfil de un usuario también esta compuesto por un conjunto de directorios y archivos ocultos que se pueden visualizar pulsando la combinación CONTROL + H](img/Sistema-archivos-perfis-usuario-con-ocultos.png)

Esto significa que fuera del perfil que le pertenece al usuario, este puede tener limitados los **permisos de lectura, escritura y ejecución**, estando estos presentes en todo archivo y directorio del sistema.  Estos permisos nos vienen a decir lo siguiente:

1.  Permiso de **lectura**: en el caso de tratarse de un archivo, este permiso te permite abrirlo y ver su contenido.  En el caso de tratarse de un directorio este permiso nos indica que podemos ver los archivos y subdirectorios que contiene.
1.  Permiso de **escritura**: nos indica que podemos modificar el contenido del archivo o directorio.
1.  Permiso de **ejecución**: en el caso de tratarse de un archivo, este permiso nos indica que si archivo es un programa vamos a poder ejecutarlo.  En el caso de tratarse de un directorio este permiso nos indica que podemos abrir/acceder a la carpeta.
Para poder consultar **quien es propietario** de un directorio o archivo simplemente hay que pinchar con el botón derecho del ratón sobre él y seleccionar la opción **Propiedades**, y en la ventana que nos aparezca, pinchar sobre la **pestaña permisos**.

![Pinchando con el botón derecho del ratón sobre un archivo o directorio podemos consultar sus Propiedades/permisos](img/Sistema-archivos-propiedades-permisos.png)

## <img src="img/Logobombilla.png" width="80"> Tarea 3.3: Gestión de Permisos en Archivos y Directorios {#Tarea3-3}

Requisitos: Es necesario haber leído todo lo referente a  **Propietarios y Permisos**

Con la finalidad de comprender el uso de permisos en Vitalinux realiza las siguientes acciones:</p><ol>
1.   Haciendo uso de la herramienta de gestión de usuarios que viste en la tarea anterior (***CONTROL + ESPACIO** y escribes **Usuarios y Grupos***), crea dos nuevas cuestas de usuario: 1) **profesor1** y 2) **profesor2** con contraseña para ambos **Passw0rd** (*la **o** es un cero*)
1.   **Cierra sesión** (*CONTROL + ESPACIO y escribe **Cerrar Sesión***) e inicia sesión como usuario **profesor1** (*password **Passw0rd***).
1.   Abre el explorador de archivos (*Tecla Windows + E*) y crea dos directorios en **/home/profesor1/Documentos** llamados **carpeta1** y **carpeta2**.  A su vez, dentro de cada uno de esos directorios crea un archivo llamado **misdatos.txt**.
1.   Pincha con el botón derecho del ratón sobre la **carpeta2** y en **Propiedades/permisos** restringe los permisos para que solamente haya acceso a el propietario y grupo de propietarios.
  
![Desde Propiedades/permisos podemos gestionar los permisos sobre archivos y directorios](img/Sistema-archivos-restringir-permisos.png)

5.   Por último, cierra la sesión del usuario **profesor1** e inicia sesión como **profesor2** (*password **Passw0rd***).  Abre como **profesor2** el explorador de archivos, navega hasta **/home/profesor1/Documentos** y comprueba que **sí** puedes ver el contenido de la **carpeta1** pero no modificarlo, pero en el caso de la **carpeta2** ni siquiera se puede acceder.

> **Formato de Entrega:** Si no encuentras muchos problemas para ello, haz capturas de pantalla de todo lo que vayas haciendo (*tecla IMPRIMIR PANTALLA, o **CONTROL + ESPACIO** y escribes **Capturar pantalla***), y almacénalas en una memoria USB o donde creas conveniente. En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil.

> Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1_apellido2_nombre_TareaX.pdf**. Si lo consideras necesario puedes indicar cualquier comentario a las capturas de pantalla.

> >*Importante entregar al tutor el documento con las imágenes en formato pdf para que no haya problemas de lectura y calificar la tarea*

> Asegúrate que el nombre no contenga la letra ñ, tildes ni caracteres especiales extraños. Así por ejemplo la alumna **Begoña Sánchez Mañas**, debería nombrar esta tarea como: **sanchez_manas_begona_Tarea3.3**
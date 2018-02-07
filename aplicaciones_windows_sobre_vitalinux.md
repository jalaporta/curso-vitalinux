# Aplicaciones Windows sobre Vitalinux

## Contenido

- [1 Ejecución de Aplicaciones Windows sobre Linux/Vitalinux](#EjecucionAppWindowsVitalinux)
- [2 Tarea 4.4: Instalar Aplicaciones Windows sobre Linux/Vitalinux mediante Wine](#Tarea4-4)
- [3 Tarea 4.5: Instalar Aplicaciones Windows sobre Linux/Vitalinux mediante PlayOnLinux](#Tarea4-5)

## Ejecución de Aplicaciones Windows sobre Linux/Vitalinux {#EjecucionAppWindowsVitalinux}

Con la finalidad de suavizar al usuario final el paso de **Microsoft Windows** a **Linux**, además de crear **Interfaces de Usuario** y **Entornos de Escritorio** muy similares a los que existen en Windows, también se ha desarrollado un sofware libre llamado **WinE** que permite la instalación y ejecución de programas creados para Windows en Linux/Vitalinux.

![WinE nos permite instalar aplicaciones Windows sobre Linux/Vitalinux](img/Wine-ofimatica.png)


A modo de ejemplo, mediante **WinE** podríamos instalar en Linux/Vitalinux las siguientes aplicaciones:

-  **Microsoft Office**.  Podría instalarse el paquete ofimático **Microsoft Office** en Vitalinux a través de Wine, pero no hay que olvidar que este software es privativo, y que por tanto requiere de una licencia en vigor.  En caso contrario estaríamos infringiendo la ley (*es ilegal instalar software privativo de manera pirata sin la licencia correspondiente*) y podría penalizarse con una multa, cosa que sería de recibo en un **Centro Educativo**.  A priori, este software no se preinstala en Vitalinux a través de Wine al carecerse de licencias en vigor, y por que existe un software equivalente: **LibreOffice**
-  **PhotoShop**.  Podría comentarse lo mismo que en el caso anterior.  A priori, este software no se preinstala en Vitalinux a través de Wine al carecerse de licencias en vigor, y por que existe un software equivalente: **Gimp**
-  **Juegos**.  Tal vez sea el uso más común de Wine: **instalación de juegos creados para Windows en Linux**. La razón de que este sea su uso habitual es porque en el caso de los juegos no existe una alternativa equivalente para Linux (**los Juegos para entorno PC normalmente sólo están disponibles para Windows**)

Para saber más sobre Wine se recomienda dirigirse a los siguientes enlaces:

-  [Sitio Oficial de Wine](http://www.winehq.org)
-  [Wiki en Español de Wine](https://es.wikipedia.org/wiki/Wine)

## <img src="img/Logobombilla.png" width="80"> Tarea 4.4: Instalar Aplicaciones Windows sobre Linux/Vitalinux mediante Wine {#Tarea4-4}

**Requisitos**: Es necesario haber leído todo lo referente a la Instalación de Aplicaciones Windows sobre Linux/Vitalinux y disponer de un equipo físico o virtual con Vitalinux instalado para realizar la Tarea

Tal como se ha explicado en la parte teórica **WinE** surge con la finalidad de suavizar al usuario final el paso de **Microsoft Windows** a **Linux** permitiéndonos la instalación y ejecución de programas creados para Windows en Linux/Vitalinux. De esta forma, en caso de no encontrar ninguna alternativa en software libre a las aplicaciones privativas que usamos en Windows (siempre es aconsejable buscar software alternativo de código libre/abierto), gracias a Wine, vamos poder instalarla y trabajar con ella. A modo de ejemplo, como tarea se propone instalar un programa de Windows en Vitalinux:

1. Localiza algún instalador de alguna aplicación Windows (*.exe) con la que estés muy familiarizado, de la que no encuentras una alternativa libre en Vitalinux, y que por tanto, que te gustaría contar con ella en Vitalinux. En caso de no disponer de ninguna te proponemos a modo de ejemplo **Sebran**: [Aplicación EXE Sebran](http://www.wartoft.nu/download/sebran.exe)
1. Pincha con el botón derecho del ratón sobre el archivo instalador anterior e indica que quieres abrirlo con **WinE** (Cargador de programas de Windows). Comprobarás que a continuación se configurará Wine y comenzará su instalación. Instala la aplicación como si estuvieras en Windows
1. Abre la aplicación como cualquier otra. Por ejemplo, **CONTROL + ESPACIO** y teclear **Sebran**. Comprueba el correcto funcionamiento de la aplicación Windows sobre Vitalinux
1. Como cualquier otra aplicación de Vitalinux, para cerrarla puedes teclear: **ALT + F4**
Comprueba que tecleando "**CONTROL + ESPACIO**" y escribiendo "**Desinstala software de Wine**" nos aparecerá una ventana o interfaz que nos permitirá desinstalar el software instalado a través de wine
1. Abre el **Explorador de Archivos** (Tecla Windows + E), y asegurandote que estás en el **HOME** del usuario (p.e. /home/dga, /home/profesor, /home/aularagon, etc.) y pulsa la combinación **CONTROL + H**. Podrás comprobar que de repente aparecerán varios **directorios y archivos ocultos** (en Linux todo archivo o directorio cuyo nombre empieza por punto, ".", es un elemento oculto que sólo se mostrará si se pulsa la combinación de teclas "**CONTROL + H**")

![Toda la configuración y programas instalados sobre WinE se localizan en un directorio oculto dentro del HOME del usuario llamado .WinE](img/vitalinux-wine-directorio-oculto-mod.png)

7. Entre los **directorios ocultos** verás uno que se llama .**wine**. En este directorio se encuentra toda la configuración y recreación de un sistema Windows y todos sus programas instalados a través de wine. Entra en él y comprueba que aparece la estructura de un disco "**C:/**" al estilo Windows. Aunque **no es la forma correcta de desinstalar/eliminar** una aplicación instalada a través de **wine**, elimina el directorio oculto .**wine** y comprueba que de repente todo lo que hayas instalado habrá dejado de funcionar

Como en ocasiones *más vale un buen videotutorial que mil palabras* a continuación se sugiere ver el siguiente vídeo relacionado con este asunto:

{% youtube %}https://youtu.be/_e9FvVcEXIk{% endyoutube %}

> **Formato de Entrega**: Si no encuentras muchos problemas para ello, haz capturas de pantalla (tecla IMPRIMIR PANTALLA) de todo lo que vayas haciendo, y almacénalas en una memoria USB o donde creas conveniente. En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil. Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1\_apellido2\_nombre\_TareaX.pdf**.


## <img src="img/Logobombilla.png" width="80"> Tarea 4.5: Instalar Aplicaciones Windows sobre Linux/Vitalinux mediante PlayOnLinux {#Tarea4-5}

**Requisitos**: Es necesario haber leído todo lo referente a la Instalación de Aplicaciones Windows sobre Linux/Vitalinux y disponer de un equipo físico o virtual con Vitalinux instalado para realizar la Tarea 

Llegado este punto habrás advertido que **WinE** nos permite la instlación de aplicaciones Windows en Linux, pero presenta algunos inconvenientes entre los cuales cabría destacar los siguientes:

1. A priori, **Wine no nos garantiza un 100% de probabilidad de que una aplicación Windows se instale de manera exitosa sobre Linux**. En ocasiones la aplicación Windows que queremos instalar depende de algún parche de Windows (Service Pack) o librería que no esta disponible en nuestro Wine provocando una instalación fallida
2. **Determinadas aplicaciones Windows requieren una determinada versión de Wine (1.6, 1.7, ..., 2.4) para funcionar**. Esto es un gran problema, ya que a priori sólo podemos tener instalada una única versión de Wine
3. Al igual que en Windows, y a diferencia de Linux, para instalar una aplicación sobre Wine previamente tenemos que buscarla por Internet, fiarnos de ella, y descargarla. En ocasiones, el software de Windows que nos descargamos esta **infectado** o realiza acciones que desconocemos poniendo en **jaque** a nuestro sistema

Con la finalidad de evitar lo anterior surge en Linux el software PlayOnLinux. Éste se caracteriza por:

* **Dispone de un repositorio público de aplicaciones Windows ya testeadas y comprobadas**, al estilo Linux. De esta forma, tan sólo tenemos que elegir que programa deseamos instalar y **PlayOnLinux** hará el resto:

    1. **PlayOnLinux se conectará con sus repositorios de Internet para buscar el software deseado**. Gracias a esto no tendremos que ir por Internet perdiendo el tiempo buscando software en Sitios Webs como Softtonic
    2. **Descargará de forma desatendida la última versión de ese software que haya sido testeado y comprobado**. Gracias a ello no tendremos que desconfiar en lo que nos estamos instalando, además de asegurarnos de que ese software va a funcionar correctamente en Linux

* En caso de que el software que deseamos instalar no este disponible en los repositorios de PlayOnLinux tendremos la opción de instalarlo igualmente al estilo Wine, pero con la ventaja de que podemos instalar y configurar la versión de Wine que nos interese, además de poder instalar de forma muy sencilla los parches y librerías de Windows que puedan ser requeridos

Para comprobar su funcionamiento se propone llevar a cabo la siguiente tarea (si te surgen dudas observa el siguiente Videotutorial donde se muestra las acciones a realizar):

* Haciendo uso de synaptic instala PlayOnLinux en tu Vitalinux (CONTROL + ESPACIO y escribes Synaptic)
* Una vez instalado, abre la aplicación: CONTROL + ESPACIO y escribes PlayOnLinux
* cSelecciona la opción de Instalar un programa en PlayOnLinux

![](img/vitalinux-interfaz-playonlinux.png)

* Una vez en la ventana referente al **Menú de Instalación de PlayOnLinux**, navega entre las diferentes categorías de aplicaciones que te proporciona **PlayOnLinux**: Accesorios, Educación,, Juegos, Desarrollo, etc. Si encuentras alguna aplicación que te interese, selecciónala e instálala. En caso de que no reconozcas ninguna de ellas, te proponemos buscar en instalar un software de Windows educativo que se usa en los centros: **Graph**

![](img/vitalinux-menu-de-instalacion-playonlinux.png)

* Una vez terminada la instalación del software de Windows elegido, en el caso de que dispongas de un Escritorio Congelado, pincha con el botón derecho del ratón sobre el acceso directo que se ha creado en tu Escritorio a dicha aplicación y elige la opción referente a **Mantener el acceso en el Escritorio Congelado**

Como en ocasiones **más vale un buen videotutorial que mil palabras** a continuación se sugiere ver el [siguiente vídeo](https://youtu.be/wULZ-xa3Om0) relacionado con este asunto:

{% youtube %}https://youtu.be/wULZ-xa3Om0{% endyoutube %}

> **Formato de Entrega**: Si no encuentras muchos problemas para ello, haz capturas de pantalla (tecla IMPRIMIR PANTALLA) de todo lo que vayas haciendo, y almacénalas en una memoria USB o donde creas conveniente. En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil. Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1\_apellido2\_nombre\_TareaX.pdf**.
# Recursos para Centros Educativos

A continuación se van a presentar algunos de los recursos disponibles en Vitalinux como alternativa a algunas de las aplicaciones que se suelen usar habitualmente en los **Centros Educativos** bajo sistemas operativos Windows. Como se verá a través de las tareas propuestas, su uso es opcional y dependerá de las **etiquetas migasfree** seleccionadas.

* [Servicio de Congelación del Equipo](../Parte_6-Aplicaciones_utiles_y_alternativas/Parte_6-Recursos_centros_educativos.md#ServiciodeCongelacion)
* [Servicio de Carpetas Compartidas](../Parte_6-Aplicaciones_utiles_y_alternativas/Parte_6-Recursos_centros_educativos.md#ServiciodeCarpetasCompartidas)
* [Servicio de Control de Equipos de Aula](../Parte_6-Aplicaciones_utiles_y_alternativas/Parte_6-Recursos_centros_educativos.md#ServiciodeControldeEquiposdeAula)
* [Servicio de Navegación Privada o Modo Incognito](../Parte_6-Aplicaciones_utiles_y_alternativas/Parte_6-Recursos_centros_educativos.md#ServiciodeNavegacionPrivada)
* [Otros Servicios](../Parte_6-Aplicaciones_utiles_y_alternativas/Parte_6-Recursos_centros_educativos.md#QueMasServicios)

##  **Servicio de Congelación** {#ServiciodeCongelacion}

Actualmente se encuentra muy extendido en los centros educativos el uso de software encargado de la **congelación del equipo** con la finalidad de evitar degradaciones del sistema.  **Esto es un grave error** por las siguientes razones:

1.  El **software/aplicaciones son algo vivo** que están en permanente evolución y mejora, razón por la cual no tiene ningún sentido **la congelación al estilo Windows**.  Es necesario permitir que las aplicaciones se actualicen con la finalidad de solucionar <b>bugs/errores/problemas</b> detectados por los propios desarrolladores de las aplicaciones.
1.  Junto con el uso de la congelación, también se suele hacer uso de **software antivirus**. Esto es un **error mayúsculo** ya que no tiene ningún sentido instalar un antivirus y no tenerlo actualizado por culpa de la congelación.
1.  **La congelación al estilo Windows es algo perjudicial para la red informática** al no permitir que las actualizaciones que se <b>descargan e instalan diarimente</b> en el equipo sean efectivas.  Es decir, la congelación esta provocando que todas las veces que el equipo se inicie, se vuelva de nuevo a tratar de descargar, instalar y actualizar las actualizaciones sin ningún éxito.  En el caso de que se trate de una aula de informática con varios equipos este problema es más fácil de detectar ya que al iniciarse se puede comprobar que la conexión a Internet se ve afectada (*va más lenta al estar todos los equipos simultáneamente descargándose las actualizaciones*) y el equipo tarda mucho más tiempo en estar en condiciones de empezar a trabajar (*la descarga e instalación de las actualizaciones que se produce al arrancar el equipo colapsa parte de la potencia de procesamiento del equipo, CPU, provocando que el equipo se note más lento durante el inicio de sesión, en la interacción con el usuario, aumentando su tiempo de respuesta*).
1.  En definitiva, <b>congelar el software y aplicaciones es el mayor error que se puede cometer</b> en una red informatica que deseamos que funcione de manera aceptable.


Como solución de compromiso en <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> se ofrece la opción de **Congelación** del equipo pero sólo en su aspecto aparente (<i>garantizando que el equipo cada vez que se inicie presente el mismo aspecto</i>), no afectando a su software o aplicaciones instaladas.  Es decir, en el caso de optar por la **Congelación en <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span>** debemos tener claro que estamos congelando los datos del usuario, su perfíl, pero no las aplicaciones instaladas.  **Las aplicaciones no se congelan permitiendo su correcta actualización**, evitando de esta forma todos los problemas que acontecen en Windows.  En concreto existen dos modalidades de congelación:

- **(1) Congelar únicamente el Escritorio**
- **(2) Congelación total del perfil del usuario**

{% notificacion_important title='¿Cómo optar por una congelación u otra en Vitalinux?' %}
Para poder hacer uso de esta funcionalidad es necesario asignar a los equipos <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> la etiqueta migasfree <b>"SRV-CONGELARESCRITORIO"</b> o <b>"SRV-CONGELADORTOTAL"</b>, dependiendo si optamos por la primera o segunda modalidad.
{% endnotificacion_important %}

A modo de ejemplo, si optáramos por la primera opción **(1)** de congelación percibiríamos que el Escritorio es inmutable (*el fondo de Escritorio, los elementos que contiene, su aspecto, etc.*), pero podríamos alterar el contenido del resto de carpetas del usuario (*Documentos, Descargas, etc.*) y las aplicaciones que tiene instaladas (*instalar nuevas aplicaciones, desinstalar cualquier aplicación y actualizar las que sean necesarias*).

En el caso de que optáramos por la segunda opción **(2)** de congelación ofrecida en <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> podríamos advertir que cualquier cosa que guardemos en cualquier carpeta de nuestro perfil (*Documentos, Descargas, Vídeos, Música, etc.*) se perdería, al igual que cualquier modificación que hiciéramos del Escritorio.  Por contra, las aplicaciones del sistema estarían sin congelar (*instalar nuevas aplicaciones, desinstalar cualquier aplicación y actualizar las que sean necesarias*).  Puntualizar que esta congelación no impide que los alumnos y profesores puedan guardar su información, ya que o bien pueden guardarlo en su **pendrive**, o bien lo pueden guardar de manera centralizada en un pequeño servidor accesible desde cualquier equipo <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> del centro.

{% notificacion_alert title='¿La congelación Total en Vitalinux no me permite guardar nada dentro de mi perfil de usuario?', logotext='¡¡Aviso!!' %}
Cuando se aplica la congelación en <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> ésta sólo afecta al directorio <b>Escritorio</b> en el caso de elegir la <b>congelación de Escritorio</b>, o a las carpetas comunes que forman parte del perfil del usuario (<i>Escritorio, Documentos, Descargas, Vídeos, Música, etc.</i>) si la <b>congelación es Total</b>.  Es decir, el resto de directorios y archivos que componen el perfil o HOME del usuario (<i>/home/profesor, /home/alumno, /home/aularagon, etc.</i>) y todas sus carpetas ocultas (<i><b>CONTROL+H</b>, para ver los directorios ocultos, los que empiezan por un punto "."</i>) no se verán afectadas por dicha congelación.
<br><br>
Por ejemplo, si el usuario <b>aularagon</b> con directorio HOME <b>/home/aularagon</b> crea un directorio dentro de su perfil llamado <b>/home/aularagon/<tt>miscosas</tt></b>, éste y su contenido nunca se verá afectado por defecto por la congelación, a no ser que se especifique explicitamente a Migasfree.
<br>
De igual forma ocurre con los programas, aplicaciones o software que tenga el equipo.  Estos nunca se verán afectados por la congelación.  Los técnicos del proyecto <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> entienden que el software esta vivo y que debe actualizarse ante cualquier mejora que su desarrollador haya considerado necesaria, de hay que la congelación no les afecte.
<br><br>
En definitiva, la congelación es a efectos de datos de usuario, no a efectos de programas instalados.  Su pretensión es mantener el equipo limpio de datos que haya almacenado el usuario en el equipo y no queramos que perduren en él (<i>archivos descargados, documentos abiertos, imágenes o vídeos guardados, etc.</i>).  Para almacenar estos datos en los centros <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> ya se dispone del servicio o recurso de <b>Carpetas Compartidas</b> el cual permite que tanto los alumnos como los profesores puedan almacenar sus datos de manera centralizada, estando de esta forma disponibles y accesibles desde cualquier equipo <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> o Windows del centro.
{% endnotificacion_alert %}

## **Servicio de Carpetas Compartidas** {#ServiciodeCarpetasCompartidas}

En muchos centros educativos se hace uso de **carpetas compartidas** para centralizar la información y tenerla accesible desde cualquier equipo del centro.  Para cubrir esta necesidad se coloca en los centros un pequeño servidor que ofrece tres carpetas compartidas a los equipos Vitalinux:
1.  Carpeta compartida **"alumnos"**.  Esta carpeta es accesible tanto por los profesores como por los alumnos, y ambos tienen permisos tanto de lectura como de escritura (*modificación*).  Esta pensada para que el alumnado pueda guardar su información, y en caso de ser necesario que este accesible por parte del profesorado
1.  Carpeta compartida **"profesores"**.  Esta carpeta es accesible tanto por los profesores como por los alumnos, pero únicamente los profesores pueden modificar su contenido, pudiendo los alumnos únicamente leer y copiar lo que allí se encuentre.  Esta pensada para que los profesores les dejen materiales y trabajos a los alumnos asegurándose que estos no van a poder modificar su contenido
1.  Carpeta compartida **"privada"**.  Esta carpeta es accesible únicamente por los profesores.  Los alumnos no pueden verla.  Esta pensada para que de manera aislada los profesores puedan guardar allí sus cosas.

Para poder hacer uso de esta funcionalidad es necesario asignar a los equipos <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> la etiqueta migasfree <b>"SRV-CARPETAS-COMPARTIDAS"</b> y disponer del servidor caché que proporciona los recursos compartidos.

## **Servicio de control de equipos de aula** {#ServiciodeControldeEquiposdeAula}

En muchas de las aulas de informática de los centros educativos se suele hacer uso de aplicaciones destinadas al control de los equipos del aula por parte del equipo del profesor.  De esta manera se les puede bloquear la pantalla a todos los alumnos o parte de ellos, se puede proyectar la pantalla del profesor en todas las pantallas de los alumnos, se puede proyectar la pantalla de uno de los alumnos en el resto, se puede enviar un mensaje a los equipos de los alumnos, ... e incluso se puede dar la orden de apagado a todos los equipos de los alumnos de manera centralizada desde el equipo del profesor.  Para cubrir esa necesidad esta disponible un software que permite toda esa funcionalidad: es necesario asignar al equipo del profesor la etiqueta migasfree **"SRV-CONTROL-EQUIPOS-SERVIDOR"** y los equipos de los alumnos la etiqueta **"SRV-CONTROL-EQUIPOS-CLIENTE"**.

## **Servicio de Navegación en modo privado o incógnito** {#ServiciodeNavegacionPrivada}

Teniendo en cuenta que los equipos de los centros educativos son usados por más de una persona, puede interesarnos navegar en modo privado o incognito para evitar dejar rastro en el navegador Web (*p.e. Google Chrome o Mozilla Firefox*) de los lugares que hemos visitado y las claves que hemos introducido.  Para cubrir esta necesidad puede asignarse a los equipos Vitalinux la etiqueta migasfree **"SRV-NAVEGADORINCOGNITO"**.

## ¿Qué más Servicios? {#QueMasServicios}

Además de todo lo anterior, si tenemos en cuenta que **Migasfree** controla totalmente todo el software que hay en los equipos Vitalinux, podemos hacer cualquier cosa que creamos necesaria en ellos.  A modo de ejemplo podríamos destacar las siguientes acciones que actualmente gestionamos a través de **Migasfree**:

1.  Configuración de la **página de inicio de los navegadores**.  Mediante **Migasfree** podemos **imponer la página de inicio** que se nos indique en los navegadores Web preinstalados en Vitalinux: Google Chrome y Mozilla Firefox
1.  Instalación y Configuración de las **impresoras en red**.  Actualmente en los centros educativos existen varias fotocopiadoras multifunción (*al menos una por centro*) para que los profesores y alumnos puedan imprimir.  Gracias a **Migasfree** descargamos a la persona encargada de la gestión informática del centro de la labor de instalar y configurar impresoras en los equipos, ya que **Migasfree** permite configurar las impresoras que se le indiquen en los equipos Vitalinux que se decida
1.  Instalación de **libros digitales**.  Muchos centros educativos hacen uso de libros digitales (*p.e. para asignaturas de inglés o francés de Burlington, Oxford o Pluriel*) para la impartición de las clases.  Con la finalidad de descargar del trabajo que implica la instalación de estos libros en los equipos del centro, se puede encargar a **"Migasfree"** llevar a cabo esa función
1.  Modificar las **password de los usuarios**
1.  Modificar las **claves Wifi asociadas a los puntos de acceso**
1.  Personalización de programas instalados
1.  Configurar la hora de apagado de los equipos Vitalinux
1.  ...


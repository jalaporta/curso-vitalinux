# Primer Contacto con Vitalinux

{% notificacion_important title='¡¡Requieres Vitalinux recién instalado!!' %}
Las tareas que vamos a realizar a partir de ahora requieren de un <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> instalado, ya sea en un equipo físico o en una máquina virtual de <b>VirtualBox</b> (<i>tarea realizada previamente</i>).
<br>
En el caso de que hayas optado por usar un equipo que ya tenía instalado <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span>, será necesario volver a la <b>Post-Instalación</b> (<i>teclea CONTROL+ESPACIO y escribe <b>volver a la  post-instalación</b></i>) para poder conocer el asistente de configuración de aparece la primera vez que se inicia <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span> tras ser instalado. <b>¡¡Adelante!! ¡¡Muchos Ánimos!!</b>
{% endnotificacion_important %}

Tras el primer arranque de <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span>, resultado de una nueva instalación o de una vuelta a la <b>Post-Instalación</b>, nos aparecerán las ventanas correspondientes a un **asistente de Post-Instalación** a las cuales deberemos contestar adecuadamente para una correcta configuración de <span style='color: darkblue; font-weight: 600'; font-size: 120%;><tt>Vitalinux</tt></span>.  Aclarar que algunas de estas cuestiones dependerán del lugar donde se le vaya a dar uso a Vitalinux: **Centro Educativo** o **casa**, siendo todos ellas configurables igualmente a posteriori.

![Informaremos desde donde se usará Vitalinux: Centro Educativo o Casa](../img/Post-instalacion-1.2.png)






## <img src="img/Logobombilla.png" width="80"> Tarea 1.4:  ¿Qué hago tras el primer Arranque?

Requisitos: Es necesario haber leído los puntos de la documentación relativos a [Probar Vitalinux](probar.md) y **Primeras Pruebas con Vitalinux**

Como habrás advertido a través de la tareas anteriores, tras instalar Vitalinux, en el primer arranque se mostrará un **asistente de Post-Instalación** de Vitalinux.  A continuación se propone la **tarea de Post-Instalación**, con la finalidad de conocer que es lo que se pretende con esta post-instalación de Vitalinux.  Para ello simplemente deberás seguir las preguntas del asistente vista ya en la documentación que ya habrás leído teniendo que indicar la información siguiente:

-  El uso que va a hacerse de Vitalinux es personal, privado, **fuera del entorno de un Centro Educativo**.
-  Vas a **crear una nueva cuenta de usuario** con los siguientes campos:
    -  Nombre: aularagon
    -  Password: 1
    -  Comentario: Usuario aulAragon
-  Indicarás que el usuario recién creado **aularagon** sea **administrador** del equipo.
-  El resto de cuentas de usuario que existen por defecto no las vas a tocar, ya que no hay necesidad para ello.
-  Indicarás que se inicie sesión de manera automática con el usuario **aularagon**.

No obstante, antes de nada, nos aseguraremos de que tenemos conexión con Internet probando a abrir un navegador Web.  Para ello pulsa la combinación **CONTROL+ESPACIO** y escribe **Firefox ...** o **Chrome ...**, de tal forma que si pulsas al **INTRO** debería iniciarse el navegador seleccionado pudiendo comprobar si ya navegas (también puedes lanzar el navegador usando el icono de firefox que hay en el escritorio).

![Al pulsar CONTROL+ESPACIO aparecerá el lanzador aplicaciones Synapse, el cual tecleando parte del nombre de la aplicación deseada nos dejará lanzarla](img/Synapse.png)

Si no tienes conexión a red y el equipo se conecta por cable, revisa que estés correctamente conectado y que la red de tu casa tenga servidor DHCP (que será lo normal en un entorno doméstico).

En el caso de que la conexión sea inalámbrica deberás configurar previamente la red Wireless pinchando con el botón izquierdo del ratón sobre el icono de red que hay en la parte derecha de la barra inferior de notificaciones, permitiéndote elegir la red Wireless a la que te quieres conectar e introduciendo la contraseña de la red a la que te conectes. Si necesitas mas información o ayuda puedes ir a la [parte 4](parte_4_gestion_del_software_en_vitalinux.md) del curso donde se explica la [configuración de la red](http://wiki.vitalinux.educa.aragon.es/index.php/Vitalinux/Configurar_la_red).

![Desde el Área de notificaciones podremos configurar nuestra red inalámbrica](img/Area-de-notificaciones_migafree_red.png)

Una vez terminado el proceso de post-instalación podremos trabajar con Vitalinux, aunque **en verdad, la Post-Intalación seguirá configurando el equipo en base a la información suministrada al asistente pero de una manera transparente para el usuario**. La Post-Instalación terminará en el momento en que finalice la comunicación con el servidor Migasfree que gestiona su software, y por tanto, en el momento en que el equipo este perfectamente actualizado.

> **Formato de Entrega:** Deberás realizar las fotos (*por ejemplo, desde tu móvil*) que acrediten que has realizado cada paso de los anterioreslo que se te pide.

> Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1_apellido2_nombre_TareaX.pdf**. Si lo consideras necesario puedes indicar cualquier comentario a las capturas de pantalla.

> *Importante entregar al tutor el documento con las imágenes en formato pdf para que no haya problemas de lectura y calificar la tarea*

> Asegúrate que el nombre no contenga la letra ñ, tildes ni caracteres especiales extraños. Así por ejemplo la alumna **Begoña Sánchez Mañas**, debería nombrar esta tarea como: **sanchez_manas_begona_Tarea1.4**
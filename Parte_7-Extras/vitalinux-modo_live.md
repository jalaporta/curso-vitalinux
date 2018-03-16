{% notificacion_important title='¿Cómo Probar Vitalinux?' %} Una vez hemos descargado la imagen ISO de Vitalinux EDU 
DGA ([Área de Descargas de Vitalinux](donde_descargar_vitalinux.md#areaDescargas)) Entre todas las opciones 
destacaremos tres: - Puedes hacer las pruebas **en tu propio ordenador** iniciando Vitalinux en **modo Live**.  El 
**modo Live** es una posibilidad que nos ofrece Linux para probar sus sistema operativos **sin tener que instalarlos 
en el disco duro de nuestro equipo**. Para ello será necesario pasar el archivo ISO con la imagen de Vitalinux a un 
DVD o memoria USB, y posteriormente indicarle a nuestro equipo que arranque desde ese DVD o USB (*el DVD o USB hará 
las veces de disco duro de la máquina*).  Ésta opción es recomendada cuando quieres tener una primera experiencia de 
uso de un sistema operativo Linux, pero no para un uso habitual del sistema ya que normalmente son sesiones de uso no 
persistentes (*tras trabajar en modo Live, cuando se apaga el equipo se pierden todos los datos, todos los cambios 
realizados o personalizaciones realizadas*). - Usar un [ **software de 
Virtualización**](http://wiki.vitalinux.educa.aragon.es/index.php/Vitalinux/Vitalinux_con_VirtualBox) como 
VirtualBox. Para llevar a cabo el presente curso de introducción a Vitalinux se va a sugerir el hacer uso de 
Virtualbox.  Si quieres o deseas hacer uso de alguna otra opción tan sólo tendrás que sugerírsela al tutor. Una vez 
decidido ésto ... podemos continuar con el curso!!
{% endnotificacion_important %}


## <img src="img/Logobombilla.png" width="80"> Tarea 1.3 Op2: ¿Cómo probar Vitalinux en modo Live? {#tarea1-3-2}

**Requisitos: Es necesario haber leído el punto de la documentación**

En primer lugar, aclarar/recordar que esta tarea es **opcional**, o como alternativa a la propuesta como obligatoria: **Probar Vitalinux mediante Virtualbox**.  Asumiendo que has leído y realizado las tareas anteriores, y que por tanto, dispones de la imagen ISO de Vitalinux, a continuación pasaremos a crear un **Live DVD o USB** para posteriormente probar **Vitalinux en modo Live**.  Arrancar el sistema en **modo Live** nos va a permitir poder probar Vitalinux de igual forma a como si estuviera instalado en el equipo pero **sin alterar para nada el sistema operativo y los datos que haya en el disco duro del equipo**.  Aunque por sencillez se sugiere la creación de un Live DVD, se puede optar por la creación de un Live USB para la realización exitosa de esta tarea ya que en ocasiones es mas sencillo contar con un USB que con un DVD. **Solo es necesario realizar la tarea con una de las dos opciones propuestas**:

-  **Live DVD**: Quema la imagen **ISO de Vitalinux** que te hayas descargado en un **DVD**, y posteriormente, configura el **Boot Loader** de tu equipo para que en lugar de arrancar con el sistema que tienes instalado en el disco duro lo haga con el sistema disponible en el DVD.  Una vez que arranque el equipo desde el DVD deberás elegir la opción de **Arranque en modo Live** en el menú de arranque que aparecerá (*ver imagen adjunta*), provocando que el sistema operativo Vitalinux arranque sin necesidad de modificar ni instalar nada del disco duro del equipo.  Tras un periodo de espera deberías visualizar el **entorno de Escritorio de Vitalinux** con una ventana emergente de configuración que aparece en el primer arranque de Vitalinux (*al trabajar en modo Live, y no guardarse nada, no hay constancia de que el sistema Vitalinux se inició en algún momento, por lo que por muchas veces que repitamos el proceso siempre nos aparecerán estas ventanas emergentes de configuración*).

![Arranque Live](img/arranque-live.png)

![Post-instalación](img/Post-instalacion-1.png)

-  **Live USB**: Vuelca la imagen **ISO de Vitalinux** en una **memoria USB** mediante algún software que te permita este proceso, como por ejemplo **UnetBootin**, y posteriormente configura el **Boot Loader** de tu equipo para que en lugar de arrancar con el sistema que tienes instalado en el disco duro lo haga con el sistema disponible en el USB.  Después deberás seguir los mismos pasos que en el caso de haber creado un **Live DVD**. Con la finalidad de que el sistema se cargue y responda rápido se recomienda hacer uso de una memoria USB 3.0.

Una vez haya arrancado **Vitalinux en modo Live**, para empezar a probar Vitalinux deberemos **cerrar** el asistente de post-instalación pinchando en **Salir de la Post-Instalación** (*Esta post-instalación la veremos en detalle más adelante*)

> **Formato de Entrega:** Deberás realizar las fotos (*por ejemplo, desde tu móvil*) que acrediten que has realizado lo que se te pide.

> Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1_apellido2_nombre_TareaX.pdf**. Si lo consideras necesario puedes indicar cualquier comentario a las capturas de pantalla.<dl><dd> Importante entregar al tutor el documento con las imágenes en formato pdf para que no haya problemas de lectura y calificar la tarea*</dd></dl>Asegúrate que el nombre no contenga la letra ñ, tildes ni caracteres especiales extraños. Así por ejemplo la alumna **Begoña Sánchez Mañas**, debería nombrar esta tarea como: **sanchez_manas_begona_Tarea1.3**
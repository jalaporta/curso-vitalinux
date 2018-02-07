# Cliente Migasfree

## Contenido

- [1 Análisis de la comunicación con el Servidor Migasfree](#AnalisisComunicacionMigasFree)
    - [1.1 Interfaz](#Interfaz)
    - [1.2 Análisis de la comunicación entre el Cliente y Servidor Migasfree](#AnalisisComunicacionClienteServidor)
    - [1.3 Actualización contra Migasfree desde la Consola](#ActualizacionContraMigasfreConsola)
- [2 Etiquetas Migasfree](#EtiquetasMigasfree)
    - [2.1 ¿Qué son y para qué sirven las etiquetas Migasfree?](#EtiquetasMigasfree)
    - [2.2 Asignación de Etiquetas Migasfree](#AsignacionEtiquetasMigasfree)
    - [2.3 Comprobación de Etiquetas Migasfree](#ComprobacionEtiquetasMigasfree)
    - [2.4 Consideración especial](#ConsideracionEspecial)

**Vitalinux EDU DGA** lleva como sistema base un **Lubuntu** (una de las versiones ligeras de ubuntu con escritorio LXDE), una personalización al entorno educativo y lo más importante: un **cliente Migasfree**. Este cliente permite a Lubuntu comunicarse con un servidor central gesgtionado por el proyecto para que a través de éste pueda gestionarse el equipo:

-  **Instalación/Desinstalación/Actualización del Software**
-  **Configuración del equipo**: *Hora de Apagado*, *Personalización del fondo de Escritorio*, *Instalación y Configuración de Impresoras*, *Instalación y configuración de Libros digitales*, etc.
-  **Detección y resolución de incidencias**
-  Inventario de todo el software y hardware del Equipo
-  ...

¡¡Y todo ello **de manera completamente desatendida**!!  Esto facilita la labor de los coordinadores de medios informáticos de los centros y del profesorado ya que de esta forma se pueden desentender de tareas muy tediosas.

Se puede ver más en profundidad todo en la [documentación oficial de migasfree](http://fun-with-migasfree.readthedocs.io/en/master/)

Éste documento pretende aclarar un poco más como se lleva a cabo dicho proceso, sin entrar en detalles complejos o de programación.

Como ***más vale un buen videotutorial que mil palabras*** a continuación se sugiere ver el [siguiente vídeo](https://youtu.be/MiPYmOzlN4g) relacionado con la teoría de esta parte del curso: **Cliente Migasfree**

{% youtube %}https://youtu.be/MiPYmOzlN4g{% endyoutube %}

## Análisis de la comunicación con el Servidor Migasfree {#AnalisisComunicacionMigasFree}

Cada vez que el equipo inicia una sesión gráfica, si éste tiene comunicación con Internet y el servidor Migasfree está activo, comienza una comunicación entre el cliente Migasfree y el servidor Migasfree.

No obstante, antes de establecerse propiamente la comunicación con el servidor Migasfree, el sistema realiza una serie de comprobaciones/acciones, como por ejemplo:

-  Comprobar si hay acceso a Internet (*para conectar después con Migasfree*)
-  Comprobar si hay conexión con el servidor caché que se coloca en los centros educativos (*para poder usarlo a posteriori*)
-  Intentar reparar instalaciones de software que se quedaron a mitad o rotas en sesiones anteriores
-  ...

Después se lanza propiamente la comunicación con el servidor Migasfree. A continuación se analizará que ocurre en dicha comunicación y como forzar para que se realice en cualquier otro momento.

### Interfaz {#Interfaz}

Como hemos dicho, cuando la máquina arranca se desencadena el proceso anterior. Podemos ver que se está ejecutando a través del icono de la barra inferior de tareas. Si aparece el **triángulo verde** significa que se están realizando acciones en ese momento y que no se ha terminado la comunicación con el servidor Migasfree:

![migasfree actualizando](img/migasfree-on.png)

Una vez haya terminado todo el proceso (*comprobaciones y posterior comunicación con el servidor*) podremos advertir que el icono referente a **Migasfree** cambia:

![Servicio de actualización finalizado](img/Migasfree-off.png)

También podemos encontrarnos con otros iconos que nos indiquen otras situaciones: *es necesario reiniciar*, *se ha detectado un problema*, etc.  En el caso de visualizar estos otros iconos, podremos pulsar sobre dicho icono para que nos de más información.


Igualmente, si pulsamos sobre el **icono de Migasfree** podremos ver otras opciones como son:

-  **Volver a lanzar el proceso de actualización**
-  **Ver la consola** (*detalles*)
-  **Conocer nuestra identificación**. El número que identifica al equipo de forma unívoca y que aparece en el Widget del escritorio como CID
-  **Obtener ayuda**

![Opciones del tray de migasfree](img/Migasfree-options.png)

### Análisis de la comunicación entre el Cliente y Servidor Migasfree {#AnalisisComunicacionClienteServidor}

A continuación veremos en detalle el proceso de comunicación entre nuestro Vitalinux (*cliente Migasfree*) y el servidor Migasfree. En concreto, una vez que se conecta con el servidor Migasfree se desencadenan las siguientes acciones:

**(1) Conectando al servidor migasfree...**

En primer lugar se comprueba que hay **conectividad** con el servidor migasfree, **migasfree.educa.aragon.es**.

**(2) Obteniendo propiedades... / Evaluando atributos... / Subiendo atributos...**

El servidor Migasfree le dice que le tiene que facilitar una información: **PROPIEDADES**. El cliente (*Vitalinux*) recopila dicha información en relación a propiedades que lo caracterizan (*el valor de la propiedad se llama **atributo**, y son **características software y hardware***), y que le permiten al servidor **identificarlo y clasificarlo**.

**(3) Ejecutando fallas... / Subiendo fallas...**

En el lado del servidor se programan **pequeños programas** llamados **"fallas"**. Estas fallas se asignan a los equipos en función de sus propiedades, atributos o etiquetas (*recordaremos que es una **Etiqueta Migasfree** en la siguiente sección*). De esta forma, en función de la información recolectada en el paso anterior, y la que ya tiene Migasfree en su base de datos decide cual de estas fallas se ejecutan en el equipo cliente. Las fallas permitirán cosas como:

-  **Realizar comprobaciones**: si no queda espacio en disco, si hay errores en instalación
-  **Arreglar pequeños Bugs**
-  **Aplicar configuraciones**: cambiar fondo de Escritorio, crear Accesos directos en el Escritorio a determinadas aplicaciones, crear archivos y directorios, etc.
-  **Configurar impresoras**
-  **Gestionar contraseñas de usuarios**
-  '*Gestionar contraseñas de redes Wireless*
-  .... ¡¡¡Cualquier cosa que nos queramos imaginar cuyo procesamiento requiera menos de un par de minutos!!!

**(4) Creando repositorios... / Obteniendo los metadatos de los repositorios...**

Un repositorio es un sitio centralizado en Internet donde se almacena software disponible para ser instalado en un equipo. El servidor Migasfree en función de las propiedades, atributos y etiquetas del equipo le asocia unos repositorios u otros para que su software asociado **este disponible**.

**(5) Desinstalando paquetes... / Instalando paquetes obligatorios... / Actualizando paquetes...**

En este punto, el servidor Migasfree da la orden al equipo cliente de desinstalación, instalación y actualización del software que se le haya indicado previamente a Migasfree. De ésta forma el equipo:

-  Tendrá el software actualizado (se corrigen errores y se mejora la funcionalidad)
-  Tendrá el software base que se le especificó
-  No tendrá el software que no queremos que tenga
*¿Podremos instalar otro software o quitar software que no queramos?* **POR SUPUESTO** (*si tenemos permisos de administrador sobre la máquina*). Con lo anterior solo forzamos a un perfil de software BASE. 

**(6) Subiendo el historial del software... / Subiendo el inventario del software...**

Por último, el servidor Migasfree registra o inventaria el cambio que se haya podido producir en el software instalado en el equipo, de tal forma que a posteriori se puede saber que ha sucedido con los programas disponibles en el equipo.

### Actualización contra Migasfree desde la Consola {#ActualizacionContraMigasfreConsola}

Para actualizar el equipo contra migasfree de una manera expicita deberemos ejecutar el siguiente comando:

```bash
$ sudo migasfree --update
# migasfree -u
```

## Etiquetas Migasfree {#EtiquetasMigasfree}

### ¿Qué son y para qué sirven las etiquetas Migasfree? {#EtiquetasMigasfree}

Las etiquetas Migasfree son utilizadas para clasificar los equipos según un criterio personal/de centro. Por ejemplo, mediante estas etiquetas podemos etiquetar a un equipo para que quede asociado a un centro educativo específico, para saber si el usuario que va a usar dicho equipo es un alumno o un profesor o para indicar que el equipo requiere de algún tipo de servicio específico (*carpetas compartidas, congelación del Escritorio, etc.*).


De esta forma, haciendo uso de estas etiquetas podemos distinguir a los equipos por centro al que pertenecen e instalar únicamente el software solicitado por dicho centro. Podemos además tener **etiquetas jerarqueizadas**, de forma que podemos agrupar los equipos de forma más lógica y sencilla. Por ejemplo, podríamos tener un centro con las siguientes necesidades:

- Una etiqueta para todos los equipos del centro (supongamos que de Primaria): PRI-MICENTRO
- Otra etiqueta para identificar a los equipos de un departamento: PRI-MICENTRO.INGLES
- E incluso una para identificar un aula (son ejemplos, cada centro decide su estructura): PRI-MICENTRO.INGLES.AULA1

De ésta forma, simplemente etiquetando a un equipo como **PRI-MICENTRO.INGLES.AULA1**, ya no hace falta etiquetarlo como de **INGLES** o de **MICENTRO** ... automáticamente le afectarán las condiciones que hayamos definido para esos grupos.


*Aclaración: Si un equipo tiene marcadas las tres etiquetas no hay problema ... pero es más fácil marcar solo una etiqueta!!!*


### Asignación de Etiquetas Migasfree {#AsignacionEtiquetasMigasfree}

Tras la instalación de Vitalinux en un equipo y en el caso de que haya conexión con Internet, la primera vez que se inicie en ese equipo una sesión gráfica se ejecutara una breve post instalación a través de la cual podremos asignarle al equipo las etiquetas que deseemos. En concreto, se nos mostrará la ventana siguiente:

![](img/014-sesion2-MIAS.png)

Entre las muchas etiquetas disponibles deberemos tener en cuenta lo siguiente para su asignación:

-  **SRV-CONGELARESCRITORIO:** Esta opción mantendrá el escritorio congelado para evitar que los usuarios guarden o modifiquen cosas en él. Dicha congelación se basa en la comparación entre lo que hay en el escritorio del usuario y un patrón que se localiza en /etc/skel/Desktop/, de tal forma que todo aquello que haya de más respecto al patrón es eliminado. Por tanto, para añadir cosas al Escritorio será necesario modificar el patrón.
-  **SRV-CONGELADORTOTAL:** Esta opción mantendrá congelado tanto el escritorio como el resto de directorios del perfil del usuario (Documentos, Imágenes, etc.). Dicha congelación se basa en la comparación entre lo que hay en los directorios del perfil del usuario y un patrón que se localiza en /etc/skel-directorios-congelados/, de tal forma que todo aquello que haya de más respecto al patrón es eliminado. Por tanto, para añadir cosas a los directorios del perfil del usuario será necesario modificar el patrón.
-  **SRV-CARPETASCOMPARTIDAS**: Esta opción permite tener acceso a varias carpetas compartidas por el servidor caché que se localiza en los centros.
-  **SRV-NAVEGADORINCOGNITO:** Esta etiqueta modificará el comportamiento de nuestros navegadores web (firefox y chrome), provocando que se incien en modo incógnito.
-  **SRV-CONTROL-EQUIPOS-******: Esta etiqueta sirve para desplegar un servicio de control y herramientas de comunicación de aula con epoptes.
-  **PRI/SEC-”Nombre del centro”:** Esta etiqueta permite indicar a qué centro pertenece el equipo, para que este pueda descargar el software y los recursos que le corresponden de una manera personalizada.
-  **ENT-ALUMNO:** Esta etiqueta indicará que el equipo está destinado al uso de los alumnos, asociándole un software específico.
-  **ENT-PROFESOR: **Esta etiqueta indicará que el equipo está destinado al uso de profesores, asociándole un software específico.

Estas etiquetas podrán ser modificadas en cualquier momento si se desea, para ello deberemos ir a: **Inicio → Vitalinux → MigaScrpts → Etiquetas → Modificación de Etiquetas**

![](img/015-sesion2-MIAS.png)

### Comprobación de Etiquetas Migasfree {#ComprobacionEtiquetasMigasfree}

Al igual que podemos asignar las etiquetas mediante el ejectuable Modifiación de Etiquetas, podemos comprobar las etiquetas que tenemos con **Consultar y Comprobar Etiquetas Migasfree**

### Consideración especial {#ConsideracionEspecial}

Existe una etiqueta "especial", y es la denominada **ENT-CASA**. Dicha etiqueta se creó con la idea de que alguien pueda usar Vitalinux en casa, pero quiera tener un "perfil" similar al de un centro. Pero si marcamos dicha etiqueta se desencadenarán algunas acciones importantes a tener en cuenta:

-  No será posible acceder al equipo de forma remota para soporte sin intervención, de forma que garantizamos su privacidad
-  No se tendrán en cuenta ciertas acciones como el cambio de passwords u otras que afecten a un centro de forma carácterística.

## Habilitar o deshabilitar el cliente

El cliente migasfree se arranca como hemos dicho de forma automática cada vez que arrancamos la máquina o iniciamos sesión. Es posible que nos interese en un momento dado deshabilitar ésta característica ya que por ejemplo estamos de viaje y no queremos consumir datos de nuestra conexión 3G, o nuestra red va muy lenta o por cualquier otro motivo. Para éstos casos podemos deshabilitar el cliente simplemente ejectuando CTRL-ESPACIO + Habilitar Deshabilitar...

![hablitar o deshabilitar el cliente migasfree](img/Habilitar-clientemigas.png)

Mientras el equipo tenga deshabilitado el cliente, NO se recibirán actualizaciones de software, no se podrá actuar de forma automática y desatendida, y no se recibirán los errores que se produzcan.


***Recuerda pues habilitarlo de nuevo para tener éstas funcionalidades*** simplemente ejecutando de nuevo el programa.


## <img src="img/Logobombilla.png" width="80"> Tarea 4.6: Análisis de la Comunicación entre el Cliente y Servidor Migasfree

Requisitos: Es necesario haber leído todo lo referente al **Cliente de migasfree** 

Para la realización de la tarea se supone que dispones de un sistema Vitalinux en una **máquina física** o **virtual**.  En concreto se propone llevar a cabo la siguiente tarea:

**Parte 1**. **Cliente migasfree**. Una vez se inicia sesión en Vitalinux abre la **consola del cliente Migasfree** y observa los mensajes que se producen. Para poder moverte con el **"scroll"** (*arriba y abajo*) deberás esperar a que termine el proceso. Haz dos capturas de pantalla:
1. Donde aparezca el momento de la actualización donde **Migasfree chequea como vas de espacio libre** a través de una falla: **CHECK-HW-ESPACIO-LIBRE-DISCO**
2. Cuando **Migasfree da la orden de actualizar el sistema**

**Parte 2**. Comprobación de **Etiquetas Migasfree**. Comprueba que etiquetas has asignado cuando hiciste la postinstalación y confirma que aparecen. Si no marcaste ninguna, lo cual es posible al marcar que ibas a usar el equipo fuera del entorno educativo, estará marcada la etiqueta de ENT-CASA. Haz una captura de pantalla con dicho listado. Más tarde asignaremos otra para instalar software.  **Importante**: *Para tener una información completa de la configuración de red y etiquetado Migasfree de tu Vitalinux puedes teclear **CONTROL + ESPACIO** y escribir* *Información Global del Sistema*

> **Formato de Entrega**: Si no encuentras muchos problemas para ello, haz capturas de pantalla (tecla IMPRIMIR PANTALLA) de todo lo que vayas haciendo, y almacénalas en una memoria USB o donde creas conveniente. En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil. Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1\_apellido2\_nombre\_TareaX.pdf**.











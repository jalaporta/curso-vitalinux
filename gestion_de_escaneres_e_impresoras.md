# Gestión de Escáneres e Impresoras







## Contenido

- [1 ¿Cómo configurar una impresora USB en Vitalinux?](#.C2.BFC.C3.B3mo_configurar_una_impresora_USB_en_Vitalinux.3F)
- [2 ¿Problemas con algún modelo HPLaserJet 1005, 1018, 1020, 1102, 2015, ...?](#.C2.BFProblemas_con_alg.C3.BAn_modelo_HPLaserJet_1005.2C_1018.2C_1020.2C_1102.2C_2015.2C_....3F)
- [3 Tarea 5.8 (Optativa): Configurar una impresora local USB](#Tarea_5.8_.28Optativa.29:_Configurar_una_impresora_local_USB)
- [4 ¿Cómo configurar un escáner USB en Vitalinux?](#.C2.BFC.C3.B3mo_configurar_un_esc.C3.A1ner_USB_en_Vitalinux.3F)
- [5 Tarea 5.9 (Optativa): Configurar un Escáner local USB](#Tarea_5.9_.28Optativa.29:_Configurar_un_Esc.C3.A1ner_local_USB)

## ¿Cómo configurar una impresora USB en Vitalinux?

La configuración de una impresora en Linux/Vitalinux es muy sencillo.  A continuación se detallan los pasos necesarios para la instalación y configuración de una impresora local USB, aunque los pasos a seguir serían similares en el caso de que se tratara de una impresora o fotocopiadora en red.


1.  Conecta la impresora a la red eléctrica y al equipo para que éste la detecte 
<li>
Accederemos al **Panel de Control de gestión de Impresoras**.  Para ello **CONTROL + ESPACIO** y escribimos **"Impresoras"**
</li>
[<img alt="" class="thumbimage" height="284" src="/images/0/0b/Vitalinux-configurar_impresora_1.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_1.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_1.png)Panel de Control para la Gestión de Impresoras
<li>
Pinchamos sobre el botón asociado a **Añadir una nueva Impresora**
</li>
1.  Seleccionamos la **Impresora Detectada** por el sistema Linux que queremos instalar y configurar (*p.e. una impresora USB*).  En el caso de que se trate de una impresora o fotocopiadora en Red deberemos pinchar en **Buscar impresora de red** e indicar su dirección IP, y seleccionar el protocolo o **modo de conexión** usado para comunicarse con ella
[<img alt="" class="thumbimage" height="338" src="/images/8/8e/Vitalinux-configurar_impresora_2.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_2.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_2.png)Tras pinchar en **Añadir Impresora** advertiremos que habrá reconocido la impresora USB que tengamos conectada.  En caso de ser una impresora o fotocopiadora en red deberemos pinchar en **Buscar impresora de red** e indicar su dirección IP
[<img alt="" class="thumbimage" height="338" src="/images/1/15/Vitalinux-configurar_impresora_3.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_3.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_3.png)Tras pinchar en **Añadir Impresora**, en el caso de que sea una impresora o fotocopiadora en red deberemos pinchar en **Buscar impresora de red** e indicar su dirección IP, y seleccionar el protocolo o **modo de conexión** con ella
<li>
Una vez el sistema haya autocomprobado que dispone del driver de comunicación adecuado para comunicarse con ese modelo de impresora, nos mostrará un dialogo con las **Opciones de Configuración de la Impresora**
</li>
[<img alt="" class="thumbimage" height="338" src="/images/2/23/Vitalinux-configurar_impresora_4.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_4.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_4.png)Opciones de Configuración de la Impresora
1.  Indicaremos un **Nombre** que identifique a la impresora (*evitaremos hacer uso de espacios en blanco*), una **Descripción** y una **Localización**, los cuales nos permitirán identificar ese modelo de impresora a posteriori 
[<img alt="" class="thumbimage" height="336" src="/images/2/2e/Vitalinux-configurar_impresora_5.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_5.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_5.png)Nombre, descripción y ubicación de la impresora
1.  Tras la configuración de la impresora se nos invitará a mandarle un trabajo de prueba y así comprobar su correcto funcionamiento 
[<img alt="" class="thumbimage" height="286" src="/images/a/a0/Vitalinux-configurar_impresora_6.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_6.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_6.png)Prueba de impresión
<li> A posteriori, desde el **Panel de Control de la gestión de Impresoras**, pinchando con el **botón derecho** del ratón sobre la impresora deseada podemos personalizar su comportamiento por defecto: *Tamaño de papel, Color o Blanco y Negro, Una cara o Doble cara, etc.*
[<img alt="" class="thumbimage" height="179" src="/images/d/d2/Vitalinux-configurar_impresora_7.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_7.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Vitalinux-configurar_impresora_7.png)Opciones de Configuración de los trabajos a Imprimir
</li>
Como ***más vale un buen videotutorial que mil palabras*** a continuación se sugiere ver el [siguiente vídeo](https://youtu.be/yuUDWJwABbM) relacionado con la teoría de esta parte del curso: **Instalación y Configuración de Impresoras**


## ¿Problemas con algún modelo HPLaserJet 1005, 1018, 1020, 1102, 2015, ...?

Gracias a **Fernando Peña**, MIA el IES Miralbueno, a continuación daremos una solución a un conjunto de impresoras HP LaserJet para las cuales los drivers disponibles por defecto no funcionan.


En el **caso de que la detección de la impresora o posterior configuración no resulte exitosa**, es posible que tengamos que hacer uso del software privativo del fabricante para darle una solución.  Este puede ser el caso de los modelos HPLaserJet 1018, 1020, P1102, P1102W, etc.  En ese caso concreto, para que sirva de ejemplo, los pasos a seguir serían los siguientes:

****<center>¡¡Cuidado si la impresora es USB!!</center>\nUn detalle a tener en cuenta antes de empezar es que **si la impresora va por USB**, no hay que conectarla hasta que nos lo diga el asistente posterior de instalación. Si ya está conectada, en un momento de la instalación habrá que desconectar el cable USB y volver a conectarlo. Si la conexión es por red puede estar conectada desde el principio</p></td>




1.  Vamos a la página **[http://hplipopensource.com/hplip-web/index.html](http://hplipopensource.com/hplip-web/index.html)** 
[<img alt="" class="thumbimage" height="225" src="/images/3/33/Ies-miralbueno-configurar_impresora-pantalla1.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla1.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla1.png)Pagina Web de hplip
1.  Pulsamos en **"Download HPLIP"** 
<li>
**Seleccionamos la distribución y versión de linux (*Ubuntu 14.04*)**, además del tipo y modelo de impresora. Nos lleva a otra pantalla donde nos da la opción de seguir o corregir. Pulsamos **"Next"** y nos lleva a otra pantalla para descargar lo necesario.  En algún punto de este proceso nos dirá que nuestra versión ya viene preparada para la impresora. Seguimos adelante.
</li>
[<img alt="" class="thumbimage" height="225" src="/images/7/7f/Ies-miralbueno-configurar_impresora-pantalla2.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla2.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla2.png)**Seleccionamos la distribución y versión de linux (*Ubuntu 14.04*)**
[<img alt="" class="thumbimage" height="225" src="/images/8/84/Ies-miralbueno-configurar_impresora-pantalla3.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla3.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla3.png)Seguimos el asistente
[<img alt="" class="thumbimage" height="225" src="/images/f/fa/Ies-miralbueno-configurar_impresora-pantalla4.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla4.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla4.png)Seguimos el asistente
<li>
Accedemos a otra pantalla con las instrucciones (*en inglés*), [http://hplipopensource.com/hplip-web/install/install/index.html](http://hplipopensource.com/hplip-web/install/install/index.html), y el botón de descargar.
</li>
[<img alt="" class="thumbimage" height="225" src="/images/e/ee/Ies-miralbueno-configurar_impresora-pantalla5.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla5.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla5.png)Seguimos el asistente
[<img alt="" class="thumbimage" height="225" src="/images/e/ef/Ies-miralbueno-configurar_impresora-pantalla6.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla6.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla6.png)Seguimos el asistente
<li> Descargamos, abrimos el terminal, nos vamos a la carpeta donde está la descarga y seguimos las instrucciones (*básicamente es elegir las opciones por defecto*)
</li>
[<img alt="" class="thumbimage" height="281" src="/images/4/41/Ies-miralbueno-configurar_impresora-pantalla7.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla7.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla7.png)Desde la terminal ejecutaremos el software descargado
[<img alt="" class="thumbimage" height="281" src="/images/0/0a/Ies-miralbueno-configurar_impresora-pantalla8.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla8.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla8.png)Seguiremos los pasos de instalación del asistente de la consola Linux
[<img alt="" class="thumbimage" height="225" src="/images/8/80/Ies-miralbueno-configurar_impresora-pantalla12.png" width="400"/>](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla12.png) [](http://wiki.vitalinux.educa.aragon.es/index.php/Archivo:Ies-miralbueno-configurar_impresora-pantalla12.png)Seguiremos los pasos de instalación del asistente de la consola Linux

## Tarea 5.8 (Optativa): <center>Configurar una impresora local USB</center>
Requisitos: Es necesario haber leído todo lo referente a [Instalación y Configuración de Impresoras en Vitalinux](http://wiki.vitalinux.educa.aragon.es/index.php/Vitalinux/Configurar_Impresoras_Locales) y disponer de un equipo con Vitalinux instalado para realizar la Tarea</tt>** *A través de esta tarea opcional se sugiere seguir los pasos explicados en la teoría e instalar y configurar una impresora USB.</p></td>





## ¿Cómo configurar un escáner USB en Vitalinux?

La configuración de un escáner en Linux/Vitalinux es muy sencillo, ya que no se requiere hacer absolutamente nada.  En el caso de que por algún motivo el escáner no sea correctamente detectado por el sistema la aplicación encargada de escanear (*p.e. Simple Scan*) nos avisará de ello:


Como ***más vale un buen videotutorial que mil palabras*** a continuación se sugiere ver el [siguiente vídeo](https://youtu.be/-A6CX4exyeg) relacionado con la teoría de esta parte del curso: **Instalación y Configuración de Escáneres**


## Tarea 5.9 (Optativa): <center>Configurar un Escáner local USB</center>
Requisitos: Es necesario haber leído todo lo referente a [Instalación y Configuración de Escáneres en Vitalinux](http://wiki.vitalinux.educa.aragon.es/index.php/Vitalinux/Configurar_Escaneres_Locales) y disponer de un equipo con Vitalinux instalado para realizar la Tarea</tt>** *A través de esta tarea opcional se sugiere seguir los pasos explicados en la teoría e instalar y configurar un escáner USB.</p></td>












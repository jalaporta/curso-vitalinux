# ¿Cómo Probar Vitalinux?



{{Importante|¿Donde probar Vitalinux?|Una vez hemos descargado la imagen ISO de Vitalinux EDU DGA (_[[Descargar|Área de Descargas de Vitalinux]]_) tenemos diferentes posibilidades/opciones para poder **probar Vitalinux** y establecer un primer contacto con él.  Ésta decisión es importante, ya que Vitalinux no es una aplicación sin más que podamos instalar y desinstalar ... sino de un Sistema Operativo completo.  Entre todas las opciones destacaremos tres:

# Puedes hacer las pruebas **en tu propio ordenador** iniciando Vitalinux en **modo Live**.  El **modo Live** es una posibilidad que nos ofrece Linux para probar sus sistema operativos **sin tener que instalarlos en el disco duro de nuestro equipo**. Para ello será necesario pasar el archivo ISO con la imagen de Vitalinux a un DVD o memoria USB, y posteriormente indicarle a nuestro equipo que arranque desde ese DVD o USB (_el DVD o USB hará las veces de disco duro de la máquina_).  Ésta opción es recomendada cuando quieres tener una primera experiencia de uso de un sistema operativo Linux, pero no para un uso habitual del sistema ya que normalmente son sesiones de uso no persistentes (_tras trabajar en modo Live, cuando se apaga el equipo se pierden todos los datos, todos los cambios realizados o personalizaciones realizadas_).
# **Instalar Vitalinux en un equipo**.  Esta es la opción más recomendable cuando tenemos claro que Vitalinux va a ser nuestro sistema operativo de trabajo de ahora en adelante.  Al instalar Vitalinux en el disco duro de tu equipo tendrás la opción de eliminar todo lo que allí exista y hacer una instalación limpia, o hacer una **instalación dual** para tener la opción de poder seguir trabajando tanto con el sistema operativo que ya tengas instalado (p.e. Windows 7) y Vitalinux.  Si deseas hacer uso de esta opción y dudas si usar tu equipo personal, puedes usar **otro ordenador** diferente, puedes usar otro ordenador que tengas de pruebas, alguno del centro educativo en el que trabajas o un equipo antiguo que no sepas que uso darle.
# Usar un [[Vitalinux/Vitalinux_con_VirtualBox | **software de Virtualización**]] como VirtualBox.  Ésta última opción es la más recomendable para tener un primer contacto con Vitalinux, poder probarlo en toda su plenitud e incluso seguir trabajando con él en un futuro.  Este tipo de software (_p.e. Virtualbox_), permite crear dentro de nuestro equipo **Máquinas Virtuales** que posteriormente podemos eliminar, al igual que eliminamos cualquier otro archivo de nuestro sistema, y sobre las cuales podemos instalar el sistema operativo que deseemos probar, en nuestro caso Vitalinux.   En concreto, haciendo uso de estas **máquinas virtuales** tendremos exactamente las mismas posibilidades que tendríamos con un equipo físico: probar Vitalinux en modo live o instalarlo en su disco duro Virtual, y todo ello **sin tener que temer que le ocurra nada a nuestro equipo**.

Para llevar a cabo el presente curso de introducción a Vitalinux se va a sugerir el hacer uso de Virtualbox.  Si quieres o deseas hacer uso de alguna otra opción tan sólo tendrás que sugerírsela al tutor. Una vez decidido ésto ... podemos continuar con el curso!!
}}


__TOC__

{{:Vitalinux/Vitalinux_con_VirtualBox}}

&lt;br&gt;

{{:Curso_Aularagon/ejercicio1-3}}

## Crear un Live DVD Bootable de Vitalinux 
Un **Live DVD** nos va a permitir poder probar **Vitalinux** sin necesidad de instalarlo.  Para ello simplemente tendremos que abrir la aplicación que normalmente usemos para grabar CDs/DVDs y buscar una de las opciones que se encuentra disponible en todos los **quemadores de CDs/DVDs** referente a **grabar una imagen existente en un CD/DVD**, la cual nos solicitará la ubicación de la imagen **ISO de Vitalinux** que hayamos descargado previamente para pasarla posteriormente a un DVD Virgen que hayáis insertado en la unidad de CDs/DVDs.
Además, por lo general, si abrimos nuestro explorador de archivos y nos situamos en el directorio donde se encuentran las imágenes ISO, y pinchamos con el botón derecho del ratón sobre la imagen ISO nos debería aparecer una opción que explícitamente nos invite a grabar dicha ISO en un CD/DVD.

## Crear un Live USB Bootable de Vitalinux 
De forma similar a un CD/DVD Arrancable, podemos grabar la imagen **ISO de Vitalinux** en una **memoria USB** con la finalidad de poder probar o instalar Vitalinux.  A diferencia de lo que nos ocurre con los CD/DVD, nuestro sistema operativo no siempre integra una aplicación que se encargue de grabar la ISO en una memoria USB, por lo que tendremos que instalar una aplicación expresamente para ello si no existe una alternativa.

{{:Curso Aularagon/crear usb bootable}}

&lt;br&gt;
{{:Curso_Aularagon/ejercicio1-4}}

&lt;br&gt;
{{:Curso Aularagon/modificar boot order}}

&lt;br&gt;

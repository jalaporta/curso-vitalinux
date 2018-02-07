# Acciones del Explorador de Archivos

## Contenido

- [1 Acciones del Explorador de Archivos](#Acciones_del_Explorador_de_Archivos)
- [2 Tarea 5.1: Acciones del Explororador de Archivos](#Tarea5-1)

## Acciones del Explorador de Archivos {#Acciones_del_Explorador_de_Archivos}

Una de las característica más importantes que suele tener la mayor parte de los **Exploradores de Archivos** en Linux es la posibilidad de poder configurar y personalizar **acciones** (*Custom Actions*), aumentando de esta forma sus posibilidades y potencia.  **Vitalinux**, al basarse en la versión ligera de Ubuntu, **Lubuntu**, hace uso del **Explorador de Archivos *pcmanfm***, posiblemente, el explorador más ligero que existe.  No obstante, aún siendo ligero, **pcmanfm** ofrece la posibilidad de configurar mediante el uso de pequeños programas, funcionalidades añadidas para poder interactuar con los directorios y archivos por los que navega.  


En concreto, se han desarrollado para **Vitalinux EDU DGA** diversas funcionalidades **para manipular archivos PDFs**, **archivos MP3**, **imágenes**, ... tal como se puede apreciar al pinchar con el botón derecho del ratón sobre cualquiera de archivos o directorios.  De entre todos los que se han desarrollado podrían destacarse las siguientes **acciones del Explorador de Archivos**:

-  Acceder al panel para Quitar un USB (se puede lanzar en cualquier momento, no es necesario estar sobre el dispositivo)
-  Abrir un directorio como Root, de forma que podemos "trabajar" con él con máximos privilegios (creación, borrado, permisos...) PRECAUCIÓN!!
- Trabajar con PDF's:
    - Unir PDFs
    -  Dividir PDFs (*extraer páginas de un PDF*)
    -  Comprimir PDFs
- Comprimir imágenes en formato JPG o PNG
- Generar imágenes en miniatura
- Convertir entre formatos de imágenes
- Comprimir archivos MP3
- Enviar archivos usando una cuenta de mail (debe ser de gmail)
- Utilidades generales de un archivo: Editar como texto, Copiar, hacer un backup en el propio directorio...
- ...se van añadiendo más...

## <img src="img/Logobombilla.png" width="80"> Tarea 5.1: Acciones del Explororador de Archivos {#Tarea5-1}

*Requisitos: Es necesario haber leído todo lo referente a las [Acciones del Explorador de Archivos](acciones_del_explorador_de_archivos.md) y disponer de un equipo con Vitalinux instalado que esté totalmente actualizado contra Migasfree (si la actualización se ha producido en la sesión actual, es posible que sea necesario cerrar sesión e iniciar sesión de nuevo)*

Mediante la siguiente tarea nos familiarizaremos con una de las características de los **Exploradores de Archivos** en Linux: el uso de **acciones** programadas.  **Vitalinux** hace uso de **pcmanfm** el cual se caracteriza por ser muy ligero, pero al mismo tiempo, muy potente.  Con la finalidad de apreciar la gran versatilidad y funcionalidad del explorador de archivos a continuación se propone comprobar las siguientes **acciones** (*en el vídeo que se adjunta, se explican y completan cada una de ellas en el mismo orden que se solicitan*):

1. Abre el **Explorador de Archivos *pcmanfm*** (*Tecla Windows + E*)
1. **Reproducir Vídeo en Miniatura**.  Almacena un **archivo de vídeo** en algún directorio de tú perfil en Vitalinux, y desde el **Explorador de Archivos pcmanfm** pincha con el botón derecho del ratón sobre él, y selecciona dentro de **"Utilidades Vídeos"** la opción **"Reproducir Vídeo en Miniatura"**.  Comprueba que el vídeo se reproduce en una de las esquinas de tu Entorno de Escritorio pudiendo trabajar simultáneamente con el equipo con otras aplicaciones.  Por ejemplo, abre **Libreoffice Writer** y redacta algo mientras se visualiza el vídeo en miniatura 
1.  *Comprimir MP3**.  Almacena **archivos MP3** en algún directorio de tú perfil en Vitalinux, y desde el **Explorador de Archivos pcmanfm** pincha con el botón derecho del ratón sobre varios de ellos simultáneamente, y selecciona dentro de **"Utilidades Música"** la opción **"Comprimir MP3"**.  Comprueba que se crea una subcarpeta con los archivos comprimidos (p.e. 64Kbps), y advierte que se ha reducido su tamaño, pero que al mismo tiempo se escuchan bien ![](img/aplicaciones-reproducir-video-en-miniatura.png)
1. **Comprimir PDFs**.  Almacena **archivos PDFs** en algún directorio de tú perfil en Vitalinux, y desde el **Explorador de Archivos pcmanfm** pincha con el botón derecho del ratón sobre varios de ellos simultáneamente, y selecciona dentro de **"Utilidades PDFs"** la opción **"Comprimir PDF"**.  Comprueba que se crean archivos resultantes junto a los seleccionados con el mismo nombre pero un sufijo **-comp** (*comprimido*).  Advierte si el tamaño se ha reducido considerablemente, conservando al mismo tiempo que sean legibles
1. **Unir PDFs**.  Almacena **archivos PDFs** en algún directorio de tú perfil en Vitalinux, y desde el **Explorador de Archivos pcmanfm** pincha con el botón derecho del ratón sobre varios de ellos simultáneamente, y selecciona dentro de **"Utilidades PDFs"** la opción **"Unir PDFs"**.  Comprueba que se crea un archivo resultante junto a los seleccionados con el nombre de **resultado-union-pdfs.pdf** (*estando seleccionado pulsa **F2** para renombrarlo*)
1. **Extraer Grupo de Páginas de un PDF**.  Almacena **archivos PDFs** en algún directorio de tú perfil en Vitalinux, y desde el **Explorador de Archivos pcmanfm** pincha con el botón derecho del ratón sobre alguno de ellos, y selecciona dentro de **"Utilidades PDFs"** la opción **"Extraer Grupo Páginas ..."**.  Comprueba que se crea un archivo resultante junto a al seleccionado con el mismo nombre pero un sufijo que indica las páginas extraídas
1. **Comprimir JPG/PNG**.  Almacena **Imágenes JPG o PNG** en algún directorio de tú perfil en Vitalinux, y desde el **Explorador de Archivos pcmanfm** pincha con el botón derecho del ratón sobre varios de ellos simultáneamente, y selecciona dentro de **"Utilidades Imágenes"** la opción **"Comprimir ..."**.  Comprueba que se crean archivos resultantes en un subdirectorio.  Advierte si el tamaño se ha reducido considerablemente, conservando al mismo tiempo su resolución
1. **Información Detallada de Imágenes**.  Almacena **Imágenes** en algún directorio de tú perfil en Vitalinux, y desde el **Explorador de Archivos pcmanfm** pincha con el botón derecho del ratón sobre varios de ellos simultáneamente, y selecciona dentro de **"Utilidades Imágenes"** la opción **"Detalles de la Imagen"**.  Advierte la información detallada de salida
1. **Cambiar formato de Imágenes**.  Almacena **Imágenes** en algún directorio de tú perfil en Vitalinux, y desde el **Explorador de Archivos pcmanfm** pincha con el botón derecho del ratón sobre varios de ellos simultáneamente, y selecciona dentro de **"Utilidades Imágenes"** la opción **"Conversor Formato Imágenes"** (*por ejemplo, cambia varias imágenes a formato BMP o PDF*).  Comprueba que se crean archivos resultantes junto a los seleccionados pero con el formato y extensión especificados
1. Por último, me gustaría que indicarás alguna funcionalidad que te gustaría que estuviera incluida dentro del Explorador de Archivos, y que actualmente no esta implementada.  ¡¡Esto nos puede servir a los que desarrollamos Vitalinux para mejorarlo!!

Como en ocasiones ***más vale un buen videotutorial que mil palabras*** a continuación se sugiere ver el siguiente vídeo relacionado con este asunto:

{% youtube %}https://youtu.be/idIYc5UG8z0{% endyoutube %}

> **Formato de Entrega**: Si no encuentras muchos problemas para ello, haz capturas de pantalla (tecla IMPRIMIR PANTALLA) de todo lo que vayas haciendo, y almacénalas en una memoria USB o donde creas conveniente. En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil. Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: **apellido1\_apellido2\_nombre\_TareaX.pdf**.
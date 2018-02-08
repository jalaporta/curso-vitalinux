## <img src="img/Logobombilla.png" width="80"> Tarea 5.2.1: Presentaciones Visuales tipo Prezi mediante Sozi

Requisitos: Es necesario haber leído todo lo referente a [Aplicaciones Multimedia](aplicaciones_multimedia.md) y disponer de un equipo físico con Vitalinux instalado para realizar la Tarea

A través de la presente tarea se propone al participante a realizar una presentación *al estilo Prezi*, pero mediante el uso de **Software Libre**: [Ejemplo de Tarea a Realizar](http://migasfree.educa.aragon.es/tarea-multimedia).  Esto nos servirá para familiarizarnos con algunas de las aplicaciones multimedia disponibles en Linux: **Inkscape** (*maneja imágenes vectoriales*) y **Sozi** (*permite crear una presentación a partir de una imagen vectorial*).  Es importante destacar, que por problemas de los **drivers gráficos de VirtualBox** esta tarea no se puede realizar en entorno Virtual, por lo que se requiere de un equipo físico con Vitalinux instalado (*si tienes algún problema para disponer de un equipo físico para poder hacer la tarea, por favor, indícarmelo*).  Aunque esta todo detallado en este [Videotutorial Explicativo](https://youtu.be/pUeT6Pm5iig), a continuación se resumen los pasos para realizar la tarea de manera rápida y exitosa:

1.    Asegurate de que sigues teniendo la etiqueta migasfree **"PER-AULARAGON"** que tuviste que asignar a tu equipo en la parte anterior del curso.  Esto hará que se instale en tu equipo de forma automática y desatendida todo el software necesario para hacer esta práctica
2.    Navega por Internet y descarga un **fondo e imágenes** para la presentación que vas a realizar 
3.    Navega por Internet y descarga una **tipografía que te guste** para la presentación a realizar
4.    Abre **Inkscape** (***CONTROL + ESPACIO** y escribes **inkscape***), y tal como se muestra en el videotutorial que se adjunta, ves importando el fondo y las imágenes a un nuevo documento de **Inkscape**, pero separados por capas (*fondo, imágenes, texto, ...*). Guarda el resultado en formato de imagen vectorial **SVG**
5.    Lanza **Sozi** (***CONTROL + ESPACIO** y escribes **sozi ...***) y abre el documento **SVG** anterior.  A continuación organiza los fotogramas o diapositivas de la presentación como bien prefieras, y guarda el resultado
6.    Si no te resulta muy complejo, edita con **leafpad** (*un bloc de notas*) el archivo **HTML** generado por **Sozi** y añade música de fondo.  Para ello, a continuación de la etiqueta **"&lt;body ...&gt;"** pega el siguiente código HTML indicando el nombre del archivo de música que quieres que suene en **"src"** substituyendo **"*nombre-canción.ogg*"** (*el archivo deberá encontrarse en la misma carpeta que el HTML*).  Si es necesario haz uso del **conversor de audio**  para convertir tu canción preferida a formato **OGG**:

    ```html
    <p style="background-color: LightSteelBlue; 
    width: 50%; text-align: center; margin-right: auto; 
    margin-left: auto; margin-top: 0px; margin-bottom: 0px;">
    <audio autoplay loop controls="controls">Your browser does not support the
    <code>audio</code> element. 
    <source src="nombre-canción.ogg" type="audio/ogg"> </audio>
    </p>
    ```

7.    Para terminar, pincha con el botón derecho del ratón sobre el documento HTML resultante e indica que deseas abrirlo con tu navegador Web preferido: Firefox o Chrome</ol><p>Como en ocasiones ***más vale un buen videotutorial que mil palabras*** a continuación se sugiere ver el siguiente vídeo relacionado con este asunto:

{% youtube %}https://youtu.be/pUeT6Pm5iig{% endyoutube %}
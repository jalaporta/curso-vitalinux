{% notificacion_task title='Presentaciones Visuales tipo Prezi mediante Sozi',
numexer='6.4.2',
req='Es necesario haber leído todo lo referente a <a href="../Parte_6-Aplicaciones_utiles_y_alternativas/Parte_6-Aplicaciones_multimedia.md">Aplicaciones Multimedia en Vitalinux</a>',
formatoentrega='En un documento ofimático escribe y pega las fotos o capturas de pantalla necesarias para justificar todo lo que se te pide a lo largo de la tarea. Si es posible expórtalo a <b>formato PDF</b> para garantizar su portabilidad, y adjúntalo como respuesta a la tarea solicitada. Por tanto, envía al tutor un único archivo <b>.pdf</b> que se nombrará siguiendo las siguientes pautas: <b>apellido1_apellido2_nombre_TareaX.pdf</b>.
<br>
Asegúrate que el nombre no contenga la letra ñ, tildes ni caracteres especiales extraños. Así por ejemplo la alumna <b>Begoña Sánchez Mañas</b>, debería nombrar esta tarea como: <b>sanchez_manas_begona_Tarea6.4.2.pdf</b>' %}

A través de la presente tarea se propone al participante a realizar una presentación <i>al estilo Prezi</i>, pero mediante el uso de <b>Software Libre</b>: <a href="http://migasfree.educa.aragon.es/tarea-multimedia">Ejemplo de Tarea a Realizar</a>.  Esto nos servirá para familiarizarnos con algunas de las aplicaciones multimedia disponibles en Linux: <b>Inkscape</b> (<i>maneja imágenes vectoriales</i>) y <b>Sozi</b> (<i>permite crear una presentación a partir de una imagen vectorial</i>).  Es importante destacar, que por problemas de los <b>drivers gráficos de VirtualBox</b> esta tarea no se puede realizar en entorno Virtual, por lo que se requiere de un equipo físico con Vitalinux instalado (<i>si tienes algún problema para disponer de un equipo físico para poder hacer la tarea, por favor, indícarmelo</i>).  Aunque esta todo detallado en este <a href="https://youtu.be/pUeT6Pm5iig">Videotutorial Explicativo</a>, a continuación se resumen los pasos para realizar la tarea de manera rápida y exitosa:

<ol>
<li>
Asegurate de que sigues teniendo la etiqueta migasfree <b>"PER-AULARAGON"</b> que tuviste que asignar a tu equipo en la parte anterior del curso.  Esto hará que se instale en tu equipo de forma automática y desatendida todo el software necesario para hacer esta práctica
</li>
<li>
Navega por Internet y descarga un <b>fondo e imágenes</b> para la presentación que vas a realizar 
</li>
<li>
Navega por Internet y descarga una <b>tipografía que te guste</b> para la presentación a realizar
</li>
<li>
Abre <b>Inkscape</b> (<i><b>CONTROL+ESPACIO</b> y escribes <b>inkscape</b></i>), y tal como se muestra en el videotutorial que se adjunta, ves importando el fondo y las imágenes a un nuevo documento de <b>Inkscape</b>, pero separados por capas (<i>fondo, imágenes, texto, ...</i>). Guarda el resultado en formato de imagen vectorial <b>SVG</b>
</li>
<li>
Lanza <b>Sozi</b> (<i><b>CONTROL+ESPACIO</b> y escribes <b>sozi ...</b></i>) y abre el documento <b>SVG</b> anterior.  A continuación organiza los fotogramas o diapositivas de la presentación como bien prefieras, y guarda el resultado
</li>
<li>
Si no te resulta muy complejo, edita con <b>leafpad</b> (<i>un bloc de notas</i>) el archivo <b>HTML</b> generado por <b>Sozi</b> y añade música de fondo.  Para ello, a continuación de la etiqueta <b>"&lt;body ...&gt;"</b> pega el siguiente código HTML indicando el nombre del archivo de música que quieres que suene en <b>"src"</b> substituyendo <b>"<i>nombre-canción.ogg</i>"</b> (<i>el archivo deberá encontrarse en la misma carpeta que el HTML</i>).  Si es necesario haz uso del <b>conversor de audio</b>  para convertir tu canción preferida a formato <b>OGG</b>:

<div style="border: 1; border-color: brown; background-color: gray; white-space: pre-wrap; color: white; font-weight: bold; font-size: 90%;">
<xmp>
    <p style="background-color: LightSteelBlue; 
    width: 50%; text-align: center; margin-right: auto; 
    margin-left: auto; margin-top: 0px; margin-bottom: 0px;">
        <audio autoplay loop controls="controls">
            Your browser does not support the
            <code>audio</code> element. 
            <source src="nombre-canción.ogg" type="audio/ogg">
        </audio>
    </p>
</xmp>
</div>
</li>
<li>
Para terminar, pincha con el botón derecho del ratón sobre el documento HTML resultante e indica que deseas abrirlo con tu navegador Web preferido: Firefox o Chrome
</li>

</ol>

Como en ocasiones <b><i>más vale un buen videotutorial que mil palabras</i></b> a continuación se sugiere ver el siguiente vídeo relacionado con este asunto:

<br><div style='text-align: center;'>
<iframe width='560' height='315' src='https://www.youtube.com/embed/pUeT6Pm5iig' frameborder='0' allow='autoplay; encrypted-media' allowfullscreen></iframe>
</div>

{% endnotificacion_task %}
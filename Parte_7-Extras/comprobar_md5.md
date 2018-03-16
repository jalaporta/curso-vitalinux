# Comprobar la Integridad de un fichero descargado

Para verificar que la descarga de un fichero ha sido correcta existen las "*firmas*", "*resúmenes*" o " *ficheros hash*". Si observas, al lado del fichero a descargar tienes otra descarga disponible: MD5SSUM. Prueba a bajar uno y abrirlo con el bloc de notas o cualquier editor de texto plano.

Observarás que es un fichero de texto que contiene simplemente una línea con el **resumen** del fichero y el nombre del fichero. El resumen de un archivo es una cadena de texto de tamaño fijo (32 caracteres) resultante de aplicar un algoritmo al fichero original, de forma que si el archivo original cambiara en lo más mínimo, el resultado de aplicar de nuevo el resumen sería completamente distinto. Así pues, si aplico el algoritmo (MD5 en éste caso) al fichero \*.iso que me he descargado y resulta la misma cadena que contiene en su adjunto ***.iso.md5**, puedo asegurar que la descarga se realizó con éxito.

¿Y cómo hago ésto? Dependerá del Sistema Operativo que uses para descargar y comprobar los ficheros de descargas:

* Si usamos cualquier **distribución GNU/Linux**, contaremos con un ejecutable llamado **md5sum**. Para comprobar el fichero, navega hasta el directorio donde has descargado la ISO y el fichero md5 y ejecutas (si se verifica el fichero saldrá un resultado de "**La suma coincide**"): 
```
md5sum -c fichero_md5_descargado.md5
```

* Si usamos **Windows**, podemos descargarnos el programa winmd5free. Lo ejecutamos y seguiremos unos sencillos pasos:
    1. Ejecuta el programa y busca el archivo ISO (o el que corresponda) a comprobar
    2. El programa comprobará el fichero y generará un resumen o hash resultante
    3. Abrimos el fichero resultante con el resumen MD5 para comprobar si coincide con el proporcionado por el suministrador de la descarga. Para ello, podemos hacer botón derecho sobre el fichero y abrir con Bloc de Notas:<br><br>![Ejecuta el programa](img/Md5_1.png)<br><br>
    4. Si la firma coincide podemos concluir que está todo correcto. Para ello podemos hacer uso del campo correspondiente en el programa:

![Comprueba el resúmen](img/Md5_1.png)
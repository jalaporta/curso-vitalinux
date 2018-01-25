# Configuración de red

__TOC__
La configuración de la red en un sistema operativo es una tarea crucial, si tenemos en cuenta que cada día mas necesitamos el uso de la red y estar conectados a Internet para desarrollar nuestro trabajo.

Linux permite gestionar el software de una forma muy cómoda a través de la red, como vamos a ir viendo en ésta parte. Es similar a un entorno Android (pero lleva así desde los inicios de los tiempor), donde simplemente busco el software que necesito y el propio sistema se encarga de descargarlo e instalarlo por nosotros. Además Vitalinux, como veremos más adelnate, hace uso de un cliente llamado **Migasfree** que se conecta al servidor del proyecto. Mediante ésta comunicación se realizan tareas de mantenimiento, actualizaciones e instalación y configuración de software de forma desatendida.

Veamos pues un poco más en detalle la configuración de red, por si nos encontramos con problemas de conectividad.
## Configuración 
Por defecto y si no hemos configurado nada aún, lo normal es que nuestro equipo Vitalinux se haya conectado a la red si es cableada o habremos seleccionado nuestra red wifi (introduciendo la contraseña)
### Gestor Network Manager 
En Vitalinux (como en muchos otros sistemas Linux) se emplea el NetworkManager para gestionar nuestra red. Para acceder al mismo podemos usar:
* **Lanzar** el programa usando CTRL+ESPACIO y ejecutando "Conexiones de red"
* Usando el **icono** que hay en la zona de notificaciones, en la barra inferior junto al reloj. Se recomienda éste método ya que según usemos el botón izquierdo del ratón o el derecho, tendremos unas funcionalidades u otras
** Con el **botón izquierdo** podremos conectarnos a una red concreta, desconectarnos de una red, crear una red inhalámbria si no está disponible o incluso configurar una VPN [[Archivo:Red izquierdo.png|center|500px|thumb|Boton izquierdo icono de red]]
** Con el **botón derecho** podremos activar o desactivar las interfaces de red de forma global, obtener información o **abrir el programa de "Conexiones de Red"** [[Archivo:Red derecho.png|center|500px|thumb|Boton derecho icono de red]]
Una vez tenemos abierto el programa de Conexiones de red podremos configurar de forma más avanzada la conexión. Por ejemplo, el direccionamiento
### Direccionamiento === 
Lo primero que tendremos que tener en cuenta es que para que un dispositivo esté en la red y se puede comunicar con otros, debe tener unos parámetros de red como la **dirección de red**. Además de la dirección debe saber cuál es la dirección por la que comunicarse con otros equipos en otras redes y quien va a ser el equipo que le traduce los nombres que usamos todos (como www.google.es) en una dirección IP que entienden los ordenadores. Así pues necesitaremos saber:
* Dirección de red. Por ejemplo: 172.30.1.120. Como dato adicional deberemos tener una máscara de red, por ejemplo la 255.255.255.0
* Puerta de enlace/router de casa/router del centro. Por ejemplo: 172.30.1.251
* Servidor de Nombres. Por ejemplo, para probar o usar podemos emplear el de google: 8.8.8.8

**¿Y debemos saber todo esto?**. Normalmente no, ya que si en la red que nos conectamos tenemos servidor DHCP, nos proporcionará estos datos de forma automática. Pero sino, deberemos meterlo nosotros a mano. ¿Donde?
:: Para ello abrimos Conexiones de red -&gt; seleccionamos la red a editar (cableada o inhalámbrica) -&gt; editar -&gt; pestaña de Ajustes de IPv4 -&gt; Métdod manual. Ahora podremos introducir los datos necesario
[[Archivo:Ip manual.png|center|thumb|Direccionamiento IP Manual]]
### Configuración Inhalámbrica 
En el caso de una red inhalámbrica además debermos proporcionar la clave de acceso a la wifi (ya que no estará abierto). Para ello cuando le demos a conectar a una red inhalámbrica (botón izquierdo sobre el icono de red -&gt; clickar sobre la red a conectar) nos pedirá una contraseña. Es posible que luego nos pida unas credenciales para guardar esa y otras contraseñas. Poner cualquier que luego no la usaremos. Podéis leer [[Vitalinux/FAQs_¿Cómo_evitar_el_anillo_o_depósito_de_Claves_al_registrar_una_red_Wireless%3F|más sobre el anillo de claves]]. 
Cuando hemos metido la clave, lo importante para que esté disponible para TODOS los demás usuarios sin tener que introducir cada vez la clave es Editar dicha conexión y en la pestaña General le indicamos que esté disponibe para todos los usuarios
[[File:evitar_anillo_de_claves-wireless-conexiones_de_red_4.png|center|thumb|Habilitamos la disponibildad de la red para todos los usuarios]]
_Nota: A los centros del programa que lo solicitan, se les **incorpora la configuración de red inhalámbrica** de forma que no es necesario que tengan que introducir dicha clave equipo por equipo cuando se instala un ordenador_

## Comprobación 
### Direccionamiento 
Evidentemente la mejor forma de comprobar que tenemos correctamente configurada la red en nuestro equipo es abrir un navegador e intentar conectarnos a cualquier servicio.
Sin embargo podemos obtener los datos de nuestra configuración de red (para usos futuros o para por ejemplo solicitar soporte). Para ello simplemente tenemos que ejecutar **CTRL+ESPACIO Conocer Dirección IP, MAC....** y nos dará la información de red
[[Archivo:Info-red.png|center|thumb|Pantalla de comprobacion de los parámetros de red]]
### Test de red 
También hay disponible un test de velocidad para obtener los datos del ancho de banda de subida y bajada de nuestra conexión de red.
Para ejectuar el test debemos lanzar el programa Test de Velocidad (CTRL+ESPACIO Test de Velocidad) y nos mostrará las estadísticas básicas
[[Archivo:Test-velocidad.png|center|thumb|Resultado del test de velocidad]]


### ¿Qué es VirtualBox? {#Que_es_virtualbox}

Tal cómo lo definen en su página oficial _"***VirtualBox*** es un poderoso software de virtualización tanto para la empresa,  como para el uso doméstico. Además se caracteriza por ser la única solución profesional que está libremente disponible como software de código abierto bajo los términos de la Licencia Pública General de GNU (GPL v2)_".


En definitiva, **VirtualBox** es un software muy interesante que nos va a permitir crear una máquina virtual, para posteriormente sobre ésta instalar y probar un sistema operativo (*p.e. Vitalinux*) y todas sus aplicaciones obteniendo como resultado exactamente lo mismo que si lo hubiéramos hecho directamente sobre el equipo físicamente.

{% notificacion_important title='¿Qué significa que la máquina es Virtual?' %}
<b>Virtualbox</b> nos va a permitir crear máquinas virtuales en un sentido metáforico, ya que cuando creamos una máquina en Virtualbox en realidad estamos cediendo parte de los recursos hardware de la máquina física a la máquina creada.  Es decir, a modo de ejemplo, si disponemos de un equipo físico con 4GB de memoria RAM y creamos una máquina en Virtualbox con 1GB de memoria RAM, ese GigaByte es real (<i>no es virtual</i>) ya que se los esta <b>quitando a la máquina física</b> dejándola únicamente con 3GB.  Entendido lo que sucede con la memoria RAM de la máquina virtual, exáctamente igual podríamos decir de la CPU, la tarjeta de sonido, las tarjetas de red, etc ...  Por tanto, Virtualbox es un software que tiene la capacidad de hacernos creer que tenemos varias máquinas en una.
{% endnotificacion_important %}
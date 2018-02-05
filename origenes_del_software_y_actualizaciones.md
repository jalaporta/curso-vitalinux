# Orígenes del Software y Actualizaciones

## Orígenes del Software (Repositorios) y Actualizaciones en Vitalinux

Una de las características más importantes del software libre es que **su distribución es Libre**.  Es decir, que podemos coger cualquier programa hecho bajo la licencia de **software libre**, y además de ser libres para poderlo modificar y mejorar, podemos posteriormente entregarlo a quien queramos y de la forma que queramos.  Gracias a esta **libertad** es posible aglutinar todo el software libre en determinadas ubicaciones de Internet y distribuirlo a quien lo desee de una manera centralizada.  Estas ubicaciones se denominan en el mundo linux **Repositorios**.


Para hacernos una idea del concepto, **android'* (*que también es un Linux**) tiene preconfigurados unos repositorios de Google de tal forma que cuando nosotros buscamos e instalamos una nueva aplicación a través de su **"Play Store"**, lo estamos haciendo entre el software recolectado por dichos repositorios.


En Linux, y como no, en Vitalinux es posible configurar la ubicación de estos repositorios (*URLs o direcciones de Internet públicas*) con la finalidad de aumentar la cantidad de software disponible y la fiabilidad del servidor que nos lo entrega.  Para configurar todo ello deberemos pulsar la combinación **"CONTROL + ESPACIO"'** y teclear **"Software y Actualizaciones ..."'**:


![Origenes del Software o Repositorios en Vitalinux](img/gestion-software-software-y-actualizaciones.png)

![Repositorios adicionales a los oficiales de Ubuntu](img/gestion-software-software-y-actualizaciones-otro-software.png)

![Actualizaciones del Software](img/gestion-software-software-y-actualizaciones-actualizaciones.png)

![Controladores Adicionales Privativos](img/gestion-software-software-y-actualizaciones-controladores-adicionales.png)

Como en ocasiones ***más vale un buen videotutorial que mil palabras*** a continuación se sugiere hacer una Tarea al respecto y visualizar un vídeo relacionado con este asunto (*es una parte del videotutorial completo: [Gestión del Software en Vitalinux](https://www.youtube.com/watch?v=8tBh8yz1FHY)*).

## <img src="img/Logobombilla.png" width="80"> Tarea 4.1: Modificar los Orígenes del Software de Vitalinux

**Requisitos**: *Es necesario haber leído todo lo referente a Orígenes del Software y Actualizaciones y disponer de un equipo con Vitalinux, físico o virtual, para realizar la Tarea.*

Todo el software que está disponible para ser instalado en Vitalinux se localiza en los **repositorios** que tenga configurados. Un **repositorio** es una ubicación en Internet (p.e. migasfree.educa.aragon.es) donde se almacena software que puede ser solicitado por un equipo Linux siguiendo un protocolo definido. En concreto, de todos los repositorios que tiene configurado Vitalinux el más importante, por su disponibilidad y por la cantidad de software que ofrece, son los repositorios oficiales de Ubuntu. Estos repositorios de Ubuntu se corresponden con servidores que se localizan en la mayor parte de los países mundiales y que a su vez son clones/replicas entre sí (en todos los servidores de Ubuntu se encuentra el mismo software disponible). Como primera tarea de esta parte se propone modificar el servidor del cual se obtiene el software de Ubuntu. Para ello:

* Accede a Software y Actualizaciones (CONTROL + ESPACIO y teclear software ...)
* Comprueba que en Vitalinux está configurado por defecto que las fuentes donde ir a buscar software se corresponden con un servidor propio mirror de los de Ubuntu (Pestaña Otro Software). Esto significa que gracias a que el software es libre, y por tanto libre su distribución, lo que hemos hecho es coger todo el software disponible para Ubuntu (más de 100 GB de software) y copiarlo en un servidor nuestro (en el mundo de la informática se dice que hemos creado un mirror de los repositorios oficiales de Ubuntu). De esta forma podemos controlar que software y que versiones de éste esta disponible para todos los Vitalinux. En concreto, esto nos permite congelar las versiones del software para evitar constantes actualizaciones del software y liberar dichas actualizaciones cuando nos interese

![Panel de Control para la Gestión de Impresoras](img/software-y-actualizaciones-mirror-vitalinux.png)

En el caso de que quisiéramos disponer de unos repositorios con software totalmente actualizado deberíamos configurar los repositorios deseados. Advierte que si configurar nuevos repositorios deberás introducir la contraseña de administración para poder realizar el cambio

![Podemos añadir un repositorio oficial para disponer de software actualizado e instalable a través de Synaptic](img/Software-y-actualizaciones-añadir-repositorio-oficial.png)

![Tenemos la opción de indicar a Ubuntu que nos seleccione el que considera mejor servidor de software](img/Software-y-actualizaciones-seleccionar-el-mejor-servidor.png)

![Deberemos confirmar y seleccionar el mejor servidor de software](img/Software-y-actualizaciones-mejor-servidor-seleccionado.png)

![Es necesario Recargar los repositorios para que surtan efecto los cambios. Tras ello podemos ir a Synaptic o a cualquier otro instalador de software e instalar el software que deseemos totalmente actualizado](img/Software-y-actualizaciones-recargar-repositorios.png)

Como en ocasiones **más vale un buen videotutorial que mil palabras** a continuación se sugiere ver el siguiente vídeo relacionado con este asunto (es una parte del videotutorial completo [Gestión del Software en Vitalinux](https://www.youtube.com/watch?v=8tBh8yz1FHY%7C)):

{% youtube %}https://youtu.be/K4NSR2o3l0k{% endyoutube %}

> **Formato de Entrega**: Si no encuentras muchos problemas para ello, haz capturas de pantalla (tecla IMPRIMIR PANTALLA) de todo lo que vayas haciendo, y almacénalas en una memoria USB o donde creas conveniente. En caso de encontrar problemas para ello puedes hacer fotos directamente desde el móvil. Elabora un documento ofimático (o usa cualquier otro formato que te resulte más comodo) donde puedas incluir las capturas solicitadas y **expórtalo como pdf** para adjuntarlo como respuesta a la tarea solicitada. El nombre del fichero deberá seguir la pauta: apellido1_apellido2_nombre_TareaX.pdf.
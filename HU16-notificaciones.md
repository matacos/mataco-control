# HU16: Como estudiante quiero poder recibir notificaciones
# ESTA HISTORIA DE USUARIO FUE ELIMINADA EN FAVOR DE LAS HU 24, 25, 26, 27

## Criterios de aceptación

1. Las notificaciones que podrá configurar un estudiante son las siguientes:
+ Notificar un día antes del examen
+ Notificar por cambio de uno de tus cursos
+ Notificar por cambio de uno de tus exámenes

2. Dado un estudiante que tiene habilitada la notificación "Notificar un día antes del examen", en el momento en el que falten 24hs para un examen en el cual se inscribió, recibirá una notificación de la aplicación con la siguiente información: Nombre de la app, "Aviso de Examen", Nombre de la Materia, Fecha del examen, Tiempo en el que inicia el examen.

3. Dado un estudiante que tiene habilitada la notificación "Notificar por cambio de uno de tus cursos", en el momento en el que se realice un cambio en los datos de un curso, el mismo recibirá una notificación con la siguiente información: Nombre de la app, "Curso Modificado", Nombre del Curso, Nombre de la Materia. Si se presiona la notificación, la misma redirigirá a la aplicación a la Oferta Académica de la Materia.

4. Dado un estudiante que tiene habilitada la notificación "Notificar por cambio de uno de tus cursos", en el momento en el que se elimine un curso, el mismo recibirá una notificación con la siguiente información: Nombre de la app, "Curso Cancelado", Nombre del Curso, Nombre de la Materia.
	
5. Dado un estudiante que tiene habilitada la notificación "Notificar por cambio de uno de tus exámenes", en el momento en el que se realice un cambio en los datos de un examen, el mismo recibirá una notificación con la siguiente información: Nombre de la app, "Examen Modificado", Fecha del Examen, Nombre de la Materia. Si se presiona la notificación, la misma redirigirá a la aplicación a la Oferta de Exámenes de la Materia.

6. Dado un estudiante que tiene habilitada la notificación "Notificar por cambio de uno de tus exámenes", en el momento en el que se elimine un examen, el mismo recibirá una notificación con la siguiente información: Nombre de la app, Examen Cancelado, "Fecha del Examen", Nombre de la Materia.

## Prototipo
![Pantallas de Configuración de Notificaciones](./prototipos/notificaciones.png)

![Menú lateral de navegación](./prototipos/side_bar.png)

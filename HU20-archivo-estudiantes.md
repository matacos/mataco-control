# HU20: Como administrador del sistema, quiero subir un archivo de estudiantes

## Importar estudiantes
El usuario ingresa un archivo CSV con los siguientes campos:
- Padrón
- Contraseña inicial (en el caso de que este usuario ya exista en el sistema, este campo puede dejarse en blanco)
- Nombre
- Apellido
- Prioridad
- Email
- Lista de carreras a las que está anotado, como enteros separados por guiones.

## Criterios de aceptación
- Si el usuario sube un archivo que no obedece el formato que le corresponde, el sistema informará la línea del archivo que genera tal error.
- Si el administrador sube un archivo que incluye una clave que ya existe (padrón), se actualizará el registro correspondiente de la base de datos.

## Criterios de acpetación pendientes de definición
- Cantidad de registros máxima soportada en un archivo

## Prototipos
![](./prototipos/administrador-v2/importar_estudiantes.png)
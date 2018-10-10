# HU19: Como administrador del sistema quiero importar datos de docentes
## Importar docentes
El usuario ingresa un archivo CSV con los siguientes campos:
- DNI
- Contraseña inicial (en el caso de que este usuario ya exista en el sistema, este campo puede dejarse en blanco)
- Nombre
- Apellido
- Email


## Criterios de aceptación
- Si el usuario sube un archivo que no obedece el formato que le corresponde, el sistema informará las líneas del archivo que generan tal error.
- Si el administrador sube un archivo que incluye una clave que ya existe (DNI), se actualizará el registro correspondiente de la base de datos.

## Criterios de acpetación pendientes de definición
- Cantidad de registros máxima soportada en un archivo

## Prototipos
![](./prototipos/administrador-v2/importar_docentes.png)
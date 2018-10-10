# HU22: Como administrador de departamento quiero importar datos de materias

## Importar materias:
El usuario administrador ingresa un archivo en formato CSV con los siguientes campos:
- Código de departamento
- Código de materia
- Nombre de la materia
- Carreras que pueden cursar la materia (códigos de carrera separados con guiones)
- Materias correlativas (códigos de materia <código de depto>.<código de materia> separadas con guiones)

## Criterios de aceptación
- Si el usuario sube un archivo que no obedece el formato que le corresponde, el sistema informará las líneas del archivo que generan tal error.
- Si el administrador sube un archivo que incluye una clave que ya existe (compuesta por código de departamento y código de materia), se actualizará el registro correspondiente de la base de datos.

## Criterios de acpetación pendientes de definición
- Cantidad de registros máxima soportada en un archivo

## Prototipos
![](./prototipos/administrador-v2/importar_cursos.png)
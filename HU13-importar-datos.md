# HU13: Como administrador quiero importar datos
# Esta historia de usuario fue eliminada y reemplazada por 19, 20, 21, 22


## Importar materias:
El usuario administrador ingresa un archivo en formato CSV con los siguientes campos:
- Código de departamento
- Código de materia
- Nombre de la materia
- Carreras que pueden cursar la materia (códigos de carrera separados con guiones)
- Materias correlativas (códigos de materia <código de depto>.<código de materia> separadas con guiones)

Archivo de eliminación: cada fila tiene los siguientes campos:
- Código de departamento
- Código de materia

## Importar cursos
El usuario administrador puede ingresa tres archivos CSV con los siguientes campos:

- Archivo de cursos:
    - Código de departamento de la materia que el curso representa
    - Código de materia que el curso representa
    - Nombre del curso
    - Cupo
- Archivo de eliminación de cursos:
    - Nombre del curso
- Archivo de docentes:
    - Nombre del curso **(referencia univocamente a un curso)**
    - DNI del docente
    - Cargo del docente en el curso
- Archivo de eliminación de docentes:
    - Nombre del curso
    - DNI del docente
- Archivo de horarios
    - Nombre del curso **(referencia univocamente a un curso)**
    - Nombre del aula
    - Sede del aula
    - Día de la semana (primeras 3 letras minúsculas del día correspondiente)
    - Hora de inicio (en formato HH:MM)
    - Hora de finalización (en formato HH:MM)
    - Tipo de clase (Práctica Obligatoria, Teórica Obligatoria, etc.)
- Archivo de eliminación de horarios:
    - Nombre del curso (se eliminan todos los horarios de ese curso)

## Importar estudiantes
El usuario ingresa un archivo CSV con los siguientes campos:
- Padrón
- Contraseña inicial (en el caso de que este usuario ya exista en el sistema, este campo puede dejarse en blanco)
- Nombre
- Apellido
- Prioridad
- Email
- Lista de carreras a las que está anotado, como enteros separados por guiones.

## Importar docentes
El usuario ingresa un archivo CSV con los siguientes campos:
- DNI
- Contraseña inicial (en el caso de que este usuario ya exista en el sistema, este campo puede dejarse en blanco)
- Nombre
- Apellido
- Email

## Importar administradores de departamento
El usuario ingresa un archivo CSV con los siguientes campos:
- DNI
- Contraseña inicial
- Nombre
- Apellido
- Email
- Departamento

El DNI puede ser el de un docente, de ser así, se actualizan los campos correspondientes y se le brinda tmbién el rango de administrador de departamento.

## Importar administradores del sistema
El usuario ingresa un archivo CSV con los siguientes campos:
- DNI
- Contraseña inicial
- Nombre
- Apellido
- Email

No se puede usar un DNI de docente ni de administrador de departamento.

## Criterios de aceptación
- Si el usuario sube un archivo que no obedece el formato que le corresponde, el sistema informará la línea del archivo que genera tal error.
- El usuario podrá subir cualquier archivo de los listados arriba
- Si el administrador sube un archivo que incluye una clave que ya existe (DNI para el archivo de docentes, padrón para el de estudiantes, código de materia para el de materias, DNI para el de administradores de departamento y para el de administradores del sistema), se actualizará el registro correspondiente de la base de datos.
- En el caso de que el administrador suba un archivo de cursos con el nombre de un curso que ya existe, tal curso se restablecerá, eliminándose los docentes y horarios del mismo.
- Los archivos de eliminación eliminan los registros correspondientes, con las mismas claves primarias que en el criterio de aceptación que se refiere a la actualización de registros.


## Historias de usuario menores:
 - 13.1: Que la subida de archivos sea por medio de un script python, que corra por línea de comandos.
 - 13.2: Que la tabla se pueda descargar
 - 13.3: Que el front-end permita subir archivos.
 - 13.4 Que el front-end permita visualizar cada tabla
 - 13.5: ABM de cursos, docentes, estudiantes y materias en el front end.
 - 13.6: se incluye la gestión de administradores de departamento y administradores del sistema

## Prototipos
![](./prototipos/administrador/importar_cursos.png)

![](./prototipos/administrador/importar_docentes.png)

![](./prototipos/administrador/importar_estudiantes.png)

![](./prototipos/administrador/importar_materias.png)

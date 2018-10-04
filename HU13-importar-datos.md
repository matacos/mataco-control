# HU13: Como administrador quiero importar datos

## Importar materias:
El usuario administrador ingresa un archivo en formato CSV con los siguientes campos:
- Código de departamento
- Código de materia
- Nombre de la materia
- Carreras que pueden cursar la materia (códigos de carrera separados con guiones)
- Materias necesarias (códigos de materia separadas con guiones)

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
    - DNI del profesor
    - Cargo del docentes en el curso
- Archivo de eliminación de docentes:
    - Nombre del curso
    - DNI del docente
- Archivo de horarios
    - Nombre del curso **(referencia univocamente a un curso)**
    - Nombre del aula
    - Sede del aula
    - Día de la semana (primeras 3 letras minúsculas del día correspondiente)
    - hora de inicio (en formato HH:MM)
    - hora de finalización (en formato HH:MM)
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

## Importar docentes
El usuario ingresa un archivo CSV con los siguientes campos:
- DNI
- Contraseña inicial (en el caso de que este usuario ya exista en el sistema, este campo puede dejarse en blanco)
- Nombre
- Apellido
- Email


## Criterios de aceptación
 - Si el usuario sube un archivo que no obedece el formato que le corresponde, el sistema informará la línea del archivo que genera tal error.
 - El usuario podrá subir cualquier archivo de los listados arriba
 - Si el administrador sube un archivo que incluye una clave que ya existe (DNI, padrón o código de materia, para el archivo de docentes, estudiantes y materias, respectivamente), se actualizará el registro correspondiente de la base de datos.
 - En el caso de que el administrador suba un archivo de cursos con el nombre de un curso que ya existe, tal curso se restablecerá, eliminándose los profesores y horarios del mismo.
 - Los archivos de eliminación eliminan los registros correspondientes

## Historias de usuario menores:
 - 13.1: Que la subida de archivos sea por medio de un script python, que corra por línea de comandos.
 - 13.2: Que la tabla se pueda descargar
 - 13.3: Que el front-end permita subir archivos.
 - 13.4 Que el front-end permita visualizar cada tabla
 - 13.5: ABM de cursos, dicentes, estudiantes y materias en el front end.

## Prototipos
![](./prototipos/administrador/importar_cursos.png)

![](./prototipos/administrador/importar_docentes.png)

![](./prototipos/administrador/importar_estudiantes.png)

![](./prototipos/administrador/importar_materias.png)
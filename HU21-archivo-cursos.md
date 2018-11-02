# HU21: Como administrador de departamento quiero importar datos de cursos

## Importar cursos
Tiene los siguientes campos:

- Código de departamento
- Código de materia
- Nombre de materia
- Carreras que pueden cursar la materia
- Materias correlativas
- Archivo de cursos con los siguientes campos:
- Código de departamento de la materia
- Código de materia
- Nombre del curso a ser mostrado a los estudiantes
- Cupo
- Campos de horarios, que se repiten 4 veces. En caso de usarse menos de 4, se dejan vacíos los sobrantes:
    - Aula
    - Sede
    - Día
    - Horario de inicio
    - Horario de finalización
    - Tipo de clase
- Campos de DNI de profesores (serán 6) (los que no se usan se dejan en blanco):
    - Jefe de cátedra
    - Jefe de Trabajos Prácticos
    - Auxiliar 1
    - Auxiliar 2
    - Auxiliar 3
    - Auxiliar 4

## Criterios de aceptación
- Si el usuario sube un archivo que no obedece el formato que le corresponde, el sistema informará las líneas del archivo que generan tal error.
- Si el administrador sube un archivo que incluye una clave que ya existe (Nombre de curso), se actualizará el registro correspondiente de la base de datos.

## Criterios de acpetación pendientes de definición
- Cantidad de registros máxima soportada en un archivo

## Prototipos
![](./prototipos/administrador-v2/importar_cursos.png)

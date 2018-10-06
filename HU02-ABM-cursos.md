# Propuestas de modificación del "HU2: ABM cursos" para la segunda iteración


## Propuesta 1: (HU2.1) Los cursos vacíos existen
Si no se le agregan profesores u horarios a un curso, en el cliente android se mostrarán tales campos como "a definir" en ese curso.

## Propuesta 2: (HU2.2) Los cursos vacíos existen pero los alumnos no los ven
Si no se le agregan profesores u horarios a un curso, estos cursos serán visibles por parte de los administradores de departamento, pero no por parte de los estudiantes a través de la app.

## Propuesta 3: (HU2.3) Los cursos vacíos no existen en la base de datos
La interfaz no envía datos de cursos vacíos al servidor. Así, si el curso no se envía a la base de datos, el usuario verá una advertencia indicándole que debe agregar docentes u horarios.

![Pantalla principal de departamento](./prototipos/depto/depto-ppal-modificado.png)

# HU2: Como administrador de departamento, quiero hacer ABM de cursos.

## Criterios de aceptación
 - El usuario sólo puede acceder a las pantallas de administración del departamento si es un administrador del departamento correspondiente.
 
 - No es posible que un usuario administre las materias de más de un departamento.
 
 - El usuario sólo puede ver las materias del departamento que le corresponde.
 
 - Si el usuario es también profesor, verá un link para ir a la vista de profesor
 
 - El usuario ve los cursos de cada materia por separado.
 
 - El usuario puede agregar cursos a cada materia
 
 - El usuario puede agregar o quitar horarios de clase de un curso. Cada período de clase de un curso está asociado a un aula.
 
 - El usuario puede agregar o quitar docentes de un curso.
 
## Criterios de aceptación respecto de los campos [nuevos 24/9]
 - **( \*1 )** En el campo **DNI** el usuario sólo puede escribir dígitos decimales, no puede escribir puntos. El campo "Cargo" permite los siguientes valores:
    - Jefe de Cátedra
    - Jefe de Trabajos Prácticos
    - Ayudante
    
 - **( \*2 )** En el campo **vacantes** el usuario sólo puede escribir dígitos decimales. Además, no se permite que este valor sea mayor a 300, lo cual se informará una vez presionado el botón "Aceptar".
 
 - **( \*3 )** El nombre del curso debe ser un texto de menos de 100 caracteres.
 
 - **( \*4 )** Las sedes válidas son:
    - Paseo Colón
    - Las Heras
    - Ciudad Universitaria
    
 - **( \*5 )** El aula es un campo alfanumérico de menos de 100 caracteres, ya que los códigos de algunas aulas incluyen letras.
 
 - **( \*6 )** Los días permitidos son:
    - Lunes
    - Martes
    - Miércoles
    - Jueves
    - Viernes
    - Sábado
    
 - **( \*7 )** y **( \*8 )**: Son horarios con el formato "HH:MM", con el horario de 00:00 a 23:59 (sin AM/PM), este campo es alfanumérico y no tiene ninguna restricción en los caracteres que puede incluir, aunque al momento de "aceptar" el diálogo, se verificará que el formato sea correcto. **[Deseable: control que permita introducir horarios más fácilmente]**. El horario de fin debe ser posterior al de finalización (ya que todas las clases empiezan y terminan en el mismo día), lo cual se verifica al momento de "aceptar" el diálogo.
 
 - **( \*9 )**: Este campo soporta las siguientes opciones:
    - Teórica Obligatoria, 
    - Práctica Obligatoria, 
    - Teórico Práctica Obligatoria, 
    - Teórica, Práctica, 
    - Teórico Práctica,
    - Desarrollo y Consulta

## Prototipos
### Pantalla principal de departamento
![Pantalla principal de departamento](./prototipos/depto/depto-ppal.png)

### Diálogos modales varios
1. Se ve al presionar "agregar docente".
2. Aparece al eliminar un curso
3. Aparece al eliminar un docente
4. El código de curso lo fija el sistema, sólo se elige la cantidad de vacantes, lo cual también puede modificarse.
5. Aparece al clickear "Agregar horario"
![Modales](./prototipos/depto/depto-modales.png)

# HU11: Como profesor quiero crear o cancelar un examen

## Criterios de aceptación
1. Dado un docente que ingresa al sistema, puede visualizar las fechas de final que creó y conocer el listado de estudiantes inscriptos a cada una de esas fechas.

2. Al ingresar a una fecha de final, el docente tendrá la información siguiente:
+ Fecha del final
+ Sede
+ Aula donde se tomará el examen
+ Hora de inicio
+ Hora de finalización
+ Nombre, apellido, padrón y condición (regular o libre) del alumno que se inscribió

3. El docente tendrá la posibilidad de agregar un final. Al agregarlo podrá ingresar información sobre el mismo: aula, fecha, sede, hora de inicio y de finalización; y confirmar o cancelar la creación del final.

4. El docente puede agregar, como máximo, 5 finales.

5. El docente tendrá la posibilidad de cancelar un final. Al hacerlo aparecerá un mensaje de confirmación de la operación, y en caso de aceptar se le enviará una notificación a los alumnos inscriptos.

6. Únicamente puede crear o cancelar exámenes un jefe de cátedra de un curso de la materia correspondiente.

7. Las sedes válidas son:
    - Paseo Colón
    - Las Heras
    - Ciudad Universitaria
    
8. El aula es un campo alfanumérico de menos de 100 caracteres, ya que los códigos de algunas aulas incluyen letras.

9. La fecha será en formato DD/MM/AAAA

10. Son horarios con el formato "HH:MM", con el horario de 00:00 a 23:59 (sin AM/PM), este campo es alfanumérico y no tiene ninguna restricción en los caracteres que puede incluir, aunque al momento de "aceptar" el diálogo, se verificará que el formato sea correcto. **[Deseable: control que permita introducir horarios más fácilmente]**. El horario de fin debe ser posterior al de finalización (ya que todas las clases empiezan y terminan en el mismo día), lo cual se verifica al momento de "aceptar" el diálogo.
## Prototipo
![](./prototipos/crear_eliminar_final.png)

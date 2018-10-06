# HU18: Como profesor quiero modificar un examen

## Criterios de aceptación

1. El docente podrá modificar la siguiente información del final:
+ Fecha del final
+ Sede
+ Aula donde se tomará el examen
+ Hora de inicio
+ Hora de finalización

2. Únicamente puede modificar exámenes un jefe de cátedra de un curso de la materia correspondiente.

3. Si un docente modifica la fecha y hora de un final, no podrá asignarle una fecha y hora que ya haya pasado, o que esté dentro de las 48 horas futuras.

4. Un docente no puede mover las fechas de final hacia atrás en el tiempo, sólo postponerlas.

5. Las sedes válidas son:
    - Paseo Colón
    - Las Heras
    - Ciudad Universitaria
    
6. El aula es un campo alfanumérico de menos de 100 caracteres, ya que los códigos de algunas aulas incluyen letras.

7. La fecha será en formato DD/MM/AAAA

8. Son horarios con el formato "HH:MM", con el horario de 00:00 a 23:59 (sin AM/PM), este campo es alfanumérico y no tiene ninguna restricción en los caracteres que puede incluir, aunque al momento de "aceptar" el diálogo, se verificará que el formato sea correcto. **[Deseable: control que permita introducir horarios más fácilmente]**. El horario de fin debe ser posterior al de finalización (ya que todas las clases empiezan y terminan en el mismo día), lo cual se verifica al momento de "aceptar" el diálogo.


## Prototipo
![](./prototipos/modificar_final.png)
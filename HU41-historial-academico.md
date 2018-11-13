# HU41: Como estudiante quiero poder ver mi historial académico

## Criterios de aceptación
1. Dado un estudiante que ingresó a la aplicación, cuando se dirige al “Historial Académico” se mostrará un listado con todos los exámenes que rindió desde que se encuentra en la facultad.
2. Se debe mostrar el título "Historial Académico".
3. Cada examen debe tener la siguiente información: 
+ Código de la materia
+ Nombre de la materia
+ Fecha en la se rindió el examen o el la que se desaprobó la materia
+ Resultado del examen ( entre 4 y 10 si aprobó, "2 (insuf)" si desaprobó)
4. Las condiciones para que figure un insuficiente en la pantalla de historial académico son:
+ *Desaprueba 3 veces:* El alumno reúne 3 desaprobaciones de finales de la materia como regular en los períodos de final de los siguientes cuatrimestres:
    + El mismo cuatrimestre en que aprobó una cursada de la misma materia
    + El cuatrimestre inmediato posterior al mismo
    + El cuatrimestre inmediato posterior a ese
+ *Como libre:* El alumno desaprobó un examen como libre
+ *Desaprueba 1 o 2 veces y se vence:* El alumno reúne 1 o 2 desaprobaciones de finales de la materia, y ninguna aprobación de algún final de la materia como regular en los períodos de final de los siguientes cuatrimestres:
    + El mismo cuatrimestre en que aprobó una cursada de la misma materia
    + El cuatrimestre inmediato posterior al mismo
    + El cuatrimestre inmediato posterior a ese


> Si al final de este lapso el estudiante se ha presentado
> al menos una vez a rendir la evaluación integradora sin
> aprobarla o si ya ha rendido y desaprobado tres veces
> aunque todavía no se haya agotado el lapso, recibe la
> calificación de Insuficiente que se asienta en los Libros
> de Actas de Examen y debe recursar la asignatura.
> Si no se presenta ninguna vez, se considera que “se le
> venció” la cursada, y debe recursar, pero no recibe la
> calificación de Insuficiente
Extraído de http://www.fi.uba.ar/sites/default/files/preguntasFrec_digital_0.pdf

## Prototipo

![Exámenes en los que me inscribí](./prototipos/historial_academico.png)

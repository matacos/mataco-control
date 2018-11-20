# HU48: Como administrador quiero visualizar un reporte de encuestas

## Criterios de aceptación
- El administrador tendrá la posibilidad de visualizar el reporte de encuestas ingresando a la opción "Reporte de encuestas" dentro de "Reportes" en el panel. 
- Al ingresar en "Reporte de encuestas" tendrá la posibilidad de seleccionar un departamento junto con un período lectivo.
- Una vez seleccionado el departamento y el período lectivo, el administrador visualizará un gráfico con todos los cursos del departamento junto con la valoración de la opinión general de ese curso en ese período lectivo, ordenados de mayor a menor. 
- Debajo del gráfico podrá observar los comentarios de los estudiantes con respecto a cada curso. Los cursos aparecerán en el mismo orden que en el gráfico. 
- Si el administrador selecciona otro departamento o período lectivo, se mostrará la información correspondiente a esos datos.
- El sistema no permitirá mostrar reportes si falta algún dato. En caso de no seleccionar un departamento se mostrará el mensaje "Debe seleccionar un departamento" y, en caso de no seleccionar un período lectivo, "Debe seleccionar un período lectivo". Si faltan ambos datos, "Por favor, seleccione el departamento y período lectivo sobre los que quiere visualizar los reportes".
- El administrador de departamento, al ingresar en "Reporte de encuestas" podrá visualizar la misma información pero únicamente para ese departamento en particular.
- El gráfico que muestra el promedio de nota recibido por materia debe seguir la siguiente configuración de colores:
	- Verde: notas mayores o iguales a 7
	- Amarillo: notas mayores o iguales a 5 y menores a 7
	- Rojo: notas menores a 5

## Prototipos
![](./prototipos/administrador-v2/reporte_encuestas.png)
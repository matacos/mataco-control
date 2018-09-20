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
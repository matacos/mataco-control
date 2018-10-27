# HU33: Como docente quiero cargar notas de cursada de los alumnos
## Criterios de aceptación
1. El profesor podrá ver las notas de cursada de los alumnos inscriptos a un curso.
2. Cuando el profesor sube un archivo csv de notas, figurará su contenido en el sistema.
3. El csv de notas debe tener 2 columnas, una de padrones, otra de notas. Los padrones deben ser cadenas de menos de 10 caracteres, las notas deben ser enteros de 1 a 10, o bien el caracter "-". Cuando se sube un archivo que no cumple esta definición, se mostrará un diálogo que informa "archivo erróneo, problema en línea N".
4. Si se sube un archivo de notas que incluye padrones que no se encuentran inscriptos al curso, los mismos serán ignorados.
## Prototipo
![Listado de alumnos inscriptos curso](./prototipos/listado_inscriptos_subir_archivo.png)
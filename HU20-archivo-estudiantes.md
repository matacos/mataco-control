# HU20: Como administrador del sistema, quiero subir un archivo de estudiantes

## Importar estudiantes
El usuario ingresa un archivo CSV con los siguientes campos:
- Padrón
- Contraseña inicial (en el caso de que este usuario ya exista en el sistema, este campo puede dejarse en blanco)
- Nombre
- Apellido
- Prioridad
- Email
- Lista de carreras a las que está anotado, como enteros separados por guiones.

## Criterios de aceptación
- Si el usuario sube un archivo que no obedece el formato que le corresponde, el sistema informará la línea del archivo que genera tal error.
- Si el administrador sube un archivo que incluye una clave que ya existe (padrón), se actualizará el registro correspondiente de la base de datos.

## Criterios de aceptación adicionales (22/10)
- Dado que el registro de un estudiante se encuentra en el archivo csv subido, que este estudiante no está en el sistema y que la entrada correspondiente del archivo figura vacía, este estudiante no será dado de alta al sistema.
- El número máximo de líneas que puede tener un archivo csv subido es de 10.000. Se soporta la subida de archivos mayores, sin embargo no se garantiza el éxito de la transacción.
- Cuando una o más lineas tienen un error de los enumerados abajo, se mostrará un mensaje con todas las líneas con error del archivo, reportando el número de línea y el error correspondiente. Los errores que se detectan son:
    - Cada línea debería tener 7 campos
    - El padrón no puede estar vacío
    - El padrón debe tener 5 o 6 caracteres
    - El padrón tiene únicamente caracteres numéricos
    - La contraseña debe tener menos de 30 caracteres
    - El nombre no puede estar vacío
    - El apellido no puede estar vacío
    - La prioridad no puede estar vacía
    - El campo 'prioridad' tiene únicamente caracteres numéricos, debe ser un entero.
    - El campo 'prioridad' debe ser un entero entre 1 y 300
    - El email no puede estar vacío
    - El email debe tener menos de 100 caracteres
    - El email suministrado no parece ser un email
    - El dominio del mail suministrado no parece serlo
    - La lista de carreras no puede estar vacía
    - XX no es un número. La lista de carreras debe ser una lista de números enteros separados por guiones, sin espacios.
    - XX No es un identificador de carrera
- El máximo número de estudiantes que puede almacenar la base de datos es 15.000

## Prototipos
![](./prototipos/administrador-v2/importar_estudiantes.png)
#HU1: Como usuario, quiero entrar al sistema

## Criterios de aceptación
1. Cuando una persona no entró al sistema, no verá otra pantalla que no sea la de login.
- Los alumnos entrarán al sistema con su padrón, que es un entero de 5 o 2. dígitos.
2. Los docentes se identificarán en el sistema utilizando su DNI, que es un número entero de 8 dígitos o menos.
4. Al usuario se le permitirá escribir un caracter no numérico en este campo, pero al realizar la acción correspondiente para enviar el formulario, se le advertirá (android) "Debés ingresar tu padrón, que sólo tiene caracteres numéricos" (web) "Debés ingresar tu DNI, sin puntos ni espacios, que sólo tiene caracteres numéricos". Al usuario no se le permitirá acceder.
5. (android) Si el usuario envía un número de más de 6 dígitos o menos de 5, se le informará "El padrón ingresado debe tiene una cantidad de dígitos incorrecta", y no se le permitirá acceder.
6. (web) Si el usuario envía un número de más de 8 dígitos, se le informa "El número ingresado en 'DNI' debe tener 8 dígitos o menos", y no se le permitirá acceder.
7. (android) Si el estudiante ingresa un padrón válido que no se encuentra en la base de datos, se le mostrará el mensaje "Esa combinación de padrón y contraseña no es correcta", y no se le permitirá acceder.
8. (web) Si el usuario ingresa un DNI válido que no se encuentra en la base de datos, se mostrará el mensaje "Esa combinación de DNI y contraseña no es correcta", y no se le permitirá acceder.
9. (web) Si el usuario ingresa un padrón y este se encuentra en la base de datos, el sistema mostrará el mensaje "Esa combinación de DNI y contraseña no es correcta", y no se le permitirá acceder.
10. (android y web) Si el usuario no ingresa un valor en el campo "contraseña", se mostrará el mensaje "Recuerde ingresar la contraseña", y no se le permitiá acceder.
11. (android y web) Si el usuario ingresa un DNI correcto (web) o un padrón correcto (android), entonces se accederá a la siguiente pantalla, que es el "mis inscripciones"(android) o es la pantalla principal del profesor o del administrador de departamento (web).

## Criterios de aceptación para siguientes sprints
12. (android y web) Si el usuario ingresa una combinación inválida de DNI y contraseña (web) o de padrón y contraseña (android), entonces se mostrará el mensaje "Esa combinación de DNI y contraseña no es correcta", y no se le permitirá acceder.
13. (android y web) Si el usuario ingresa una combinación válida de DNI y contraseña (web) o de padrón y contraseña (android), entonces se accederá a la siguiente pantalla, que es el "mis inscripciones"(android) o es la pantalla principal del profesor o del administrador de departamento (web).

## Prototipos
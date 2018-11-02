# HU1-A: Como estudiante, quiero entrar al sistema

## Criterios de aceptación para siguientes sprints

1. Cuando una persona no entró al sistema, no verá otra pantalla que no sea la de login.

2. Los estudiantes entrarán al sistema con su padrón, que es un entero de 5 o 6 dígitos.

3. Al usuario se le permitirá escribir un caracter no numérico en este campo, pero al realizar la acción correspondiente para enviar el formulario, se le advertirá "Debés ingresar tu padrón, que sólo tiene caracteres numéricos" **[En android se mostrará un teclado que no permite introducir caracteres]**. Al usuario no se le permitirá acceder.

4. Si el usuario envía un número de más de 6 dígitos o menos de 5, se le informará "El padrón ingresado tiene una cantidad de dígitos incorrecta", y no se le permitirá acceder.

5. Si el estudiante ingresa un padrón válido que no se encuentra en la base de datos, se le mostrará el mensaje "Esa combinación de padrón y contraseña no es correcta", y no se le permitirá acceder.

6. Si el usuario no ingresa un valor en el campo "contraseña", se mostrará el mensaje "Recuerde ingresar contraseña", y no se le permitiá acceder.

7. Si el usuario no ingresa un valor en el campo "padrón", se mostrará el mensaje "Recuerde ingresar padrón", y no se le permitiá acceder.

8. Los mensajes referidos a los errores sintácticos o falta de datos ingresados serán marcados dentro de los campos en donde se produjo la falta luego de haber tocado "enviar" para enviar el formulario.

9. Los mensajes referidos a usuarios bien formulados pero con errores referidos a la inexistencia del mismo o a una contraseña no correspondiente al mismo se muestran como mensajes toast, luego de haber tocado "enviar" para enviar el formulario.

10. Si el usuario ingresa una combinación inválida de padrón y contraseña, entonces se mostrará el mensaje "Esa combinación de DNI y contraseña no es correcta", y no se le permitirá acceder.

11. Si el usuario ingresa una combinación válida de padrón y contraseña, entonces se accederá a la siguiente pantalla, que es el "Oferta Académica".

## Criterios de aceptación respecto de los campos [nuevo 24/9]

 - Al ingresar datos en el campo "padrón", se mostrará un teclado únicamente numérico
 
 - En el campo "contraseña" se mostrará un teclado alfanumérico, permitiendo introducir cualquier caracter.
 

## Prototipo

### App android:
![ingreso en app](./prototipos/ingreso_app.png)

# HU1-B: Como docente/administrador, quiero entrar al sistema

## Criterios de aceptación para siguientes sprints

1. Cuando una persona no entró al sistema, no verá otra pantalla que no sea la de login.

2. Los docentes se identificarán en el sistema utilizando su DNI, que es un número entero de 8 dígitos o menos.

3. Al usuario se le permitirá escribir un caracter no numérico en este campo, pero al realizar la acción correspondiente para enviar el formulario, se le advertirá "Debés ingresar tu DNI, sin puntos ni espacios, que sólo tiene caracteres numéricos". Al usuario no se le permitirá acceder.

4. Si el usuario envía un número de más de 8 dígitos, se le informa "El número ingresado en 'DNI' debe tener 8 dígitos o menos", y no se le permitirá acceder.

5. Si el usuario ingresa un DNI válido que no se encuentra en la base de datos, se mostrará el mensaje "Esa combinación de DNI y contraseña no es correcta", y no se le permitirá acceder.

6. Si el usuario ingresa un padrón y este no se encuentra en la base de datos, el sistema mostrará el mensaje "Esa combinación de DNI y contraseña no es correcta", y no se le permitirá acceder.

7. Si el usuario no ingresa un valor en el campo "contraseña", se mostrará el mensaje "Recuerde ingresar contraseña", y no se le permitiá acceder.

8. Los mensajes detallados en los criterios de aceptación anteriores se muestran como texto rojo en la pantalla de ingreso, luego de enviar el formulario.

9. Si un docente es también administrador de departamento, al ingresar entrará a la pantalla de docente, y tendrá un link que lo conducirá a la pantalla de administración de departamento.

10. Si el usuario ingresa una combinación inválida de DNI y contraseña, entonces se mostrará el mensaje "Esa combinación de DNI y contraseña no es correcta", y no se le permitirá acceder.

11. Si el usuario ingresa una combinación válida de DNI y contraseña, entonces se accederá a la siguiente pantalla, que es la pantalla principal del docente o del administrador de departamento.

## Criterios de aceptación respecto de los campos [nuevo 24/9]

 - El campo "DNI" permite introducir cualquier caracter, pero se muestran los mensajes correspondientes, descriptos en el título "Criterios de aceptación"
 
 - El campo "contraseña" permite escribir cualquier caracter.

## Prototipo

### Interfaz web:
![ingreso web](./prototipos/ingreso_web.png)

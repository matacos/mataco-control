# HU39: Como administrador quiero modificar un período lectivo

## Criterios de aceptación
1. Se podrán modificar todos los campos excepto el código del período
2. Si el período ya terminó, es imposible modificar alguna fecha del mismo.
3. Si el período todavía no empezó, es imposible modificar alguna fecha del mismo para que sea anterior a la fecha actual.
4. Si el período está en curso, las fechas anteriores a la fecha actual deben mantenerse luego de la actualización, y las fechas posteriores a la actual pueden ser modificadas únicamente por fechas futuras.
5. Se debe preservar el orden de las fechas según lo establecido en la HU37.

## Prototipos
![](./prototipos/administrador-v2/modificar_periodo.png)

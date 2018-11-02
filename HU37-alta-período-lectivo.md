# HU37: Como administrador, quiero dar de alta un período lectivo

## Criterios de aceptación
1. Un período lectivo está conformado por los siguientes campos:
    1. Fecha de **publicación de la oferta académica**.
    2. Fecha de inicio del **período de inscripción a cursos**.
    3. Fecha de fin del **período de inscripción a cursos**.
    4. Fecha de inicio del **período de cursada**.
    5. Fecha de fin del **período de desinscripción a cursos**.
    6. Fecha de **publicación de la oferta de finales**.
    7. Fecha de fin del **período de cursada**.
    8. Fecha de fin del **período de finales**.
    9. Código del período lectivo
2. Los campos 1 a 8, que son fechas, deben ser consecutivos en el tiempo en el orden que se presentaron, es decir, el 2 debe ser posterior al 1, el 3 debe ser posterior al 2, el 4 debe ser posterior al 3, etc.
3. Los estudiantes sólo podrán consultar los cursos disponibles entre la fecha de publicación de la oferta académica y la fecha de fin de cursada.
4. Los estudiantes sólo podrán inscribirse a cursos durante el período de inscripción a cursos.
5. Los estudiantes sólo podrán desinscribirse a cursos desde la fecha de inicio del período de inscripción a cursos y hasta la fecha de fin del período de desinscripción a cursos.
6. Los estudiantes sólo podrán inscribirse o desinscribirse a finales entre la fecha de publicación de la oferta de finales y el fin del período de finales.
7. Los docentes sólo podrán crear finales que tengan lugar entre la fecha de fin de cursada y la fecha de fin del período de finales.
8. El código del período lectivo tiene como máximo 10 caracteres.

![Períodos](./HU37-esquema.png)



## Prototipos
![](./prototipos/administrador-v2/crear_periodo.png)

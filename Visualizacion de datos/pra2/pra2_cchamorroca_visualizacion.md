# Práctica 2: Visualización de datos

## Estudio del sistema ferroviario de media y larga en la península ibérica

Los datos se han obtenido de la dirección url: https://data.renfe.com/dataset/horarios-de-alta-velocidad-larga-distancia-y-media-distancia .
Se ha de tener en cuenta que, a pesar de ser datos oficiales ofrecidos por la propia Renfe, estos no muestran datos fiables, por lo que el uso de este set de datos se da con fines puramente académicos

Renfe mantiene un total de 599 líneas.

### Servicios de Renfe 

Estudiamos la distribución de los servicios,a tenor de la cantidad de rutas que ofrece cada uno.

![My Image](output_9_0.png)

Vemos que la mayor parte de las rutas pertenecen a sericios de ámbito nacional como MD (media distancia) o Alvia, frente a servicios autonómicos como rodalies.

### 2. Accesibilidad 

Nos preguntamos por el estado de la accesibilidad para sillas de ruedas en el sistema ferroviario. En el siguiente gráfico observamos la distribución por servicio.

![My Image](output_14_1.png)

Parece que rodalies no ofrece en absoluto servicio para personas con movilidad reducida. Esto puede deberse a una mala ibtención de los datos por renfe, por lo que no debemos tomarlo como un dato real.

Observamos en el mapa la localización de las paradas con accesibilidad.

![My Image](accesibilidad.png)

Vemos que, a pesar de que muchos de los servicios ofrecen accesibilidad, la mayor parte de las paradas aún carecen de este tipo de ayuda al consumidor. También podemos observar que muchas de las paradas con acceso a sillas de ruedas se encuentran en centros poblacionales como capitales de provincia. Esto, a pesar de tener lógica, hace que el servicio público no sea una buena solución para personas con discapacidad en entornos rurales.

Vemos que la infraestructura de alta velocidad es más simple que el conjunto de la infraestructura total

### Distribución de los servicios en el mapa

![My Image](distribucion_servicios.png)

Para comprender mejor la complejidad de los servicios ferroviarios, estudiaremos por separado los servicios de alta velocidad de los demás.

![My Image](output_31_0.png)

Vemos que, en efecto, los servicios de alta velocidad representan menos de una quinta parte de los servicios otorgados por Renfe.

### Alta velocidad

![My Image](alta_velocidad.png)

Observamos a continucación los movimientos de los trenes a través del tiempo durante la semana de navidad

![My Image](alta_velocidad.gif)

### Otros servicios

Los servicios de media y larga distnacia que no usan infrestructura de alta velocidad suponen más del 80% del total.

![My Image](media_distancia.png)

Aquí podemos ver, además, como se distribuyen dichos servicios en la península.

![My Image](otros_servicios.gif)

En este clip podemos apreciar la complejidad del sistema durante la semana de navidad del 2022.

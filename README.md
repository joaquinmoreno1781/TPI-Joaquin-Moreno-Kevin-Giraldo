Gestión de Datos de Países en Python

Descripción

Este proyecto fue desarrollado para la materia Programación 1 de la Tecnicatura Universitaria en Programación.

La aplicación permite gestionar información de países almacenada en un archivo CSV, realizando operaciones de búsqueda, filtrado, ordenamiento y generación de estadísticas.

Los datos de cada país incluyen:

* Nombre
* Población
* Superficie (km²)
* Continente

La información se almacena en el archivo `Paises.csv` y se manipula mediante un menú interactivo en consola.

Integrantes

Joaquin Moreno
Kevin Giraldo


Estructura del Proyecto

```
Proyecto
│
├── main.py
├── funciones.py
├── Paises.csv
├── README.md
└── Informe.pdf
```

---

Requisitos

* Python 3.x

No se requieren librerías externas.

Ejecución

1. Descargar o clonar el repositorio.
2. Verificar que los archivos `main.py`, `funciones.py` y `Paises.csv` se encuentren en la misma carpeta.
3. Ejecutar:

```bash
python main.py
```

4. Seleccionar una opción del menú.

Funcionalidades

1. Agregar país

Permite registrar un nuevo país indicando:

* Nombre
* Población
* Superficie
* Continente

Validaciones implementadas:

* No se permiten campos vacíos.
* No se permiten poblaciones o superficies menores o iguales a cero.
* No se permite agregar países repetidos.
* Se agrega los contientenes mediante menu 

2. Actualizar datos

Permite modificar:

* Población
* Superficie

de un país existente.


3. Buscar país

Realiza búsquedas por nombre.

Acepta coincidencias parciales o exactas.


4. Filtrar países

Permite filtrar por:

* Continente
* Rango de población
* Rango de superficie


5. Ordenar países

Permite ordenar por:

* Nombre
* Población
* Superficie

En forma:

* Ascendente
* Descendente


6. Estadísticas

Muestra:

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

Ejemplos de Uso

Agregar País

Entrada:

```
Nombre del país: Canadá
Población: 40100000
Superficie: 9984670
Continente: América
```

Salida:

```
País agregado correctamente
```

Buscar País

Entrada:

```
Ingrese el nombre del país a buscar:
Argentina
```

Salida:

```
Nombre: Argentina
Población: 45376763
Superficie: 2780400 km²
Continente: América
```

Estadísticas

Salida:

```
---- Estadísticas ----

País con mayor población: China
País con menor población: Uruguay

Promedio de población: 54234567.45

Promedio de superficie: 1356789.22 km²

Cantidad de países por continente:

América: 8
Europa: 6
Asia: 7
África: 5
Oceanía: 2
```
Manejo de Errores

El sistema controla:

* Campos vacíos.
* Ingreso de letras donde se esperan números.
* Rangos inválidos.
* Países inexistentes.
* Países duplicados.
* Opciones inválidas en los menús.

Tecnologías Utilizadas

* Python 3
* CSV
* Listas
* Diccionarios
* Funciones
* Estructuras condicionales
* Estructuras repetitivas
  
Enlace del video
https://youtu.be/LfhPk2hqSb4
  
Enlace git
https://github.com/joaquinmoreno1781/TPI-Joaquin-Moreno-Kevin-Giraldo

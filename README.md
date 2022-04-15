![blockbuster.jpg](images/blockbuster.jpg)


# Proyecto base de datos SQL
## Introducción:

En el siguiente proyecto se me ha encargado realizar una base de datos de un videoclub partiendo de algunos archivos csv, al que tendré que añadir alguno más. Para ello utilizaré la librería de pandas para explorar, limpiar y modificar los datos y convertirlos en dataframes.

Una vez conocidos los datos diseñaré la estructura de la base de datos con sus respectivas realaciones. La crearé, introduciré los datos y para terminar relacionaré cada una de las tablas.

Por último realizaré una serie de consultas para ver que la base de datos esta perfectamente bien contruida y aprovecharé para hacer alguno análisis de los datos

## Fuentes de los datos:

 - Ironhack
 - https://extendsclass.com/csv-generator.html

## Objetivos:

- Importar, explorar y limpiar los datos.
- Diseñar, crear y alimentar la base de datos.
- Realizar consultas para analizar los datos.

## Entregables:

- `explore_clean_data.ipynb` 
- `create_db_insert_data.ipynb`
- `selects.ipynb`
- `blockbuster_diagram.sql`



## Exploración y limpieza:

Comienzo importando todos los csv a un jupyter notebook y los guardo como dataframes de pandas para revisar de que datos se tratan. 

Continuo limpiando los datos, eliminado columnas con datos nulos y cambiando el tipo de datos.

Creo algún dataset mas que necesitaré mas tarde, para todo ello utilizo pandas y numpy.


## Diseño y creación de la base de datos:


Primero me diseño la estructura de la base de datos en un papel y cuando tengo claro cuales son las primary y foreign keys de cada tabla me dispongo a generarla en mySQL

Para ello utilizo otra vez jupyter nootebook y me ayudo de mysql-conector y sqlalchemy para realizarlo de forma automatizada. Primero creo la base de dato, luego las tablas, le inserto los datos y termino alterando las tablas con las relaciones.


## Consulta y análisis:

Por último realizo una serie de queries en jupyter notebook con el motor de sqlalchemy para comprobar que todo está en orden y aprovecho para analizar algunos datos unicamente con join, where, group by, order by...
        

## Enlaces y Recursos:

- <https://www.kaggle.com/teajay/global-shark-attacks>
- <https://numpy.org/doc/1.18/>
- <https://pandas.pydata.org/>
- https://docs.python.org/3/library/functions.html
- https://plotly.com/python/
- https://matplotlib.org/
- https://seaborn.pydata.org/
- https://pandas.pydata.org/docs/
- https://www.sqlalchemy.org/library.html
- https://dev.mysql.com/doc/connector-python/en/



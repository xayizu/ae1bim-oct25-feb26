

 ORM con SQLAlchemy

Este proyecto corresponde a la actividad “Use los conceptos de ORM a través de la librería SqlAlchemy en lenguaje Python – AE1” de la Unidad 3: Acceso a base de datos relacionales mediante ORM.

La idea es modelar un pequeño sistema de investigación con instituciones, departamentos, investigadores y publicaciones, usando SQLite + Python + SQLAlchemy.




1. Tecnologías usadas

Lenguaje: Python

Base de datos: SQLite

ORM: SQLAlchemy





2. Estructura de archivos principales

configuracion.py
Contiene la configuración de la base de datos (conexión a SQLite, creación del engine y de la sesión, y la clase Base para los modelos).
👉 Cumple con el criterio “Archivo de conexión a la base de datos”.

crear_base_entidades.py
Define las entidades y crea las tablas:

Institucion (id, nombre, ciudad, pais)

Departamento (id, nombre, codigo, institucion_id)

Investigador (id, nombre, apellido, email, area_investigacion, departamento_id)

Publicacion (id, titulo, fecha_publicacion, doi, tipo_publicacion, investigador_id)


poblar_base.py
Inserta datos de ejemplo en todas las tablas (instituciones, departamentos, investigadores y publicaciones).
👉 Cumple con el criterio “Archivo de ingreso de información a la base de datos”.

Archivos de consulta de información:

consulta_all.py → usa query(...).all() para listar todas las filas de cada tabla.

consulta_filter.py → usa filter(...) para filtrar por país, área de investigación y tipo de publicación.

consulta_order_by.py → usa order_by(...) para ordenar investigadores por apellido y publicaciones por fecha.

consulta_or.py → usa or_(...) para combinar condiciones (por ejemplo, investigadores de IA o Desarrollo Web).

consulta_and.py → usa and_(...) para combinar condiciones (por ejemplo, artículos del año 2024).


👉 Estos archivos cumplen con el criterio “Archivo de consulta de información a la base de datos” usando all, filter, order_by, or y and.





3. Cómo se ejecuta el proyecto (pensado para PC)

> Nota: yo desarrollé el código pensando en un entorno local con Python instalado.
Actualmente solo tengo acceso desde el celular, así que no pude ejecutar los scripts, pero el flujo esperado sería el siguiente:



1. Instalar dependencias (si fuera necesario):



pip install sqlalchemy

2. Crear las tablas en la base de datos:



python crear_base_entidades.py

3. Poblar la base con datos de ejemplo:



python poblar_base.py

4. Ejecutar las consultas:



python consulta_all.py
python consulta_filter.py
python consulta_order_by.py
python consulta_or.py
python consulta_and.py

Cada script imprime en consola los resultados de las consultas correspondientes.




4. Comentario sobre calidad y uso de ORM

El uso de SQLAlchemy como ORM ayuda a mejorar la calidad de la aplicación web porque:

Hace el código más mantenible (las tablas se manejan como clases Python).

Facilita la portabilidad de la base de datos (cambiar de SQLite a otra BD es más simple).

Aumenta la seguridad, reduciendo el riesgo de ataques de SQL injection.

Evita repetir código SQL y permite enfocarse más en la lógica de negocio.
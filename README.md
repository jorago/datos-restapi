# datos-restapi
RestAPI para la carga masiva de datos, desarrollado en Python - micro framework flask

Si desea ver la aplicación corriendo en un servidor de prueba ingresa a: http://jorago.pythonanywhere.com/

Esta app utiliza los siguientes paquetes:
- Flask_mysqldb https://flask-mysqldb.readthedocs.io/en/latest/
- Openpyxl https://openpyxl.readthedocs.io/en/stable/
- Flask_bootstrap https://pythonhosted.org/Flask-Bootstrap/

Se utilizó Mysql como manejador de base de datos:
    - Nombre de la base de datos: bd_cargadatos  
    - Ejecutar script para crear la base de datos: 
        CREATE DATABASE `bd_cargadatos` /*!40100 DEFAULT CHARACTER SET utf8mb4 */

    - Ejecutar el siguiente script para crear la tabla datos 
        CREATE TABLE `datos` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nombre` varchar(100) NOT NULL,
        `apellido` varchar(100) NOT NULL,
        `nacionalidad` varchar(100) NOT NULL,
        `fechaContrato` date NOT NULL,
        `sexo` varchar(20) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
      

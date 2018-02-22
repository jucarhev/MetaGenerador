# Generador de datos
Generador de datos para mysql, permite crear 100 registros aleatorios para llenar tus tablas, pero a diferencia de otros este es extensible de una manera que puede ser modificado y mejorado. Antes de empezar debes configurar la conexion a tu base de datos en el menu preferences.

<a href="" target="_blank"><img src="https://github.com/pacpac1992/MetaGenerador/blob/master/main.png"/></a>
## Menu
<ul>
    <li>File: Guarda los archivos si existen, crea un nuevo documento, abre archivos si existen, exporta a los formatos ya mencionados, cierra la aplicacion</li>
    <li>Preferences: Abre el menu de preferencias donde encontrara campos para excluir bases de datos o columnas de tablas</li>
    <li>Help: Muestra el archivo de acerca de</li>
</ul>
## Toolbar
<ul>
    <li>Icono 1: Crear nuevo documento(lista de datos)</li>
    <li>Icono 2: Preferencias</li>
    <li>Icono 3: Conexion a la base de datos</li>
    <li>Icono 4: Ayuda</li>
    <li>Icono 5: Cerrar</li>
</ul>
### Nuevo documento
Permite crear archivos que seran utilizadas para rellenar las columnas seleccionadas

### Preferencias
En esta ventana podemos poner las bases de datos que no queremos que se muestren, estas pueden ser del sistema, tambien las columnas que no queremos que aparescan, como el id que es auto incrementable.

### Databases
En este archivo solo definimos los datos escenciales para la conexion a la base de datos.

## Interface
Si elegimos una base de datos y luego elegimos una tabla que corresponda a ella y presionamos el boton con icono de tabla, aparecera una ventana con la informacion de esa tabla de la base de datos, en esta se muestran los metadatos de cada columna.

Si ademas elegimos la columna de la tabla y un archivo del combo list podemos obtener los datos que se generaran y un ejemplo.
Es importante señalar que la caja de texto opciones permitira hacer algunas modificaciones a como saldra el datos.

### Opciones
Por defecto ya vienen unas listas predeterminadas con opciones
<ul>
<li><strong>Email:</strong> Por defecto no tiene opciones</li>
<li><strong>Password: </strong>Tiene la opcion de longitud y la de codificacion ejemplo pones <em>10,md5</em> o <i>8,sha1</i> o simplemente <i>8<i></li>
<li><strong>Telephone:</strong> si pones home en la casilla aparecera un numero distinto al que sale si no pones nada, solo para tipos de datos varchar</li>
<li><strong>Direction: </strong>No tiene opciones</li>
<li><strong>Random: </strong>por defecto [0:100] un numero aleatorio entre esos dos valores, puede persolnalizar los rangos por ejemplo <i>4000,9000</i></li>
<li><strong>Feature: </strong> por defecto [item1,item2] elegira uno de esos, pero puede poner una cadena y se elegira de manera aleatoria una de ellas, por ejemplo <i>piedra,papel,tijera</i></li>
<li><strong>Date: </strong>por defecto sale una fecha con este formato dia-mes-año, si colocas r  en las opciones, retornara la diferencia entre la fecha actual y la fecha dada.</li>
</ul>

<h2>Requirements</h2>
<ul>
	<li>wxpython: python-wxgtk3.0</li>
	<li>pymysql: PyMySQL</li>
	<li>python: >= 2.6 or >= 3.3 </li>
	<li>PyPy >= 4.0</li>
</ul>

<h2>License</h2>
MetaGenerator is released under the MIT License. See LICENSE for more information.

<small>Juankarlos.0304@gmail.com</small>

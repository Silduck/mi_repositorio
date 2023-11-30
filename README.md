PROYECTO FINAL-SILVANA ROJAS
Proyecto de desarrollo de app web "Calzados Los Patos".Sito web dinámico destinado a ventas de calzados.

Proyecto Final Silvana Rojas, curso de programacion back-end en centro de formacion laboral n°406 (cfln°406).
Desarrollé una aplicación web estilo blog programada en Python en Django. Esta web será dinámica e interactiva tendrá admin, perfiles, registro, páginas y formularios.

Este proyecto no utiliza Python puro sino Python con Django para desarrollo web. Y la magia de HTML5 Y CSS3 combinada de herencia de plantillas de Bootstrap nos facilitan el diseño FrontEnd de este proyecto.

Requisitos previos📋
Debes tener instalado para correr este proyecto:

Visual Studio Code u otro editor de texto, Python 3.10 o superior, Django, navegador y DB SQLITE.

Instalacion🔧
Se instala en primera instancia VS Code se descarga de https://code.visualstudio.com/download se elige el sistema operativo que usa Windows, Mac o Linux se descarga y se siguen los pasos que nos indica hasta instalar VS CODE.

Luego se instala Python 3.10 se descarga de https://www.python.org/ en la primera pantalla seleccionando la caja de ruta será de utilidad para este proyecto y luego seguir con la instalación del mismo.

Descargue aquí DB SQLITE https://www.sqlite.org/index.html y siga los pasos.

construido con🛠️
VS CODE, PYTHON 3.10 DB NAVEGADOR SQLITE Django, HTML 5, CSS Y BOOTSTRAPP.

<strong>Comandos usados ​​en la consola de VS CODE para hacer funcionar el proyecto</strong>
python -m venv entorno (creamos el entorno virtual)

.\entorno\Scripts\activate (activación del entorno virtual)

django-admin startproject MiProyecto (crea el proyecto)

cd .\MiProyecto\ (nos posicionamos en la carpeta del proyecto)

python manage.py startapp app (crea la aplicación)

python manage.py makemigrations (hace los cambios en la base de datos y los modelos)

python manage.py migrate (Guarda los cambios de los modelos)

python manage.py RunServer (corre el servidor web en localhost).


Gestionando mi aplicación
python admin.py aplicación de inicio app

Creamos nuestros modelos dentro de models.py

En nuestro views.py, definimos la vista para mostrar nuestro modelo, importamos nuestros modelos!!

Creamos nuestra plantilla .html con las líneas de código necesarias para mostrar la información de nuestros modelos.

Creamos nuestro archivo urls.py (dentro de la app), creamos la url para la vista deseada, importamos nuestra vista!!

En nuestro archivo settings.py (configuramos nuestro proyecto) incluimos la aplicación creada en INSTALLED_APPS, agregamos la dirección de la carpeta de nuestros templates en la sección DIRS, de templates. ¡Listo!

Autor✒️
SILVANA ROJAS 


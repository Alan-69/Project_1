
# Descripción de la App:
Con esta aplicación web desarrollada con Django, el usuario va a poder gestionar cursos, listas de profesores, estudiantes, y las entregas realizadas.

# Sus funciones son:

Realizar busqueda de cursos disponibles (en caso de que no se encuentre poder agregarlo) registrar nuevos profesores y estudiantes, estos últimos con dirección Email.

# Esta App fue realizada con:

La última versión de Python disponible al momento (3.12.4) y Django en su versión (4.2)

# Instalación de la App:

Primero creamos nuestro entorno virtual. En caso de no tener instalado pipenv, instalar desde el terminal con el comando pip install pipenv --python 3.12.4  (aclaramos la versión de Python que requiere nuestra App)

Luego instalamos los requisitos ubicados en el archivo requirements con el comando:

pipenv install -r requirements.txt

Realiza la migración de datos con el comando:

python manage.py migrate

Creamos un superusuario para tener acceso a Django como administrador con el siguiente comando:

python manage.py createsuperuser (completa los campos solicitados por el terminal)

Levantamos el servidor con el comando:

python manage.py runserver (hacemos ctlr+click sobre la dirección web en el terminal para abrirlo en nuestro navegador)

# Eso es todo! ya tendriamos acceso a nuestra App.

Recorda que teniendo acceso como administrador en Django podrás ver más información sobre profesores estudiantes y entregas que se encuentran en la base de datos.

# Tercera_pre-entrega_Martin

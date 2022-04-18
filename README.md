# flask_socketio_ejemplos
En este repositorio se encuentran 5 ejemplos de uso de la librería Socket.IO con el framework Flask y el paquete Flask-SocketIO. Es necesario establecer la variable de entorno FLASK_APP=application.py para correr los ejemplos desde la terminal mediante "flask run". Todos los paquetes utilizados se detallan en el archivo requirements.txt y puedes instalarlos mediante el siguiente comando en la terminal "pip install -r requirements.txt"

Para ejecutar estos 5 ejemplos deberas moverte en la terminal a la carpeta del ejemplo que desees ejecutar y escribir en la terminal "python application.py" o "flask run".

El ejemplo de conexión muestra la estructura inicial del proyecto de flask y las importaciones desde HTML.
El ejemplo de emitir muestra la carga de archivos de javascript mediante url_for y la lógica para enviar eventos con la función emit desde javascript.
El ejemplo de recibir muestra como manejar o recepcionar eventos desde el servidor y devolver una respuesta al cliente que generó dicho evento.
El ejemplo de emitir desde servidor muestra como emitir una respuesta desde la recepción de un evento a todos los usuarios conectados.
El ejemplo de rooms te muestra como ingresar un usuario a una sala y enviar eventos a salas específicas.

No se detalla la función leave_room porque funciona de manera similar a la función join_room explicada en el ejemplo rooms.

Esta serie de ejemplos estan orientados de manera de introducción a estudiantes para una clase de socket.io con flask, sin enfocarse en manejo de bases de datos, simplemente manejo de la librería, emisión y recepción de eventos y salas.
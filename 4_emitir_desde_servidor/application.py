from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reemplazar_clave_secreta'

# Instancia de SocketIo
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

# Al recibir el evento saludar
@socketio.on('saludar')
def saludar(nombre):
    print(f'Hola {nombre}')

    #Emitir solo al usuario que origino este evento
    emit("mensaje", f'Hola {nombre}')

    #Enviar respuesta de evento emit del cliente
    return f'Hola {nombre}'

# Al recibir el evento saludar a todos
@socketio.on('saludar a todos')
def saludar_a_todos():
    # Emitir a todos los usuarios con el argumento broadcast=True
    emit('mensaje', 'Hola a todos!', broadcast=True)

# Opcional
if __name__ == '__main__':
    socketio.run(app)
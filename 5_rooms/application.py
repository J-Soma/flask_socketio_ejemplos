from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reemplazar_clave_secreta'

# Instancia de SocketIo
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("entrar")
def entrar(sala):
    # Ingresamos al usuario a la sala
    join_room(sala)

    # Emitimos un aviso a los usuarios conectados a la sala, exceptuando a la persona que se unio
    emit('mensaje', f'Un usuario ha entrado a la sala {sala}', broadcast=True, include_self=False, to=sala)

    # Mandamos una respuesta al evento emit del cliente
    return f'Te has unido a la sala {sala}'

# Opcional
if __name__ == '__main__':
    socketio.run(app)
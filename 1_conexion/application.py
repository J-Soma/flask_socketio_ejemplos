from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reemplazar_clave_secreta'

# Instancia de SocketIo
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

# Opcional
if __name__ == '__main__':
    socketio.run(app)
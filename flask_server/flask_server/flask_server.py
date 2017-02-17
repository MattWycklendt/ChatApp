from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return send_from_directory('../../client', 'index.html')

@socketio.on('chat message')
def handle_message(message):
    print('[new_message] ' + message)
    emit('chat message', message, broadcast=True)

@socketio.on('connection')
def handle_connection(message):
    print('Connected!')

if __name__ == '__main__':
    socketio.run(app)

from gevent import monkey
monkey.patch_all()

from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='gevent_uwsgi')

@app.route('/')
def hello_world():
    return send_from_directory('../../client', 'index.html')

@socketio.on('chat message')
def handle_message(message):
    print('[new_messageb] ' + message)
    socketio.send('chat message', "msg1: " + message)
    emit('chat message', "msg2: " + message, broadcast=True)
    print ('emitted')

@socketio.on('connect')
def handle_connect():
    print('Connected!')

@socketio.on('disconnect')
def handle_disconnect():
    print('Disconnected!')

if __name__ == '__main__':
    socketio.run(app)

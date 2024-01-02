import socketio
import random
import eventlet

sio=socketio.Server(cors_allowed_origins='*')
app=socketio.WSGIApp(sio)

@sio.event

def connect(sid,environ):
    print(f"client {sid} connected")

@sio.event
def disconnect(sid):
    print(f"client {sid} disconnected")

@sio.event
def random_numbers(sid):
    random_value=random.randint(1,100)
    sio.emit('random_value', random_value, room=sid)


if __name__=='__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
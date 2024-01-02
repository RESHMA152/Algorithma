import socketio

sio=socketio.Client()

   
@sio.event
def random_no(data):
    print(f"random value :{data}")
  
if __name__=='__main__':
    
    sio.connect('http://localhost:5000', transports=['websocket'])
    while True:
        input("random number:")
        sio.emit('random_numbers')
        sio.disconnect()
    
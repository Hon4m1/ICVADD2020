import socket
import time

ADDRESS = 'localhost'
PORT = 8889
MESSAGE = 'Pong'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
print('Server connected to port address '+ ADDRESS +' and port',PORT)
print('Client launched')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

init = True
server.listen(1)
conn, addr = server.accept()

while True:
    data = conn.recv(1024).decode()
    if data :
        print(data)
        time.sleep(2)
        if init:
            client.connect((ADDRESS, 8888))
            init = False
        client.send(MESSAGE.encode())
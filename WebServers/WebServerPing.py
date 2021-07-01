import socket
import time

ADDRESS = 'localhost'
PORT = 8888
MESSAGE = 'Ping'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
print('Server connected to port address '+ ADDRESS +' and port',PORT)
print('Client launched')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ADDRESS, 8889))
client.send(MESSAGE.encode())
print('1rst message sended \n')
server.listen(1)
conn, addr = server.accept()

while True:
    data = conn.recv(1024).decode()
    if data:
        print(data)
        time.sleep(2)
        client.send(MESSAGE.encode())

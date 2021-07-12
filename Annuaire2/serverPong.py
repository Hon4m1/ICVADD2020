import socket, time, clientsUtils

ADDRESS = 'localhost'
PORT = 8889
MESSAGE = 'Pong'

#Setting up server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
print('Server connected to port address ' + ADDRESS + ' and port', PORT)
#Connect client to Annuary
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = clientsUtils.connectAnnuary(client, server, ADDRESS, PORT)

#Listen for incoming connection
print('Listening for incoming')
server.listen(1)
conn, addr = server.accept()

#Connection to the other server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
notConnected = True
while notConnected:
    try:
        client.connect((ADDRESS, int(data)))
        notConnected = False
    except Exception as e:
        print("Address-related error connecting to server: %s" % e)

init = True
while True:
    client.send(MESSAGE.encode())
    try :
        data = conn.recv(1024).decode()
    except Exception as e:
        print('Error : %s' % e)
    if data:
        print(data)
        time.sleep(2)

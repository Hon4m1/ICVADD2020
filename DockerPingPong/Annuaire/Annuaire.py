import socket
import time

ADDRESS = 'localhost'
LOCALPORT = 8090
MESSAGE = 'Ping'
SERVER1 = 8888
SERVER2 = 8889


def connectToClient(client, server, data):
    notConnected = True
    while notConnected:
        try:
            client.connect((ADDRESS, int(data)))
            notConnected = False
            server.listen(1)
        except socket.gaierror as e:
            print("Address-related error connecting to server: %s" % e)


def returnAddressToClient(client, data):
    while True:
        time.sleep(2)
        if int(data) == SERVER1:
            print('server 2')
            client.send(SERVER2.__str__().encode())
            break
        if int(data) == SERVER2:
            print('server 1')
            client.send(SERVER1.__str__().encode())
            break

def Run():
    global conn
    # Receiving information when getting hit
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    print(data + ' has reached the server')

    # Setting up client to return information to askers
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectToClient(client, server, data)

    # Send port number to the first client
    returnAddressToClient(client, data)
    conn.close()

# Setting up the server to receive requests
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, LOCALPORT))
print('Annuary connected to port address ' + ADDRESS + ' and port', LOCALPORT)
server.listen(2)

while 1:
    Run()
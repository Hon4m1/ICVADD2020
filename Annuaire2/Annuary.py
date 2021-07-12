import socket
import time

ADDRESS = 'localhost'
LOCALPORT = 8090


def connectToClient(client, receiver):
    notConnected = True
    while notConnected:
        try:
            client.connect((ADDRESS, int(receiver)))
            notConnected = False
        except socket.gaierror as e:
            print("Address-related error connecting to server: %s" % e)


def returnAddressToClient(client, data):
    while True:
        time.sleep(2)
        if int(data) == server1:
            print('server 2')
            client.send(server2.__str__().encode())
            break
        if int(data) == server2:
            print('server 1')
            client.send(server1.__str__().encode())
            break


def Run():
    global conn
    global server1, server2
    # Receiving information when getting hit
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    print(data + ' has reached the server')
    server1 = data
    notOk = True
    while notOk:
        data = conn.recv(1024).decode()
        if data != server1:
            server2 = data
            break

    # Setting up client to return information to askers
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectToClient(client, server1)

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

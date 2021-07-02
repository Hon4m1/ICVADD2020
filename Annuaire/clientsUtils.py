import  time

def connectAnnuary(client,server,ADDRESS,PORT):
    global e
    annuary = True
    while annuary:
        try:
            client.connect((ADDRESS, 8090))
            annuary = False
        except Exception as e:
            print("Unable to connect to server: %s" % e)
            time.sleep(10)
    client.send(PORT.__str__().encode())
    print('Port to annuary discovering \n')
    server.listen(1)
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    print('Port to target = ', data)
    Ping = data
    print('Closing connection to annuary')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    print('Connection closed.')
    conn.close()
    return data
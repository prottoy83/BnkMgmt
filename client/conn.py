import socket 

def connectS(data):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8369))

    client.send(data)
    print(client.recv(1024).decode())
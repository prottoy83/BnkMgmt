import socket 

def connectS(method, data):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8369))

    print(method + " " + data[0] + data[1])
    client.send(data[0].encode())
    print(client.recv(1024).decode())
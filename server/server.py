import socket


PORT = 8369

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('127.0.0.1', PORT))

server.listen()

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    client.send('Server SENT YOU THIS'.encode())
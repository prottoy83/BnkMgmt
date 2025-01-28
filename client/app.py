import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8369))

client.send('Requesting to connect'.encode())
print(client.recv(1024).decode())
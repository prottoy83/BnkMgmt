import socket
import json

PORT = 8369

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('127.0.0.1', PORT))

server.listen()

while True:
    client, addr = server.accept()

    authData = client.recv(1024).decode()
    json_ad = json.loads(authData)
    print(json_ad["method"])
    
    if(json_ad["method"] == 'login'):
        response = "Logged in with cred\nUsername:"+json_ad["username"]+"\nPassword:"+json_ad["password"]
        client.send(response.encode())
    
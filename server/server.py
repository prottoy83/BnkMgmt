import socket
import json

PORT = 8369
HOST = '127.0.0.1'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Server listening on {HOST}:{PORT}")

while True:
    try:
        client, addr = server.accept()
        print(f"Connection established with {addr}")
        

        auth_data = client.recv(1024).decode()
        try:
            json_data = json.loads(auth_data)
        except json.JSONDecodeError:
            client.send("Invalid JSON format".encode())
            client.close()
            continue
        
        method = json_data.get("method")
        if method == "login":
            username = json_data.get("username", "Unknown")
            password = json_data.get("password", "Unknown")
            response = {
                "status": "success",
                "message": "Logged in successfully",
                "username": username,
                "password": password  
            }
        elif method == "signup":
            response = {"status": "error", "message": "Signup not implemented yet"}
        else:
            response = {"status": "error", "message": "Invalid method"}
        
        client.send(json.dumps(response).encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

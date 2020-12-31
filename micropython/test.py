import socket
import time
import json
HOST = '192.168.137.223'  # The server's hostname or IP address
PORT = 80        # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = {
        "username":"adminsmarthome",
        "passwork":"adminsmarthome"
        }
    data = str(json.dumps(data)).encode()
    print(data)
    s.sendall(data)
    data = s.recv(1024)
    print('Received', repr(data))
     
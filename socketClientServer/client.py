import socket

host = "127.0.0.1"
port = 2121

with socket.socket() as socket1:
    
    socket1.connect((host, port))
    socket1.sendall(b"Hi Cyber :)")
    data = socket1.recv(1024)

print(data)
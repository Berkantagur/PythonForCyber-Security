import socket

host = "127.0.0.1"
port = 2121

with socket.socket() as socket1:
    
    socket1.bind((host, port))
    socket1.listen()
    conn, addr = socket1.accept()

    with conn:
        print("The Connection is successful...")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    
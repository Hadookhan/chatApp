import socket

def start_server():
    s = socket.socket()
    s.bind(("localhost", 9999)) # binds socket to localhost on port 9999
    s.listen(1) # listens every second
    conn, addr = s.accept() # when connection found, return conn and addr
    print('connected:', addr)
    conn.send(b"Hello from server")

start_server()

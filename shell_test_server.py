import socket

IP = '192.168.1.2'
PORT = 5333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))
s.listen()
conn, addr = s.accept()
with conn:
    print(f"Connected by {addr}")
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)


import socket
import threading

busy = False
lock = threading.Lock()

def handle_client(conn):
    global busy

    while True:
        msg = conn.recv(1024).decode()

        if not msg:
            break

        if msg == "REQUEST":
            with lock:
                if not busy:
                    busy = True
                    conn.send("GRANTED".encode())
                else:
                    conn.send("WAIT".encode())

        elif msg == "RELEASE":
            with lock:
                busy = False
            conn.send("RELEASED".encode())

    conn.close()

server = socket.socket()
server.bind(("localhost", 5001))
server.listen()

print("Coordinator running...")

while True:
    conn, addr = server.accept()
    threading.Thread(
        target=handle_client, args=(conn,)
    ).start()

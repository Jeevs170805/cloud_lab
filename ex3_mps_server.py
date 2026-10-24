
import socket
import threading

clients = []

def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            print("Received:", msg)

            for client in clients:
                if client != conn:
                    client.send(msg.encode())

        except:
            break

    clients.remove(conn)
    conn.close()

server = socket.socket()
server.bind(("localhost", 5000))
server.listen()

print("Server waiting for clients...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print("Client connected:", addr)

    threading.Thread(target=handle_client, args=(conn,)).start()

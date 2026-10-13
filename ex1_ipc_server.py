
import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Server is waiting for client...")

conn, addr = server.accept()
print("Client connected")

data = conn.recv(1024).decode()
print("Received:", data)

numbers = data.split(",")
total = sum(int(n) for n in numbers)

conn.send(str(total).encode())
print("Sum sent:", total)

conn.close()
server.close()

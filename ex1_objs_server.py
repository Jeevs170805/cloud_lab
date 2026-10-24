
import socket
import pickle

server = socket.socket()
server.bind(("localhost", 5001))
server.listen(1)

print("Server is waiting for client...")

conn, addr = server.accept()
print("Client connected")

data = conn.recv(4096)
obj = pickle.loads(data)

print("Name:", obj["name"])
print("Values:", obj["values"])

total = sum(obj["values"])

response = "Hello " + obj["name"] + ", Sum = " + str(total)
conn.send(pickle.dumps(response))

print("Response sent")

conn.close()
server.close()


import socket
import pickle

client = socket.socket()
client.connect(("localhost", 5001))

data = {
    "name": "Jeevan",
    "values": [10, 20, 30]
}

message = pickle.dumps(data)
client.send(message)

response = client.recv(4096)
result = pickle.loads(response)

print("Server response:", result)

client.close()


import socket

client = socket.socket()
client.connect(("localhost", 5000))

message = input("Enter numbers separated by commas: ")
client.send(message.encode())

result = client.recv(1024).decode()
print("Sum from server:", result)

client.close()


import socket
import time

client = socket.socket()
client.connect(("localhost", 5001))

client.send("REQUEST".encode())
reply = client.recv(1024).decode()

print("Permission:", reply)

if reply == "GRANTED":
    print("Process entered Critical Section")
    time.sleep(2)
    print("Process leaving Critical Section")

    client.send("RELEASE".encode())
    print(client.recv(1024).decode())

client.close()

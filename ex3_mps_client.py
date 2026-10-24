
import socket
import threading

client = socket.socket()
client.connect(("localhost", 5000))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print("\nMessage received:", msg)
        except:
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    msg = input("Enter message (exit to quit): ")
    if msg == "exit":
        break
    client.send(msg.encode())

client.close()

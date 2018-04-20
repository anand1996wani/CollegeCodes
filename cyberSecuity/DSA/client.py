import socket
import random
import hashlib

client = socket.socket()
port = int(input("Enter the port number"))
client.connect(("localhost",port))
msg = client.recv(20)
print("Server msg is : ",msg)

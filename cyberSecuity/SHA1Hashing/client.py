import hashlib
import socket
clientSocket = socket.socket()
clientSocket.connect(("127.0.0.1",5000))
message = clientSocket.recv(512)
message = message.split("\t")
hexDigest1 = message[1]
message = message[0]
print("Received Mesage is  : ",message)
hashObject = hashlib.sha1(message)
hexDigest = hashObject.hexdigest()
if(hexDigest==hexDigest):
	print("Hash verified successfully")
else:
	print("Error in hash verification")


import hashlib
import socket
serverSocket = socket.socket()
serverSocket.bind(("127.0.0.1",5000))
serverSocket.listen(5)
clientSocket,clientAddress = serverSocket.accept()
print("Connection established to client ",clientAddress)
#message = str(raw_input("Enter your message"))
image = open('temp.png','rb')
message = image.read(1024)	
hashObject = hashlib.sha1(message)
hexdigest = hashObject.hexdigest()
clientSocket.send(message+"\t"+hexdigest)
clientSocket.close()


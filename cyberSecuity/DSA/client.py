import socket
import random
import hashlib

clientSocket = socket.socket()
clientSocket.connect(("127.0.0.1",5000))

receivedMessage = clientSocket.recv(4096)


messageArr = receivedMessage.split("\t")
message1 = messageArr[0]
p1 = int(messageArr[1])
q1 = int(messageArr[2])
g1 = int(messageArr[3])
y1 = int(messageArr[4])
r1 = int(messageArr[5])
s1 = int(messageArr[6])

#verification Algo

hexObject = hashlib.sha1(message1)
hexDig = hexObject.hexdigest()
hexint = int(hexDig,16)

print("Message received from client is : ",message1)

sInverse = 0
while(s1*sInverse % q1 != 1):
	sInverse = random.randint(1, q1)

if(r1>=1 and r1 <=q1-1 and s1>=1 and s1<=q1-1):
	w = sInverse
	u1 = (hexint*w)%q1
	u2 = (r1*w)%q1
	v = ((pow(g1,u1)*pow(y1,u2))%p1)%q1
	if(v==r1):
		print("Signature Verified Successfully")
	else:
		print("Signature Verification Failed")
		
else:
	print("Digital signature is not correct")

 

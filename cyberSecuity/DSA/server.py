import socket
import hashlib
import random
from Crypto.Util import number

serverSocket = socket.socket()
serverSocket.bind(("127.0.0.1",5000))
serverSocket.listen(5)
clientSocket,clientAddress = serverSocket.accept()
print("Connected to client ",clientAddress)
message = str(raw_input("Enter the message"))
hashObject = hashlib.sha1(message)
hexDig = hashObject.hexdigest()
hashInt = int(hexDig, 16)

p = 0
q = 0
g = 0
h = 0
x = 0
y = 0
k = 0
r = 0
s = 0
#Key Generation
q = number.getPrime(8)	#8 is the bit length of Q

while(True):
	p = number.getPrime(64) #64 is the bit length of P	
	if((p-1)%q==0):
		break
	
while(True):
	h = random.randint(2,p-2)	# 1 < h < p-1
	g = pow(h,(p-1)/q,p)
	if(g!=1):
		break

#User Private key
x = random.randint(1,q-1)	#  0 < x < q

print("User Private key is : ")
print("P : ",p)
print("Q : ",q)
print("G : ",g)
print("X : ",x)

#User Public Key
y = pow(g,x,p)			# y = g ^ x % p

print("User Public key is : ")
print("P : ",p)
print("Q : ",q)
print("G : ",g)
print("Y : ",y)


#signing logic
while(True):
	k = random.randint(2,q-1)	# 1 < k < q
	r = pow(g,k,p)%q
	if(r!=0):
		break

kInverse = 0	
while(k*kInverse % q != 1):
	kInverse = random.randint(1, q)

s = kInverse * (hashInt + x*r) % q

#Signature is (r,s)

print("Digital Signature is : ")
print("R : ",r)
print("S : ",s)

clientSocket.send(message+"\t"+str(p)+"\t"+str(q)+"\t"+str(g)+"\t"+str(y)+"\t"+str(r)
+"\t"+str(s))





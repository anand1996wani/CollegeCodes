import socket
import random
import hashlib
import math

def isPrime(n):
	if(n==2):
		return True
	for i in range(2,int(math.sqrt(n))+2):
		if(n%i==0):
			return False
	return True

q = 0
while(True):
	q = random.randint(2,10)
	if(isPrime(q)):
		break


print("Value of q is : ",q)

p = 0
while((p-1)%q!=0):
	while(True):
		p = random.randint(2,31)
		if(isPrime(p)):
			break
		
print("Value of p is : ",p)

h = random.randint(1,p-1)

g = pow(h,((p-1)/q),p)

print("Value is g is : ",g)

#Private Key
x = random.randint(1,q)

print("Value of x is ",x)

print("Private Key is :")

print("p : ",p)
print("q : ",q)
print("g : ",g)
print("x : ",x)


y = pow(g,x,p)

print("Value of y is ",y)

print("p : ",p)
print("q : ",q)
print("g : ",g)
print("y : ",y)


	

#signature Components
k = random.randint(1,q)
r = pow(g,k,p)%q
while(r==0):
	k = random.randint(1,q)
	r = pow(g,k,p)%q	
s = int((172/k + x*r)%q)

print("Signature Components")
print("r is : ",r)
print("s is : ",s)

#client side
w = random.randint(1,100)
while((s*w)%q!=1):
	w = random.randint(1,100)

u1 = 172*w%q
u2 = r*w%q
v = ((g**u1*y**u2)%p)%q

print("Verifing Components")
print("v is : ",v)


if(v==r):
	print("Signature verified")
else:
	print("Signature Incorrect")
	







'''
server = socket.socket()
port = int(input("Enter the port number"))
server.bind(("localhost",port))
server.listen(5)
client,address = server.accept()
temp = "Anand Dinesh Wani"
#client.send(temp.encode('ascii'))
client.send(temp)



client.close()
server.close()
'''

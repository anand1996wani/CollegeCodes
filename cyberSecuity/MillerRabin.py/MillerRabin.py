#It is a primality test, But accutually it tests wheather the number is composite. ie if the test says that number is composite then it is composite and if test says that the number is prime then it is probably composite.
import random
n = int(input("Enter the number"))
#step 1 n-1 = 2^k * q

p = n - 1
k = 0
while(True):
	if(p/2!=int(p/2) or p < 0):
		break
	p = int(p/2)
	k = k + 1
	#print(p)
print(k)
print(p)
print("Step 1 : n-1 = 2^k * m")
print("n = ",n)
print("k = ",k)
print("m = ",p)
m = p
#Step 2 Find an a such that 1 < a < n-1

a = random.randint(2,n-2)
print("Step 2 : 1 < a < n-1")
print("a = ",a)

#Step 3 b = a ^ m mod n

b = pow(a,m,n)
if(b == 1 or b == n-1):
	print("N Is Probably Prime")
else:
	t = 0
	flag = False
	while(t < k):
		t = t + 1
		b = pow(b,2,n)
		if(b == 1):
			print("Number is Composite")
			flag = True
			break
		elif(b == n-1):
			print("Number is probably prime")
			flag = True
			break
	if(flag == False):
		print("Number is Composite")
	

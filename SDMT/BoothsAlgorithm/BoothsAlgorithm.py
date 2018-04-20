'''
	binary arr is in reverse order 
	
'''

import copy
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def loadMain():
	return render_template('index.html')

@app.route("/",methods=['POST'])
def respond():
	num1 = int(request.form['num1'])
	num2 = int(request.form['num2'])
	binaryNum1 = decimalToBinary(num1)
	binaryNum2 = decimalToBinary(num2)
	print("gotcha")
	return str(boothsMultiplication(binaryNum1,binaryNum2))

 
def decimalToBinary(num):	
	length = 16
	binaryArr = []
	negative = False
	if(num < 0):
		negative = True
		num = num * -1
	for i in range(length):
		binaryArr.append(num%2)
		num = num//2
	if(negative):
		flag = False
		for i in range(length):
			if(flag!=True and binaryArr[i]==1):
				flag = True
			elif(flag==True):
				if(binaryArr[i]==1):
					binaryArr[i] = 0
				else:
					binaryArr[i] = 1
	#print(binaryArr[::-1])
	return binaryArr
	
def binaryToDecimal(binaryArr):
	length = len(binaryArr)
	negative = False 
	temp = copy.deepcopy(binaryArr)
	if(binaryArr[-1]==1):
		negative = True
	num = 0
	if(negative==True):
		flag = False
		for i in range(length):
			if(flag!=True and binaryArr[i]==1):
				flag = True
			elif(flag==True):
				if(binaryArr[i]==1):
					binaryArr[i] = 0
				else:
					binaryArr[i] = 1
	for i in range(len(binaryArr)):
		num = num + binaryArr[i]*pow(2,i)
	if(negative):
		num = num * -1
	binaryArr = copy.deepcopy(temp)
	print(binaryArr)	
	print(num)
	return num

def additionOfBinaryNumbers(binaryArr1,binaryArr2):
	binaryResult = []
	carry = 0
	#print("First number is : ",binaryArr1[::-1])
	#print("Second number is : ",binaryArr2[::-1])
	for i in range(0,16):
		if(binaryArr1[i]==0 and binaryArr2[i]==0 and carry==0):
			binaryResult.append(0)
			carry = 0
		elif(binaryArr1[i]==0 and binaryArr2[i]==0 and carry==1):
			binaryResult.append(1)
			carry = 0
		elif(binaryArr1[i]==1 and binaryArr2[i]==0 and carry==0):
			binaryResult.append(1)
			carry = 0
		elif(binaryArr1[i]==0 and binaryArr2[i]==1 and carry==0):	
			binaryResult.append(1)
			carry = 0
		elif(binaryArr1[i]==0 and binaryArr2[i]==1 and carry==1):
			binaryResult.append(0)
			carry = 1
		elif(binaryArr1[i]==1 and binaryArr2[i]==0 and carry==1):
			binaryResult.append(0)
			carry = 1
		elif(binaryArr1[i]==1 and binaryArr2[i]==1 and carry==0):
			binaryResult.append(0)
			carry = 1
		elif(binaryArr1[i]==1 and binaryArr2[i]==1 and carry==1):
			binaryResult.append(1)
			carry = 1
	#print(binaryResult[::-1])
	#binaryToDecimal(binaryResult)
	return binaryResult
	
def differenceOfBinaryNumbers(binaryArr1,binaryArr2):
	#2 compliment of first number
	temp = copy.deepcopy(binaryArr2)
	length = 16
	flag = False
	for i in range(length):
		if(flag!=True and binaryArr2[i]==1):
			flag = True
		elif(flag==True):
			if(binaryArr2[i]==1):
				binaryArr2[i] = 0
			else:
				binaryArr2[i] = 1
	result = additionOfBinaryNumbers(binaryArr1,binaryArr2)
	binaryArr2 = copy.deepcopy(temp)
	return result,binaryArr2
	
def arithmeticShiftRight(A,Q,Q_):
	A = A[::-1]
	Q = Q[::-1]
	Q_ = Q[-1]
	tempA = A[-1]
	for i in range(len(A)-1,0,-1):
		A[i] = A[i-1]
		Q[i] = Q[i-1]
	Q[0] = tempA
	A = A[::-1]
	Q = Q[::-1]
	print(Q)
	return A,Q,Q_ 
	'''
	carryA = A[0]
	for i in range(1,len(A)):
		A[i-1] = A[i]
		Q[i-1] = Q[i]
	Q[-1] = carryA		# pay attention here the HSB(m) takes value of LSB(a)
	A[-1] = Q_ 		# HSB(a) takes value of LSB(m) since q_0 is @0 position of m
	return A,Q
	'''
def boothsMultiplication(binaryNum1,binaryNum2):
	n = 16
	Q1 = 0
	#Q0 = None
	A = [0 for x in range(16)]
	Q = copy.deepcopy(binaryNum2)
	M = copy.deepcopy(binaryNum1)
	print("A : ",A[::-1])
	print("M : ",M[::-1])
	print("Q : ",Q[::-1])
	while(n!=0):
		if(Q[0] == 0 and Q1 == 1):
			#A = A - M
			A = additionOfBinaryNumbers(A,M)
			#print(A+M)
		elif(Q[0]==1 and Q1==0):
			#A = A + M
			A,M = differenceOfBinaryNumbers(A,M)
			#print(A+M)
		print("A : ",A[::-1])
		print("M : ",M[::-1])
		print("Q : ",Q[::-1])
		A,Q,Q1 = arithmeticShiftRight(A,Q,Q1)
		print("N : ",n)
		print("A : ",A[::-1])
		print("M : ",M[::-1])
		print("Q : ",Q[::-1])
		n = n - 1
	print("Multiplication result is :")
	return binaryToDecimal(Q + A)
	

if __name__ == "__main__":
	app.run()


'''
num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))
binaryNum1 = decimalToBinary(num1)
binaryNum2 = decimalToBinary(num2)
print("1 : Addition")
print("2 : Subtraction")
print("3 : Booths Multiplication")
choice = int(input("Enter your choice"))
if choice==1:
	additionOfBinaryNumbers(binaryNum1,binaryNum2)
elif choice==2:
	differenceOfBinaryNumbers(binaryNum1,binaryNum2)
elif choice==3:
	boothsMultiplication(binaryNum1,binaryNum2)
#binaryToDecimal(binaryNum1)
#binaryToDecimal(binaryNum2)
'''


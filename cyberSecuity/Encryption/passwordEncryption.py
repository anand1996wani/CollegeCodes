from pyDes import *;

def ceaserCipher(text):
	arr = list(text)
	for i in range(len(arr)):
		if(ord(arr[i]) >= 97 and ord(arr[i])<=122):
			arr[i] = chr((((ord(arr[i])-97)+3)%26)+97)
		elif(ord(arr[i]) >= 65 and ord(arr[i])<=90):
			arr[i] = chr((((ord(arr[i])-65)+3)%26)+65)
		elif(ord(arr[i]) >= 48 and ord(arr[i])<=57):
			arr[i] = chr((((ord(arr[i])-48)+3)%10)+48)
	return str(arr)
	
	
def dataEncryptionStandards(data,key):
	d = des(key,CBC,b"\0\0\0\0\0\0\0\0",pad = None,padmode = PAD_PKCS5)
	cipher = d.encrypt(data)
	return cipher,d.decrypt(cipher)
	

print("1 : Ceaser Encryption")
print("2 : DES")
choice = int(input("Enter your choice"))
if choice==1:
	print("Enter the text for encryption is small case or capital case")
	text = input()
	print("Original Text is : ",text)
	print("Encrpted Text Is  : ",end = " ")
	print(ceaserCipher(text))
elif choice==2:
	data = str(input("Enter data for encryption"))
	key = str(input("Enter key for encryption 8 bytes only"))
	print("Original Text is : ",data)
	print("Key is   : ",key)
	print("Encrypted Text is : ",end = " ")
	cipher,original = dataEncryptionStandards(data,key)
	print(cipher)
	print("Decrypted text is : ")
	print(original)	
	
'''
Class initialization
--------------------
pyDes.des(key, [mode], [IV], [pad], [padmode])
pyDes.triple_des(key, [mode], [IV], [pad], [padmode])

key     -> Bytes containing the encryption key. 8 bytes for DES, 16 or 24 bytes
	   for Triple DES
mode    -> Optional argument for encryption type, can be either
	   pyDes.ECB (Electronic Code Book) or pyDes.CBC (Cypher Block Chaining)
IV      -> Optional Initial Value bytes, must be supplied if using CBC mode.
	   Length must be 8 bytes.
pad     -> Optional argument, set the pad character (PAD_NORMAL) to use during
	   all encrypt/decrpt operations done with this instance.
padmode -> Optional argument, set the padding mode (PAD_NORMAL or PAD_PKCS5)
	   to use during all encrypt/decrypt operations done with this instance.

I recommend to use PAD_PKCS5 padding, as then you never need to worry about any
padding issues, as the padding can be removed unambiguously upon decrypting
data that was encrypted using PAD_PKCS5 padmode.

'''

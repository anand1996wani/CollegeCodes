def Display():
	for i in range(1,boardSize+1):
		for j in range(1,boardSize+1):
			if rowColumn[i]==j:
				print("Q",end = " ")
			else:
				print("B",end = " ")
		print()

def safe(row,column):
	for j in range(1,row):
		if(rowColumn[j]==column or abs(rowColumn[j]-column)==abs(j-row)):
			return False
	return True

def EightQueens(row):
	global flag
	for column in range(1,boardSize+1):
		if(safe(row,column)==True):
			rowColumn[row] = column
			if(row==boardSize):
				print(rowColumn[1:])
				print()
				Display()
				print()
			else:
				EightQueens(row+1)


boardSize = 8
rowColumn = [0 for x in range(boardSize+1)]
colFirstQueen = int(input("Enter The Column In Which Queen In The First Row Is To Be Placed : "))
rowColumn[1] = colFirstQueen
EightQueens(2)




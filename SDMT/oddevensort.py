import time
import threading
from threading import Thread
from multiprocessing.pool import ThreadPool

def serialOddEvenSort():
	
	isSorted = False
	while(isSorted==False):
		isSorted = True
		for i in range(1,n-1,2):
			if(arr[i] > arr[i+1]):
				temp = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = temp
				isSorted = False
	
		for i in range(0,n-1,2):
			if(arr[i] > arr[i+1]):
				temp = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = temp
				isSorted = False


def parallelOddEvenSort(elements):
	#elements =list(map(int, elements.split(",")))
	sorted = False
	lthread = None
	rethread  = None

	while(not(sorted)):
		pool = ThreadPool(processes=1)

		thread1 = pool.apply_async(innersort,(elements,1))
		thread2 = pool.apply_async(innersort,(elements,0))

		sorted = thread1.get()
		sorted = thread2.get() and sorted

		

	return elements

def innersort(array,val):
	sorted = True

	for i in range (val,len(array)-1,2):
		if array[i]>array[i+1]:
			temp  =array[i]
			array[i] = array[i+1]
			array[i+1] = temp
			sorted = False

	return sorted



num = input("Enter the elements to be sorted in space separated format")
#arr = list(map(int, num.split()))
arr = []
for i in range(1000):
	arr.append(1000-i)
#print(arr)
n = len(arr)
#print(n)

print("1 : serial oddeven sort")
print("2 : Parallel oddeven sort")
choice = input("Enter your choice")

if(choice=="1"):
	start_time = time.time()
	serialOddEvenSort()
	print("Sorted array is ",arr)
	print("Execution time is :",time.time() - start_time," sec")
elif(choice=="2"):
	start_time = time.time()
	parallelOddEvenSort(arr)
	print("Sorted array is ",arr)
	print("Execution time is :",time.time() - start_time," sec")

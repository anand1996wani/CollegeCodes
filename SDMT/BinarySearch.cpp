//============================================================================
// Name        : BinarySearch.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class BinarySearch{
	int n;
	int *array;
public:
	BinarySearch(int n);
	int Partition(int low,int high);
	void QuickSort(int low,int high);
	void DisplayArray();
	int SearchElement(int num);
};
BinarySearch::BinarySearch(int n){
	this->n = n;
	this->array = new int[n];
	cout<<"Enter The Array Elements"<<endl;
	for(int i = 0;i<this->n;i++){
		cin>>this->array[i];
	}
}
int BinarySearch::Partition(int low,int high){
	int pivot = this->array[high];
	int i = low - 1;
	for(int j = low;j < high;j++){
		if(this->array[j] < pivot){
			int temp = this->array[i + 1];
			this->array[i + 1] = this->array[j];
			this->array[j] = temp;
			i++;
		}
	}
	int temp = this->array[i+1];
	this->array[i+1] = pivot;
	this->array[high] = temp;
	return i+1;
}
void BinarySearch::QuickSort(int low,int high){
	if(low < high){
		int pivot = this->Partition(low,high);
		this->QuickSort(low,pivot-1);
		this->QuickSort(pivot+1,high);
	}
}
void BinarySearch::DisplayArray(){
	for(int j = 0;j < this->n;j++){
		cout<<this->array[j]<<"\t";
	}
	cout<<endl;
}
int BinarySearch::SearchElement(int num){
	int low = 0;
	int high = this->n - 1;
	int mid = (low + high)/2;
	while(low <= high){
		if(this->array[mid]==num){
			return mid;
		}
		else if(this->array[mid] < num){
			low = mid + 1;
		}
		else{
			high = mid - 1;
		}
		mid = (low + high)/2;
	}
	return -1;
}
int main() {
	int n;
	cout<<"Enter The Size Of Array"<<endl;
	cin>>n;
	BinarySearch *binarySearch = new BinarySearch(n);
	binarySearch->QuickSort(0,n-1);
	binarySearch->DisplayArray();
	cout<<"Enter The Element To Be Searched"<<endl;
	cin>>n;
	int temp = binarySearch->SearchElement(n);
	if(temp==-1)
		cout<<"Element "<<n<<" Not Found"<<endl;
	else
		cout<<"Element "<<n<<" Is Found At Position "<<temp+1<<" "<<endl;
	return 0;
}

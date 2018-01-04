#include <iostream>
#include <stdlib.h>
#include <ctime>
#include <omp.h>
using namespace std;
class QuickSort{
	public:
	int *array;
	int n;
	double start,stop;
	QuickSort(){
		cout<<"Enter the size of array\n";
		cin>>n;
		array = new int[n];		
		for(int i = 0;i<n;i++){
			array[i] = rand()%1000;
		}		
	}
	int partition(int low,int high){
		int i = low - 1;
		int pivot = array[high];
		for(int j = low;j < high;j++){
			if(array[j] < pivot){
				int temp = array[i+1];
				array[i+1] = array[j];
				array[j] = temp;
				i++;
			}
		}
		int temp = array[i+1];
		array[i+1] = array[high];
		array[high] = temp;
		return i+1;
	}
	void parallelQuickSort(int low,int high){
		if(low < high){
			int pivot = partition(low,high);
			#pragma omp parallel sections
			{
				#pragma omp section
				{
					quickSort(low,pivot-1);
				}
				#pragma omp section
				{
					quickSort(pivot+1,high);
				}
			}			
		}	
	}	
	void quickSort(int low,int high){
		if(low < high){
			int pivot = partition(low,high);
			quickSort(low,pivot-1);
			quickSort(pivot+1,high);			
		}	
	}	
	void print(){
		for(int i = 0;i<n;i++){
			cout<<array[i]<<"\t";
		}
		cout<<"\n";
		cout<<"Execution Time is : \t"<<((stop - start)/CLOCKS_PER_SEC)<<"\n";
	}
};
int main(){
	QuickSort quickSort;
	int choice;
	cout<<"1 Serial QuickSort, 2 Parallel QuickSort\n";
	cin>>choice;
	cout<<"Array before sorting\n";
	quickSort.print();
	if(choice==1){
		quickSort.start = clock();		
		quickSort.quickSort(0,quickSort.n - 1);
		quickSort.stop = clock();
	}
	else if(choice==2){
		quickSort.start = clock();
		quickSort.parallelQuickSort(0,quickSort.n - 1);
		quickSort.stop = clock();
	}
	cout<<"Array after sorting\n";	
	quickSort.print();
	return 0;
}


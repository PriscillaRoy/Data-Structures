#include <stdio.h>
#include <iostream>

using namespace std;

int maxSubArray(int a[] , int size){
    int max_so_far = 0;
    int max_ending_here = 0;
    

    
    for(int i = 0; i < size; i++){
        max_ending_here += a[i];
        if(max_ending_here < 0){
            max_ending_here = 0;
        }
        if(max_so_far < max_ending_here){
            max_so_far = max_ending_here;
        }
    }
    return(max_so_far);
}
int findLargestElement(int arr[], int n){

   int temp = arr[0];
   for(int i=0; i<n; i++) {
      if(temp<arr[i]) {
         temp=arr[i];
      }
   }
   return temp;
}
int main() {
	//code
	int T, index = 0;
	cin >> T;
	int result[T];
	while(T--){
	    int size;
	    cin >> size;
	    int num[size];
	    for(int j = 0; j < size ; j++){
	        cin >> num[j];
	    }
	    int max_ele = maxSubArray(num,size);
	    //cout << max_ele;
	    if(max_ele == 0){
	        max_ele = findLargestElement(num, size);
	    }
	    result[index] = max_ele;
	    index++;
	}
	for(int i = 0 ; i < index ; i++){
	    cout << result[i] << "\n";
	    
	}
	return 0;
}
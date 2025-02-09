/*
Largest element of an array
*/

#include <iostream>
using namespace std;
int largest_element(int arr[], int n){
    int largest = arr[0];
    for(int i = 0; i<n; i++){
        if (arr[i] >= largest){
            largest = arr[i];
        }
    }
    return largest;
}

int main(){
    int n= 5;
    int arr[5];
    for(int i = 0; i <n; i++){

        cin>> arr[i];
    }
    int greatest_elemnt = largest_element(arr, n);
    cout<<"The largest element of the input array is "<< greatest_elemnt;
    return 0;
}

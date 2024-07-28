/*
Pattern Name: Two pointer
Question: Pair with Target Sum
Descrption: Find a pair in an array that adds up to a specific target sum.
Problem Statement: Given an array of numbers sorted in ascending order and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target. If no such pair exists return [-1, -1].
*/

#include <iostream>
using namespace std;

void target_sum(int arr[], int sum_target){
    cout << "The input array is: "<< arr <<"\n";
    cout << "The input target value is :"<< sum_target;


}

int main(){
    int n= 5,target;
    cout << "Enter the length of the input array: "<< endl;
    cin >> n;

    int input_array[n];

    cout << "Enter the target sum value";
    cin >> target;
    for (int i =0; i<n; i++){
        cout <<i<< "\n";
        cin>> input_array[i];
    }
    cout << "the length of array is :"<< sizeof(input_array)/sizeof(input_array[0]);
    
    return 0;
}
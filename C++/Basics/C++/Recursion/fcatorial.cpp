/*
Problem: Find the sum of first N numbers using Recursion
Solution/idea: Two ways of finding the sum using Recursion--> 1. Parameterised Rceursion way 2. Functional way
*/

#include <iostream>
using namespace std;


void factorial_param(int i,int factorial ){
    if (i<1){
        cout<< factorial<< endl;
        return;
    }
    factorial_param(i-1, factorial*i);
}

int factorial_func(int i){
    if (i == 0){
        return 1;
    }
    return i * factorial_func(i-1);
}




int main(){
    int factorial = 1;
    int N;
    cout<< "Ente rthe input number N:";
    cin>> N;
    factorial_param(N, factorial);

    int factorial_output = factorial_func(N);
    cout<< "Factorial output is: "<<factorial_output;


    return 0;
}
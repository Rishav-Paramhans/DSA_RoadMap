/*
Problem: Find the sum of first N numbers using Recursion
Solution/idea: Two ways of finding the sum using Recursion--> 1. Parameterised Rceursion way 2. Functional way
*/

#include <iostream>
using namespace std;

void sum_recursion_param(int i, int total){

    if (i < 1){
        cout<< "Sum: "<<total;
        return ;

    }
    sum_recursion_param(i-1, total+i);

}

int sum_recursion_func(int i){
    if (i == 0){
        return 0; 
    }

    return i + sum_recursion_func(i-1);

}



int main(){
    int n= 5;
    int total = 0;
    sum_recursion_param(n,total);

    int func_total = sum_recursion_func(5);
    cout<< "Func total"<<func_total;
}
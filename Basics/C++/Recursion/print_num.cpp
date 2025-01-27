/*
Print number lineraly from 1-N , N-1 usinf recursion
*/
#include <iostream>
using namespace std;

void print_num(int N){
    if (N < 0){
        return;
        
    }
    cout<< N <<" , ";
    print_num(N-1);
}

int main(){
    int N;
    cout<<"Enter the input N:";
    cin>>N;
    print_num(N);
}
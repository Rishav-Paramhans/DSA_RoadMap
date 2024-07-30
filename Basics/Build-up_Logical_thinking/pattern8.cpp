/*
Basic program examples to explore logical building through Patterns
C++ Concepts: loops- for loop
Why Patterns: For practsing the loops which is used in all DSA
Pattern 1: 
    * * * * * * * * *
      * * * * * * *
        * * * * *
          * * *
            * 

*/

#include <iostream>
using namespace std;

void pattern(int n){
    for (int i = 0; i<n ; i++){
        for (int j=0; j< i; j++){
            cout<< " ";
        }
        for (int j =0; j< (2*n -(2*i +1)); j++){
            cout<<"*";
        }
        for(int j =0; j<i; j++){
            cout<<" ";
        }
        cout<<endl;
    }

}

int main(){
    cout<< "Enter the value of n:";
    int n;
    cin>>n;
    pattern(n);
    return 0;
}
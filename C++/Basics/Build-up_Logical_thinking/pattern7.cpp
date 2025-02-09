/*
Basic program examples to explore logical building through Patterns
C++ Concepts: loops- for loop
Why Patterns: For practsing the loops which is used in all DSA
Pattern 1: 
    * * * *
    * * * *
    * * * *
    * * * *
Pattern 2:
    * 
    * *
    * * *
    * * * *
    * * * * *
*/

#include <iostream>
using namespace std;

void pattern(int n){
    for(int i =0; i< n; i++){    // i =0
        for(int j = 0; j < (n -i -1); j++ ){
            cout<<" ";
        }
        for (int j= 0; j < 2*i + 1; j++){
            cout<<"*";

        }
        for (int j= 0; j< n-i-1; j++){
            cout<< " ";
        }
        cout<< endl;
    }

}

int main(){
    int n= 5;
    pattern(n);
    return 0;
}
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
#include <bits/stdc++.h>
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

void pattern9(int n){
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

void pattern10(int n){
    for(int i=0; i<n+1; i++){
        for(int j =0; j<i;j++){
            cout<<"*";
        }
        cout<<endl;
    }
    for( int i =1; i<n; i++){
        for(int j=0; j< n-i; j++){
            cout<<"*";
        }
        cout<<endl;
    }
}

int main(){
    cout<< "Enter the value of n:";
    int n;
    cin>>n;
    pattern9(n);
    pattern10(n);
    return 0;
}
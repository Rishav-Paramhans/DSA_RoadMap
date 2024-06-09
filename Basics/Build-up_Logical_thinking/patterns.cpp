/*
Basic program examples to explore logical building through Patterns
C++ Concepts: loops- for loop
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
void pattern(string pattern_name, int n){
    if (pattern_name == "Pattern 1"){
        for(int i =0; i<n; i++){
            for(int j=0 ; j<n; j++){
                cout<<"* ";
        }
        cout<<endl;
        }
    }
    else if (pattern_name == "Pattern 2"){
        for(int i =0; i<n; i++){
            for(int j=0 ; j<=i; j++){
                cout<<"* ";
        }
        cout<<endl;
        } 
    }
    else if (pattern_name == "Pattern 3"){
        for( int i = 1; i <=n; i++){
            for (int j=1; j<=i; j++){
                cout<<j;
            }
            cout<<endl;
        }
    }
    else if (pattern_name == "Pattern 4"){
        for( int i = 1; i<=n;i++){
            for(int j = 1; j<=i; j++){
                cout<<i;
            }
            cout<<endl;
        }
    }
    else {
        cout<<"Invalid input, please try again"<<endl;
    }
}
int main(){
    // Pattern 1
    int n;
    cout<<"Enter the number of rows and columns: ";
    cin>>n;
    pattern("Pattern 1", n);
    //Pattern 2
    pattern("Pattern 2", n);
    //Pattern 3
    pattern("Pattern 3", n);
    //Pattern 4
    pattern("Pattern 4", n);
    return 0;
}
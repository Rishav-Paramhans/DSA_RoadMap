/*
Basic Recursion problem 1::
Problem Stament: Print Name N times using Recursion
*/
#include <iostream>
#include <string>
using namespace std;

void print_name(int i, int n, string name){
    if (i > n){
        return;
    }
    cout<< name<< endl;
    print_name(i+1, n, name);
    

}


int main(){
    int n;
    string name;
    cout<< "Enter the number of time the name is to be printed: ";
    cin>> n;
    cout<< "Enter the name:";
    cin>> name;
    int cnt = 1;
    print_name(cnt, n, name);

}
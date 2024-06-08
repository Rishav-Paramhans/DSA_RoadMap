/*
Basic program to explore and introduce c++ functions
C++ Concepts: Datatypes, conditional statements, nested statments, namespaces
              ,functions (pass by reference/value)

Used to- encapsulate code to perform something, modularise code, incerase readibility, used same code multiple time(DRY)
four kinds majorly: void, return, parameterized and non-parameterized
The function can be user-defined or in-built function
*/

#include <iostream>
using namespace std;
//void function and non parameterized- doesnot return anything
void printName(){
    cout << "Hi my name is Rishav"<<endl;
}
//void function andparameterized- doesnot return anything
void printInputName(string input_name){
    cout << "Hi! Rishav. My name is "<< input_name <<endl;
}
// Note: the return type of the function can be actually any data type
int sum(int num1, int num2){
    return num1 + num2;
}
// Another point: Suppose a function expects a return type and may be due to some conditions the 
//the return statament doesnot get executed--> then the function returns a garabge value

// Very important concept: Pass by value and reference
void doSomething(string &s1, string s2 ){
    s1[0] = 't';
    s2[0] = 't';
    cout<< "String 1 "<< s1 <<" string 2"<< s2;
}
int main(){
    printName(); 
    string name;
    cout<< "Enter you name: ";
    getline(cin,name);
    printInputName(name);

    cout<<"Enter the two numbers that you wat to add: "<<endl;
    int num1, num2;
    cin>>num1>>num2;
    // first the function will be executed and then the returned value will be passed in the function
    int result = sum(num1, num2);
    cout<<"The sum of "<<num1 <<" and " <<num2 <<"is "<< result<<endl;

    int max = std::max(num1, num2);
    cout<< "the maximum of "<<num1 <<" and "<< num2 <<" is "<<max <<endl;

    cout<< "Enter string 1 and string 2: " <<endl;
    string s1,s2;
    cin>>s1>>s2;
    doSomething(s1, s2);
    cout<< "Orginal strings were" << s1 <<s2;
    return 0;
}
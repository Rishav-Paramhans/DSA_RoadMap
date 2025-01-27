/*
    Task: Write a program that takes an input of age and prints if you are
    an adult or not
    Thought process:
    1. Takes an input- so input the age--> since age so integer datatype should be enough
    2. Conditional- comparision if input age is >=18 or not
    3.Print Statemnt based on the conditional

*/
#include<iostream>

using namespace  std;

int main(){
    int age;
    cout<<"Enter your age: ";
    cin>>age;
    if (age >= 18){
        cout<< "You are an adult.";
    }
    else{
        cout<<"You are "<<(18-age)<<"years shy of being adult";
    }

    return 0;
}

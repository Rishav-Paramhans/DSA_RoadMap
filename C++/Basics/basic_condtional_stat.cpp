/*
Basic program to check whether a person is actually eligible for a job
C++ Concepts: Datatypes, conditional statements, nested statments, namespaces
*/

#include <iostream>
using namespace std;

int main(){
    cout<<"Enter the age of the person"<<endl;
    int age;
    cin>> age;

    if (age <18){
        cout<< " not eligible for a job"<< endl;
    }
    else if (age <= 57){
        if (age <=54){
            cout<< "Eligible for job"<<endl;
        }
        else{
            cout<<"Eligible for job, but retirement soon"<<endl;

        }
    }
    else{
        cout<<"retirement time"<<endl;
    }


    return 0;
}
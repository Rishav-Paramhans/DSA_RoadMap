/*
Basic program to print the days of the week using day number and using the switch staments
C++ Concepts: Datatypes, conditional statements, nested statments, namespaces, switch staments
*/
// Few learnings: always use break statemenet- if not used, all the switch staments after the first 
// correct one will be executed. break stament- used to break out of all the conditional statements

#include <iostream>
using namespace std;

int main(){
    int day_num = 0;
    cout<< "Enter the day number: "<<endl;
    cin>> day_num;

    switch(day_num){
        case 1:
            cout<< "Moday";
            break;
        case 2:
            cout<< "Tuesday";
            break;
        case 3:
            cout<< "Wednesday";
            break;
        case 4:
            cout<< "Thurday";
            break;
        case 5:
            cout<< "Friday";
            break;
        case 6:
            cout<< "Saturday";
            break;
        case 7:
            cout<< "Sunday";
            break;
        default:
            cout<<"Invalid input";
    }
    return 0;
}

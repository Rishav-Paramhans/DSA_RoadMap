/*
Basic program to explore and introduce arrays
C++ Concepts: Datatypes, conditional statements, nested statments, namespaces, arrays
              for loops, while loops and do-while loops
*/
#include <iostream>
using namespace std;

int main(){
    int arr[5], arr2[5], arr3[5];
    // if we dont initialize the array element--> it takes garnage values
    // stored in a contagious memeory--> we dont where in the memory the first element is stored but once
    // we the location of first element in memmory --> then we know the location of next elements
    // Arrays stored values of same datatyes and 0-indexed

    cout<< "enter the values of elements of the array arr";
    // in the for loop, last part (here i= i+1) is executed after the statments inside the for loop are executed
    // and then the condition for the for loop. Here--> i<5
    
    // using for loop to take in the elements of arrary arr
    for (int i =0; i<5; i = i+1){
        cin>>arr[i];
        cout<< "Value of the " <<i<<"element" <<arr[i]<<endl;
    }
    
    // using while loop to take in the elements of arrary arr2
    cout<< "enter the values of elements of the array arr2";
    int i = 0; // Initializing the looping variable for 0th index
    while (i < 5){
        cin>>arr2[i];
        cout<< "Value of the " <<i+1<<"element" <<arr2[i]<<endl; 
        i++;  // incrementing the looping varaible
    }

    // using do-while loop--> we use this to run the statment atleast one time even if the while condition is not met
    int j = 4; // Initializing the looping variable for 0th index
    do{
        cout<< "Value of the arra2 using do while loop: " <<j+1<<"element" <<arr2[j]<<endl; 
        j++;  // incrementing the looping varaible
    }while (j < 5);  //Dont forget the semicolon after the while conditional statements


    return 0;
}

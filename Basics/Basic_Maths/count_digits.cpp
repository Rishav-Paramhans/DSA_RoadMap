/*
Problem Stament: Given a number "n", find out and return the number of digits in a mumber
*/

#include <iostream>
using namespace std;



int count_digits(int n){
    int cnt = 0;
    while (n>0){
        n = n/10;
        cnt++;
    }
    return cnt;
}



int main(){
    cout<< "Enter the input number: ";
    int input_num;
    cin>> input_num;
    int digit_cnt;
    digit_cnt = count_digits(input_num);
    cout<<" The number of digits in "<< input_num << " is " << digit_cnt <<endl;

    return 0;
}

// Time complexity of this code from my understanding is O(N)
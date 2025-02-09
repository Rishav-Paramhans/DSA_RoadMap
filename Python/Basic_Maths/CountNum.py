"""
This file will have code for Basic Maths
1. Extarcting digits

"""

def extract_digit(n):
    while (n%10 !=0):
        print("Extracted digits in n are : ", n%10)
        n= int(n/10)
def count_digit(n):
    count = 0
    while (n%10 !=0):
        count = count+1
        n = int(n/10)
        print("n", n)
    print("total number of digits in n are: ", count)
def reverseNum(n):
    reversed_num = 0
    while (n%10 !=0):
        print("Extracted number: ", n% 10)
        reversed_num = reversed_num*10 + n%10
        n= int(n/10)
    print("Reversed numbe of n is {}".format(reversed_num))

    return reversed_num

def isPaliandrome(n, reverseNum= reverseNum):
    reversed_number = reverseNum(n)
    if reversed_number == n:
        print("Its a palindrome")
    else:
        print("Its not a Plaindromee")

def hcf(n1, n2 ):
    """_summary_: Finds the Highest common factor 
    Args:
        n1 (_type_): _description_
        n2 (_type_): _description_
    Thought process: get the factors of both the numbers and then find the highest common one
    Brute forve: Loop over every number until n  and colect every divisior with n% i == 0
                i.e we will loop n time ---> Time Complexity O(N)
    Another Solution: Lets say number is 36--> 1X36, 2X18, 3X12, 4X9, 6X6 --> no after this any number we
                        get a divisior, it would be one of the number in this. 
    
    """
    for i in range(1, int(n1/2)):
        divisors = set()
        if n1%i ==0:
            divisors.add(i)
            dividend = int(n1/i)
            divisors.add(dividend)
        for div in divisors:
            print(div)
if __name__ == "__main__":
    n1= int(input("Enter the number n: "))
    n2 = int(input("Enter the second numebr n2:"))
    extract_digit(n1)
    count_digit(n1)
    reverseNum(n1)
    isPaliandrome(n1)
    hcf(n1, n2)

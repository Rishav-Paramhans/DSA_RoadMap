"""_summary_

Some learnings: Always understand what is the base condition for the recursion-
                this gives us the understanding that when i need to add a return statement
                to stop recursion- otherwise stackoverflow
"""
# Print Name n time using Recursion
def printtName(name, times, iteration):
    #time complexity: O(N)
    if (iteration > times):
        return
    else:
        print("Name:", name)
        printtName(name, times, iteration+1)
      
#Print number linealy until N
def printNum(N, i):
    #time complexity: O(N)
    if i > N:
        print("\n")
        return
    else:
        print(i, end=" ")
        printNum(N, i+1)
    
#Print number lineraly from N to 1
def printNumDecreasing(N,i):
    if (i < 1):
        return
    else:
        print(i, end=" ")
        printNumDecreasing(N, i-1)

# Print sum of first N numbers
def sumNum(n, summation):
    if n<1:
        print("Summation:", summation)
        return
    else:
        summation= summation + n
        sumNum(n-1, summation)

def sumNum2(n):
    if n == 0:
        return 0
    else:
        return n + sumNum2(n-1) 
    
#Factorial of n
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

#Reverse an array

def reverse_array(A):
    l_index = 0
    r_index = len(A)-1

    while (l_index != r_index):
        A[l_index], A[r_index] = A[r_index], A[l_index]
        l_index+=1
        r_index-=1
    return A

def revArrayRecursion(A, l_index, r_index):
    if l_index > r_index:
        return 
    else:
        A[l_index], A[r_index] = A[r_index], A[l_index]
        revArrayRecursion(A, l_index+1, r_index-1)
    

def isPalindromeSting(input_string):
    input_list = list(input_string)
    revArrayRecursion(input_list, 0, len(input_list)-1)
    if list(input_string) == input_list:
        print("Is Plaindrome")
    else:
        print("Not a palindrome")

def isPaliandromeStringRecursion(input_string, i):
    if i>= (int(len(input_string)/2)):
        return True
    elif (input_string[i] != input_string[len(input_string)-i-1]):
        False
    return isPaliandromeStringRecursion(input_string, i+1)


def fibonacci(n):
    if n == 0:     
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

if __name__=="__main__":
    ame = "Rishav Kumar Paramhans"
    times = 5
    printtName(ame, times,0)

    printNum(5,0)

    printNumDecreasing(5,i=5)
    sumNum(5,0)

    total = sumNum2(5)
    print("total: ", total)

    result = factorial(5)
    print("The factorial of 5 is:", result)

    input_array = [1,2,3,4,5]
    reversed_array = reverse_array(input_array)
    print("The reversed array of {}".format(reversed_array))

    A= [2, 3, 1, 1,4,8]
    revArrayRecursion(A, 0, (len(A)-1))
    print("The reversed array is ", A)

    B = "abba"
    isPalindromeSting(B)

    plaindrome_status = isPaliandromeStringRecursion(B, i=0)
    print("Palindrome Stataus", plaindrome_status)

    a= fibonacci(6)
    print(a)

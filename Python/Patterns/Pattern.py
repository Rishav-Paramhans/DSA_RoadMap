"""
Pattern: 1
         1 2
         1 2 3
         1 2 3 4 
         1 2 3 4 5
         Thought process: Whenever something like this - one something for some times and 
         do it everytime with some modification- think of loops and secondly in every time
         you have to do things again a certain number of time, so two loops

         Conclusion: if something like this in 2D layeout- two loops required'
Pattern4: * * * * *
          * * * *
          * * *
          * *
          * 
"""

def pattern3(n):
    #Time complexity: O(n^2)
    """_summary_

    Args:
        n (_int_): _number of time and until you want to so it here // changes with problem
    """
    for i in range(n+1):   # Why start with 1-because we want to print 1 and range takes from 0 until input-1 
        for j in range(1, i+1):
            print(j, end = " ")
        print("\n")

def pattern5(n):
    #Time complexity: O(n^2)
    for i in range(n, 0, -1):
        for j in range(i,0,-1):
            print("*", end= " ")
        print("\n")

def pattern5(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j, end = " ")
        print("\n")

def pattern7(n):
    for i in range(1,n+1,1):
        for j in range((n-i)):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end= "")
        for l in range((n-i)):
            print(" ", end="")
        print("\n")

def pattern8(n):
    for i in range(n,0,-1):
        for j in range((n-i)):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end= "")
        for l in range((n-i)):
            print(" ", end="")
        print("\n")

def pattern9(n):
    for i in range(1,n+1,1):
        for j in range((n-i)):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end= "")
        for l in range((n-i)):
            print(" ", end="")
        print("\n")
    for i in range(n,0,-1):
        for j in range((n-i)):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end= "")
        for l in range((n-i)):
            print(" ", end="")
        print("\n")

def pattern10(n):
    for i in range(1, n+1):
        for l in range(i):
            print("*", end="")
        print("\n")
    for j in range(n-1,0,-1):
        for k in range(j):
            print("*", end="")
        print("\n")

if __name__ == "__main__":
    n = int(input("Enter the values of n:" ))
    pattern10(n)

"""_summary_: Second largest array without sorting
"""

# This is the first implementataion- but lets do it this way-
"""1. Brute Force-> First sort the array and then keep checking the numbers from left for second highest
    2. Better-> First find the greatest element using TC-> O(N) and then do another pass find the seconf highest
    3. Best-> Single pass, take greatest a[0] and second largest -1 and then single pass keep assigning greatest and also chaning the second largest
"""
def second_largest_element(input_array):
    """
    Psuedo code: 

    """
    largest_elemnt = input_array[0]
    for i in range(len(input_array)):
        if input_array[i]> largest_elemnt:
            largest_elemnt = input_array[i]
        else:
            pass

    print(largest_elemnt)
    input_array = [x for x in input_array if x!=largest_elemnt]
    print("input_array", input_array)

    second_largest = input_array[0]
    for i in range(len(input_array)):
        if input_array[i]> second_largest:
            second_largest = input_array[i]
        else:
            pass

    print(second_largest)

def second_largest_optimized(input_array):
    greatest_element = input_array[0]
    second_largest = -1

    for i in range(len(input_array)):
        
        if input_array[i] > second_largest:  #Candidate of interest to us

            if input_array[i] > greatest_element and greatest_element != input_array[i]:
                second_largest = greatest_element
                greatest_element = input_array[i]
            elif(input_array[i] < greatest_element):
                second_largest = input_array[i]
            else:
                pass
                  
        else:
            pass
    return second_largest

if __name__ == "__main__":
    input_arr = [10,20,60,14,14,29,10, 60]
    #second_largest_element(input_arr)
    second_greatest = second_largest_optimized(input_arr)
    print("Second largest", second_greatest)
        
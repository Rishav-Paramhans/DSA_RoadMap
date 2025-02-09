"""
Problem Statement: You are given a sorted integer arr "ARR" of size "N"
. You need to remove the duplicates from the array such that each element appears
only once. Return the length of this new array

Considerations: Donot allocate extra space for another array. You need to do this modifyning by modifying the given input array in-place with O(1) extra memory
"""


def num_unique_elements(input_array, n):
    i = 0
    for j in range(1, n):
        if input_array[j] != input_array[i]:
            input_array[i+1] = input_array[j]
            i+=1
        else:
            pass
    return i+1


if __name__ == "__main__":
    arr = [1,1,2,2,2,3,3]
    num_unique_ele = num_unique_elements(arr, len(arr))
    print("No of unique elements in the given input array is:", num_unique_ele)
"""_summary_: Check if an input array is sorted
"""

def issorted(input_array):
    isSorted = True
    for i in range(len(input_array)-1):
        if input_array[i+1]>= input_array[i]:
            pass
        elif input_array[i+1] < input_array[i]:
            isSorted = False
            break
    return isSorted



if __name__ == "__main__":
    input_arr = [10,20,60,14,14,29,10, 60]
    isSORTED = issorted(input_arr)
    print("Is the array sorted:",isSORTED)
    input_arra2= [1,2,3,5,5,7]
    isSORTED = issorted(input_arra2)
    print("Is the array sorted:",isSORTED)
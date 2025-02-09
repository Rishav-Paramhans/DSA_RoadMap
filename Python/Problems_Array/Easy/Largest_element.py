"""_summary_: Largest element in Array
"""

def largest_element(input_array):
    # But time complexity of this is O(N)--> Can we imporve it?
    largest = input_array[0]
    for i in range(len(input_array)):
        if input_array[i] >= largest:
            largest = input_array[i]
        else:
            pass

    return largest



if __name__ == "__main__":
    input_array = [2, 5,10, 54, 0, 1]
    greatest_element = largest_element(input_array=input_array)
    print("Greatest element in the input array is : ", greatest_element)

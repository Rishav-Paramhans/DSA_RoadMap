"""_summary_: Bubble sorting
"""


def bubble_sort(input_array, n):
    for i in range(n-1, 0, -1):
        print("i", i)
        didSwap = 0
        for j in range(i):
            if input_array[j] > input_array[j+1]:
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
                didSwap = 1
            else:
                pass
        if didSwap ==0:
            break







if __name__ == "__main__":
    array = [13,46,24,52,20,9]
    sorted_array_input = [1,2,3,4,5,6]
    bubble_sort(array, n= len(array))
    print(array)
    bubble_sort(array, n= len(sorted_array_input))
    print(sorted_array_input)
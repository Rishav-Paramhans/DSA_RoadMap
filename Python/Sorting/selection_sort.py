"""_summary_: Selection sort
"""


def selection_sort(input_array, n):
    for i in range(n-1):
        min_index = i
        for j in range(i, n):
            if input_array[j] < input_array[min_index]:
                input_array[min_index], input_array[j] = input_array[j], input_array[min_index]
            else:
                pass


if __name__ == "__main__":
    array = [13,46,24,52,20,9]
    selection_sort(array, n= len(array))
    print(array)


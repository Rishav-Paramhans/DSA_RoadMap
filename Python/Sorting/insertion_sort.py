"""_summary_: Bubble sorting
"""

def insertion_sort(array, n):
    for i in range(1, n):  # selecting element loop
        print("i", i)
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                pass

if __name__ == "__main__":
    array = [13,46,24,52,20,9]
    insertion_sort(array, n= len(array))
    print(array)
    print(9%2)
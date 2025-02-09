"""_summary_: Merge sort algorithm
"""
def merge(array, low, mid, high):
    temp = []
    left = low
    right = mid+1

    while (left <=mid and right <=high):
        if (array[left] <= array[right]):
            temp.append(array[left])
            left+=1
        else:
            temp.append(array[right])
            right+= 1
    while (left<= mid):
        temp.append(array[left])
        left+=1
    while (right<=high):
        temp.append(array[right])
        right+=1
    
    for i, val in enumerate(temp, start=low):
        array[i] = val
        
def merge_sort(array, low, high):
    
    if (low >= high):
        return
    else:
        mid = (low + high )//2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)

    
    
    

if __name__ == "__main__":
    input_array = [13,46,24,52,20,9]
    merge_sort(input_array, low = 0, high = len(input_array)-1)
    print(input_array)
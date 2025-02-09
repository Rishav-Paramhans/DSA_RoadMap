"""_summary_: remove duplicates
"""


def remove_duplicates(input_array):
    seen = set()
    unique_element_list = []
    for i in range(len(input_array)):
        if (input_array[i] not in seen):
            seen.add(input_array[i])
            unique_element_list.append(input_array[i])     
        else:
            pass
            
            
    print(unique_element_list)
    #Note: This approach is good for list look-ups has TC -> O(N), so over all TC for us beacome O(N^2) but less SC as i am usinf just one more array
    # if we use a set for look up the TC for look ups in set is O(1)

if __name__ =="__main__":
    arr = [5,7,7,3,4,6,4,9,10]
    remove_duplicates(arr)

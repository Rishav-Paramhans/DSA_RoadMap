

if __name__== "__main__":
    arr = [-1,2,3,3,4,5,-1]
    k=4
    max_sum =0
    index = 0
    for i in range(len(arr)-k):
        sum = arr[i]+ arr[i+1] + arr[i+2]+ arr[i+3]
        if sum > max_sum:
            max_sum = sum
            index = i

            
        else:
            pass
    print("Max Sum", max_sum)
    print("indexes", index, index+1, index+2, index+3 )
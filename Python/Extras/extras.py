

N =1234
reversed_number = 0
while (N>0):
    element = int(N%10)
    N=int(N/10)
    reversed_number = reversed_number*10 + element
print("Reversed number", reversed_number)


#printname

def printName(cnt,N, name):
    if cnt>N:
        return
    else:
        cnt+=1
        print("Name", name)
        printName(cnt, N, name)


def occurence_has_array(input_array):
    # Lets say the input array can have only numbers until 12
    hash_array =[0]*12

    for i in range(len(input_array)):
        hash_array[input_array[i]] +=1

    return hash_array

if __name__ =="__main__":
    printName(0,5, "Rishav")
    input_array = [1,2,2,3,3,4,4,4]
    occurnec_array = occurence_has_array(input_array)
    print("Number of time 4 is in the array are ", occurnec_array[4])

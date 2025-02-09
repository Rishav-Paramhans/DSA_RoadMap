"""_summary_: This containes basic character hasinf implementation to find out the number of occurence of a character in a given string

"""

def char_frequency(input_string):
    #  lets say the string can only have lower case letters
    char_hash_array = [0]*26
    for i in range(len(input_string)):
        char_hash_array[ ord(input_string[i])- ord('a')] +=1
    
    return char_hash_array








if __name__ =="__main__":
    input_str = "rishavrr"
    frequency_array = char_frequency(input_str)
    print(frequency_array[ord('r')-ord('a')])
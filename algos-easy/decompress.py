# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

# def decompress(s):#decompress function is designed to take a string s as input and perform a specific operation to decompress it.
#     # pass #TODO:



def decompress(s):
    decompressed = ""  # Initialize an empty string to store the decompressed version
    num = ""  # Initialize an empty string to store the numerical part of each group
    
    for char in s:  # Iterate through each character in the input string
        if char.isdigit():  # Check if the current character is a digit
            num += char  # Append the digit to the 'num' string
        else:
            if num:  # Check if the 'num' string is not empty
                decompressed += char * int(num) # char is the string "a" and num is the string "3".
                #The line decompressed += char * int(num) would append "aaa" to the existing value of decompressed.

                       #This line effectively deco
                # Append the character repeated 'num' times to 'decompressed'
                num = ""  # Reset 'num' to an empty string, indicating the end of a group
            else:
                decompressed += char  # Append the character to 'decompressed' since it is not part of a group
    
    return decompressed  # Return the decompressed string

# TEST CASES
print (decompress("2c3a1t")) # -> 'ccaaat'
print(decompress("4s2b")) # -> 'ssssbb'
print(decompress("2p1o5p")) # -> 'ppoppppp'
print(decompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'
print(decompress("127y"))# -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

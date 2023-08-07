# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.


def compress(s):
    pass # TODO:

    compressed = ""  # Initialize an empty string to store the compressed version
    count = 1  # Initialize a count variable to keep track of consecutive occurrences

    # Iterate through each character in the string
    for k in range(1, len(s)):
        if s[k] == s[k-1]:  # If current character is the same as previous character
            count += 1  # Increment the count
        else:
            if count > 1:  # If count is greater than 1, append it to the compressed string
               compressed += str(count)
            compressed += s[k-1]  # Append the previous character to the compressed string
            count = 1  # Reset the count for the new character

    # Handle the last character
    if count > 1:#This condition checks if there were consecutive occurrences of the same character before reaching the last character. If count is greater than 1, it means there were consecutive occurrences.
        compressed += str(count)# If the condition is true, we append the value of count (converted to a string using str()) to the compressed.This indicates the number of consecutive occurrences of the last character.
    compressed += s[-1]#This ensures that the last character is included in the compressed result

    return compressed

# TEST CASES
print(compress('ccaaatsss')) # -> '2c3at3s'
print(compress('ssssbbz')) # -> '4s2bz'
print(compress('ppoppppp') )# -> '2po5p'
print(compress('nnneeeeeeeeeeeezz')) # -> '3n12e2z'
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'));  # -> '127y'

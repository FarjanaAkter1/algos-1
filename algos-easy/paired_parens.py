# Paired Parentheses

# Write a function, paired_parens, that takes in a string as an argument. 
# The function should return a boolean indicating whether or not the string has well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.


# def paired_parens(string): pass # todo



def paired_parens(string):# takes a single argument string.
    result = []# This line initializes an empty list named result.
    
    for char in string:#This line starts a loop that iterates through each character. 
        if char == '(':# This line checks if the current character char is an opening parenthesis. 
            result.append(char)#If the character is an opening parenthesis, it's added to the result list
        elif char == ')':# This line checks if the current character char is a closing parenthesis ')'
            if len(result) == 0:# If the character is a closing parenthesis, this line checks if the result list is empty. If it's empty, 
                #it means we have an unmatched closing parenthesis without a corresponding opening parenthesis.
                return False# In this case, the function immediately returns False because the parentheses are not well-formed.
            result.pop()#If the result list is not empty and we encounter a closing parenthesis, we remove the last element from the result list.
            #This simulates the pairing of the closing parenthesis with its corresponding opening parenthesis.
    
    return len(result) == 0 # After the loop completes, this line checks if the result list is empty.
    #If it is, all parentheses were correctly paired, so the function returns True. 

# TEST CASES
print(paired_parens("(david)((abby))")) # -> True
print(paired_parens("()rose(jeff"))     # -> False
print(paired_parens(")("))              # -> False
print(paired_parens("()"))              # -> True
print(paired_parens("(((potato())))"))  # -> True
print(paired_parens("(())(water)()"))   # -> True




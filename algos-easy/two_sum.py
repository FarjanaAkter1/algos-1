# Two Sum

# Write a function, two_sum, that takes in a list and a target sum as arguments. 
# The function should return a tuple containing a two of indices whose elements sum to the given target. 
# The indices returned must be unique.
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such two that sums to the target.

def two_sum(numbers, target_sum):#defines a function named two_sum that takes two parameters: numbers, which is a list of numbers, and target_sum, which is the sum we're trying to achieve.
    a = {}  # A dictionary to store previously a numbers and their indices
    
    for i, num in enumerate(numbers):# a loop that iterates through each element in the numbers list, where enumerate(numbers) provides both the index and the corresponding number in each iteration. This is done using the enumerate function.
        set = target_sum - num #For each element in the loop, the code calculates the difference between the target_sum and the current number, storing it in the variable set. This represents the value that, when added to the current number, would give us the desired target_sum.
        if set in a:
            return (a[set], i)  # Return the indices of the two elements
        
        a [num] = i  # Store the current number and its index/If the set is not found in a, we add the current number as a key to the seen dictionary, with its index as the corresponding value. This allows us to keep track of numbers we've encountered, along with their indices.
 
    return None  # Return None if no valid pair is found

# TEST CASES
print(two_sum([3, 2, 5, 4, 1], 8))  # Should print: (0, 2)
print(two_sum([4, 7, 9, 2, 5, 1], 5))  # Should print: (0, 5)
print(two_sum([4, 7, 9, 2, 5, 1], 3))  # Should print: (3, 5)
print(two_sum([1, 6, 7, 2], 13))  # Should print: (1, 2)
print(two_sum([9, 9], 18))  # Should print: (0, 1)
print(two_sum([6, 4, 2, 8], 12))  # Should print: (1, 3)








#   ////////////////////////////////////////////////////////////



def two_sum(numbers, target_sum):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return (i, j)
    return None

# TEST CASES

print(two_sum([3, 2, 5, 4, 1], 8))  # Should print: (0, 2)
print(two_sum([4, 7, 9, 2, 5, 1], 5))  # Should print: (0, 5)
print(two_sum([4, 7, 9, 2, 5, 1], 3))  # Should print: (3, 5)
print(two_sum([1, 6, 7, 2], 13))  # Should print: (1, 2)
print(two_sum([9, 9], 18))  # Should print: (0, 1)
print(two_sum([6, 4, 2, 8], 12))  # Should print: (1, 3)



















# def two_sum(numbers, target_sum):
# This line defines a function named two_sum that takes two parameters: numbers, which is a list of numbers, and target_sum, which is the sum we're trying to achieve.

#     seen = {}
# This initializes an empty dictionary named seen which will be used to keep track of numbers encountered so far, along with their indices.
# 
# for index, num in enumerate(numbers):
# This starts a loop that iterates through each element in the numbers list, where enumerate(numbers) provides both the index and the corresponding number in each iteration. This is done using the enumerate function.
# 
# complement = target_sum - num
# For each element in the loop, the code calculates the difference between the target_sum and the current number, storing it in the variable complement. This represents the value that, when added to the current number, would give us the desired target_sum.
# 
#  if complement in seen:
# This checks if the calculated complement is already present as a key in the seen dictionary.
# 
#             return (seen[complement], index)
# If the complement is found in the seen dictionary, it means we've already encountered a number that, when added to the current number, gives the target_sum. In this case, we return a tuple containing the index of the previously encountered number and the current index. This tuple represents the indices of the two elements that sum up to the target_sum.
# 
#   seen[num] = index
# If the complement is not found in seen, we add the current number as a key to the seen dictionary, with its index as the corresponding value. This allows us to keep track of numbers we've encountered, along with their indices.
# 
#  return None
# If the loop completes without finding a valid pair of indices that sums up to the target_sum, the function returns None to indicate that no such pair was found.
# Overall, this code efficiently uses a dictionary to keep track of numbers encountered so far, allowing us to find pairs of indices whose corresponding numbers sum up to the desired target_sum. If such a pair is found, the function returns the indices of the two elements; otherwise, it returns None.

# # Sum List

# # Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. 
# # The function should return the total sum of all values in the linked list.

# # Do not edit Class
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def sum_list(head):
#     total = 0  # Initialize a variable to keep track of the sum

#     # Create a variable for tracking where I am in the linked list
#     current = head

#     # Iterate through the entire list
#     while current is not None:
#         # Add the value of the current node to the total
#         total += current.val

#         # Move on to the next node
#         current = current.next

#     return total  # Return the sum of values
#///////////////recursive way 



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sum_list(head):
    # Create a variable to track the total
    total = 0
    current = head

    while current is not None:
        total += current.val
        current = current.next

    return total

def recursive_sum_list(head):
    # Base case: we have gone past the tail (visited all nodes)
    if head is None:
        return 0

    # Recursive case: we still have one or more nodes to visit
    return head.val + recursive_sum_list(head.next)

# TEST CASES
# 1.
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)
a.next = b
b.next = c
c.next = d
d.next = e
print(sum_list(a))  # -> 19

# 2.
x = Node(38)
y = Node(4)
x.next = y
print(sum_list(x))  # -> 42

# 3.
z = Node(100)
print(sum_list(z))  # -> 100

# 4.
print(sum_list(None))  # -> 0






# # TEST CASES
# # 1. 
# a = Node(2)
# b = Node(8)
# c = Node(3)
# d = Node(-1)
# e = Node(7)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# print(sum_list(a)) # -> 19

# 2.
# x = Node(38)
# y = Node(4)
# x.next = y
# print(sum_list(x)) # -> 42

# 3.
# z = Node(100)

# # 4.
# print(sum_list(z)) # -> 100

# # 5.
# print (sum_list(None)) # -> 0

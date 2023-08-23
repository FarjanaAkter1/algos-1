# # Depth First Values

# # Write a function, depth_first_values, that takes in the root of a binary tree. 
# # The function should return a list containing all values of the tree in depth-first order.

# # Do not edit Class
#recursive way 
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
    
#   pass # todo

# def depth_first_values(root):
#     if root is None:
#         return []
#     # Terminal case when reaching bottom of tree
#     elif not root.left and not root.right:
#         return [root.val]
#     # Get current value and continue to append list
#     else:
#         return [root.val] + depth_first_values(root.left) + depth_first_values(root.right)


# # TEST CASE

# # 1.
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')        
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# print(depth_first_values(a,) )# EXPECTED OUTPUT  -> ['a', 'b', 'd', 'e', 'c', 'f']

# # 2. 
# a = Node('a')
# print (depth_first_values(a)) #   -> ['a']








#iterative way

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values (root ) :
#initialize list
 values =[]

#initialize a stack,starting with root
 stack = [root]
# loop thru the stack
 while stack: 
#remove the last node,extract it value and place into list
   current =stack.pop()
   values.append(current.val)
#if right exits,appened right node to the stack 
   if current.right:
     stack.append(current.right)
#if left exits,appened left node to the stack 
   if current.left:
    stack.append(current.left)
 return values


# TEST CASE

# 1.
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(depth_first_values(a) )# EXPECTED OUTPUT  -> ['a', 'b', 'd', 'e', 'c', 'f']

# 2. 
a = Node('a')
print (depth_first_values(a)) #   -> ['a']


####### Dhruv recursive way#############


def dfs_recursive(root):
  # base case: root is None
  if not root:
    return []

  # recursive case: current root has a left or right
  left_values = dfs_recursive(root.left)
  right_values = dfs_recursive(root.right)
  return [root.val, *left_values, *right_values] # JS: ...left_values
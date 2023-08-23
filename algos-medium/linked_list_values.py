
# Linked List Values

# Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
# The function should return a list containing all values of the nodes in the linked list.

# Do not edit Class
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  values =[]
  #create a variable for tracking where i am in the ll
  current  = head
  #iterate thru the entire list 
  while (current is not None ):

  #extract value and place it into my list 
    values.append(current.val)
  #move onto next node
    current =current.next
  #return extracted values.
  return values 
##.............................recursive model......................................





# TEST CASES

# 1.
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
print (linked_list_values(a) )# -> [ 'a', 'b', 'c', 'd' ]

2.
x = Node("x")
y = Node("y")
x.next = y
print (linked_list_values(x)) # -> [ 'x', 'y' ]

3.
q = Node("q")
print (linked_list_values(q)) # -> [ 'q' ]

4.
print(linked_list_values(None)) # -> [ ]

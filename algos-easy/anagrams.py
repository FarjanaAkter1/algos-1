# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.





# def anagrams(s1, s2):
#   return sorted(s1) == sorted(s2)

#another approach 

# def anagrams(s1, s2):
#   if (sorted(s1)==sorted(s2)):
#     print ("the strings are anagrams")
#   else:
#     print("the strings are not anagrams")
#   pass #TODO:

# # TEST CASES
# print (anagrams('restful', 'fluster')) # -> True
# anagrams('cats', 'tocs') # -> False
# anagrams('monkeyswrite', 'newyorktimes') # -> True
# anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# anagrams('pp', 'oo') # -> False





#dhruv solition:

def anagrams (s1, s2):
  if len(s1) != len(s2):
    return False
  

  #intitalize a dict to hold the letters present infirst string

  count ={}
  for char in s1:
    if char not in count:
      count[char] =1
    else:
      count[char] +=1
      #loop thuru secound string and check letter with the dict

  for char in s2:
      if char not in count:
        return False
      else:
          count[char] -= 1
          if count[char]<0:
            return False
  return True
      
print (anagrams('restful', 'fluster')) # -> True
print(anagrams('taxi', 'tax')) # -> False
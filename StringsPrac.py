# 1. Write a Python program to calculate the length of a string.
# str = "Krupanshi is a decent girl."
# print(type(str))
# print(len(str))

#---------------------------------------------------------------------------------------------------------------------------------------------

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# str = "google.com"
# for i in str:
#     dict = {print(f"{i}: ", str.count(i))}

# #---------------------------------------------------------------------------------------------------------------------------------------------  

# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

inputString = "Geeksforgeeks"
count = 0
for i in inputString:
      count = count + 1
      print(count)
newString = inputString[ 0:2 ] + inputString [count - 2: count ]
print(newString)
# str = "Krupanshi"

# if len(str) > 2:
      
'''
    list in python
    c, c++, java - array
    array - single datatype


numbers = [1,2,3]
print(numbers)'''
#       -4    -3    -2    -1
#        0    1     2     3   
#mixed = [1, "abc", 3.14, 'a']

'''print(mixed)
print(mixed[2])'''


'''for i in range(len(mixed)):
    print(mixed[i])'''

'''for name in mixed:
    print(name)'''

'''print(mixed[-1])
print(mixed[-4])'''

# :
'''print(mixed[1:3])
print(mixed[1:])
print(mixed[:])
print(mixed[::-1])'''


# 1. Append function - adds element to the last of the list
#mixed.append(1)
#print(mixed)

# check the end of list - if even element then append 0, if odd element append 1
# [1,2,3,4] - [1,2,3,4,0]
# [1,2,3] - [1,2,3,1]

# list is mutable in nature
'''mixed = [1, "abc", 3.14, 'a']
print(mixed)
mixed[1] = "abcd"
print(mixed)
del mixed[1]
print(mixed)
mixed.remove('a')
print(mixed)'''

'''names = ["abc", "cde", "def", "ghi", "hij", "ghi", 1]
print(names)
# delete - removes element according to the index
del names[1]
print(names)

# remove - removes element according to the value
names.remove("ghi")
print(names)

if 1 in names:
    print("exists")
    print(names.index(1))
else:
    print("does not exists")

# write a program to move all zero digits to the end of the list
# [0, 1, 5, 0, 3] - [1, 5, 3, 0, 0]
# [0, 1, 3, 1, 9] - [1, 3, 1, 9, 0]
# find unique elements from a list
# [0, 1, 1, 3, 0, 2, 3, 4]'''

names = ["abc", "def", "ghi"]
'''popped_element = names.pop(2)
print(popped_element)

numbers = [1, 2, 1, 3, 4, 2]
count = numbers.count(1)
print(count)'''

for i in range(len(names), 0, -1):
    print(names[i])

'''
            AUTHOR:- KRUPANSHI PATEL
            DOC:-16.01.2023
            OBJECTIVE:-TO LEARN ABOUT LIST
'''

#Lists are used to store multiple items in a single variable.

numbers = [1,2,3]
print(numbers)

print("--------------------")

my_list = [1,"abc", 1.2, 3, 3123, "kds", 23]
print(my_list)

print(my_list[-2])

print("--------------------")
for i in range(len(my_list)):
    print(my_list[i])

print("--------------------")
#slicing of list

print(my_list [1:3])#from 1 to 2,
#number after : would be exculsive

print(my_list [2:]) #all the ele from 2
#no num after : makes it till end

print(my_list [:]) #prints all the elemets 
#no num before/after : is for printing every ele

print(my_list [:: -1])
#print's list from the back

print(my_list [:-1])
#print's list except last number

print(my_list [-1:])
#print's last number

#appending into the list
my_list.append(6)
print(my_list)

#chaning the value
my_list[2] = "dps"

#program
for i in range(len(my_list)):
    if my_list[i] == 6:
        my_list[i] = 12

print(my_list)

#sum of the list
Numbers = [1,2,3,4,5]
Sum = 0
for i in range(len(Numbers)):
    Sum += Numbers[i]

print(Sum)

#find the max number
Num = [-4,5,0,9,2]
Max = 0
Index = 0

for i in range (len(Num)):
    if Num[i] > Max:
        Max = Num[i]
        Index = i
        
print(Max)
print(Index)


Num.remove(2)
print(Num)
#removes the element 2

del Num[2]
print(Num)
#delete's from the index

Num.pop()
print(Num)
#removes the last element







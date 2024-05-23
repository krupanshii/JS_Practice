'''
                AUTHOR:-KRUPANSHI PATEL
                DOC:-23/01/2023
                OBJECTIVE:- Write a Python program to get unique values from a list
'''

List = [3,1,2,3,0,8,2,0,0,3]

for x in List:
    count = List.count(x)
    if count == 1:
        print(x)

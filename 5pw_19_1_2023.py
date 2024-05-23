'''
                AUTHOR:-KRUPANSHI PATEL
                DOC:-19/01/2023
                OBJECTIVE:- Write a Python program to remove duplicates from a list
'''

List = [3,1,2,3,0,8]
NewList = []

for i in List:
    if i not in NewList :
        NewList.append(i)

print(NewList)



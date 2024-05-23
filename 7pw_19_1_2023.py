'''
                AUTHOR:-KRUPANSHI PATEL
                DOC:-19/01/2023
                OBJECTIVE:- Write a Python program to move all zero digits to the
                            end of a given list of numbers
'''

List = [3,1,2,3,0,8,2,0,0,3]

if 0 in List:
    for i in range(len(List)):
        List.remove(0)
        List.append(0)
        
print(List)

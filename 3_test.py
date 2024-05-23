'''
                    Author:- Krupanshi Patel
                    Doc:- 2/2/2023
                    Objective:- 3. Write a Python program to remove duplicates
                                from a list. [1, 1, 2, 3, 2] - [1,2,3]
'''

Numbers = [3,1,2,3,2,3,0,8,2,0,0,3]
Num = []

for x in Numbers:
    if x not in Num:
        Num.append(x)

print(Num)

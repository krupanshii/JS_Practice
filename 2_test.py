'''
                    Author:- Krupanshi Patel
                    Doc:- 2/2/2023
                    Objective:- 2. Find the index of unique elements from the list
                                and display those elements

'''

Numbers = [3,1,2,3,2,3,0,8,2,0,0,3]
index = 0

for x in Numbers:
    count = Numbers.count(x)
    index += 1
    if count == 1:
        print("The number is ",x)
        print("The index of " ,x , " is " ,index - 1)

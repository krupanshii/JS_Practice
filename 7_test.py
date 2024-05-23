'''
                    Author:- Krupanshi Patel
                    Doc:- 2/2/2023
                    Objective:- 7. Python program to find second largest number in a list.
'''

Numbers = [0,1,2,3,4,5,6,7,8,9,-1,-2,-3,-3,-4]
MAX1 = 0
MAX2 = 0

for x in Numbers:
    if MAX1 < x:
        MAX2 = MAX1
        MAX1 = x
        
print("The second largest number is ", MAX2)

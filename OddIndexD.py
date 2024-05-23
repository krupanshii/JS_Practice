'''
                AUTHOR:-KRUPANSHI PATEL
                DOC:-19/01/2023
                OBJECTIVE:- Use a loop to display elements from a given list
                            present at odd index positions.
'''

NUMBERS = [ 1,2,3,4,5,6,7,8,9,10]

for i in range (len(NUMBERS)):
    if i % 2 != 0:
        print(NUMBERS[i])


'''
                Author:- Krupanshi Patel
                DOC:-12/01/2023
                Objective:-to find th factorial of given number.
'''

number = int(input("Enter the number: "))

fact = 1
 
for i in range(1, number+1):
    fact = fact * i
 
print("The factorial of the number is ", fact)

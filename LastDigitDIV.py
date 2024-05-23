'''
                    Author:-Krupanshi Patel
                    DOC:-11/01/2023
                    Objective:- to check whether the last digit of a nuber enterd
                                is divisible by 3 or not.
'''

number = int(input("Enter the number: "))

Last_digit = number % 10

if Last_digit % 3 == 0:
    print("The last digit of enterd number is divisible by 3.")
else:
    print("The last digit of enterd number isn't divisible by 3.")

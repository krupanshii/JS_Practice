'''
                    Author:- Krupanshi Patel
                    Doc:- 2/2/2023
                    Objective:- 6. Write a Python function to calculate the factorial
                                    of a number (a non-negative integer).
                                    The function accepts the number as an argument.
'''
def FACTORIAL(Number):
    Fact = 1

    for i in range(1,Number+1):
        Fact = Fact * i

    print("The factorial of ", Number ," is " , Fact)

Number = int(input("Enter the number: "))
FACTORIAL(Number)

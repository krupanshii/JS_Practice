'''
                    Author:- Krupanshi Patel
                    Doc:- 2/2/2023
                    Objective:- 5. Write a Python function that checks whether a passed
                                   string is palindrome or not.

'''
def PALINDROME(String):
    if String == String[::-1]:
        print("The string is palindrome")
    else:
        print("The string isn't palindrome")

String = input("Enter the string: ")
PALINDROME(String)




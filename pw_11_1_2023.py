'''
                Author:- Krupanshi Patel
                DOC:-11/01/2023
                Objective:-to find whether the year is leap year or not.
'''

year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 != 0:
        print("It is a leap year.")
    else:
        print("It isn't a leap year.")
elif year % 400 == 0:
    print("It is a leap year.")
else:
    print("It isn't a leap year.")

print("Thank you.")

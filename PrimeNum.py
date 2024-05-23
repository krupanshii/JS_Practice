'''
                Author:- Krupanshi Patel
                DOC:-12/01/2023
                Objective:-to determine whether a number is prime or not.
'''

number = int(input("Enter the number: "))
count = 0

for i in range(2, number):
    if number % i == 0:
        count += 1
        
if count >= 2 or number == 1:
    print("The number enter is not prime.")
else:
    print("The number enter is prime.")

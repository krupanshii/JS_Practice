
print ("name")

name = "abc"
print(name)

#concat
print("my name is", name)

#by user
number = input("enter any number = ")
print(number)

#number default
number1 = input("enter the number1: ")
print(number1)
print(type(number1))

#number in int
number2 = int(input("enter the number1: "))
print(number2)
print(type(number2))

#number in float
number3 = float(input("enter the number1: "))
print(number3)
print(type(number3))

#if else
number = int(input("Enter the number: "))
if number>10:
    print("number is greater than 10")
    print("inside the if statement")
else:
    print("number is less than 10")
    print("inside the else statement")

print("outside")

#odd/even
number = int(input("enter the number: "))
if ((number % 2) == 0):
    print("The number is even")
else:
    print("The number is odd")

#+/-
number = int(input("Enter the number:"))
if number > 0:
    print("Positive number")
elif number == 0:
    print("It's zero")
else:
    print("Negative number")

#if else if
marks = int(input("Enter the marks:"))
if marks > 90:
    print("A Grade")
elif marks > 80 and marks <= 90:
    print("B Grade")
elif marks >=60 and marks <= 80:
    print("C Grade")
else:
    print("D grade")

print("Congratulations for your grade")

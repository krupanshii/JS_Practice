
#for loop
for i in range (10):
    print(i)

#i = 0
#initialize - 0
#condition < 10
#increment - +1

#argument sequence
(intialize, condition, increment)

for i in range (1, 10):
    print(i)

for i in range (1,10,2):
    print(i)

#even_no - first 10 multiples
#odd_no - first 20 multiples
number = int(input("Enter the number: "))

if number % 2 == 0: 
    for i in range(1, 11):
        print(number * i)
else:
    for i in range(1, 21):
        print(number * i)

#sum in sequence
number = int(input("Enter the number: "))
sum = 0

for i in range(1,number+1):
    sum = sum + i
print(sum)

#for loop in array-
fruits = ["a","b","c"]
for fruit in fruits:
    print(fruit)

#while loop
i = 1
while i < 10:
    print(i)
    i +=1

#even_no - first 10 multiples
#odd_no - first 20 multiples
number = int(input("Enter the number: "))
if number % 2 ==0:
    i = 1
    while i < 11:
        print(number * i)
        i +=1
else:
    i = 1
    while i < 21:
        print(number * i)
        i += 1

#continue, break
for i in range(10):
    if i % 2 == 0:
        print("hi")
        continue
    elif i == 5:
        break
    else:
        print(i)

#prime numbers between 30 and 70

for number in range(30 ,71, 1):
    if number > 1:
        for i in range(2, number):
            if (number % i == 0):
                break
        else:
            print(number)
 
        



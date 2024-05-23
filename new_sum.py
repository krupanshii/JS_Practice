x = int(input("Enter a number: "))
n = int(input("Enter the digit you want to add upto: "))

Num = 0
Sum = 0

for i in range(0,n):
    Num += x *pow(10, i)
    Sum += Num
     
print(Num)
print(Sum)
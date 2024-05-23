n1 = 0
n2 = 1
Num = 0
Count= 0 

Terms = int(input("Enter the number of terms you want to print"))

if Terms <= 0:
    print("No of terms can't be negative.")
elif Terms == 1:
    print(n1)
else:
    while(Count < Terms):
        print(n1)
        Num = n1 + n2
        n1 = n2
        n2 = Num

        Count +=1


    
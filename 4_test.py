'''
                    Author:- Krupanshi Patel
                    Doc:- 2/2/2023
                    Objective:- 4. Write a program to calculate the sum of series up
                                to n term. For example, if n =5 the series will become
                                3 + 33 + 333 + 3333 + 33333 
'''

Number = int(input("Enter the number: "))
Terms = int(input("Enter the number of terms: "))

Total = 0
Num = 0

for i in range(0,Terms):
    Num += Number * pow(10,i)
    Total += Num
 
print(Total)

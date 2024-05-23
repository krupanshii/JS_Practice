'''
                    Author:- Krupanshi Patel
                    DOC:-12/01/2023
                    Objective:- to calculate the sum of series up to n term.
                                For example, if n =5 the series will
                                become 2 + 22 + 222 + 2222 + 22222 = 24690
                                

'''
number = int(input("Enter the number: "))
Terms = int(input("Enter the terms: "))

Num = 0
Total = 0

for i in range(0,Terms):
    Num += (number * pow(10,i))
    Total += Num
    
print(Total)

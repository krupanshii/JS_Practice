'''
                Author:- Krupanshi Patel
                DOC:-12/01/2023
                Objective:-to print fibonacci series.
'''

Terms = int(input("Enter the number of terms: "))

n1 = 0
n2 = 1
count = 0

if Terms <= 0:
   print("Invalid choice")
elif Terms == 1:
   print("Fibonacci sequence for 1 term: ")
   print(n1)
else:
   print("Fibonacci series:")
   while count < Terms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

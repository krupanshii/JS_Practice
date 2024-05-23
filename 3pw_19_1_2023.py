'''
                AUTHOR:-KRUPANSHI PATEL
                DOC:-19/01/2023
                OBJECTIVE:- Display the Fibonacci series up to 10 terms
'''

Terms = int(input("Enter the number of terms: "))
n1 = 0
n2 = 1

if Terms < 0:
    print("Invalid terms")
elif Terms == 1:
    print(n1)
else:
    for x in range(1,Terms+1):
        print (n1)
        N = n1 + n2
        n1 = n2
        n2 = N
    

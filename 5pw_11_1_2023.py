'''
                    Author:- Krupanshi Patel
                    DOC:-11/01/2023
                    Objective:-to accept the cost price of a bike and display the
                               road tax to be paid according to the following criteria:
                               Cost price (in Rs)                 Tax    

                                > 100000                           15%
                                > 50000 and <= 100000              10%
                                <= 50000                            5%
'''

Cost = int(input("Enter the cost price of the bike: "))

if Cost > 100000:
    print("You've to pay 15% tax.")
elif Cost > 50000 and Cost <= 100000:
    print("You've to pay 10% tax.")
elif Cost <= 50000:
    print("You've to pay 5% tax.")

print("Thank You.")


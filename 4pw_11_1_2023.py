'''
                    Author:- Krupanshi Patel
                    DOC:-11/01/2023
                    Objective:- to calculate the electricity bill according
                                to the following criteria:
                                
                                Unit First 100 units           no charge
                                Next 100 units                 Rs 5 per unit
                                After 200 units Price          Rs 10 per unit

                                For example if input unit is 350 than total bill
                                amount is Rs2000.
                                

'''

Units = int(input("Enter the units used: "))

A = Units - 100
B = Units - 200

Cost  = 0
Cost1 = 0
Cost2 = 0

if Units <= 100:
    print("Your bill has no charges.")

if 100 < Units <= 200:
    Cost = (Units - 100)*5
    
if Units >= 200:
    Cost1 = 100 * 5
    
if 200 < Units:
    Cost2 = (B * 10)
    
Amount = Cost + Cost1 + Cost2

print("Your bill has amount of Rs.", Amount)
    

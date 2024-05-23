class Royal:
   __BankAmount = 10000   
   _Accountant = 4   
   years = 15   
   wifi_pw = "1234"   
   
   def __init__(self, name, fees):
        self.name = name
        self.fee = fees
        print("Constructor has been called") 

   def edit_fee(self, new_fees):
        self.fee = new_fees

   def dis_details(sf):
        print(sf.name,'---->',sf.fee)


   def edit_pw(cls):    
        cls.wifi_pw = "4321"
        print('Password has been Changed')

   def show_years():
        print("This is method for showing years")

K = Royal("Krupanshi" , 10000)
R = Royal("Rudra" , 20000)


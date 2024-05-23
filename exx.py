class Royal:
    __Bank_Ac_money = 1000000000   # Private
    _Accountant = 4   # Protected
    total_years = 15   # public
    wifi_password = "1234"   # class Variable

    def __init__(self, name, fees):
        self.name = name
        self.fee = fees
        print("Constructor Called")

    def edit_fee(self, new_fees):
        # self.fee = int(input())
        self.fee = new_fees

    def display_details(sf):
        print(sf.name,'---->',sf.fee)

    @classmethod
    def edit_password(cls):    # class Method
        cls.wifi_password = "Manoj"
        print('Password Changed')

    @staticmethod
    def show_years():   # For faster Use
        print("This is Show_years static Method")


arin = Royal("Arin", 1000)
nupur = Royal("Nupur", 2000)

# arin.edit_fee(int(input()))
arin.edit_fee(500)
arin.display_details()
nupur.display_details()


nupur.edit_password()   # object called Class Method
# Royal.edit_password()   # object called Class Method
print(Royal.wifi_password)
Royal.show_years()
# print(arin.Accountant)  # Error
print(arin._Accountant)  # 4
# print(arin.__Bank_Ac_money)   # Error
print(arin._Royal__Bank_Ac_money) 
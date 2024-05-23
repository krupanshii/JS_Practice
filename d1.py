def wish():
    my_wish = True
    ans = ""

    while my_wish:
        print("Enter today's date in date/month")
        ans = input()

        if ans == "3/12":
            print("Oh, my heart leaps with joy cause It's your birthday")
            print("Happy Birthday!!!")
            print("I love you ❤")
            break
        
        else:
            print("Not a special day but I love you ❤")

wish()

print("So lemme ask you a question Okayy")

def propose():
    my_heart = True
    ans = ""

    while my_heart:
        print("Hey love, will you be mine?")
        ans = input("Enter 'yes' or 'no': ")

        if ans == "yes":
            print("My big flat smile appears and I love you❤")
            break
        elif ans == "no":
            print("Hey love, will you be mine?")
            ans = input("Enter 'yes' or 'no': ")
            if ans == "yes":
                print("My big flat smile appears and I love you❤")
                break
       
propose()
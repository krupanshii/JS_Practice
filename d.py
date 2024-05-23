def propose():
    my_heart = True
    your_response = ""

    while my_heart:
        print("My love, will you be mine?")
        your_response = input("Enter 'yes' or 'no': ")

        if your_response == "yes":
            print("Oh, my heart leaps with joy!")
            break
        elif your_response == "no":
            print("My love, will you be mine?")
            your_response = input("Enter 'yes' or 'no': ")
            if your_response == "yes":
                print("Oh, my heart leaps with joy!")
       
propose()
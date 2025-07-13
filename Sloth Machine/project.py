def deposit():
    while True:
        amount = input("What would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount == 0:
                print("Amount should be greater then 0")
            else:
                break
        else:
            try:
                if int(amount) < 0:
                    print("Type a number greater then 0")

            except:
                print("Type in a number")



    return amount


deposit()
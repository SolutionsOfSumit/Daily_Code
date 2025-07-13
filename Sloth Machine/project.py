MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit?  ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a deposit amount greater then 0")

        else:
            print("Type a valid number to deposit")

    return amount 

def get_lines():
    while True:
        amount = input("how many lines would you like to bet on?  ")
        if amount.isdigit():
            amount = int(amount)
            if amount <= MAX_LINE:
                break
            else:
                print("Enter a valid number of Lines")

        else:
            print("Type a valid NUMBER of lines")

    return amount 

def get_bet():
    while True:
        amount = input("How many bets would you like to play?  ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print("Enter a amount greater then 0")

        else:
            print("Type a valid number")

    return amount 

def main():
    balance = deposit()
    lines = get_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting {bet} on {lines} lines. Total bet is equals to: {total_bet}")

main()
    


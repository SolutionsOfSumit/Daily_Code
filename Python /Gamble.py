import random



MAX_LINES  = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 4,
    "D": 2
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def  print_sloth_machine(columns):
    for row in range(len(columns[0])): #if you are confused of columns[0] index zero, so here it is indicating the length column which is a row so it is just getting the number of that column which is just a line insted of columns which is a matirx
        for i, column in enumerate(columns): #What enumerate does it gives us the index as well as the item 
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")

        print()

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

def get_number_lines():
    while True:
        amount = input(f"Enter the number of Lines to bet on? (1-{str(MAX_LINES)}) ")
        if amount.isdigit():
            amount = int(amount)
            if 1<= amount <= MAX_LINES:
                break
        else:
            try:
                if int(amount) < 0:
                    print("The lines should me more then 0")

            except:
                print("Enter a valid number of lines")

    return amount

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be less then {MAX_BET}")
        else:
            try:
                if int(amount) < 0:
                    print("Type a number greater then 0")

            except:
                print("Type in a number")
    
    return amount

def check_machine(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break 

        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)

    return winnings, winning_line 






def spin(balance):
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough amount to bet, Please reduce the betting amount on each line")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_sloth_machine(slots)
    winnings, Winning_lines = check_machine(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *Winning_lines) #*Winning_lines

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press ENTER to spin.(q to quit)")
        if ans.lower() == "q":
            break 
        balance += spin(balance)

    print(f"You left with ${balance}")



main()
    
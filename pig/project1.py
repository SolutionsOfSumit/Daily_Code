import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
while True:

    players = input("Numbers of players (1-4):  ")
    if players.isdigit():
        players = int(players)
        if 1 <= players >= 4:
            break
    
    else:
        print("Type in numbers only")

print(players)
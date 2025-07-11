import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2 to 4 ):  ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players are either too small or too much type in the numebr of players as specified")

    else:
        print("invalid input try again in numbers")
max_score = 58
players_scores =[0 for _ in range(players)] #this will put 0 for every player which we entered in as number of players

print(players_scores) 

while max(players_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started")
        print("Your total score is:", players_scores[player_idx],"\n")

        current_score = 0

        while True:

            should_roll = input("would you like to roll (y)?:  ")
            if should_roll.lower() != "y":
                break



            value = roll()



            if value == 1:
                print("You rolled a 1! Turn Done!")
                current_score = 0
                break

            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        players_scores[player_idx] += current_score
        print("Your total Score is:", players_scores[player_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx +1,"is the winner with the score of:", max_score)
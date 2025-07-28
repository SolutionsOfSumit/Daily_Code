import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"] #This is a list and

while True:
    user_input = input("Type in Rock/Paper/Scisors or Q to quit").lower()
    if user_input == 'q':
        break

    if user_input not in options :  #"in" checks that the given argument is in the list or not. and typing "not" in front of in wiil jsut reverse the arguminet as the not gate
        continue 

    random_nuber = random.randit(0, 2)
    computer_pick = options[random_nuber] #here [number] means the element of that number in the list. and the indexing of the list starts from number 0 an in reverse it starts form -1.

    print("computer picked", computer_pick +'.') 

    if user_input == "rock" and computer_pick == "scissors":
        print("You win")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1
print("You won", user_wins, 'times.')
print("The computer won", computer_wins, "times.")
print("Good Bye")
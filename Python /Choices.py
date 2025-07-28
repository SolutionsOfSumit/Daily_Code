#Intrection 
def Q(Question, Answer):
    ans = input(Question,"type your answer")
    if ans == Answer:
        points += 1
        print(f"Now I can spear your life for {str(points)} years")
    
    else:
        print("Wrong answer")
    return points  


name = input("Wwhats you name Participent\n YOU>>")

while True:

    choice = input(f"Lets play a game,choice {name}(y/n)>>")
    
    if choice.lower() == "y":
        print(f"Great Choice, {name}\n \n")
        break

    elif choice.lower() == "n":
        print(f"You have no choice {name}\n \n ")
        break 

    else:
        print(f"I wonder if you are blind then how are you typing \n \n")
        continue

print("Lets play the game of your life")

points = 0
questions =0

print(Q("What are your intensions", "u"))

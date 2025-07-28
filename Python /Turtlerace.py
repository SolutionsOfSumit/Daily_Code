import turtle
import time

WIDTH, HEIGHT = 500, 500


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers:  ")
        if racers.isdigit():
            racers = int(racers)
            if 2<= racers <= 10:
                return racers
            else:
                print("Racers should be between 2 to 10")
        else:
            try:
                if racers > 0:
                    print("The number should be more then zero")
            except:
                print("Enter NUMBERS only.")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
print(racers)
init_turtle() 
racer = turtle.Turtle()
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.left(90)
racer.forward(100)

time.sleep(5)
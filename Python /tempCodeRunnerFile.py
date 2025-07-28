if range.isdigit():
    range = int(range)

    if range < 0:
        print("Please type a number larger than 0 next time")
        quit()

else:
    print("Please type a number next time")
    quit()


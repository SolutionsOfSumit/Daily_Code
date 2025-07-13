import random
import time

OPERATIONS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

total_problems = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATIONS)

    expr = str(left) +" "+operator+" " +str(right) 
    answer = eval(expr) #here what eval will do is that it will evaluate the given expression.

    print(expr)
    return expr, answer

wrong = 0
input("Press any key to start")
print

start_time = time.time()

("---------------------------------------------------------------------------------")

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr)
        if guess == str(answer):
            break 
end_time = time.time()
total_time = end_time - start_time

print("---------------------------------------------------------------------------------")
print("Nice work! you finished in ", total_time, "seconds")

 
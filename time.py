import random#mports the random module, which provides functions for generating random numbers and making random choices.
import time # imports the time module, which provides functions for working with time-related operations.

OPERATORS = ["+", "-", "*"]#defines a list named OPERATORS that contains three arithmetic operators: addition (+), subtraction (-), and multiplication (*). These operators will be used to generate random arithmetic problems.
MIN_OPERAND = 3#defines a variable named MIN_OPERAND and assigns it the value 3. This variable represents the minimum value that an operand (number) in the arithmetic problem can have.
MAX_OPERAND = 12#defines a variable named MAX_OPERAND and assigns it the value 12. This variable represents the maximum value that an operand (number) in the arithmetic problem can have.
TOTAL_PROBLEMS = 10#    


def generate_problem():# defines a function named generate_problem().The function is responsible for generating a random arithmetic problem.
    left = random.randint(MIN_OPERAND, MAX_OPERAND)#generates a random integer between MIN_OPERAND and MAX_OPERAND and assigns it to the variable left. This will be the left operand of the arithmetic problem.
    right = random.randint(MIN_OPERAND, MAX_OPERAND)#generates a random integer between MIN_OPERAND and MAX_OPERAND and assigns it to the variable right. This will be the right operand of the arithmetic problem.
    operator = random.choice(OPERATORS)#Randomly selects an operator from the OPERATORS list and assigns it to the variable operator. This will determine the type of arithmetic operation to be performed.

    expr = str(left) + " " + operator + " " + str(right)#creates a string expression that represents the arithmetic problem. It combines the left operand, operator, and right operand using string concatenation.
    answer = eval(expr)#evaluates the string expression expr as a Python expression and assigns the result to the variable answer. The eval() function interprets the expression and returns the computed value.
    return expr, answer#returns a tuple containing the arithmetic problem expression (expr) and its corresponding answer (answer) as the output of the generate_problem() function.

wrong = 0# uses a variable named wrong and assigns it the value 0. This variable will keep track of the number of incorrect guesses made by the user.
input("Press enter to start!")#prompts the user to press the enter key to start the arithmetic problem-solving process.
print("----------------------")#prints a line of dashes to visually separate the start of the problem-solving process.

start_time = time.time()#line records the current time as the starting point of the problem-solving process. The time.time() function returns the current time in seconds

for i in range(TOTAL_PROBLEMS):#line starts a loop that will iterate TOTAL_PROBLEMS number of times. The loop variable i will take on values from 0 to TOTAL_PROBLEMS - 1
    expr, answer = generate_problem()#line calls the generate_problem() function and assigns the returned tuple (containing the arithmetic problem expression and answer) to the variables expr and answer.
    while True:#line starts an infinite loop. The code inside this loop will keep executing until a break statement is encountered.
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")# line prompts the user to enter their guess for the arithmetic problem. The prompt includes the problem number (i + 1), the problem expression (expr), and an equal sign. The user's input is stored in the variable guess.
        if guess == str(answer):#line checks if the user's guess (guess) is equal to the string representation of the correct answer (answer). The str() function is used to convert the answer to a string for comparison.
            break#the user's guess is correct, this line breaks out of the innermost loop (the while loop) and continues with the next iteration of the outer loop.
        wrong += 1#he user's guess is incorrect, this line increments the wrong variable by 1, indicating that the user made a wrong guess.

end_time = time.time()#line records the current time as the end point of the problem-solving process.
total_time = round(end_time - start_time, 2)# calculates the total time taken to solve the problems by subtracting the start time from the end time. The result is rounded to 2 decimal places and assigned to the variable total_time.

print("----------------------")# prints a line of dashes to visually separate the end of the problem-solving process.
print("Nice work! You finished in", total_time, "seconds!")#prints a congratulatory message along with the total time taken to solve the problems. The total_time variable is automatically converted to a string and concatenated with the other parts of the message.

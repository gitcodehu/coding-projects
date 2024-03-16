print("Welcome to my computer quiz!")#prints the message "Welcome to my computer quiz!" to the console. It serves as a greeting to the user.

playing = input("Do you want to play? ")#prompts the user with the question "Do you want to play?" and waits for the user's input. The user's response is stored in the variable playing.

if playing.lower() != "yes":#checks if the user's response is not equal to the string "yes". The .lower() method is used to convert the user's response to lowercase, ensuring that it is case-insensitive.
    quit()# If the user's response is not "yes", this line terminates the program. 

print("Okay! Let's play :)")#If the user's response is "yes", this line prints the message "Okay! Let's play :)" to the console. It serves as a confirmation that the quiz will begin.
score = 0#uses a variable named score with a value of 0. This variable will keep track of the user's score in the quiz.

answer = input("What does CPU stand for? ")#prompts the user with the question "What does CPU stand for?" and waits for the user's input. The user's response is stored in the variable answer.
if answer.lower() == "central processing unit":#checks if the user's response is equal to the string "central processing unit". The .lower() method is used to convert the user's response to lowercase, ensuring that the comparison is case-insensitive.
    print('Correct!')#the user's response is "central processing unit", this line prints the message "Correct!" to the console. It indicates that the user's answer was correct.
    score += 1#If the user's response is "central processing unit", this line increments the value of the score variable by 1. It adds a point to the user's score.
else:#If the user's response is not "central processing unit", this line marks the beginning of the code block that will execute if the condition in the previous if statement is not met.
    print("Incorrect!")#If the user's response is not "central processing unit", this line prints the message "Incorrect!" to the console. It indicates that the user's answer was incorrect.

answer = input("What does GPU stand for? ")#prompts the user with the question "What does GPU stand for?" and waits for the user's input. The user's response is stored in the variable answer.
if answer.lower() == "graphics processing unit":#checks if the user's response is equal to the string "graphics processing unit". The .lower() method is used to convert the user's response to lowercase, ensuring that the comparison is case-insensitive 
    print('Correct!')#the user's response is "graphics processing unit", this line prints the message "Correct!" to the console. It indicates that the user's answer was correct.
    score += 1#If the user's response is "graphics processing unit", this line increments the value of the score variable by 1. It adds a point to the user's score.
else:#If the user's response is not "graphics processing unit", this line marks the beginning of the code block that will execute if the condition in the previous if statement is not met.
    print("Incorrect!")#If the user's response is not "graphics processing unit", this line prints the message "Incorrect!" to the console. It indicates that the user's answer was incorrect.

answer = input("What does RAM stand for? ")#prompts the user with the question "What does RAM stand for?" and waits for the user's input. The user's response is stored in the variable answer.
if answer.lower() == "random access memory":#checks if the user's response is equal to the string "random access memory". The .lower() method is used to convert the user's response to lowercase, ensuring that the comparison is case-insensitive
    print('Correct!')#the user's response is "random access memory", this line prints the message "Correct!" to the console. It indicates that the user's answer was correct.
    score += 1#If the user's response is "random access memory", this line increments the value of the score variable by 1. It adds a point to the user's score.
else:#If the user's response is not "random access memory", this line marks the beginning of the code block that will execute if the condition in the previous if statement is not met.
    print("Incorrect!")#If the user's response is not "random access memory", this line prints the message "Incorrect!" to the console. It indicates that the user's answer was incorrect.

answer = input("What does PSU stand for? ")#prompts the user with the question "What does PSU stand for? " and waits for the user's input. The user's response is stored in the variable answer.
if answer.lower() == "power supply":#checks if the user's response is equal to the string "random access memory". The .lower() method is used to convert the user's response to lowercase, ensuring that the comparison is case-insensitive
    print('Correct!')##the user's response is "power supply", this line prints the message "Correct!" to the console. It indicates that the user's answer was correct.
    score += 1#If the user's response is "power supply, this line increments the value of the score variable by 1. It adds a point to the user's score.
else:##If the user's response is not "power supply", this line marks the beginning of the code block that will execute if the condition in the previous if statement is not met.
    print("Incorrect!")#If the user's response is not "power supply", this line prints the message "Incorrect!" to the console. It indicates that the user's answer was incorrect.

print("You got " + str(score) + " questions correct!")# prints a message to the console that includes the user's score. It uses string concatenation to combine the strings "You got ", the value of the score variable (converted to a string using str()), and the string " questions correct!".
print("You got " + str((score / 4) * 100) + "%.")#calculates the percentage of questions the user answered correctly and prints it to the console. It uses the formula (score / 4) * 100 to calculate the percentage. The value is then converted to a string using str() and combined with the strings "You got " and "%." using string concatenation.
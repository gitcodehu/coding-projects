import random # Import the random module to generate random numbers.


def roll():
    # Define a function 'roll' that simulates a dice roll.
  min_value=1
  max_value = 6
  roll = random.randint(min_value,max_value)# Generate a random number between 1 and 6.

  return roll #Return the result of the dice roll.

while True:
  players = input("Enter the number of players (2-4): ")# Request user for the number players
  if players.isdigit():# checks whether the value stored in the varabile players is a number
    players = int(players) #coverts the input stored in variable players from string to a integer
    if 2 <= players <=4:# if the value stored in the variable players is between 2 and 4 the condition is true .If players is less than 2 or greater than 4,the condition is flase,and the code will be skipped
      break #Exit the loop if a valid number of player is provided
    else:
        print("Must be between 2 - 4 players.")# if condition above is not turn then this output will be executed
    
  else: 
      print("invalid,try again")# Display an error message for invalid input

max_score = 50
player_scores = [0 for _ in range(players)] #Set initial scores to zero for each player 

while max(player_scores) < max_score:#Enter a loop that continues untill the maxium score is reached or exceeded by any player 
  for player_idx in range(players):# the loop will be executed for each player where player_idx is a variable that represents the current player's index
      print("\nPlayer number", player_idx + 1, "turn has just started!\n")#prints message indicating that its the start of the current player's turn.The player_idx + 1 is used to display a player number starting form 1 instead of 0. 
      print("Your total score is:", player_scores[player_idx], "\n")# this prints the total score of the current player, using the paler_idx to access the score in the player_scores list
      current_score = 0# the current score for the current player's turn. 

      while True:
          should_roll = input("Would you like to roll (y)? ")# this line asks the player to roll the dice
          if should_roll.lower() != "y":# it checks if the lowercase version of the variable should_roll is not equal to the string y. indicating the user did not input y when asked
             break#Exit the inner loop if the player chooses not to roll 

          value = roll()#roll the dice
          if value == 1:#checks if the variable value is equal to 1 
            print("You rolled a 1! Turn done!")# tell the user they have rolled a 1
            current_score = 0 #sets current score to 0, showing that the player's turn is over due to rolling a 1.
            break#End the turn if a 1 is rolled
          else:
            current_score += value#This line increases the value of current_score by the value of value.
            print("You rolled a:", value)# This line will print the message. "You rolled a:", followed by the value of value.
             
            print("Your score is:", current_score)#This line displays the message "Your score is:", followed by the value of current_score.
              
      player_scores[player_idx] += current_score#Adds the current_score to the player's score at index player_idx.
      print("Your total score is:", player_scores[player_idx])#prints the updated overall score of the player at index.
max_score = max(player_scores)#gets the highest score among all players.
winning_idx = player_scores.index(max_score)#Finds out the index of the player with the highest score.
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)#Prints the winner's index and score.
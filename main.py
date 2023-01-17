#Create a Rock, Paper, Scissors game
## Requirements
import random

Rock = "Rock"
Paper = "Paper"
Scissor = "Scissor"

boolean=True
while boolean:

  user_input = input("Enter a choice (Rock, Paper, Scissor): ").lower()
  print("You chose:" + user_input)

  choice = ["Rock", "Paper", "Scissor"]
  computer = random.choices(choice)
  print([user_input], "vs", [computer])

  if user_input == computer:
    print("Both Players Selected ([user_input]). It's a tie")
  
  
  
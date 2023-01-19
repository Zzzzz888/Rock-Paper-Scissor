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

  
  
  boolean=False
 
  
  
  choice = ["Rock", "Paper", "Scissor"]
  outcome=random.choice(choice)
  computer = random.choices(choice)
  print(user_input, "vs", outcome)

  
  
  if user_input == computer:
    print("I mean its a unwanted result but it could be worse:)")

  elif user_input>computer:
    print("YOU ARE VICTORIUS! YOU WILL HAVE ALL THE FULLIMENT IN LIFE THAT YOU DESERVE")
  elif user_input<computer:
    print("YOU TAKE Ls! YOU WILL NEVER GET RID OF YOUR FAILMENT HERE")
      
    
    
  

  
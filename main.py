#Create a Rock, Paper, Scissors game
## Requirements
import random

Rock = "rock"
Paper = "paper"
Scissor = "scissor"

boolean=True
while boolean:

  user_input = input("Enter a choice (Rock, Paper, Scissor): ").lower()
  print("You chose:" + user_input)

  
  
  boolean=False
 
  
  
  choice = ["Rock", "Paper", "Scissor"]
  outcome=random.choice(choice).lower()
  
  print(user_input, "vs", outcome)

  
  
  if user_input == outcome:
      print("I mean its a unwanted result but it could be worse:)")
  
  elif user_input == Rock and outcome == Scissor:
      print("\nYOU ARE VICTORIUS! YOU WILL HAVE ALL THE FULLIMENT IN LIFE THAT YOU DESERVE WITH THE EMPOWERMENT YOU'VE GAINED")
      
  elif user_input == Paper and outcome == Scissor:
      print("\nYOU TAKE Ls! YOU WILL NEVER GET RID OF YOUR FAILMENT HERE")
     
  elif user_input == Scissor and outcome == Paper:
      print("\nYOU ARE VICTORIUS! YOU WILL HAVE ALL THE FULLIMENT IN LIFE THAT YOU DESERVE WITH THE EMPOWERMENT YOU'VE GAINED")
     
  elif user_input == Paper and outcome == Rock:
      print("\nYOU ARE VICTORIUS! YOU WILL HAVE ALL THE FULLIMENT IN LIFE THAT YOU DESERVE WITH THE EMPOWERMENT YOU'VE GAINED")
      
  elif user_input == Rock and outcome == Paper:
      print("\nYOU TAKE Ls! YOU WILL NEVER GET RID OF YOUR FAILMENT HERE")
    
  elif user_input == Scissor and outcome == Rock:
      print("\nYOU TAKE Ls! YOU WILL NEVER GET RID OF YOUR FAILMENT HERE")
    
      
    
  

  
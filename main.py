import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Choose rock, paper, or scissors: \n")

print("player choice is: " + player)
print("Computer choice is: " + computer)

# Who wins
if player == computer:
  print("the game is a TIE!!")
else:
  if player == "rock":
    if computer == "paper":
      print("computer WON!")
    else:
      print("player WON!")
  elif player == "paper":
    if computer == "scissors":
      print("computer WON!")
    else:
      print("player WON")
  else: # scissors
    if computer == "rock":
      print("computer WON!")
    else:
      print("player WON")





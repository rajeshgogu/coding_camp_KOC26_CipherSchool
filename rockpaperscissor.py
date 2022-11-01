import random

user_input = input("Enter the choice : (rock, paper, scissor)")
possible_actions = ["rock","paper","scissor"]
computer_action = random.choice(possible_actions) 

#print user action and computer action 

if user_input  == computer_action:
    print("tie")
elif user_input  == "rock":
    if computer_action == "paper":
        print("computer wins")
    else:
      print("user wins") 
      
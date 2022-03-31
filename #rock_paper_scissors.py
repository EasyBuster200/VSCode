#rock_paper_scissors

import random 

user_score = 0
computer_score = 0
while True:
    user_action = input("Enter your choice (rock, paper, scissors): ")

    options = ["rock", "paper", "scissors"]
    computer_action = random.choice(options)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print (f"Both palyers chose {user_action}, its a draw") 

    elif user_action == "rock":
        if computer_action == "scissors": 
            print ("Rock smashes scissors, you win")
            user_score += 1
        else:
            print ("Paper covers rock, you lose")
            computer_score += 1

    elif user_action == "paper":
        if computer_action == "scissors": 
            print ("Scissors cuts paper, you lose")
            computer_score += 1
        else:
            print ("Paper covers rock, you win")
            user_score += 1

    elif user_action == "scissors":
        if computer_action == "rock": 
            print ("Rock smashes scissors, you lose")
            computer_score += 1
        else:
            print ("Scissors cut paper, you win")
            user_score += 1

    play_again = input ("Do you want to play again (Y/N): ")
    if play_again.lower() != "y":
        print ("")
        print (f"Your score is {user_score} and the computers score is {computer_score}")
        
        if user_score == computer_score:
            print ("Its a tie")

        elif user_score > computer_score:
            print ("You won, good job")

        else:
            print ("You lost, better luck next time")

        break

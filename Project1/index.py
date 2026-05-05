

# i am gonna build a game rock paper scissors 

# the cases are 
# rock beats scissors 
# scissors beat paper
# paper beats rock 


# two person will be playing , one is the user and the other is the computer 

# first version of code (basic )//////////////////////

# def play_game():
#     import random 

#     computer_input=random.randint(1 ,3)

#     computer= ""
#     if computer_input==1:
#         computer="rock"
#     elif computer_input==2:
#         computer="paper"
#     else:
#         computer="scissors"

#     # instead that you can also choose among the list of strings like that 
#     # computer=random.choice(["rock " , "paper" , "scissors"])

#     user=input("Enter one of the following rock/paper/scissors :")
#     if user==computer:
#         print("Its a tie!")
#     elif user=="rock" and computer=="scissors":
#         print("You won , rock beats scissors")
#     elif user=="rock" and computer=="paper":
#         print("YOu lost! as paper beats rock ")
#     elif user=="scissors" and computer=="rock":
#         print("Computer Won! as scissor is beaten by rock ")
#     elif user=="scissors" and computer=="paper":
#         print("You Won! as scissor beats paper ")
    
#     elif user=="paper" and computer=="scissors":
#         print("You won as paper beats scissors  ")
    
#     elif user=="paper" and computer=="rock":
#         print("You won  Won! as paper beats rock  ")
    
    
# play_game()



# now here my program is working fine but i should  refactor the code , by making the improvements 


# a little better version is here//////////////////////////////////
# random can also choose among the list of choices given 

# import random

# choices = ["rock", "paper", "scissors"]

# user = input("Enter rock, paper, or scissors: ").lower()

# # choose from the choice list 
# computer = random.choice(choices)

# print("Computer chose:", computer)

# if user == computer:
#     print("It's a tie!")
#     # assemble all the winnning conditions 
# elif (user == "rock" and computer == "scissors") or \
#      (user == "scissors" and computer == "paper") or \
#      (user == "paper" and computer == "rock"):
#     print("You win!")
# else:
#     print("You lose!")





    # third advance version to track the scores of the user and computer /////////////////////////
import random

choices = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        user = input("Enter rock, paper, or scissors: ").lower()
        if user in choices:
            return user
        else:
            print("Invalid input! Try again.")

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print("Computer chose:", computer)

        result = decide_winner(user, computer)

        if result == "win":
            print("You win this round!")
            user_score += 1
        elif result == "lose":
            print("You lose this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
play_game()



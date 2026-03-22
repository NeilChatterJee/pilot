import random

def rock_paper_scissors():
    choices = ["rock","paper", "scissors"]
    while True:
        user_choice = input("Choose Between Rock, Paper, and Scissors: ")
        if user_choice.lower() not in choices:
            print("That's not rock, paper, or scissors!")
        elif user_choice.lower() in choices:
            computer_choice = random.choice(choices)
            if user_choice.lower() == computer_choice:
                print("It's a tie!")
                break
            elif user_choice.lower() != computer_choice:
                if user_choice.lower() == "rock" and computer_choice == "paper":
                    print(f"You Chose {user_choice} and The CPU Chose {computer_choice}: CPU Wins!")
                    break
                elif user_choice.lower() == "paper" and computer_choice == "rock":
                    print(f"You Chose {user_choice} and The CPU Chose {computer_choice}: Player Win!")
                    break
                elif user_choice.lower() == "scissors" and computer_choice == "rock":
                    print(f"You Chose {user_choice} and The CPU Chose {computer_choice}: CPU Wins!")
                    break
                elif user_choice.lower() == "paper" and computer_choice == "scissors":
                    print(f"You Chose {user_choice} and The CPU Chose {computer_choice}: CPU Wins!")
                    break
                elif user_choice.lower() == "scissors" and computer_choice == "paper":
                    print(f"You Chose {user_choice} and The CPU Chose {computer_choice}: Player Win!")
                    break
                elif user_choice.lower() == "rock" and computer_choice == "scissors":
                    print(f"You Chose {user_choice} and The CPU Chose {computer_choice}: Player Win!")
                    break



rock_paper_scissors()

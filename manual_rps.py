import random

def play():
    def get_computer_choice():
        options = ['Rock', 'Paper', 'Scissors']
        return random.choice(options)

    def get_user_choice():
        user_choice = input('Rock, paper, scissors, go!')
        return user_choice

    def get_winner(computer_choice, user_choice):
        # user winning outcomes
        if computer_choice == "Rock" and user_choice == "Paper":
            print("You won!")
        elif computer_choice == "Scissors" and user_choice == "Rock":
            print("You won!")
        elif computer_choice == "Paper" and user_choice == "Scissors":
            print("You won!")
        # computer winning scenarios
        elif computer_choice == "Rock" and user_choice == "Scissors":
            print("You lost")
        elif computer_choice == "Scissors" and user_choice == "Paper":
            print("You lost")
        elif computer_choice == "Paper" and user_choice == "Rock":
            print("You lost")
        else:
            print("It is a tie!")

    get_winner(get_computer_choice(), get_user_choice())

play()
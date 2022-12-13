import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def get_user_choice():
    user_choice = input('Rock, paper, scissors, go!')
    return user_choice

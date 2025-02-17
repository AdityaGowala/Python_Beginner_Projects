# program generate a number 
# you make guesses if too far it says "too high" or "too less"
# (optional) in said number of tryies

import random
import string

easy_number_length = [2 , 2 , 1 , 2 ]
hard_number_length = [ 3 , 4 , 3 , 2 , 3 , 3 , 4 , 5]
no_of_guesses = 10

all_numbers = string.digits 

def make_guessing_number(mode):
    if mode == 'e':
        number_length = random.choice(easy_number_length)
        guessing_number = ""
        for _ in range(number_length):
            guessing_number += str(random.choice(all_numbers))
        return guessing_number
    
    if mode == 'd':
        number_length = random.choice(hard_number_length)
        guessing_number = ""
        for _ in range(number_length):
            guessing_number += str(random.choice(all_numbers))
        return guessing_number

def number_game(): 
    mode = input("Enter game mode : \n Press 'e' for easy mode \n Press 'd' for hard mode \n").lower().strip()
    guessing_number =int( make_guessing_number(mode))
    for _ in range(no_of_guesses):
        your_guess = int(input("Enter your guess: "))
        if your_guess == guessing_number:
            print("CONGRATULATIONS!! You Won")
            break

        elif abs(your_guess - guessing_number) <= 7:
            print("Close")

        elif your_guess > guessing_number:
            print("Too far")

        else:
            print("Too less")


    else:
        print(f"Game Over!! the correct answer is {guessing_number}")

    
number_game()
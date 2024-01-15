# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# type = input("Choose a difficulty, Type 'easy' of 'hard': ")

# chance = 0

# if type == "easy":
#     print("You have 10 attempts remaining to guess the number.")
    
#     chance = 10
        
    
# elif type == "hard":
#     print("You have 5 attempts remaining to huess the number.")
    
#     chance = 5

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


turns = 0
#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number if turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
def game():
    print(logo)
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to huess the number.")

    #Repeat the guessing functionality if they get it wrong.  
    guess = 0
    while guess != answer:
        #Let the user guess a number.
        guess = int(input("Make a guess:"))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
            

#Track the number of turn and reduce by 1 if they get it wrong.

game()
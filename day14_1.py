from day14_art import logo, vs
from day14_0 import data
import random
import os 

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower count and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"    

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


# random.sample(data, 뽑을data갯수) 중복없이 데이터 선택 (3.6 이상 버전부터 가능)
# account_ab = random.sample(data, k=2)  



# Make the game repeatable.
while game_should_continue:

    # Generate a random account from the game data.   
    
    # Making account at position B become the next account at position A. 
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is corrent.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # Clear the screen between rounds.
    os.system("cls")
    print(logo)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        # if guess == "a":
        #     account_b = account_a
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False












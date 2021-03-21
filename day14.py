# import random
#
# import data from game_data as followers_list
#
# continue_game = True
# score = 0
# already_used = []
#
# option_1 = random.choice(list(followers_list.keys()))
# key_list = list(followers_list.keys())
#
# while continue_game:
#     already_used.append(option_1)
#
#     option_2 = random.choice(list(followers_list.keys()))
#
#     if followers_list.get(option_1) > followers_list.get(option_2):
#         compare = "l"
#
#     else:
#         compare = "h"
#
#     answer = input(f"Guess if {option_2} has higher or lower instagram followers than {option_1}\n h or l = ")
#
#     if answer == "h" and compare == "h":
#         print(f"You got that right {option_2} has {followers_list.get(option_2)} followers.")
#         score += 1
#         option_1 = option_2
#     elif answer == "l" and compare == "l":
#
#         print(f"You got that right {option_2} has {followers_list.get(option_2)} followers.")
#         score += 1
#         option_1 = option_2
#
#     else:
#         print("Sorry, Your guess was wrong. ")
#         continue_game = False


'''======================================================================='''

import game_data
import random


#display art
print(game_data.logo)

# generate a random account from the game data


#format the account data into printable format


continue_game = True
score = 0
already_used = []

account_a = random.choice(game_data.data)

while continue_game:

    account_b = random.choice(game_data.data)

    if account_a == account_b:
        account_b = random.choice(game_data.data)

    account_a_name = account_a["name"]
    account_b_name = account_b["name"]
    account_a_follower = account_a["follower_count"]
    account_b_follower = account_b["follower_count"]
    account_a_description = account_a["description"]
    account_b_description = account_b["description"]
    account_a_country = account_a["country"]
    account_b_country = account_b["country"]

    if account_a_follower > account_b_follower:
        result = "H"

    else:
        result = "L"

    answer = input(f"Guess if \n A : {account_a_name} a {account_a_description} from {account_a_country}\n has more followers than \n B : {account_b_name} a {account_b_description} from {account_b_country}\n Enter H or L :").upper()

    if answer == "H" and result == "H":
        print(f"You got that right {account_a_name} has {account_a_follower} million followers and {account_b_name} has {account_b_follower} million.")
        score += 1
        account_a = account_b
    elif answer == "L" and result == "L":

        print(f"You got that right {account_b_name} has {account_b_follower} million followers and {account_b_name} has {account_b_follower} million.")
        score += 1
        account_a = account_b

    else:
        print("Sorry, Your guess was wrong. ")
        continue_game = False

    print(f"Your score is {score}")
# Ask the user for a guess

# Check if the user is correct

# Get the followers count of each account

# give user a feedback  on their guess

#keep scores

# make the game repeatable

# making the account at position b to position a

#clear the screen


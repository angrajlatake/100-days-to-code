
'''
#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.


import random

def deal():
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    comp.append(random.choice(cards))
    comp.append(random.choice(cards))
    print(f"Player has {player} and Dealer has {comp}")

def check_total(cards):
    return sum(cards)

    print(f"Player Score : {p_score} , Computer score : {c_score}")
def hit(list):
    list.append(random.choice(cards))
    if 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)
    print(f"Player has {player} and Dealer has {comp}")

# def stand():
player_total = 0
comp_total = 0

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player = []
comp = []

# bet_amount = int(input("Welcome to the game of BlackJack\nHow much would you like to bet? : $"))

deal()
while sum(player) <= 21:
    print(sum(player))
    player_input = input("Do you want another card or stand?")
    if player_input =="card":
        hit(player)

    elif player_input == "stand":
        while sum(comp) < 17:
            hit(comp)
        print(f"Player has {player} and Dealer has {comp}")


'''


import random

def hit(list):
    list.append(random.choice(cards))
    if (11 in list) and sum(list) < 21:
        list.remove(11)
        list.append(1)


def check_total(cards):
    return sum(cards)

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player = []
comp = []



player.append(random.choice(cards))
player.append(random.choice(cards))
comp.append(random.choice(cards))
comp.append(random.choice(cards))



continue_game = True

while continue_game:
    player_score = check_total(player)
    comp_score = check_total(comp)

    print(f"Player has {player} and Dealer has {[comp[0]]}")
    print(f" total for Players is : {player_score} ")
    if comp_score >= 21 or player_score >= 21:
        continue_game = False

    else:
        player_input = input("Do you want to deal another card 'y' or 'n':")
        if player_input == "y":
            hit(player)

        else:
            while sum(comp) < 17:
                hit(comp)
            print(f"Player has {player} and Dealer has {comp}")
            print(f" total for Players is : {player_score} Dealer score is :{check_total(comp)} ")
            continue_game = False


if sum(comp)> 21:
    print("Player won this round")
elif sum(player)> 21:
    print("Dealer won this round")
elif sum(player) > sum(comp):
    print(f"Player won the round")
elif sum(player) == sum(comp):
    print("Its a tie")
else:
    print("Dealer won this round")











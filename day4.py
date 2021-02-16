"""

import random

name_string = input("give me everybody's name seperated by a comma.")
names = name_string.split(", ")

winner = random.choice(names)

print(f"{winner} is going to buy the meal today!")



row1 = ["X", "X", "X"]
row2 = ["X", "X", "X"]
row3 = ["X", "X", "X"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[horizontal - 1]
selected_row[vertical - 1] = "O"

print(f"{row1}\n{row2}\n{row3}")

"""

# rock paper scissors

import random

print("Let's play Rock paper Scissors. Best of 3!")
rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


list = [rock, paper, scissors]

player_win = 0
comp_win = 0
games_played = 0
while games_played != 3 :

    comp = random.randint(1, 3)
    player = int(input("What do you want to choose? Type 1 for Rcok, 2 for paper and 3 for Scissors.\n"))

    print("You chose : " + list[player - 1])
    print("Computer chose : " + list[comp - 1])

    if comp == player:
        print("Its' a draw!")
        print(f"Score Computer {comp_win} : Player {player_win}")
        games_played += 1
    elif comp == 1 and player == 2 :
        print("You win!")
        player_win += 1
        games_played += 1
        print(f"Score Computer {comp_win} : Player {player_win}")
    elif comp == 1 and player == 3:
        print("You lost!")
        comp_win += 1
        games_played += 1
        print(f"Score Computer {comp_win} : Player {player_win}")
    elif comp == 2 and player == 1:
        print("You lost!")
        comp_win += 1
        games_played += 1
        print(f"Score Computer {comp_win} : Player {player_win}")
    elif comp == 2 and player == 3:
        print("You win!")
        player_win += 1
        games_played += 1
        print(f"Score Computer {comp_win} : Player {player_win}")
    elif comp == 3 and player == 1:
        print("You win!")
        player_win += 1
        games_played += 1
        print(f"Score Computer {comp_win} : Player {player_win}")

    else:
        print("You lost!")
        comp_win += 1
        games_played += 1
        print(f"Score Computer {comp_win} : Player {player_win}")



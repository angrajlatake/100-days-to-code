# the final project hangman game
#step 1




import random

from hangmanart import logo
from hangmanart import stages
from wordlist import word_list
print(logo)



chosen_word = random.choice(word_list)

letters_tried =[]
display = []
for i in range(len(chosen_word)):
    display += "_"

print(display)


score = 0
end_of_game = True

while (score < 7) and ("_" in display)  :

    guess = input("Guess a letter for the word:\n").lower()



    if guess in letters_tried:
        print("You have already guessed this letter. Try another one.")

    elif guess in chosen_word:

        for i in range(0, len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess


    else:
        score +=1
        print(stages[score -1])

    print(display)
    letters_tried.append(guess)
if score == 7:
    print(f"You have lost the game. The word was {chosen_word}")

elif "_" not in display:
    print(f"You guessed it. The word is {chosen_word}. ")
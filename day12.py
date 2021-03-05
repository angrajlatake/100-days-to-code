import random

# def compare(guess,life):




number = random.randint(1,100)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

choice = input("Choose a difficulty. Type 'easy' or 'hard':")

if choice == "easy" :
    lives = 10
else:
    lives = 5
continue_game = True
while lives != 0 and continue_game:
    print(f"You have {lives} attempts")
    guess = int(input("Guess the number:"))

    if guess > number:
        lives -= 1
        print("Too high.")

    elif guess < number:
        lives -= 1
        print("Too Low.")

    elif guess == number:
        print(f"You guess it right. The number is {number}.")
        continue_game = False

if lives == 0:
    print(f"Psss! You could guess the number. It was {number}")




"""
# average height calculator.
# write the program without using sum() or len() function
# write using for look

student_heights = input("Input a list of students heights.").split()
total = 0
length = 0
for n in student_heights:
    total += int(n)
    length += 1

print(f"sum of the list of height is {total}")
print(f"length of the list is {length}")


# find the highest number in the list using for loop
# 123 132 143 154 145 165 144 122 174
# without using max() function and min() function
student_scores = input("Input a list of students score").split()

highest_score = 0
for score in student_scores:
    if int(score) > int(highest_score):
        highest_score = score

print(f"the highest score among the whole class is {highest_score}")


#we have to print a sum of numbers from 1 to 100 of only even numbers
# range(1,101,2)
total = 0
for numb in range(2, 101, 2):
    total += numb

print(f"Total sum of even numbers from 2 to 100 is {total}")


# NEW CODING CHALLANGE
#PROGRAM FOR FIZZBUZZ A CHILDERN'S GAME

# your program should print each number from 1 to 100 in turn.
# when the number is divisible by 3 then instead of printing the number it should print "Fizz:.
# When the number is divisible by 5, then instead of printing the number it should print "Buzz"
# and when the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for numb in range(1,101):
    if numb % 3 == 0 and numb % 5 == 0:
        print("FizzBuzz")
    elif numb % 5 == 0:
        print("Buzz")
    elif numb % 3 == 0:
        print("Fizz")
    else:
        print(numb)

"""
# Pypassword generator!
# ask the user how many letter would you like in your password
# ask how many symbols and numbers

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

    password =""
    #Eazy Level - Order not randomised: not my way of doing things
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    for char in range(1,nr_letters +1):
        password +=(random.choice(letters))

    for char in range(1,nr_numbers +1):
        password +=(random.choice(numbers))

    for char in range(1,nr_symbols +1):
        password +=(random.choice(symbols))
    print(f"This is your new password :\n{password}")

    print(f"This is your shuffled password:" ,''.join(random.sample(password,len(password))))
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# functions
'''
def greet(name, location):
    print(f"Hello {name}!" )
    print("How are you doing today?")
    print(f"Isnt the weather nice today in {location}?")

greet("Angraj", "mumbai")



#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#number of cans = (wall height ✖️ wall width) ÷ coverage per can

import math
# this will give us the ability to round up to the next number with math.ceil
def calculate(wall_h, wall_w, coverage):
    can_required = (wall_h* wall_w) / coverage
    #can_required = round(can_required) is one of the method of rounding but the issue with this is it will round to the nearest number not the next integer
    can_required = math.ceil(can_required)
    print(f"You will need {can_required} cans to paint wall of {wall_h} high and {wall_w} wide.")

test_h = int(input("How tall is the wall? \n"))
test_w = int(input("How wide is the wall? \n"))
test_coverage = int(input("How much area can one can cover? \n"))

calculate(test_h, test_w,test_coverage)



# check if the number is a prime number

# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
'''
# Code cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# def decrypt(text, shift):
#     encrypted_text = []
#     for i in text:
#         if i == " ":
#             encrypted_text.append(" ")
#         else:
#             index_in_list = alphabet.index(i)
#             shifted_index = index_in_list - shift
#             if shifted_index < 0:
#                 shifted_index +=26
#             encrypted_text.append(alphabet[shifted_index])
#     print("Your decoded word is : " +''.join(map(str, encrypted_text)))
#
# def encrypt(text, shift):
#     encrypted_text = []
#     for i in text:
#         if i == " ":
#             encrypted_text.append(" ")
#         else:
#             index_in_list = alphabet.index(i)
#             shifted_index = index_in_list + shift
#             if shifted_index > 25:
#                 shifted_index -=26
#             encrypted_text.append(alphabet[shifted_index])
#     print("Your encoded word is : " +''.join(map(str, encrypted_text)))

#combined function
def caesar(text, shift, direction):
    encrypted_text = []
    for i in text:
        if i not in alphabet:
            encrypted_text.append(i)

        else:
            index_in_list = alphabet.index(i)
            if direction == "encode":
                shifted_index = index_in_list + shift
                if shifted_index > 25:
                    shifted_index = shifted_index % 26
            elif direction == "decode":
                shifted_index = index_in_list - shift
                if shifted_index < 0:
                    shifted_index = shifted_index % 26
            encrypted_text.append(alphabet[shifted_index])
    code_word = (''.join(map(str, encrypted_text)))
    print(f"Your {direction}d word is : {code_word}." )

# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift,direction)

    restart = input("Would like to go again. enter 'Yes' or 'no': \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")

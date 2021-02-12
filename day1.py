"""#print command
print("Hello World!")
name = input("What's your name? ")  # setup a variable
# you can setup a value to variable and change it later as well e.g
a = 21
print(a)
a = 99
print(a)

print("Hello " + name)  # this way dont have to write another line for input
print("Welcome to the world of\nCODING!")  # this is to move word coding to the next line
print(len(name))  # find length of the object
"""
'''#switch values from one variable to another

a = input("a:")
b = input("b:")

# CREATE ONE MORE VARIABLE TO ASSIGN THE FIRST VALUE

c = a
a = b
b = c

print("a: " + a + "\nb: " + b )
'''
#band name generator

print("Welcome to the Band Name Generator!")
user_city = input("What is the city name you grow up in?\n")
user_pet_name = input("What is the name of your pet?\n")

print("Your band name would be " + user_city + " " +user_pet_name)



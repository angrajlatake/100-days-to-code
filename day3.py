
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
total = 0
if height >= 120 :
    print("You can ride the rollercoaster!")
    age = int(input("Please enter your age:\n"))
    if age <= 12:
        total += 5
        print(f"Your ticket is ${total}")
    elif age <= 18:
        total +=7
        print(f"Your ticket is ${total}")
    elif age > 45 and age < 55:
        print("Dont worry about it, We got you covered for the ticket!")
    else:
        total += 12
        print(f"Your ticket is ${total}")

    photo = input("Would you like to get a picture in during the ride? Y or N\n")
    photo = photo.upper()
    if photo == "Y":
        total+= 3
        print(f"Your final total is ${total}")
    else:
        print(f"Your total is ${total}")
else:
    print("Sorry, You have to grow taller before you ride.")


 #modulo with conditional statements

numb = int(input("Please enter the number you want to check\n"))

if numb % 2 == 0:
    print("The number is EVEN")
else:
    print("the number is ODD")



#check leap year program

year = int(input("Which year do you want to check?\n"))

#if the number is divisible by 4 except for the number which is divisible by 100 unless it is also divisible by 400

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year!")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year!")
else:
    print("It is not a leap year")

# pizza order application

print("Welcome to Gino's")
bill = 0
size = int(input("Which pizza would you like to have today? Choose 1 for small pizza, 2 for Medium and 3 for large pizza"))
add_pepperoni = input("Would you like to add extra pepperoni to your pizza? Y or N")
add_pepperoni = add_pepperoni.upper()
extra_cheese = input("Would you like to add extra cheese? Y or N")
extra_cheese = extra_cheese.upper()
order=[]
if size == 1:
    bill += 15
    order.append("Small Pizza")
    if add_pepperoni == "Y":
        bill += 2
        order.append("Extra Pepperoni")
elif size == 2:
    bill +=20
    order.append("Medium Pizza")
    if add_pepperoni == "Y":
        bill += 3
        order.append("Extra Pepperoni")
elif size == 3 :
    bill +=25
    order.append("Large Pizza")
    if add_pepperoni == "Y":
        bill += 3
        order.append("Extra Pepperoni")

if extra_cheese == "Y":
    bill +=1
    order.append("Extra Cheese")

print("Your order is ", order)
print(f"and your total bill is ${bill}. Thank you!")



#Code Challange
#Love Calculator
# refer to https://repl.it/@appbrewery/day-3-5-exercise
print("Welcome to the love calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
true = 0
love = 0
name1 = name1.lower()
name2 = name2.lower()
new_name = name2+name1

'''
#This is one way of doing it
for word in new_name:
    for letter in word:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            true +=1


for word in new_name:
    for letter in word:
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            love +=1
'''
#other way is to use count function
t = new_name.count("t")
r = new_name.count("r")
u = new_name.count("u")
e = new_name.count("e")

true = t + r + u + e

l = new_name.count("l")
v = new_name.count("v")
o = new_name.count("o")
e = new_name.count("e")

love = l + o + v + e

total_score = str(true)+str(love) #have to convert to str to put the number together. If int they will get added which is not what we are looking to do

print("Your score is " +total_score) # no need to convert into int because already str

total_score = int(total_score) # converted into integer to be able to use it in conditional statement

if total_score < 10 or total_score > 90:
    print("You go together like Coke and Mentos.")

if total_score > 40 and total_score < 50:
    print("You are alright together.")



# code challange
#Tresure hunt

print("Welcome to the Treasure Island. \n Your mission is to find the treasure.")
choice1 = input("Which way would you like to go ? left or right...").lower()

if choice1 == "left":
    print("Ohh shoot! you fell in a river.")
    choice2 = input("Do you want to continue swimming or wait?").lower()
    if choice2 =="wait":
        choice3 =input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")




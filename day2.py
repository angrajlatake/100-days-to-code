#pulling out a perticular element from string, list or directories
# printing first element of the word Angraj is A
# To get that you need to use [0]
print("Angraj"[0])
#printing last element of the word
print("Angraj"[-1])
#printing second last element
print("Angraj"[-2])
#printing elements from 2nd to last
print("Angraj"[1:])
#when using range the last element is not used
print("Angraj"[1:-1])
#to reverse the elements
print("Angraj"[::-1])
#to skip an element
print("Angraj"[::2])
#to skip element in reverse
print("Angraj"[::-2])
#convert str into int or vice versa
a = 123
b = str(a)
c = int(b)
d= float(c)

#check type of data
print(type(d))

'''Code Challange
take input from the user of a 2 digit number
Check if the number is 2 digits. If it is, add those two digits and return the answer'''

numb = input("Please enter any two digit number \n")

if len(numb) == 2:

    print("Total of your digits is " + str(int(numb[0]) + int(numb[1])))  #the input is str type need to convert it to int for addition and then convert again to str to print
else:
    print("Invalid entry. Please run the program again! ")

'''Code Challenge
Create is Body mass index calculator
BMI = weight(kg)/height**2(m**2)'''

wt = float(input("Please enter your weight in kilograms:\n"))
ht = float(input("Please enter your height in meters:\n"))

bmi = wt / (ht**2)

print("Your Body Mass Index is : " + str(round(bmi,2))) # rounding the number to 2 digits after decimal



#f-string can be used to convert all the data type together to strings, to avoid repeating of type change for multiple elements

score = 0
height = 1.8
isWinning = True

#f-string
print(f"your score is {score}, your height is {height},your winning is {isWinning}")



'''Code challenge
Ask the user for its age and return the number of days, weeks and months left till he becomes 90 years of age'''

user_age = int(input("How old are you? \n"))
year_left = (90 - user_age)
month_left = year_left * 12
weeks_left = year_left * 52
days_left = year_left * 365

print(f"You have {days_left} days, {weeks_left} weeks and {month_left} months left.")

print("Welcome to the tip calculator")
bill_amount = float(input("What was your total bill amount? $"))
tip_amount = float(input("What percentage tip would you like to give? "))
numb_of_ppl = int(input("How many people are splitting the bill? "))

total_bill_amount = bill_amount + (bill_amount * tip_amount / 100)
split = round(total_bill_amount / numb_of_ppl, 2)

print(f"Each person should pay: ${split} ")


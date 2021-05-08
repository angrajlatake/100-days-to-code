#list comprehension shortens the code where we use for loop

numbers = [1,2,3]
# if you wnat to add +1 to each element and add it to a new list, you can create an empty list, loop thrugh the numbers, add 1 to ech number and append it to the new list
#e.g.

new_numbers = []

for n in numbers:
    new_number = n +1
    new_numbers.append(new_number)

# this can be shortened with a shortcut
#e.g. new_numbers = [new_item for item in list if test]
#new_item is the change you want to make to the item in the list
#test is if you want to add any condition

new_list = [n+1 for n in numbers]
new_conditional_list = [num + 1 for num in numbers if num % 2 == 0]

print(new_list,new_conditional_list)

#You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [num ** 2 for num in numbers_list]


#Write your code 👆 above:

print(squared_numbers)

'''You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.'''

result = [num for num in numbers_list if num % 2 == 0]

print(result)

'''Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.'''

with open("file1.txt") as file1:
    file1_list = file1.readlines()

with open("file2.txt") as file2:
        file2_list = file2.readlines()

results = [int(num) for num in file1_list if num in file2_list]

print(f"{results}")

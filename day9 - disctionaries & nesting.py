'''
programming_dictionary = {
    "Bug": "An error in a person that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again"
}
#retriving items from dictionary
# print(programming_dictionary["Function"])

# Adding new item to the dictionary
programming_dictionary["new item"] = "value"

print(programming_dictionary)



#new grading program
# the program will replace the scores with greades


student_scores = {
    "Harry" : 81 ,
    "Ron" : 78 ,
    "Hermione" : 99 ,
    "Drako" : 74 ,
    "Neville" : 62
}

# dont change the code above

# TODO1 : create and empty dictionary called students_grades
student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"

    elif student_scores[key] >=81:
        student_grades[key] = "Exceeds Expectation"

    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"

    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"



#TODO2 : Write your below to add the grades

print(student_grades )


##################################################################

#nesting

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(name, visits, cities):
    travel_log.append({"country": name, "visits": visits, "cities": cities})





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

'''

#####################################

#blind auction game

# have not found a solution to clear the screen to make it blind
# 1st thing to do is to write a function to add the name and bid to an empty dictionary

database = {}

def add_bid(name, bid):
    database[name] = int(bid)

#2nd is to write a function to go through the dictionary and find the highest bid

def find_winner(name_of_dictonary):
    highest_bid = 0
    for key, value in database.items():

        if value > highest_bid:
            highest_bid = value
            winner = key
    print(f"....and the winning bid goes to {winner} for ${highest_bid} ")

#Welcome screen
print("Welcome to the secret auction")

continue_loop = True
while continue_loop:
    name = input("What is your name? :")
    bid = input("What's your bid? :$")
    add_bid(name,bid)
    another_bidder = input("Are there any other bidders? 'yes' or 'no'. \n")
    if another_bidder == "no":
        continue_loop = False



find_winner(database)
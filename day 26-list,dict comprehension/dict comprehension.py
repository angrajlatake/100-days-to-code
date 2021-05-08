# new_dict = {new_key:new_value for item in list
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_score = {student:random.randint(80,100) for student in names}

passed_students = {student:score for (student,score) in student_score.items() if score > 85}

print(passed_students)

'''You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.'''

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word:len(word) for word in sentence.split()}

print(result)

'''You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
'''

# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day :(temp * 9/5) + 32 for (day,temp) in weather_c.items()}

print(weather_f)


#coverting dictionary into to list

days = [day for day in weather_f.keys()]
temp_f = [temp_f for temp_f in weather_f.values()]

#converting the days and temp to dict for dataframe

weather = {
    "days": days,
"tempreture": temp_f}

#using pandas for dataframe
import pandas

weather_df = pandas.DataFrame(weather)
print(weather_df)

#iterating through dataframe by looping through

for (index, row) in weather_df.iterrows():
    print(row) #prints data both columns
    print(row.days) #print only days
    print(row.tempreture) # print only temps
#make sure the .days and .tempreture matches spelling with dataframe




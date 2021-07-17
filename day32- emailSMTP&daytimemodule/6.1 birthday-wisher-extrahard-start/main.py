##################### Extra Hard Starting Project ######################
import random
import smtplib

import pandas as pd
import datetime as dt
# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day_tuple = (now.day, now.month)
new_dict = {(row.day, row.month): row for index, row in data.iterrows()}
if day_tuple in new_dict:
    name = new_dict[day_tuple]["name"]
    email = new_dict[day_tuple]["email"]
    print(email)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letter1 = "./letter_templates/letter_1.txt"
    letter2 = "./letter_templates/letter_2.txt"
    letter3 = "./letter_templates/letter_3.txt"
    letters_list = [letter3,letter1,letter2]
    chosen_letter = random.choice(letters_list)
    placeholder = "[NAME]"
    with open(chosen_letter, mode="r") as letter:
        content = letter.read()
        print(content)
        new_content = content.replace(placeholder, name)
        print(new_content)


# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
    connection.starttls()
    connection.login(user="lataketest@gmail.com", password="Qwerty@987")#replace the correct password
    connection.sendmail(from_addr="lataketest@gmail.com", to_addrs="angraj.latake@gmail.com", msg=f"Subject: Happy Birthday")





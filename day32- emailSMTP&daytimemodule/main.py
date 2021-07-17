#this code is giving Unicode encode error
'''import datetime as dt
import random

import smtplib


if dt.datetime.weekday(dt.datetime.now()) == 4:
    with open("quotes.txt") as file:
        list = file.readlines()
        quote = (list[random.randint(0,102)])

print(uni(quote))

my_email = "email"
password = "password"
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password= password)
    connection.sendmail(from_addr=my_email,to_addrs=my_email, msg=f"Subject:Monday Motivation Test\n\n {quote}")
'''


#Monday Motivation Project

import smtplib
import datetime as dt
import random

MY_EMAIL = "lataketest@gmail.com"
MY_PASSWORD = "Qwerty@987" #replace the correct password

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Monday Motivation\n\n{quote}"
    )

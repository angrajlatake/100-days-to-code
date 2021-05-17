import smtplib
import time

import requests
from datetime import datetime
#--------------------------ISS DATA--------------------------#
response = requests.get(url = "http://api.open-notify.org/iss-now.json")
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])

#-------------------MY DATA---------------------------------#

my_lat = 19.122545
my_long = 72.821952
my_time = datetime.utcnow()
utc_my_time = my_time.strftime("%I:%M:%S %p")

response = requests.get(url = f"https://api.sunrise-sunset.org/json?lat={my_lat}&lng={my_long}")

utc_sunset_time = response.json()["results"]["sunset"]
utc_sunrise_time = response.json()["results"]["sunrise"]

continue_program = True

iss_visible = False
while continue_program:
    time.sleep(60) #the code cand be added to run it every 60 mins
    if utc_sunrise_time < utc_my_time > utc_sunset_time :
        if (my_lat - 15) > iss_lat < (my_lat + 15) or (my_long - 15) > iss_long < (my_lat + 15):
            iss_visible = True

    if iss_visible:

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="email", password="password")
            connection.sendmail(
                from_addr= "lataketest@gmail.com",
                to_addrs= "lataketest@gmail.com",
                msg=f"Subject: Look up now\n\n The International Space station is in the sky. ISS position is {iss_lat} {iss_long}. "
            )


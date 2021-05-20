#this program takes information from weather API and it checks if it going to rain in the next 12 hours and send you a text message
import requests
from twilio.rest import Client
import os
api_key = os.environ["WX_API"]
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_number = os.getenv("MY_NUMBER")


response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=19.076090&lon=72.877426&exclude=daily,minutely&appid={api_key}")

data = response.json()["hourly"]

need_umbrella = False
for n in range(12):
    hourly_weather = data[n]["weather"][0]['id']

    if hourly_weather < 700:
        need_umbrella = True

if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(
        to=my_number,
        from_="+12053863536",
        body="It looks like its going to rain today. ☔️ Dont forget your umbrell🌂"
    )
    print(message.status)

#the program can be uploaded to run it everyday at a certain time

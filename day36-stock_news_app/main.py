import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import os
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = "2c7795acbd33451cad7492c391decf77"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH_TOKEN")
MY_NUMB = os.environ.get("MY_NUMBER")
SENDER = "+12053863536"
todays_date = datetime.now().date()
yesterday_date = todays_date - timedelta(days=1)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_data = requests.get(
    F"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}")

daily_price = stock_data.json()["Time Series (Daily)"]

closing_prices = [value["4. close"] for value in daily_price.values()]

today_closing = float(closing_prices[0])
yest_closing = float(closing_prices[1])

percent_change = round((today_closing - yest_closing) / today_closing * 100, 2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.



data = requests.get(
    f"https://newsapi.org/v2/everything?q=tesla&from={yesterday_date}&sortBy=popularityAt&apiKey={NEWS_API_KEY}")
news = data.json()["articles"]

headlines = []
for n in range(3):
    headlines.append(f"{news[n]['source']['name']} : {news[n]['title']}")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
print(headlines)
if percent_change > 2 or percent_change < -2:
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        to=MY_NUMB,
        from_=SENDER,
        body=f"{todays_date}\nTesla Inc = {percent_change}%\n{headlines[0]}\n{headlines[1]}\n{headlines[2]}"
    )
    print(message.status)




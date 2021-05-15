import requests
import json
response = requests.get(url = "http://api.open-notify.org/iss-now.json")

data = response.json()

print(data)

print(data["iss_position"]["latitude"])
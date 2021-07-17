import requests
from datetime import datetime

today = datetime.now().date().strftime("%Y%m%d")

TOKEN = "letsbuildahabbittracker"
USERNAME = "angrajlatake"
GRAPHID = "graph265"
#creating user
pixela_endpoint= "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}
# response = requests.post(url=pixela_endpoint,json=parameters)

graph_config = {
    "id" : GRAPHID,
    "name" : "Running Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
pixel_update_endpoint = f"{graph_endpoint}/{GRAPHID}"
pixel_data = {
    "date": today,
    "quantity" : "10"
}

# response = requests.post(url=pixel_update_endpoint, headers= headers, json=pixel_data)

# response = requests.put(url=f"{pixel_update_endpoint}/{today}", headers=headers, json={"quantity" : "15"})

response = requests.delete(url=f"{pixel_update_endpoint}/{today}", headers=headers)
print(response.text)
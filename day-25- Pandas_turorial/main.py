# with open("weather_data.csv") as data:
#     data_list = data.readlines()
#
# print(data_list)

# import csv
#
# with open("weather_data.csv") as data:
#     data_file = csv.reader(data)
#     temperature = []
#     for row in data_file:
#         if row[1] != "temp":
#
#             temperature.append(row[1])
#     print(temperature)

import pandas as pd

data = pd.read_csv("weather_data.csv")

# find the day where tempreture is maximum

print(data[data.temp == data["temp"].max()])

#get temp for Monday in degree f

monday = data[data.day == "Monday"]
print(9/5* monday.temp +32)


#create dataframe from scratch

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]

}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_file.csv")



# This project will read the date and create new csv with number of squirrel in each color
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")

Gray = 0
Cinnamon = 0
Black = 0

fur_color = data["Primary Fur Color"].tolist()

for color in fur_color:
    if color == "Gray":
        Gray += 1

    if color == "Cinnamon":
        Cinnamon += 1

    if color == "Black":
        Black +=1

data_dict = {
    "Fur Color" : ["Grey", "Cinnamon", "Black"],
    "Number" : [Gray, Cinnamon, Black]
}

new_data = pd.DataFrame(data_dict)

print(new_data)
new_data.to_csv("Primary fur color data.csv")


'''=======================================================================
#shorter version of the same code

gray_count = len(data[data["Primary Fur Color"] == "Gray"])

cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_count = len(data[data["Primary Fur Color"] == "Black"])

'''
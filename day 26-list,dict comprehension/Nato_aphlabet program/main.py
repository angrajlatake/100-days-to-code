#this program takes input of a name from the user and then gives out a list of word that can be used as phonetics

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}


name = input("Please enter your name:").upper()

list_of_phonetics = [phonetic_dict[item] for item in name]


print(list_of_phonetics)


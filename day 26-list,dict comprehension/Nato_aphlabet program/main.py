#this program takes input of a name from the user and then gives out a list of word that can be used as phonetics

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}

#the improvement was made to get any kind of input and not let the program end


def generate_phonetics():
    name = input("Please enter your name:").upper()
    try:
        letter_of_phonetics = [phonetic_dict[item] for item in name]

    except KeyError:
        print("Sorry, only letter in alphabet please")
        generate_phonetics()
    else:
        print(letter_of_phonetics)


generate_phonetics()


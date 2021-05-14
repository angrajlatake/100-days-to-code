import tkinter.messagebox
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
french_word = None
language = None
english_word = None
current_card = None
list_of_words = {}
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/French_to_English - Sheet1.csv")
    list_of_words = original_data.to_dict(orient="records")
except pd.errors.EmptyDataError:
    original_data = pd.read_csv("./data/French_to_English - Sheet1.csv")
    list_of_words = original_data.to_dict(orient="records")
else:
    list_of_words = data.to_dict(orient="records")



# ---------------------------- SELECT LEVELS ------------------------------- #


# ----------------- NOTE IF YOU KNOW THE WORD OR NOT ------------------ #
def known_word():
    global current_card, list_of_words
    print(len(list_of_words))
    try:
        list_of_words.remove(current_card)

        data = pd.DataFrame(list_of_words)
        data.to_csv("./data/words_to_learn.csv", index= False)
        random_word()
    except:
        error_fucntion()


def error_fucntion():
    tkinter.messagebox.showinfo(title="", message="You have learned all the words\n Closing the game")
    window.destroy()


# --------------------------- SHOW TRANSLATION ------------------------ #
def show_translation():
    canvas.itemconfig(card_front_image, image=card_back)
    canvas.itemconfig(lang_lable, text='English')
    canvas.itemconfig(word_lable, text=english_word)


# ---------------------------- CHOOSE RANDOM WORD --------------------- #
def random_word():
    global french_word, english_word, flip_timer, current_card

    window.after_cancel(flip_timer)
    canvas.itemconfig(card_front_image, image=card_front)
    canvas.itemconfig(lang_lable, text='French')
    current_card = random.choice(list_of_words)
    french_word = current_card['French']
    english_word = current_card['English']
    canvas.itemconfig(word_lable, text=french_word)
    flip_timer = window.after(3000, show_translation)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
window.title("Learn French")

flip_timer = window.after(3000, show_translation)

canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_front_image = canvas.create_image(400, 263, image=card_front)

card_back = PhotoImage(file="./images/card_back.png")

lang_lable = canvas.create_text(400, 150, text=language, font=("Arial", 30, "bold"))

word_lable = canvas.create_text(400, 263, text=french_word, font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=3)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(column=2, row=1)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_buttom = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_buttom.grid(column=0, row=1)

random_word()

window.mainloop()

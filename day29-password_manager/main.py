import tkinter.messagebox
from tkinter import *
import random
import json
import pyperclip

# data = pd.DataFrame({"Email/Username" : [],
#                    "Password" : [],
#                    "Website" : []})
# data.to_csv("data_file.csv")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#this function generates password, copies it to the clipboard
def generate_password():
    password = ""

    for char in range(0, 10):
        password += (random.choice(letters))

    for char in range(2):
        password += (random.choice(numbers))

    for char in range(2):
        password += (random.choice(symbols))

    password = "".join(random.sample(password, len(password)))
    password_input.delete(0, END)
    password_input.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # website information
    website = website_input.get()
    # email information
    email = email_input.get()
    # password information
    password = password_input.get()
    #JSON format
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }
    #Error message
    if website_input.index("end") == 0 or email_input.index("end") == 0 or password_input.index("end") == 0:
        tkinter.messagebox.showinfo(title="Field is empty", message="Please fill in all the details")
    else:
        try:
            with open("manager.json", mode="r") as manager:
                data = json.load(manager)
                data.update(new_data)
        except FileNotFoundError:
            with open("manager.json", "w") as manager:
                json.dump(new_data, manager, indent = 4)
        else:
            data.update(new_data)

            with open("manager.json", "w") as manager:
                json.dump(data, manager, indent=4)
        finally:
            tkinter.messagebox.showinfo(title="", message="new details have been added to the file")
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    try:
        with open("manager.json", "r") as manager:
            data = json.load(manager)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error",message=f"You haven't saved any passwords yet!")

    else:
        if website_input.get() in data:
            email = data[website_input.get()]["email"]
            password = data[website_input.get()]["password"]
            pyperclip.copy(password)
            tkinter.messagebox.showinfo(title=f"{website_input.get()}",
                                        message=f"Email : {email} \n Password: {password} \n Password has been copied to clipboard")
        else:
            tkinter.messagebox.showinfo(title="Error",
                                        message=f"{website_input.get()} is not saved in the manager")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
file = PhotoImage(file="logo.png")
image = canvas.create_image(100, 100, image=file)
canvas.grid(column=1, row=0)

website_input = Entry(width=21)
website_input.grid(column=1, row=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=3, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=4)

website_lable = Label(text="Website:")
website_lable.grid(column=0, row=2)
email_lable = Label(text="Email/Username:")
email_lable.grid(column=0, row=3)
password_lable = Label(text="Password")
password_lable.grid(column=0, row=4)

pass_gen = Button(text="Generate Password", command=generate_password)
pass_gen.grid(column=2, row=4)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=5, columnspan=2)
search_button = Button(width= 13,text="Search", command=search_password)
search_button.grid(column= 2, row = 2)

window.mainloop()

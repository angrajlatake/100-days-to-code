from tkinter import *

THEME_COLOR = "#375362"


class User_Interface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Entertainment Quiz")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        question = self.canvas.create_text(150, 125, text="What the fuck", font=("Arial", 20, "italic"))

        self.lable = Label(text="Score", bg=THEME_COLOR, fg="white")
        self.lable.grid(column=1, row=0)

        true_image = PhotoImage(file="../Quiz app/images/true.png")
        self.true_button = Button(image=true_image)
        self.true_button.grid(column=0, row=3)

        false_image = PhotoImage(file="../Quiz app/images/false.png")
        self.false_button = Button(image=false_image)
        self.false_button.grid(column=1, row=3)

        self.window.mainloop()

    def get_next_question
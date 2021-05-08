import turtle
from turtle import Turtle, Screen
import pandas as pd

#setup screen with background
screen = Screen()
screen.title("US States guessing game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

#create a turtle writing and move to the right place

def create_turtle(guess_word,x,y):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(guess_word, align="left", font=("Arial", 10, "normal"))


#read data from the csv
data = pd.read_csv("50_states.csv")

print(data["state"].tolist())
#keep the score
score = 0

# list of states guessed
guessed_states = []
#list of states to learn
states_to_learn = []
while score < 50:

    guess = screen.textinput(f"{score}/50 States Correct", "What's another state name? \nEnter 'Exit' of you want to quit ").title()
    guess_data = data[data.state == guess]
    # if the guess is correct create turtle and move it to the right place
    if guess == "Exit":
        break

    if guess in data["state"].tolist():

        x_cor = int(guess_data.x)
        y_cor = int(guess_data.y)
        create_turtle(guess, x_cor, y_cor)
        score += 1
        guessed_states.append(guess)


if score < 50 :
    # for state in data["state"].tolist():
    #     if state not in guessed_states:
    #         states_to_learn.append(state)
    states_to_learn = [state for state in data["state"].tolist() if state not in guessed_states] #list comprehension
list_to_learn = pd.DataFrame(states_to_learn)

list_to_learn.to_csv("State to learn")


screen.exitonclick()
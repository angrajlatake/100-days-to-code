from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0

check_mark = "✔"
check_mark1 = "✔"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    canvas.after_cancel(timer)
    canvas.itemconfig(time_left, text="00:00")
    timer_lable.config(text="Timer")
    reps = 0
    check_mark = "✔"
    check_lable.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN)
        timer_lable.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN)
        timer_lable.config(text="BREAK", fg=GREEN)
    elif reps % 2 == 1:
        countdown(WORK_MIN)
        timer_lable.config(text="WORK", fg=PINK, )


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# define the countdown func.
def countdown(count):
    global check_mark
    global timer
    if count >= 0:
        minutes, seconds = divmod(count, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)
        canvas.itemconfig(time_left, text=time_format)
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_lable.config(text=check_mark)
            check_mark += check_mark1


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=500, height=500, )
window.config(padx=100, pady=100, bg=YELLOW)
window.title("Pomodoro")

timer_lable = Label(text="Timer", font=(FONT_NAME, 60), fg=GREEN, bg=YELLOW)
timer_lable.grid(column=2, row=1)

check_lable = Label(text="", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
check_lable.grid(column=2, row=5)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
file = PhotoImage(file="tomato.png")
image = canvas.create_image(150, 150, image=file)
time_left = canvas.create_text(150, 175, text="00:00", fill="white", font=(FONT_NAME, 60, "bold"))

canvas.grid(column=2, row=2)

start_button = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 20), highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 20), highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()

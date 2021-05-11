import tkinter
import random
window = tkinter.Tk()

window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

def button_click():
    text_input = input.get()
    my_lable.config(text=text_input)

#lable
my_lable = tkinter.Label(text= "Waiting for the text input", font= ("Arial", 24, ))
my_lable.grid(column= 0)



#Button
button = tkinter.Button(text= "Click me!", command= button_click)
button.grid(column =2, row=2)
button = tkinter.Button(text= "New Button")
button.grid(column =3, row=0)
#Entry

input = tkinter.Entry(width = 10)
input.grid(column =4, row=3)







window.mainloop()
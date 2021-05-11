import tkinter
from itertools import cycle
window = tkinter.Tk()

window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)

converted_number = 0
#Conversion fucntion
def convert_miles_to_km():
    miles = input.get()
    global converted_number
    converted_number = round((int(miles)*1.60934),2)
    lable2.config(text= converted_number)

def convert_km_to_miles():
    km = input.get()
    global converted_number
    converted_number = round((int(km) / 1.60934), 2)
    lable2.config(text=converted_number)



#INPUT
input = tkinter.Entry(text="Miles",width=10)
input.grid(column=2,row=1)

#LABLES
lable1= tkinter.Label(text="is equal to",font=("Arial", 20))
lable1.grid(column=1,row=2)

lable2= tkinter.Label(text=converted_number,font=("Arial", 20))
lable2.grid(column=2,row=2)

lable3= tkinter.Label(text="Km",font=("Arial", 20))
lable3.grid(column=3,row=2)

lable3= tkinter.Label(text="Miles",font=("Arial", 20))
lable3.grid(column=3,row=1)

#Button

button = tkinter.Button(text= "Calculate", command= convert_miles_to_km)
button.grid(column=2,row=3)

#This is the given task. Lets go one step further and make a button to switch the units




window.mainloop()
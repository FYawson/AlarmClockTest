from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import time
import datetime

root = Tk()
root.geometry("640x480")
root.frame = Frame(root)
root.frame.pack(fill = "both")
label = Label(root, text= "Welcome", bg = "black", fg = "white", font=("Times", 50))
label.pack(side= "top", fill = "both", expand = 1)
root.title_font = tkfont.Font(family = "Times", size = 100, weight = "bold", slant = "italic")
root.title("Clock")

def alarm():
    current_time = tick()
    wake_entry = Entry(root)
    wake_entry.pack()
    wake_entry_button = Button(root, text="Set Alarm")
    wake_entry_button.pack(side = BOTTOM)
    wake = wake_entry.get()
    wake = time.strftime("%I:%M")
    if wake == current_time:
        label.config(root, bg = "red")


def tick(time1 = ""):

    time2 = time.strftime("%I:%M:%S")
    if time2 != time1:
        time1 = time2
        label.config(text = time1)
    label.after(200, tick)
    return time1

button_alarm = Button(text = "Alarm")
button_alarm.config(command = alarm)
button_alarm.pack()

tick()
root.mainloop()
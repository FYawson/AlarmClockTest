import datetime
import winsound
import tkinter as tk

filename = "old-fashioned-door-bell.wav"

#-------Creating a window-----------
window = tk.Tk()

window.title("Alarm Clock")
window.geometry("400x400")

#-------Creating Background colour-------
window.configure(background="Brown")

#------Creating a function------
def alarm_Clock():

    alarmHour = int(Entry1.get())
    alarmMinute = int(Entry2.get())
    amPm = str(Entry3.get())

    if (amPm == "pm"):
        alarmHour += 12

    while (1 == 1):
        if (alarmHour == datetime.datetime.now().hour and
            alarmMinute == datetime.datetime.now().minute):
            winsound.PlaySound(filename, winsound.SND_LOOP)
            break

def update_btn():
    alarmHour, alarmMinute, amPM = Entry1.get(), Entry2.get(), Entry3.get()
    if alarmHour.isdigit() and alarmMinute.isdigit() and amPM.isdigit():
        return alarm_Clock()

#------Creating Prompts------
Prompts1 = tk.Label(text="Kels Alarm Clock", font=("Times New Roman", 40), bg="brown", fg="white")
Prompts1.grid(column=0, row=0)

Prompts2 = tk.Label(text="Please enter the time Alarm should ring!", font=("Times New Roman", 15), bg="brown", fg="white")
Prompts2.grid(column=0, row=1, sticky="W")

#----Creating Labels-----------
Label1 = tk.Label(text="Enter Hour", bg="brown", fg="white", font="Garamond")
Label1.grid(column=0, row=2, sticky="W")

Label2 = tk.Label(text="Enter Minute", bg="brown", fg="white", font="Garamond")
Label2.grid(column=0, row=3, sticky="W")

Label3 = tk.Label(text="Am or Pm", bg="brown", fg="white", font="Garamond")
Label3.grid(column=0, row=4, sticky="W")

#------Creating entry fields-------
Entry1 = tk.Entry()
Entry1.grid(column=1, row=2)

Entry2 = tk.Entry()
Entry2.grid(column=1, row=3)

Entry3 = tk.Entry()
Entry3.grid(column=1, row=4)

#------Creating Buttons-------
Button1 = tk.Button(text="Set Alarm", command="update_btn")
Button1.grid(column=1, row=5)

window.mainloop()

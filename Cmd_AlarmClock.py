import datetime
import winsound

filename = "old-fashioned-door-bell.wav"


alarmHour = int(input("What hour do you want the alarm to ring? "))


alarmMinute = int(input("What minute do you want the alarm to ring? "))


amPm = str(input("am or pm? "))

print("waiting for alarm at: ", alarmHour, alarmMinute, amPm)

if (amPm == "pm"):
    alarmHour += 12

while(1 == 1):
    if(alarmHour == datetime.datetime.now().hour and
       alarmMinute == datetime.datetime.now().minute):
        print("Time to wake up")
        winsound.PlaySound(filename, winsound.SND_LOOP)
        break


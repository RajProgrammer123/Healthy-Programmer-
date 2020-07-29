"""
# healthy programmer
# water - sound - 3.5l - done-log
# eyes - sound - 30m - done - log
# activity - sound - 45m - done - log
"""

# imports:-
import pyttsx3
import notify2
import time


# create speaker
speaker = pyttsx3.init()
speaker.setProperty('voice', "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0")
speaker.setProperty('rate', 150)

# functions:


def water():
    speaker.say("Drink a glass of water")
    speaker.runAndWait()


def getinput():
    res = input("Have you done it?{yes/no}")
    if res.lower == "yes":
        return True
    else:
        return False
# office_time = datetime.datetime.now().hour
# if not 9 < office_time < 17:
#     quit()
print(">>>>>>>>>>>>>>>>>>>> Healthy programmer <<<<<<<<<<<<<<<<<<<<")
print("This program will remind you to:-")
print(" * Drink water after every 30 min")
print(" * Do eye exercise every 45 min")
print(" * Do physical exercise every 2 hours")

timeinit = time.time()

while True:
    time_runtime = time.time()
    change_time = round(-(timeinit - time_runtime))
    print(change_time)
    for x in range(1, 9):
        if change_time == x*5:
            res_w = False
            while not res_w:
                water()
                getinput()













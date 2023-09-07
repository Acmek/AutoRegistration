import pyautogui as auto
import datetime
import time
from PIL import Image

registration = Image.open('Images\\Registration.png')
prompt = Image.open('Images\\Prompt.png')
unsuccessful = Image.open('Images\\Unsuccessful.png')
added = Image.open('Images\\Added.png')

file = open("Courses.txt")

dateLine = ""
while not "/" in dateLine:
    dateLine = file.readline()

target = datetime.datetime(int(file.readline()),int(file.readline()),int(file.readline()),int(file.readline()),int(file.readline()),int(file.readline())) #year, month, day, hour, min, sec

courses = {}
inputCourse = ''
for line in file:
    if line.strip('\n'):
        if('/' in line):
            inputCourse = line[1:].strip('\n')
            courses[inputCourse] = []
        else:
            courses[inputCourse].append(line.strip('\n'))

def sleep_until(target):
    now = datetime.datetime.now()
    delta = target - now

    if delta > datetime.timedelta(0):
        time.sleep(delta.total_seconds())
        return True

sleep_until(target)

auto.moveTo(auto.locateOnScreen(registration, confidence = 0.7))
auto.click()

waiting = True
while waiting:
    if auto.locateOnScreen(prompt, confidence = 0.7):
        waiting = False

for course in courses:
    print('\nRegistering for ' + course + "...")
    for code in courses[course]:
        auto.moveTo(auto.locateOnScreen(prompt, confidence = 0.7))
        auto.click()
        auto.write(code)
        auto.press('enter')

        time.sleep(0.5)

        waiting = True
        while waiting:
            if auto.locateOnScreen(prompt, confidence = 0.7):
                waiting = False

        if auto.locateOnScreen(added, confidence = 0.7):
            print('- Successfully added ' + code + ' for ' + course)
            break
        elif auto.locateOnScreen(unsuccessful, confidence = 0.7):
            print('- Unsuccessfully added ' + code + ' for ' + course)
        else:
            print('- Registration status for ' + code + ' unknown. Ending program may be needed')
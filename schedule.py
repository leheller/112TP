#Scheduling page where new users fill out a weekly schedule for when they can meet
###########
#schedule.py citation comment
#basic animation framework from 112 website
#lines 7-99: original code
###########
import random
import pickle
from tkinter import *
from Register import *
from schedule import *
from login import *
from home import *
from profile import *
from messaging import *
from dates import *
from cv2 import *
from pickleFile import *
from PIL import ImageTk,Image 
import socket
import threading
from queue import Queue

#Turns the image into a cropped grayscale list of pixels
def processPicture(image):
    img = Image.open(image)
    cropped = img.crop([520, 270, 760, 510]).convert('LA')
    data = list(cropped.getdata(0))
    s = ""
    for px in data:
        s += str(px) + "&"
    return s

#Turns the schedule from a dictionary to a string
def processSchedule(d):
    s = ""
    for day in d:
        s += day + "&" + d[day] + "&"
    return s

#Makes sure schedule is completely filled out    
def checkSchedule(data):
    counter = 0
    for day in ["Monday:","Tuesday:","Wednesday:","Thursday:","Friday:","Saturday:","Sunday:"]:
        if data.schedule[day] == "":
            return False
    return True

def scheduleMousePressed(event, data):
    i = 2
    #Clicking in boxes
    for day in ["Monday:","Tuesday:","Wednesday:","Thursday:","Friday:","Saturday:","Sunday:"]:
        j = 0
        for time in ["6pm","7pm","8pm","9pm","10pm","11pm"]: 
            if event.x > 4*data.size+j*data.size and event.x < j*data.size+5*data.size and event.y > i*data.size+data.height//7 and event.y < (i+1)*data.size+data.height//7:
                data.schedule[day] = time
            j += 1.5
        i += 1.75
    #Continue to home page
    if event.x > 8*data.width//9 - data.size and event.x < 8*data.width//9 + data.size:
        if event.y > data.height//2 - data.size and event.y < data.height//2 + data.size:
            if checkSchedule(data) == True:
                image = processPicture(data.imageName)
                sched = processSchedule(data.schedule)
                data.myProfile = (data.username,data.password,data.GPA,data.school,data.bio,sched,image)
                data.profiles.add(data.myProfile)
                writePickle(data)
                setToString(data,data.myProfile)
                writePickle(data)
                sorting(data,data.otherProfiles)
                data.mode = "home"

def scheduleKeyPressed(event, data):
    pass

def scheduleRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor="nw",image=data.background)
    #Title
    canvas.create_text(data.width//2,data.size,anchor="center",text="Fill in your availability for each day",font=("Comic Sans MS","26","bold"),fill="white")
    i = 2
    #Schedule
    for day in ["Monday:","Tuesday:","Wednesday:","Thursday:","Friday:","Saturday:","Sunday:"]:
        times = ["6pm","7pm","8pm","9pm","10pm","11pm"]
        j = 0
        canvas.create_text(data.size//2,i*data.size+data.height//7,anchor="nw",font=("Comic Sans MS","16","bold"),text=day,fill="white")
        for time in times:
            if data.schedule[day] == time:
                color = "yellow"
            else:
                color = "white"
            canvas.create_rectangle(4*data.size+j*data.size,i*data.size+data.height//7,j*data.size+5*data.size,(i+1)*data.size+data.height//7,fill=color,activefill="yellow")
            canvas.create_text(4.5*data.size+j*data.size,data.size+data.height//7,font=("Comic Sans MS","10","bold"),fill="white",text=time)
            j += 1.5
        i += 1.75
    #Contune text
    canvas.create_text(8*data.width//9,data.height//2,anchor="center",text="continue",font=("Comic Sans MS","18","bold"),fill="white",activefill="yellow")
    if checkSchedule(data) == False:
        canvas.create_rectangle(8*data.width//9-2*data.size,data.height//2-data.size,8*data.width//9+1.5*data.size,data.height//2+2*data.size,fill="red")
        canvas.create_text(8*data.width//9,data.height//2,anchor="center",text="please fill in\nall fields",font=("Comic Sans MS","12","bold"))
        
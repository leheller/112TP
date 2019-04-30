#Home screen, shows profile

# Basic Animation Framework 
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
####################################
#From 112 website
# customize these functions
####################################
#Sorting algorithm
def sorting(data, s):
    college = []
    rest = []
    for ppl in s:
        if ppl[3] == data.school:
            diff = abs(float(ppl[2])-float(data.GPA))
            college.append(diff)
        else: 
            diff = abs(float(ppl[2])-float(data.GPA))
            rest.append(diff)
    college.sort()
    rest.sort()
    for ppl in s:
        diff = abs(float(ppl[2])-float(data.GPA))
        if ppl[3] == data.school:
            for i in range(len(college)):
                if college[i] == diff:
                    college[i] = ppl
        else:
            for i in range(len(rest)):
                if rest[i] == diff:
                    rest[i] = ppl
    data.otherProfiles = college + rest
    
    
#Supermatch algorithm
def autoMatch(data):
    diff = abs(float(data.otherProfiles[0][2])-float(data.GPA))
    if data.otherProfiles[0][3] == data.school and diff <= 0.2:
        sched1 = createSchedule(data.myProfile[5])
        sched2 = createSchedule(data.otherProfiles[0][5])
        closestTime = 100
        for day in sched1:
            time1 = ""
            for c in sched1[day]:
                if c in "1234567890":
                    time1 += c
            time1 = int(time1)
            time2 = "  "
            for c in sched2[day]:
                if c in "1234567890":
                    time2 += c
            time2 = int(time2)
            if sched1[day] == sched2[day]:
                day,time = day[:-1] + "  ",sched1[day]
                data.match = (data.myProfile[0],data.otherProfiles[0][0],day,time,"SUPERMATCH")
                data.match2 = (data.otherProfiles[0][0],data.myProfile[0],day,time,"SUPERMATCH")
                data.matches.add(data.match)
                data.matches.add(data.match2)
                writePickle2(data)
                setToString2(data,data.match)
                setToString2(data,data.match2)
                writePickle2(data)
                

def homeMousePressed(event, data):
    if event.x>=(10+2*data.width//3) and event.y>=(2*data.size+data.height//2) and event.x<=(data.width-10) and event.y<=(data.height-2*data.size):
        data.profileImage = recreate(data, data.otherProfiles[0][6])
        findMatches(data)
        data.mode = "profile"
    elif event.x>=10+data.width//3 and event.x<=2*data.width//3-10:
        if event.y>=2*data.size+data.height//2 and event.y<=data.height-2*data.size:
            writePickle3(data)
            messageReader(data)
            data.mode = "messaging"
    elif event.x>=10 and event.x<=2*data.width//3-10:
        if event.y>=2*data.size+data.height//2 and data.height-2*data.size:
            findMatches(data)
            data.mode = "dates"
            
def homeKeyPressed(event, data):
    pass

def homeRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor="nw",image=data.background)
    canvas.create_rectangle(data.width//2+5,10,data.width-10,data.height//2,fill="white")
    #Name
    canvas.create_text(data.width//2+10,data.size,anchor="nw",font=("Comic Sans MS","24","bold"),text="AndrewID: "+data.username)
    #Picture
    try:
        if data.image != "":
            canvas.create_image(10, 10, anchor="nw", image=data.image)
        else:
            canvas.create_image(10, 10, anchor="nw", image=data.myImage)
    except: 
        canvas.create_rectangle(10,10,data.width//2,data.height//2,fill="black")
        canvas.create_oval(120-40,80-40,160,120,width=3,outline="white")
        canvas.create_line(120,120,120,250,width=3,fill="white")
        canvas.create_line(120,140,200,200,width=3,fill="white")
        canvas.create_line(120,140,40,200,width=3,fill="white")
        canvas.create_text(120,70,anchor="center",text="O   O",font=("32"),fill="white")
        canvas.create_line(100,90,120,110,140,90,smooth=1,width=3,fill="white")
    #GPA
    canvas.create_text(data.width//2+10,2.5*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="GPA: "+data.GPA)
    #College
    canvas.create_text(data.width//2+10,4*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="School: "+data.school)
    #Bio
    canvas.create_text(data.width//2+10,5.5*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="Bio: "+data.bio)
    #Matches
    canvas.create_rectangle(10,2*data.size+data.height//2,data.width//3-10,data.height-2*data.size,fill="white",activefill="yellow")
    canvas.create_text(data.width//5-data.size//2,4*data.height//5-data.size,anchor="c",text="upcoming dates",font=("Comic Sans MS","12","bold"))
    #Messages
    canvas.create_rectangle(10+data.width//3,2*data.size+data.height//2,2*data.width//3-10,data.height-2*data.size,fill="white",activefill="yellow")
    canvas.create_text(data.width//2,4*data.height//5-data.size,anchor="c",text="ongoing messages",font=("Comic Sans MS","12","bold"))
    #Other singles at CMU
    canvas.create_rectangle(10+2*data.width//3,2*data.size+data.height//2,data.width-10,data.height-2*data.size,fill="white",activefill="yellow")
    canvas.create_text(5*data.width//6,4*data.height//5-data.size,anchor="c",text="see other singles @ CMU",font=("Comic Sans MS","12","bold"))
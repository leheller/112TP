#Shows all of the matches you have and dates you have gone on/will go on
from tkinter import *
import random
import pickle

def findMatches(data):
    people = set()
    for match in data.matches:
        if len(match) < 5:
            pass
        elif match[0] == data.username:
            people.add(match[1])
    for match in data.matches:
        if len(match) < 5:
            pass
        elif match[1] == data.username and match[0] in people:
            data.myMatches.add(match) 

def dates(canvas,data):
    findMatches(data)
    i = 0
    for matches in data.myMatches:
        day = matches[2]
        time = matches[3]
        place = matches[4]
        canvas.create_text(2*data.size,data.size+data.height//10*(i+1),fill="white",font=("Comic Sans MS","18","bold"),text=matches[0],anchor="n")
        canvas.create_text(data.width//4,data.size+data.height//10*(i+1),fill="white",font=("Comic Sans MS","16","bold"),text="  --->  "+day+time+place,anchor="nw")
        i += 1

def datesMousePressed(event, data):
    if event.x>=10 and event.x<=data.size+10:
        if event.y>=10 and event.y<=data.size+10:
            data.mode = "home"

def datesRedrawAll(canvas, data):
    profilesFilename = "matches.py"
    with open(profilesFilename,"rb") as rfp:
        matches = pickle.load(rfp)
        data.matches = matches
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    canvas.create_image(0,0,anchor="nw",image=data.background)
    canvas.create_text(data.width//2,10,text="Upcoming Dates",font=("Comic Sans MS","26","bold"),anchor="n",fill="white")
    dates(canvas,data)
    #home button
    canvas.create_rectangle(10,10,data.size+10,data.size+10,fill="white",activefill="yellow")
    canvas.create_text(25,25,text="HOME",font=("Comic Sans MS","8","bold"),anchor="center") 


    
































#Shows all of the matches you have and dates you have gone on/will go on
from tkinter import *
import random


def dates(canvas,data):
    i = 0
    for matches in data.matchedProfiles:
        day = data.matchedProfiles[i][1]
        time = data.matchedProfiles[i][2]
        place = data.matchedProfiles[i][3]
        canvas.create_text(2*data.size,data.size+data.height//10*(i+1),font=("Comic Sans MS","18","bold"),text=data.matchedProfiles[i][0],anchor="n")
        canvas.create_text(data.width//4,data.size+data.height//10*(i+1),font=("Comic Sans MS","16","bold"),text="  --->  "+day+time+place,anchor="nw")
        i += 1

def datesMousePressed(event, data):
    if event.x>=10 and event.x<=data.size+10:
        if event.y>=10 and event.y<=data.size+10:
            data.mode = "home"

def datesRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    canvas.create_text(data.width//2,10,text="Upcoming Dates",font=("Comic Sans MS","26","bold"),anchor="n")
    dates(canvas,data)
    #home button
    canvas.create_rectangle(10,10,data.size+10,data.size+10,fill="white",activefill="yellow")
    canvas.create_text(25,25,text="HOME",font=("Comic Sans MS","8","bold"),anchor="center") 


    
































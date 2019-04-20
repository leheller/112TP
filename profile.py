#Profile page for all of the potential matches

from tkinter import *
import random

def profileMousePressed(event, data):
    if (event.x>=10) and (event.y>=2*data.size+data.height//2) and (event.x<=data.width//3-10) and (event.y<=data.height-2*data.size):
        data.color1 = "yellow"
        day = random.choice(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
        time = random.choice(["  8pm","  4:30pm","  Midnight","  6:30pm","  2pm","  9:30am","  11am","  Noon"])
        place = random.choice(["  iNoodle","  the Fence","  Walking to the Sky","  Sorrels","  ABP","  CFA Lawn","  the Exchange","  Number Garden","  Doherty 2315","  Donner Dungeon"])
        data.matchedProfiles.append([data.otherProfiles[0][0],day,time,place])
    elif event.x>=10 and event.x<=data.size+10:
        if event.y>=10 and event.y<=data.size+10:
            data.mode = "home"
    elif event.x>=10+data.width//3 and event.x<=2*data.width//3-10:
        if event.y>=2*data.size+data.height//2 and event.y<=data.height-2*data.size:
            data.messagingProfiles += [data.otherProfiles[0]]
    elif event.x>=2*data.width//3+10 and event.x<=10+2*data.width//3+3.5*data.size:
        if event.y>=2*data.height//3 and event.y<=5*data.height//6:
            if len(data.otherProfiles) > 1:
                data.otherProfiles.pop(0)
                data.color1 = "white"
        
def profileKeyPressed(event, data):
    pass

def profileRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    #Name
    canvas.create_text(data.width//2+10,data.size,anchor="nw",font=("Comic Sans MS","24","bold"),text="Name: "+data.otherProfiles[0][0])
    #Picture
    canvas.create_rectangle(10,10,data.width//2,data.height//2,fill="white")
    #GPA
    canvas.create_text(data.width//2+10,2.5*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="GPA: "+data.otherProfiles[0][2])
    #College
    canvas.create_text(data.width//2+10,4*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="School: "+data.otherProfiles[0][3])
    #Bio
    canvas.create_text(data.width//2+10,5.5*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="Bio: "+data.otherProfiles[0][4])
    #Go on a date
    canvas.create_rectangle(10,2*data.size+data.height//2,data.width//3-10,data.height-2*data.size,fill=data.color1,activefill="yellow")
    canvas.create_text(data.width//5-data.size//2,4*data.height//5-data.size,anchor="c",text="ask "+data.otherProfiles[0][0]+" on a date",font=("Comic Sans MS","12","bold"))
    #Message
    canvas.create_rectangle(10+data.width//3,2*data.size+data.height//2,2*data.width//3-10,data.height-2*data.size,fill="white",activefill="yellow")
    canvas.create_text(data.width//2,4*data.height//5-data.size,anchor="c",text="message "+data.otherProfiles[0][0],font=("Comic Sans MS","12","bold"))
    #Next
    canvas.create_polygon(2*data.width//3+10,data.height-3.5*data.size,10+2*data.width//3,data.height-5*data.size,10+2*data.width//3+2*data.size,data.height-5*data.size,10+2*data.width//3+2*data.size,data.height-6*data.size,10+2*data.width//3+3.5*data.size,data.height-4.25*data.size,10+2*data.width//3+2*data.size,data.height-2.5*data.size,10+2*data.width//3+2*data.size,data.height-3.5*data.size,fill="white",activefill="yellow")
    canvas.create_text(2.3*data.width//3+10,data.height-4.25*data.size,anchor="c",text="see more CMU singles",font=("Comic Sans MS","10","bold"))
    #Home
    canvas.create_rectangle(10,10,data.size+10,data.size+10,fill="white",activefill="yellow")
    canvas.create_text(25,25,text="HOME",font=("Comic Sans MS","8","bold"),anchor="center")   
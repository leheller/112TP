#Home screen, shows profile

# Basic Animation Framework
from tkinter import *
####################################
#From 112 website
# customize these functions
####################################


def homeMousePressed(event, data):
    if event.x>=(10+2*data.width//3) and event.y>=(2*data.size+data.height//2) and event.x<=(data.width-10) and event.y<=(data.height-2*data.size):
        data.mode = "profile"
    elif event.x>=10+data.width//3 and event.x<=2*data.width//3-10:
        if event.y>=2*data.size+data.height//2 and event.y<=data.height-2*data.size:
            data.mode = "messaging"
    elif event.x>=10 and event.x<=2*data.width//3-10:
        if event.y>=2*data.size+data.height//2 and data.height-2*data.size:
            data.mode = "dates"
            
def homeKeyPressed(event, data):
    pass

def homeRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    #Name
    canvas.create_text(data.width//2+10,data.size,anchor="nw",font=("Comic Sans MS","24","bold"),text="Name: "+data.username)
    #Picture
    canvas.create_rectangle(10,10,data.width//2,data.height//2,fill="white")
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
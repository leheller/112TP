#Initial login/register page for when the app is opened

from tkinter import *
# Basic Animation Framework from 112 website
####################################
# customize these functions
####################################

def loginMousePressed(event, data):
    if event.x>=data.width//2-data.sizeX1 and event.x<=data.width//2+data.sizeX1:
        if event.y>=data.height//2-data.sizeY1 and event.y<=data.height//2+data.sizeY1:
            data.boxState = (True,"username")
    if event.x>=data.width//2-data.sizeX1 and event.x<=data.width//2+data.sizeX1:
        if event.y<=data.height//2+3.5*data.sizeY1 and event.y>=data.height//2+1.5*data.sizeY1:
            data.boxState = (True,"password")
    if event.x>=data.width//2-30 and event.x<=data.width//2+30:
        if event.y>=data.height//2+data.size1-20 and event.y<=data.height//2+data.size1+20:
            data.boxState = ("Register")
    if event.x>=data.width//2-50 and event.x<=data.width//2+50:
        if event.y>=data.height//2+data.size1-15 and event.y<=data.height//2+data.size1+15:
            data.mode = "Register"
    else:
        data.boxState = (False, 0, 0)
        
def loginKeyPressed(event, data):
    if event.keysym == "Return":
        data.boxState == "login"
    elif data.boxState[0] == True and data.boxState[1] == "username":
        data.username1 += event.char
    elif data.boxState[0] == True and data.boxState[1] == "password":
        data.password1 += event.char
        
def loginRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    #username box
    canvas.create_rectangle(data.width//2-data.sizeX1,data.height//2-data.sizeY1,\
        data.width//2+data.sizeX1,data.height//2+data.sizeY1,fill="white",\
        activefill="yellow",width=2)
    #password box
    canvas.create_rectangle(data.width//2-data.sizeX1,data.height//2+1.5*data.sizeY1,\
        data.width//2+data.sizeX1,data.height//2+3.5*data.sizeY1,fill="white",\
        activefill="yellow",width=2)
    #Seeking@CMU
    canvas.create_text(data.width//2,data.height//2-data.size1,anchor="c",\
        font="ComicSans 28 bold",text="Seeking@CMU",fill="white")
    #login
    canvas.create_text(data.width//2,data.height//2-data.sizeX1,anchor="c",\
        font="ComicSans 18 bold",text="login",fill="white")
    #register
    canvas.create_text(data.width//2,data.height//2+data.size1,anchor="c",\
        font="ComicSans 18 bold",text="register",fill="white",\
        activefill=data.color2)
    #username text
    canvas.create_text(data.width//2,data.height//2,anchor="c",text=data.username1)
    #password text
    canvas.create_text(data.width//2,data.height//2+2.5*data.sizeY1,anchor="c",text=data.password1)


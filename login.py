#Initial login/register page for when the app is opened
import pickle
from tkinter import *
# Basic Animation Framework from 112 website
####################################
# customize these functions
####################################

def loginMousePressed(event, data):
    if event.x>=data.width//2-data.sizeX1 and event.x<=data.width//2+data.sizeX1:
        if event.y>=data.height//2-data.sizeX1-20 and event.y<=data.height//2-data.sizeX1+20:
            if knownPerson(data) == True:
                data.mode = "home"
        elif event.y>=data.height//2-data.sizeY1 and event.y<=data.height//2+data.sizeY1:
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
        
def knownPerson(data):
    profilesFilename = "profiles.py"
    with open(profilesFilename,"rb") as rfp:
        profiles = pickle.load(rfp)
        data.profiles = profiles
    print(data.profiles)
    data.otherProfiles = list(data.profiles)
    for ppl in data.profiles:
        if ppl[0] == data.username1 and ppl[1] == data.password1:
            data.myProfile = ppl
            data.username = ppl[0]
            data.GPA = ppl[2]
            data.school = ppl[3]
            data.bio = ppl[4]
            return True
    return False
        
def loginKeyPressed(event, data):
    if event.keysym == "Return":
        data.boxState == "login"
    elif data.boxState[0] == True and data.boxState[1] == "username":
        data.username1 += event.char
    elif data.boxState[0] == True and data.boxState[1] == "password":
        data.password1 += event.char
        
def loginRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    if knownPerson(data) == False:
        canvas.create_text(data.width-3*data.size,data.size,text="unknown username\n or password",fill="red",anchor = "center")
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
        font="ComicSans 18 bold",text="login",fill="white",activefill="yellow")
    #register
    canvas.create_text(data.width//2,data.height//2+data.size1,anchor="c",\
        font="ComicSans 18 bold",text="register",fill="white",\
        activefill=data.color2)
    #username text
    canvas.create_text(data.width//2,data.height//2,anchor="c",text=data.username1)
    #password text
    canvas.create_text(data.width//2,data.height//2+2.5*data.sizeY1,anchor="c",text="*"*len(data.password1))
    #if checkPassword(data) != True:
        #canvas.create_rectangle(data.width-2*data.size,0,data.width,2*data.size,fill="red")
        #canvas.create_text(data.width-2*data.size,data.size,anchor="w",text="passwords\nmust\nmatch!",font=("Comic Sans MS","12","bold"))


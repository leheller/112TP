#Registration page where user creates an account and profile

from tkinter import *
# Basic Animation Framework from 112 website
####################################
# customize these functions
####################################

def registerInit(data):
    data.size = 30
    data.sizeX = 90
    data.sizeY = 30
    data.boxState = (False,"")
    data.username = ""
    data.password = ""
    data.confirmPassword = ""
    data.GPA = ""
    data.school = ""
    data.bio = ""
    data.counter = 0
    data.counter2 = 0
    data.profilePic = ""

def registerMousePressed(event, data):
    if event.x>=data.width//2-data.sizeX and event.x<=data.width//2+data.sizeX and event.y<data.height//2:
        if event.y>=data.sizeX and event.y<=data.sizeX+data.sizeY:
            data.boxState = (True,"username")
        elif event.y<=data.sizeX+2.5*data.sizeY and event.y>=data.sizeX+1.5*data.sizeY:
            data.boxState = (True,"password")
        elif event.y>=data.sizeX+3*data.sizeY and event.y<=data.sizeX+4*data.sizeY:
            data.boxState = (True,"confirmPassword")
        else:
            data.boxState = (False, "")
    elif event.x>=data.width//3-data.sizeX//2 and event.x<=data.width//3+data.sizeX//2 and event.y<data.height-data.size:
        if event.y>=data.sizeX+5.5*data.sizeY and event.y<=data.sizeX+6.5*data.sizeY:
            data.boxState = (True,"GPA")
        elif event.y>=data.sizeX+7*data.sizeY and event.y<=data.sizeX+8*data.sizeY:
            data.boxState = (True,"school")
    elif event.y>=data.height//2 and event.x>=data.width//2:
        #3 lines taken from stackoverflow --> https://stackoverflow.com/questions/3520493/python-show-in-finder
        # import subprocess
        # file_to_show = "/Applications/Photos.app"
        # subprocess.call(["open", "-R", file_to_show])
        
        filename = "profilePic.gif"
        data.profilePic = PhotoImage(file=filename)
    elif event.y>=data.sizeX+8.5*data.sizeY:
        if event.x<=data.width//3+2*data.sizeX//3:
            data.boxState = (True,"bio")  
    elif event.x>=3*data.width//4 and event.x<=3*data.width//4+2*data.size:
        if event.y<=data.height//4+2*data.size and event.y>=data.height//4:
            data.mode = "home"
    else:
        data.boxState = (False, "")
        
def registerKeyPressed(event, data):
    if event.keysym == "Return":
        data.boxState == "login"
    elif data.boxState[0] == True and data.boxState[1] == "username":
        if event.keysym == "BackSpace":
            data.username = data.username[:-1]
        elif len(data.username)>22:
            pass
        else:
            data.username += event.char
    elif data.boxState[0] == True and data.boxState[1] == "password":
        if event.keysym == "BackSpace":
            data.password = data.password[:-1]
        elif len(data.password)>22:
            pass
        else:
            data.password += event.char
    elif data.boxState[0] == True and data.boxState[1] == "confirmPassword":
        if event.keysym == "BackSpace":
            data.confirmPassword = data.confirmPassword[:-1]
        elif len(data.confirmPassword)>22:
            pass
        else:
            data.confirmPassword += event.char
    elif data.boxState[0] == True and data.boxState[1] == "GPA":
        if event.keysym == "BackSpace":
            data.GPA = data.GPA[:-1]
        elif len(data.GPA)>4:
            pass
        elif event.char in "1234567890.":
            data.GPA += event.char
    elif data.boxState[0] == True and data.boxState[1] == "school":
        if event.keysym == "BackSpace":
            data.school = data.school[:-1]
        elif len(data.school)>14:
            pass
        else:
            data.school += event.char
    elif data.boxState[0] == True and data.boxState[1] == "bio":
        if event.keysym == "BackSpace":
            data.bio = data.bio[:-1]
            data.counter -= 1
        elif data.counter > 20:
            data.bio += "\n"
            data.counter = 0
            data.counter2 += 1
        elif data.counter2 > 7:
            pass
        else:
            data.bio += event.char
            data.counter += 1
            
def registerRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    #continue
    canvas.create_text(3*data.width//4+data.size,data.height//4+data.size,anchor="c",text="continue",font=("Comic Sans MS","16","bold"),fill="white",activefill="yellow")
    #username box
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX,\
        data.width//2+data.sizeX,data.sizeX+data.sizeY,fill="white",\
        activefill="yellow",width=2)
    #password box
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX+1.5*data.sizeY, data.width//2+data.sizeX,data.sizeX+2.5*data.sizeY,fill="white",activefill="yellow",width=2)
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX+3*data.sizeY, data.width//2+data.sizeX,data.sizeX+4*data.sizeY,fill="white",activefill="yellow",width=2)
    #GPA box
    canvas.create_rectangle(data.width//3-data.sizeX//2,data.sizeX+5.5*data.sizeY, data.width//3+data.sizeX//2,data.sizeX+6.5*data.sizeY,fill="white",activefill="yellow",width=2)
    #college box
    canvas.create_rectangle(data.width//3-2*data.sizeX//3,data.sizeX+7*data.sizeY, data.width//3+2*data.sizeX//3,data.sizeX+8*data.sizeY,fill="white",activefill="yellow",width=2)
    #bio box
    canvas.create_rectangle(data.sizeX//2,data.sizeX+8.5*data.sizeY,data.width//3+2*data.sizeX//3,data.height-data.size,fill="white",activefill="yellow",width=2)
    #create profile text
    canvas.create_text(data.width//2,data.size,anchor="c",font=("Comic Sans MS","28","bold"),text="Create Profile",fill="white")
    #username
    canvas.create_text(data.width//8,data.sizeX,anchor="c",font=("Comic Sans MS","18","bold"),text="username:",fill="white")
    #password 
    canvas.create_text(data.width//8,data.sizeX+1.5*data.sizeY,anchor="c",font=("Comic Sans MS","18","bold"),text="password:",fill="white")
    canvas.create_text(data.width//8,data.sizeX+3*data.sizeY,anchor="c",font=("Comic Sans MS","18","bold"),text="confirm\npassword:",fill="white")
    #GPA 
    canvas.create_text(data.width//8,data.sizeX+5.8*data.sizeY,anchor="c",font=("Comic Sans MS","18","bold"),text="GPA:",fill="white")
    #college
    canvas.create_text(data.width//9,data.sizeX+7.5*data.sizeY,anchor="c",font=("Comic Sans MS","18","bold"),text="school:",fill="white")
    #Bio
    canvas.create_text(10,data.sizeX+9*data.sizeY,anchor="w",font=("Comic Sans MS","18","bold"),text="bio:",fill="white")
    #username text
    canvas.create_text(data.width//2,data.sizeX+data.sizeY//2,anchor="c",text=data.username)
    #password text
    canvas.create_text(data.width//2,data.sizeX+2*data.sizeY,anchor="c",text=data.password)
    canvas.create_text(data.width//2,data.sizeX+3.5*data.sizeY,anchor="c",text=data.confirmPassword)
    #GPA text
    canvas.create_text(data.width//3,data.sizeX+6*data.sizeY,anchor="c",text=data.GPA)
    #college text
    canvas.create_text(data.width//3,data.sizeX+7.5*data.sizeY,anchor="c",text=data.school)
    #bio text
    canvas.create_text(data.sizeX//2+10,data.sizeX+8.5*data.sizeY,anchor="nw",text=data.bio,fill="black")
    #image box
    try: 1/0#canvas.create_image(data.width//2, data.height//2, anchor="nw", image=data.profilePic)
    except: canvas.create_rectangle(data.width//2,data.height//2,data.width-data.size,data.height-data.size,fill="black")
    #image text
    canvas.create_text(3*data.width/4-data.size//2,3*data.height/4-data.size//2,anchor="c",text="upload image",fill="white",activefill="yellow")
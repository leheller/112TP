#Direct messaging page between two clients

# Basic Animation Framework
from tkinter import *
#From 112 website
####################################
# customize these functions
####################################

def messagingTexts(canvas,data):
    i = 0
    for message in data.myMessages:
        x1 = 2*data.width//3 - 10
        x2 = data.width - 10
        y1 = data.height-5*data.size - i*data.size
        y2 = y1 + 1.5*data.size
        x3 = 5*data.width//6 - 10
        y3 = data.height-4.2*data.size - i*data.size
        canvas.create_rectangle(x1,y1,x2,y2,fill="white")
        canvas.create_text(x3,y3,font=("Comic Sans MS","12","bold"),anchor="center",text=message)
        i += 2
    try: 
        for message in data.messagingProfiles[0][5]:
            x1 = 2*data.width//3 - 10
            x2 = data.width - 10
            y1 = data.height-5*data.size - i*data.size
            y2 = y1 + 1.5*data.size
            x3 = 5*data.width//6 - 10
            y3 = data.height-4.2*data.size - i*data.size
            canvas.create_rectangle(x1,y1,x2,y2,fill="white")
            canvas.create_text(x3,y3,font=("Comic Sans MS","12","bold"),anchor="center",text=message)
            i += 2
    except: pass

def messagingMousePressed(event, data):
    if event.x>=10 and event.x<=data.size+10:
        if event.y>=10 and event.y<=data.size+10:
            data.mode = "home"
    elif event.x>=2*data.width//3+10 and event.x<=10+2*data.width//3+3.5*data.size:
        if event.y>=3*data.height//4 + 20:
            if len(data.messagingProfiles) > 1:
                if len(data.myMessages) > 0:
                    try: data.messagingProfiles[0][5] += data.myMessages
                    except: data.messagingProfiles[0].append(data.myMessages)
                lastPerson = data.messagingProfiles.pop(0)
                data.messagingProfiles.append(lastPerson)
                data.myMessages = []

def messagingKeyPressed(event, data):
    if event.keysym == "Return":
        data.myMessages.insert(0,data.text)
        data.text = ""
    elif event.keysym == "BackSpace":
        data.text = data.text[:-1]
    elif len(data.text) > 26:
        pass
    else:
        data.text += event.char


def messagingRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    if len(data.messagingProfiles) == 0:
        canvas.create_text(data.width//2,data.height//2,anchor="center",text="NO MESSAGES:(",font=("Comic Sans MS","30","bold"))
    else:
        #text box
        canvas.create_rectangle(10,data.height-10-2*data.size,data.width-10,data.height-10,fill="white")
        canvas.create_text(11,data.height-35,text=data.text,font=("Comic Sans MS","16","bold"),anchor="w")
        #messages
        messagingTexts(canvas,data)   
        #name
        canvas.create_text(data.width//2,data.size,text=data.messagingProfiles[0][0],font=("Comic Sans MS","22","bold"),anchor="n")
        #Next
        canvas.create_polygon(2*data.width//3+10,data.height-data.size,10+2*data.width//3,data.height-2.5*data.size,10+2*data.width//3+2*data.size,data.height-2.5*data.size,10+2*data.width//3+2*data.size,data.height-3.5*data.size,10+2*data.width//3+3.5*data.size,data.height-1.75*data.size,10+2*data.width//3+2*data.size,data.height,10+2*data.width//3+2*data.size,data.height-data.size,fill="red",activefill="yellow")
        canvas.create_text(2.3*data.width//3+10,data.height-1.75*data.size,anchor="c",text="see more messages",font=("Comic Sans MS","10","bold"))
    #home button
    canvas.create_rectangle(10,10,data.size+10,data.size+10,fill="white",activefill="yellow")
    canvas.create_text(25,25,text="HOME",font=("Comic Sans MS","8","bold"),anchor="center") 
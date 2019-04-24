#Direct messaging page between two clients

# Basic Animation Framework
from tkinter import *
from pickleFile import *
#From 112 website
####################################
# customize these functions
####################################
def messageReader(data):
    myName = data.username
    mySent = []
    myReceived = []
    for message in data.messages:
        if message[0] == myName: 
            mySent += [message]
        elif message[1] == myName:
            myReceived += [message]
    data.mySent = mySent
    data.myReceived = myReceived
    
def addMessages(data):
    print("NEW MESSAGE:",data.newMessage)
    lst = data.newMessage
    messages = data.messages
    person1 = lst[0]
    person2 = lst[1]
    text = lst[2]
    print("MESSAGES:",messages)
    for message in messages:
        print("123", message)
        if message[0] == person1 and message[1] == person2:
            print("made it!!!!!$$$$$")
            messages.remove(message)
            message2 = [message[0],message[1]]
            for texts in message[2:]:
                message2 += [texts]
            message2 += [text]
            message = tuple(message2)
            messages.add(message)
            break
    print("MESSAGES2:",messages)
    data.messages = messages
    
def messageReaderReverse(data, oneMessage):
    otherName = oneMessage[1]
    for message in data.messages:
        if message[0] == otherName:
            messages = message[2:]
    return messages
    
def messagingTexts(canvas,data):
    i = 0
    for text in data.mySent[0][2:]:
        x1 = 2*data.width//3 - 10
        x2 = data.width - 10
        y1 = data.height-5*data.size - i*data.size
        y2 = y1 + 1.5*data.size
        x3 = 5*data.width//6 - 10
        y3 = data.height-4.2*data.size - i*data.size
        canvas.create_rectangle(x1,y1,x2,y2,fill="white")
        canvas.create_text(x3,y3,font=("Comic Sans MS","12","bold"),anchor="center",text=text)
        i += 2
    for ppl in data.myReceived:
        if ppl[0] == data.mySent[0][1]:
            for text in ppl[0][2:]:
                x1 = 10
                x2 = data.width//3 - 10
                y1 = data.height-5*data.size - i*data.size
                y2 = y1 + 1.5*data.size
                x3 = data.width//6 - 10
                y3 = data.height-4.2*data.size - i*data.size
                canvas.create_rectangle(x1,y1,x2,y2,fill="white")
                canvas.create_text(x3,y3,font=("Comic Sans MS","12","bold"),anchor="center",text=text)
                i += 2

def messagingMousePressed(event, data):
    if event.x>=10 and event.x<=data.size+10:
        if event.y>=10 and event.y<=data.size+10:
            data.mode = "home"
    elif event.x>=2*data.width//3+10 and event.x<=10+2*data.width//3+3.5*data.size:
        if event.y>=3*data.height//4 + 20:
            if len(data.mySent) > 0:
                lastPerson = data.mySent.pop(0)
                data.mySent.append(lastPerson)

def messagingKeyPressed(event, data):
    if event.keysym == "Return":
        data.newMessage = (data.username,data.mySent[0][1],data.text)
        addMessages(data)
        writePickle3(data)
        setToString3(data,data.newMessage)
        writePickle3(data)
        data.text = ""
    elif event.keysym == "BackSpace":
        data.text = data.text[:-1]
    elif len(data.text) > 26:
        pass
    else:
        data.text += event.char

def messagingRedrawAll(canvas, data):
    messageReader(data)
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    name = data.mySent[0][1]
    if len(data.messages) == 0:
        canvas.create_text(data.width//2,data.height//2,anchor="center",text="NO MESSAGES:(",font=("Comic Sans MS","30","bold"))
    else:
        #text box
        canvas.create_rectangle(10,data.height-10-2*data.size,data.width-10,data.height-10,fill="white")
        canvas.create_text(11,data.height-35,text=data.text,font=("Comic Sans MS","16","bold"),anchor="w")
        #messages
        messagingTexts(canvas,data)   
        #name
        canvas.create_text(data.width//2,data.size,text=name,font=("Comic Sans MS","22","bold"),anchor="n")
        #Next
        canvas.create_polygon(2*data.width//3+10,data.height-data.size,10+2*data.width//3,data.height-2.5*data.size,10+2*data.width//3+2*data.size,data.height-2.5*data.size,10+2*data.width//3+2*data.size,data.height-3.5*data.size,10+2*data.width//3+3.5*data.size,data.height-1.75*data.size,10+2*data.width//3+2*data.size,data.height,10+2*data.width//3+2*data.size,data.height-data.size,fill="red",activefill="yellow")
        canvas.create_text(2.3*data.width//3+10,data.height-1.75*data.size,anchor="c",text="see more messages",font=("Comic Sans MS","10","bold"))
    #home button
    canvas.create_rectangle(10,10,data.size+10,data.size+10,fill="white",activefill="yellow")
    canvas.create_text(25,25,text="HOME",font=("Comic Sans MS","8","bold"),anchor="center") 
    

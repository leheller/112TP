#Registration page where user creates an account and profile
#from 112TP import login

from tkinter import *
# Basic Animation Framework from 112 website
####################################
# customize these functions
####################################

def init(data):
    data.size = 30
    data.sizeX = 90
    data.sizeY = 30
    data.boxState = (False,"")
    data.username = ""
    data.password = ""
    data.confirmPassword = ""
    data.GPA = ""
    data.school = ""

def mousePressed(event, data):
    if event.x>=data.width//2-data.sizeX and event.x<=data.width//2+data.sizeX:
        if event.y>=data.sizeX and event.y<=data.sizeX+data.sizeY:
            data.boxState = (True,"username")
        elif event.y<=data.sizeX+2.5*data.sizeY and event.y>=data.sizeX+1.5*data.sizeY:
            data.boxState = (True,"password")
        elif event.y>=data.sizeX+3*data.sizeY and event.y<=data.sizeX+4*data.sizeY:
            data.boxState = (True,"confirmPassword")
        else:
            data.boxState = (False, "")
    else:
        data.boxState = (False, "")
        
def keyPressed(event, data):
    if event.keysym == "Return":
        data.boxState == "login"
    elif data.boxState[0] == True and data.boxState[1] == "username":
        data.username += event.char
    elif data.boxState[0] == True and data.boxState[1] == "password":
        data.password += event.char
    elif data.boxState[0] == True and data.boxState[1] == "confirmPassword":
        data.confirmPassword += event.char
        
def redrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    #username box
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX,\
        data.width//2+data.sizeX,data.sizeX+data.sizeY,fill="white",\
        activefill="yellow",width=2)
    #password box
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX+1.5*data.sizeY, data.width//2+data.sizeX,data.sizeX+2.5*data.sizeY,fill="white",activefill="yellow",width=2)
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX+3*data.sizeY, data.width//2+data.sizeX,data.sizeX+4*data.sizeY,fill="white",activefill="yellow",width=2)
    #GPA box
    canvas.create_rectangle(data.width//3-data.sizeX//2,data.sizeX+5.5*data.sizeY, data.width//3+data.sizeX//2,data.sizeX+6.5*data.sizeY,fill="white",activefill="yellow",width=2)
    #create profile text
    canvas.create_text(data.width//2,data.size,anchor="c",font="ComicSans 28 bold",text="Create Profile",fill="white")
    #username
    canvas.create_text(data.width//8,data.sizeX,anchor="c",font="ComicSans 18 bold",text="username:",fill="white")
    #password 
    canvas.create_text(data.width//8,data.sizeX+1.5*data.sizeY,anchor="c",font="ComicSans 18 bold",text="password:",fill="white")
    canvas.create_text(data.width//8,data.sizeX+3*data.sizeY,anchor="c",font="ComicSans 18 bold",text="confirm\npassword:",fill="white")
    #GPA text
    canvas.create_text(data.width//8,data.sizeX+5.8*data.sizeY,anchor="c",font="ComicSans 18 bold",text="GPA:",fill="white")
    #username text
    canvas.create_text(data.width//2,data.sizeX+data.sizeY//2,anchor="c",text=data.username)
    #password text
    canvas.create_text(data.width//2,data.sizeX+2*data.sizeY,anchor="c",text=data.password)
    canvas.create_text(data.width//2,data.sizeX+3.5*data.sizeY,anchor="c",text=data.confirmPassword)
    #GPA text
    canvas.create_text(data.width//3,data.sizeX+6*data.sizeY,anchor="c",text=data.GPA)
    #image box
    canvas.create_rectangle(data.width//2,data.height//2,data.width-data.size,data.height-data.size,fill="black")
    #image text
    canvas.create_text(3*data.width/4-data.size//2,3*data.height/4-data.size//2,anchor="c",text="upload image",fill="white",activefill="yellow")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)

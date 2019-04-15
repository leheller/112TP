#Initial login/register page for when the app is opened

from tkinter import *
# Basic Animation Framework from 112 website
####################################
# customize these functions
####################################

def init(data):
    data.sizeX = 70
    data.sizeY = 20
    data.size = 170
    data.color1 = "white"
    data.color2 = "yellow"
    data.boxState = (False, 0, 0, "")
    data.username = ""
    data.password = ""

def mousePressed(event, data):
    if event.x>=data.width//2-data.sizeX and event.x<=data.width//2+data.sizeX:
        if event.y>=data.height//2-data.sizeY and event.y<=data.height//2+data.sizeY:
            data.boxState = (True, data.width//2, data.height//2, "username")
    if event.x>=data.width//2-data.sizeX and event.x<=data.width//2+data.sizeX:
        if event.y<=data.height//2+3.5*data.sizeY and event.y>=data.height//2+1.5*data.sizeY:
            data.boxState = (True, data.width//2, data.height//2+2.5*data.sizeY, "password")
    if event.x>=data.width//2-30 and event.x<=data.width//2+30:
        if event.y>=data.height//2+data.size-20 and event.y<=data.height//2+data.size+20:
            data.boxState = ("Register")
    else:
        data.boxState = (False, 0, 0)
        
def keyPressed(event, data):
    if event.keysym == "Return":
        data.boxState == "login"
    elif data.boxState[0] == True and data.boxState[3] == "username":
        data.username += event.char
    elif data.boxState[0] == True and data.boxState[3] == "password":
        data.password += event.char
        
def redrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    #username box
    canvas.create_rectangle(data.width//2-data.sizeX,data.height//2-data.sizeY,\
        data.width//2+data.sizeX,data.height//2+data.sizeY,fill="white",\
        activefill="yellow",width=2)
    #password box
    canvas.create_rectangle(data.width//2-data.sizeX,data.height//2+1.5*data.sizeY,\
        data.width//2+data.sizeX,data.height//2+3.5*data.sizeY,fill="white",\
        activefill="yellow",width=2)
    #Seeking@CMU
    canvas.create_text(data.width//2,data.height//2-data.size,anchor="c",\
        font="ComicSans 28 bold",text="Seeking@CMU",fill="white")
    #login
    canvas.create_text(data.width//2,data.height//2-data.sizeX,anchor="c",\
        font="ComicSans 18 bold",text="login",fill="white")
    #register
    canvas.create_text(data.width//2,data.height//2+data.size,anchor="c",\
        font="ComicSans 18 bold",text="register",fill="white",\
        activefill=data.color2)
    #username text
    canvas.create_text(data.width//2,data.height//2,anchor="c",text=data.username)
    #password text
    canvas.create_text(data.width//2,data.height//2+2.5*data.sizeY,anchor="c",text=data.password)

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
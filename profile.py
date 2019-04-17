#Profile page for all of the potential matches

# Basic Animation Framework
from tkinter import *
####################################
#From 112 website
# customize these functions
####################################

def init(data):
    data.username = "Lauren"
    data.GPA = "4.0"
    data.school = "CIT"
    data.bio = "I like to make maple\nsyrup and ski!"
    data.size = 30

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    pass

def redrawAll(canvas, data):
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
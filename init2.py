#Main function to run Seeking@CMU
# Mode Demo
import random
from tkinter import *
from Register import *
from login import *
from home import *
from profile import *
from messaging import *
from dates import *
import socket
import threading
from queue import Queue
####################################
HOST = "" # put your IP address here if playing on multiple computers
PORT = 50003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")

def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8")
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg)
      command = msg.split("\n")
####################################
# init
####################################
def init(data):
    data.mode = "login"
    data.sizeX1 = 70
    data.sizeY1 = 20
    data.size1 = 170
    data.color1 = "white"
    data.color2 = "yellow"
    data.boxState = (False, 0, 0, "")
    data.username1 = ""
    data.password1 = ""
    data.size = 30
    data.sizeX = 90
    data.sizeY = 30
    data.boxState = (False,"")
    data.username = ""
    data.password = ""
    data.confirmPassword = ""
    data.counter = 0
    data.counter2 = 0
    data.profilePic = ""
    data.username = ""
    data.GPA = ""
    data.school = ""
    data.bio = ""
    data.messages = []
    data.myMessages = []
    data.text = ""
    data.messagingProfiles = []
    data.otherProfiles = [["John","3.49","SCS","I like dogs!"],["Bob","4.0","CIT","hi"],["David","2.7","CFA","Just hangin"]]
    data.matchedProfiles = []
    data.myProfile = []
    data.otherStrangers = dict()


####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "login"):   loginMousePressed(event, data)
    elif (data.mode == "Register"): registerMousePressed(event, data)
    elif (data.mode == "home"): homeMousePressed(event, data)
    elif (data.mode == "profile"): profileMousePressed(event, data)
    elif (data.mode == "messaging"): messagingMousePressed(event, data)
    elif (data.mode == "dates"): datesMousePressed(event, data)
    #elif (data.mode == "messaging"):  messagingMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "login"):   loginKeyPressed(event, data)
    elif (data.mode == "Register"): registerKeyPressed(event, data)
    elif (data.mode == "home"): homeKeyPressed(event, data)
    elif (data.mode == "profile"): profileKeyPressed(event, data)
    elif (data.mode == "messaging"): messagingKeyPressed(event, data)
    #elif (data.mode == "messaging"):    messagingKeyPressed(event, data)

def redrawAll(canvas, data):
    if (data.mode == "login"): loginRedrawAll(canvas, data)
    elif (data.mode == "Register"):   registerRedrawAll(canvas, data)
    elif (data.mode == "home"): homeRedrawAll(canvas, data)
    elif (data.mode == "profile"): profileRedrawAll(canvas, data)
    elif (data.mode == "messaging"): messagingRedrawAll(canvas, data)
    elif (data.mode == "dates"): datesRedrawAll(canvas, data)
    #elif (data.mode == "messaging"):       messagingRedrawAll(canvas, data)


####################################
#Run function from 112 website
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
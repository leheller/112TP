#############################
# Sockets Client Demo
# by Rohan Varma
# adapted by Kyle Chin
#############################
from init import *
import socket
import threading
from messaging import *
from queue import Queue

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


from tkinter import *
from message import *
import random
####################################
# customize these functions
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
    data.messages = set()
    data.newMessage = ()
    data.mySent = []
    data.myReceived = []
    data.text = ""
    data.profiles = ()
    data.matches = set()
    data.match = ()
    data.myProfile = ()
    data.image = ""
    data.myMatches = set()
    data.otherProfiles = []

def mousePressed(event, data):
    initMousePressed(event,data)

def keyPressed(event, data):
    initKeyPressed(event,data)

def timerFired(data):
    # timerFired receives instructions and executes them
    while (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)
        print(msg)
        try:
            print("received: ", msg, "\n")
            msg = msg.split("&")
            command = msg[0]
            
            if (command == "NewProfile"):
                myPID = msg[1]
                name = msg[2]
                password = msg[3]
                GPA = msg[4]
                college = msg[5]
                bio = msg[6]
                profile = (name,password,GPA,college,bio)
                data.profiles.add(profile)
                writePickle(data)
                
            elif (command == "Match"):
                myPID = msg[1]
                name1 = msg[2]
                name2 = msg[3]
                day = msg[4]
                time = msg[5]
                place = msg[6]
                match = (name1,name2,day,time,place)
                data.matches.add(match)
                writePickle2(data)
                
            elif (command == "NewMessage"):
                myPID = msg[1]
                name1 = msg[2]
                name2 = msg[3]
                text = msg[4]
                message = (name1,name2,text)
                print("message:", message)
                addMessages(message,data.messages)
                print("bcdhjwibv", data.messages)
                writePickle3(data)
                messageReader(data)
                
        except:
            print("failed")
        serverMsg.task_done()

def redrawAll(canvas, data):
    initRedrawAll(canvas,data)

####################################
# use the run function as-is
####################################

def run(width, height, serverMsg=None, server=None):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.server = server
    data.serverMsg = serverMsg
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

run(500, 500, serverMsg, server)
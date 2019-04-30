#Client file that runs the entire program
###########
#profile_client.py citation comment
#lines 25-199: adapted from sockets client demo by Rohan Varma on 112 website
#lines 47-140: structure still from sockets demo but heavily reconstructed by me
###########
from init import *
from login import *
from Register import *
from schedule import *
from home import *
from profile import *
from messaging import *
from dates import *
import pickle
import socket
import threading
from queue import Queue
from cv2 import *
from tkinter import *
from PIL import ImageTk,Image 
import random 

#Sets up socket stuff
HOST = "" # put your IP address here if playing on multiple computers
PORT = 50003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")
#Receives messages from server
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

#Init for whole program
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
    data.match2 = ()
    data.myProfile = ()
    data.image = ""
    data.myMatches = set()
    data.otherProfiles = []
    data.myImage = ""
    data.profileImage = ""
    data.background = ""
    schedule = {}
    for day in ["Monday:","Tuesday:","Wednesday:","Thursday:","Friday:","Saturday:","Sunday:"]:
        schedule[day] = ""
    data.schedule = schedule

#Mouse pressed for entire program
def mousePressed(event, data):
    data.background = PhotoImage(file = "no-image-event.gif")
    initMousePressed(event,data)

#Keypressed for entire program
def keyPressed(event, data):
    initKeyPressed(event,data)

#Executes instructions from server
def timerFired(data):
    while (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)
        try:
            print("received: ", msg)
            msg = msg.split("&")
            command = msg[0]
            #Recreates and adds new profile to existing profiles
            if (command == "NewProfile"):
                myPID = msg[1]
                name = msg[2]
                password = msg[3]
                GPA = msg[4]
                college = msg[5]
                bio = msg[6]
                schedule = tuple(msg[7:21])
                image = tuple(msg[21:])
                profile = (name,password,GPA,college,bio,schedule,image)
                data.profiles.add(profile)
                writePickle(data)
            #Recreates and adds new match to existing matches    
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
            #Recreates and adds new message to existing messages    
            elif (command == "NewMessage"):
                myPID = msg[1]
                name1 = msg[2]
                name2 = msg[3]
                text = msg[4]
                message = (name1,name2,text)
                data.newMessage = message
                addMessages(data)
        
        except:
           print("failed")
        serverMsg.task_done()

#Draws canvas for entire function
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
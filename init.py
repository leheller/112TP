#Main function to run Seeking@CMU
# Mode Demo
import random
import pickle
from tkinter import *
from Register import *
from login import *
from home import *
from profile import *
from messaging import *
from dates import *
from sorting import *
from cv2 import *
from PIL import ImageTk,Image 
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
    data.otherProfs = set(("John","3.49","CIT","ncjoewbv"),("Bob","2","SCS","hncubiowvhodb2"))
    data.otherProfiles = []
    data.matchedProfiles = []
    data.myProfile = ["","","",""]
    data.image = ""
    data.msg = ""


####################################
# mode dispatcher from 112 website
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
    
def timerFired(data):
    # timerFired receives instructions and executes them
    while (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)
        print(msg)
        try:
            print("received: ", msg, "\n")
            #New profile recieved (only adds to profile set if its not my profile)
            if type(msg) == list:
                if data.myProfile == msg:
                    pass
                else:
                    data.otherProfs += tuple(msg)
            else:
                msg = msg.split()
                command = msg[0]
    
                if (command == "myIDis"):
                    myPID = msg[1]
                    data.me.changePID(myPID)
    
                elif (command == "playerWrote"):
                    PID = msg[1]
                    text = msg[2]
                    data.otherStrangers[PID].writeText(text)
            
                elif (command == "playerMatched"):
                    PID = msg[1]
                    dx = int(msg[2])
                    dy = int(msg[3])
                    data.otherStrangers[PID].move(dx, dy)
          
        except:
            print("failed")
        serverMsg.task_done()


####################################
#Run function from 112 website
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

run(400, 400, serverMsg, server)

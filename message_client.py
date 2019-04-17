#############################
# Sockets Client Demo
# by Rohan Varma
# adapted by Kyle Chin
#############################

import socket
import threading
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
    data.me = Message("Lauren",data.width//2,data.height//2)
    data.otherStrangers = dict()
    data.text = ""

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    dx, dy = 0, 0
    msg = ""
    directions = ["Up", "Down", "Left", "Right"]
    #moving
    if event.keysym in directions:
        speed = 5
        if event.keysym == "Up":
            dy = -speed
        elif event.keysym == "Down":
            dy = speed
        elif event.keysym == "Left":
            dx = -speed
        elif event.keysym == "Right":
            dx = speed
        # move myself
        data.me.move(dx, dy)
        # update message to send
        msg = "playerMoved %d %d\n" % (dx, dy)

    #writing text
    elif (event.keysym not in directions) and (event.keysym != "space"):
        text = event.keysym
        data.me.writeText(text)
        msg = "playerWrote " + str(text) + "\n"

    #writing spaces
    elif (event.keysym == "space"):
        text = " "
        data.me.writeText(text)
        msg = "playerWrote " + str(data.text) + "\n"

    # send the message to other players!
    if (msg != ""):
        print ("sending: ", msg,)
        data.server.send(msg.encode())

def timerFired(data):
    # timerFired receives instructions and executes them
    while (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)
        print(msg)
        try:
            print("received: ", msg, "\n")
            msg = msg.split()
            command = msg[0]

            if (command == "myIDis"):
                myPID = msg[1]
                data.me.changePID(myPID)

            elif (command == "newPlayer"):
                newPID = msg[1]
                x = data.width/2
                y = data.height/2
                data.otherStrangers[newPID] = Message(newPID, x, y)

            elif (command == "playerWrote"):
                PID = msg[1]
                text = msg[2]
                data.otherStrangers[PID].writeText(text)
          
            elif (command == "playerMoved"):
                PID = msg[1]
                dx = int(msg[2])
                dy = int(msg[3])
                data.otherStrangers[PID].move(dx, dy)
          
        except:
            print("failed")
        serverMsg.task_done()

def redrawAll(canvas, data):
    # draw other players
    for playerName in data.otherStrangers:
        data.otherStrangers[playerName].drawMessage(canvas, "blue")
    # draw me
    data.me.drawMessage(canvas, "red")

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

run(400, 400, serverMsg, server)

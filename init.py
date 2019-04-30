#Init file contains mode dispatcher
###########
#profile_server.py citation comment
#lines 23-50: adapted from mode dispatcher demo from 112 website
###########
import random
import pickle
from tkinter import *
from Register import *
from schedule import *
from login import *
from home import *
from profile import *
from messaging import *
from dates import *
from cv2 import *
from pickleFile import *
from PIL import ImageTk,Image 
import socket
import threading
from queue import Queue

def initMousePressed(event, data):
    if (data.mode == "login"):  loginMousePressed(event, data)
    elif (data.mode == "Register"): registerMousePressed(event, data)
    elif (data.mode == "schedule"): scheduleMousePressed(event, data)
    elif (data.mode == "home"): homeMousePressed(event, data)
    elif (data.mode == "profile"): profileMousePressed(event, data)
    elif (data.mode == "messaging"): messagingMousePressed(event, data)
    elif (data.mode == "dates"): datesMousePressed(event, data)

def initKeyPressed(event, data):
    if (data.mode == "login"):   loginKeyPressed(event, data)
    elif (data.mode == "Register"): registerKeyPressed(event, data)
    elif (data.mode == "schedule"): scheduleKeyPressed(event, data)
    elif (data.mode == "home"): homeKeyPressed(event, data)
    elif (data.mode == "profile"): profileKeyPressed(event, data)
    elif (data.mode == "messaging"): messagingKeyPressed(event, data)

def initRedrawAll(canvas, data):
    if (data.mode == "login"): 
        img = Image.open("Logo.png")
        data.img = ImageTk.PhotoImage(img) 
        loginRedrawAll(canvas, data)
    elif (data.mode == "Register"):   registerRedrawAll(canvas, data)
    elif (data.mode == "schedule"): scheduleRedrawAll(canvas, data)
    elif (data.mode == "home"): homeRedrawAll(canvas, data)
    elif (data.mode == "profile"): profileRedrawAll(canvas, data)
    elif (data.mode == "messaging"): messagingRedrawAll(canvas, data)
    elif (data.mode == "dates"): datesRedrawAll(canvas, data)

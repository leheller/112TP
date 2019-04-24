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
from pickleFile import *
from PIL import ImageTk,Image 
import socket
import threading
from queue import Queue
####################################
# mode dispatcher from 112 website
####################################


def initMousePressed(event, data):
    if (data.mode == "login"):   loginMousePressed(event, data)
    elif (data.mode == "Register"): registerMousePressed(event, data)
    elif (data.mode == "home"): homeMousePressed(event, data)
    elif (data.mode == "profile"): profileMousePressed(event, data)
    elif (data.mode == "messaging"): messagingMousePressed(event, data)
    elif (data.mode == "dates"): datesMousePressed(event, data)

def initKeyPressed(event, data):
    if (data.mode == "login"):   loginKeyPressed(event, data)
    elif (data.mode == "Register"): registerKeyPressed(event, data)
    elif (data.mode == "home"): homeKeyPressed(event, data)
    elif (data.mode == "profile"): profileKeyPressed(event, data)
    elif (data.mode == "messaging"): messagingKeyPressed(event, data)

def initRedrawAll(canvas, data):
    if (data.mode == "login"): loginRedrawAll(canvas, data)
    elif (data.mode == "Register"):   registerRedrawAll(canvas, data)
    elif (data.mode == "home"): homeRedrawAll(canvas, data)
    elif (data.mode == "profile"): profileRedrawAll(canvas, data)
    elif (data.mode == "messaging"): messagingRedrawAll(canvas, data)
    elif (data.mode == "dates"): datesRedrawAll(canvas, data)

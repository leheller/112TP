#Registration page where user creates an account and profile
###########
#Register.py citation comment
#basic animation framework from 112 website
#lines 11-34: original code
#lines 37-61: found on stackoverflow (https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv)
#lines 62-65: cv2 modules found in openCV library (can be found at https://docs.opencv.org/3.2.0/d4/da8/group__imgcodecs.html)
#lines 65-208: original code
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

#Determines if the passwords match and that all fields are filled in
def checkPassword(data):
    if data.password != data.confirmPassword:
        return "passwords must match!>:("
    elif data.password == "" or data.username == "" or data.bio == "" or data.GPA == "" or data.school == "" or data.image == "":
        return "please fill in all fields"
    else: return True

#The code in this function is from stackoverflow (https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv)
#Takes an image and saves it to init
def takePicture(data):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Seeking@CMU")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        i = cv2.resize(frame,(240,240))
        cv2.imshow("Seeking@CMU", i)
        #cv2.resizeWindow("Seeking@CMU", 20,20)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    im = Image.open(img_name).convert('LA')
    cropped = im.crop([520, 270, 760, 510])
    data.image = ImageTk.PhotoImage(cropped) 
    data.imageName = img_name

def registerMousePressed(event, data):
    if event.x>=data.width//2-data.sizeX and event.x<=data.width//2+data.sizeX and event.y<data.height//2:
        if event.y>=data.sizeX and event.y<=data.sizeX+data.sizeY:
            data.boxState = (True,"username")
        elif event.y<=data.sizeX+2.5*data.sizeY and event.y>=data.sizeX+1.5*data.sizeY:
            data.boxState = (True,"password")
        elif event.y>=data.sizeX+3*data.sizeY and event.y<=data.sizeX+4*data.sizeY:
            data.boxState = (True,"confirmPassword")
        else:
            data.boxState = (False, "")
    elif event.x>=data.width//3-data.sizeX//2 and event.x<=data.width//3+data.sizeX//2 and event.y<data.height-data.size:
        if event.y>=data.sizeX+5.5*data.sizeY and event.y<=data.sizeX+6.5*data.sizeY:
            data.boxState = (True,"GPA")
        elif event.y>=data.sizeX+7*data.sizeY and event.y<=data.sizeX+8*data.sizeY:
            data.boxState = (True,"school")
    elif event.y>=data.height//2 and event.x>=data.width//2:
        takePicture(data)
    elif event.y>=data.sizeX+8.5*data.sizeY:
        if event.x<=data.width//3+2*data.sizeX//3:
            data.boxState = (True,"bio")  
    elif event.x>=3*data.width//4 and event.x<=3*data.width//4+2*data.size:
        if event.y<=data.height//4+2*data.size and event.y>=data.height//4:
            if checkPassword(data) == True:
                data.mode = "schedule"
    else:
        data.boxState = (False, "")
        
def registerKeyPressed(event, data):
    if event.keysym == "Return":
        data.boxState == "login"
    elif data.boxState[0] == True and data.boxState[1] == "username":
        if event.keysym == "BackSpace":
            data.username = data.username[:-1]
        elif len(data.username)>22:
            pass
        else:
            data.username += event.char
    elif data.boxState[0] == True and data.boxState[1] == "password":
        if event.keysym == "BackSpace":
            data.password = data.password[:-1]
        elif len(data.password)>22:
            pass
        else:
            data.password += event.char
    elif data.boxState[0] == True and data.boxState[1] == "confirmPassword":
        if event.keysym == "BackSpace":
            data.confirmPassword = data.confirmPassword[:-1]
        elif len(data.confirmPassword)>22:
            pass
        else:
            data.confirmPassword += event.char
    elif data.boxState[0] == True and data.boxState[1] == "GPA":
        if event.keysym == "BackSpace":
            data.GPA = data.GPA[:-1]
        elif len(data.GPA)>4:
            pass
        elif event.char in "1234567890.":
            data.GPA += event.char
    elif data.boxState[0] == True and data.boxState[1] == "school":
        if event.keysym == "BackSpace":
            data.school = data.school[:-1]
        elif len(data.school)>14:
            pass
        else:
            data.school += event.char
    elif data.boxState[0] == True and data.boxState[1] == "bio":
        if event.keysym == "BackSpace":
            data.bio = data.bio[:-1]
            data.counter -= 1
        else:
            if event.char == "&":
                pass
            elif len(data.bio) > 120:
                pass
            elif len(data.bio) % 20 == 0:
                data.bio += "\n"
            else:
                data.bio += event.char
                data.counter += 1
                
def registerRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    canvas.create_image(0,0,anchor="nw",image=data.background)
    #continue
    canvas.create_text(3*data.width//4+data.size,data.height//4+data.size,anchor="c",text="continue",font=("Comic Sans MS","16","bold"),fill="white",activefill="yellow")
    #username box
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX,\
        data.width//2+data.sizeX,data.sizeX+data.sizeY,fill="white",\
        activefill="yellow",width=2)
    #password box
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX+1.5*data.sizeY, data.width//2+data.sizeX,data.sizeX+2.5*data.sizeY,fill="white",activefill="yellow",width=2)
    canvas.create_rectangle(data.width//2-data.sizeX,data.sizeX+3*data.sizeY, data.width//2+data.sizeX,data.sizeX+4*data.sizeY,fill="white",activefill="yellow",width=2)
    #GPA box
    canvas.create_rectangle(data.width//3-data.sizeX//2,data.sizeX+5.5*data.sizeY, data.width//3+data.sizeX//2,data.sizeX+6.5*data.sizeY,fill="white",activefill="yellow",width=2)
    #college box
    canvas.create_rectangle(data.width//3-2*data.sizeX//3,data.sizeX+7*data.sizeY, data.width//3+2*data.sizeX//3,data.sizeX+8*data.sizeY,fill="white",activefill="yellow",width=2)
    #bio box
    canvas.create_rectangle(data.sizeX//2,data.sizeX+8.5*data.sizeY,data.width//3+2*data.sizeX//3,data.height-data.size,fill="white",activefill="yellow",width=2)
    #create profile text
    canvas.create_text(data.width//2,data.size,anchor="c",font=("Comic Sans MS","28","bold"),text="Create Profile",fill="white")
    #username
    canvas.create_text(data.width//8,data.sizeX,anchor="c",font=("Comic Sans MS","18","bold"),text="andrew ID:",fill="white")
    #password 
    canvas.create_text(data.width//8,data.sizeX+1.5*data.sizeY,anchor="c",font=("Comic Sans MS","18","bold"),text="password:",fill="white")
    canvas.create_text(data.width//8,data.sizeX+3*data.sizeY,anchor="c",font=("Comic Sans MS","18","bold"),text="confirm\npassword:",fill="white")
    #GPA 
    canvas.create_text(data.width//8,data.sizeX+5.8*data.sizeY,anchor="c",font=("Comic Sans MS","18","bold"),text="GPA:",fill="white")
    #college
    canvas.create_text(data.width//9,data.sizeX+7.5*data.sizeY,anchor="c",font=("Comic Sans MS","18","bold"),text="school:",fill="white")
    #Bio
    canvas.create_text(10,data.sizeX+9*data.sizeY,anchor="w",font=("Comic Sans MS","18","bold"),text="bio:",fill="white")
    #username text
    canvas.create_text(data.width//2,data.sizeX+data.sizeY//2,anchor="c",text=data.username)
    #password text
    canvas.create_text(data.width//2,data.sizeX+2*data.sizeY,anchor="c",text="*"*len(data.password))
    canvas.create_text(data.width//2,data.sizeX+3.5*data.sizeY,anchor="c",text="*"*len(data.confirmPassword))
    #GPA text
    canvas.create_text(data.width//3,data.sizeX+6*data.sizeY,anchor="c",text=data.GPA)
    #college text
    canvas.create_text(data.width//3,data.sizeX+7.5*data.sizeY,anchor="c",text=data.school)
    #bio text
    canvas.create_text(data.sizeX//2+10,data.sizeX+8.5*data.sizeY,anchor="nw",text=data.bio,fill="black")
    #image text
    canvas.create_rectangle(data.width//2,data.height//2,data.width-data.size,data.height-data.size,fill="black")
    canvas.create_oval(2.3*data.size+data.width//2,data.size+data.height//2,data.width-3.5*data.size,data.height//2+3.5*data.size,width=3,outline="white")
    canvas.create_line(355,data.height//2+3.5*data.size,355,data.height-data.size,width=3,fill="white")
    canvas.create_line(355,data.height//2+120,300,data.height//2+160,width=3,fill="white")
    canvas.create_line(355,data.height//2+120,400,data.height//2+160,width=3,fill="white")
    canvas.create_text(355,data.height//2+60,anchor="center",text="O   O",font=("32"),fill="white")
    canvas.create_line(335,data.height//2+80,355,data.height//2+90,375,data.height//2+80,smooth=1,width=3,fill="white")
    canvas.create_text(3*data.width/4+data.size,8*data.height//9,anchor="c",text="       upload image\n(SPACE to take picture\n     ESC to return)",fill="white",activefill="yellow",font=("Comic Sans MS","8","bold"))
    #Error box
    if checkPassword(data) == "passwords must match!>:(":
        canvas.create_rectangle(data.width-2*data.size,0,data.width,2*data.size,fill="red")
        canvas.create_text(data.width-2*data.size,data.size,anchor="w",text="passwords\nmust\nmatch!",font=("Comic Sans MS","12","bold"))
    elif checkPassword(data) == "please fill in all fields":
        canvas.create_rectangle(data.width-3*data.size,0,data.width,2*data.size,fill="red")
        canvas.create_text(data.width-3*data.size,data.size,anchor="w",text="please fill in\nall fields",font=("Comic Sans MS","12","bold"))
    #image box
    try: 
        canvas.create_image(data.width//2, data.height//2, anchor="nw", image=data.image)
    except: pass
    
    
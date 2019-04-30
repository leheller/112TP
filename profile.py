#Profile page for all of the potential matches
from pickleFile import *
from messaging import *
from tkinter import *
import random
from cv2 import *
from PIL import ImageTk,Image 

def createSchedule(s):
    s = s.split('&')
    d = {}
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "":
                s.pop(i)
            else:
                d[s[i]] = s[i+1]
    return d
    
def matchSchedules(data):
    sched1 = createSchedule(data.myProfile[5])
    sched2 = createSchedule(data.otherProfiles[0][5])
    closestTime = 100
    for day in sched1:
        time1 = ""
        for c in sched1[day]:
            if c in "1234567890":
                time1 += c
        time1 = int(time1)
        time2 = "  "
        for c in sched2[day]:
            if c in "1234567890":
                time2 += c
        time2 = int(time2)
        if sched1[day] == sched2[day]:
            return day[:-1] + "  ",sched1[day]
        elif abs(time1-time2) < closestTime:
            closestTime = time1 + abs(time1-time2)//2
            closestDay = day[:-1] + "  "
    return closestDay, str(closestTime)

def recreate(data, s):
    s = s.split('&')
    for i in range(len(s)):
            if s[i] == "":
                s.pop(i)
            else:
                t = (int(s[i]),255) 
                s[i] = t
    im2 = Image.new('LA',(240,240))
    im2.putdata(s)
    return ImageTk.PhotoImage(im2)

def profileMousePressed(event, data):
    if (event.x>=10) and (event.y>=2*data.size+data.height//2) and (event.x<=data.width//3-10) and (event.y<=data.height-2*data.size):
        place = random.choice(["  iNoodle","  the Fence","  Walking to the Sky","  Sorrels","  ABP","  CFA Lawn","  the Exchange","  Number Garden","  Doherty 2315","  Donner Dungeon"])
        day,time = matchSchedules(data)
        data.match = (data.myProfile[0],data.otherProfiles[0][0],day,time,place)
        data.matches.add(data.match)
        writePickle2(data)
        setToString2(data,data.match)
        writePickle2(data)
    elif event.x>=10 and event.x<=data.size+10:
        if event.y>=10 and event.y<=data.size+10:
            data.mode = "home"
    elif event.x>=10+data.width//3 and event.x<=2*data.width//3-10:
        if event.y>=2*data.size+data.height//2 and event.y<=data.height-2*data.size:
            writePickle3(data)
            data.newMessage = (data.username,data.otherProfiles[0][0],"Hi!")
            addMessages(data)
            setToString3(data,data.newMessage)
    elif event.x>=2*data.width//3+10 and event.x<=10+2*data.width//3+3.5*data.size:
        if event.y>=2*data.height//3 and event.y<=5*data.height//6:
            if len(data.otherProfiles) > 1:
                pop = data.otherProfiles.pop(0)
                data.otherProfiles.append(pop)
                data.profileImage = recreate(data, data.otherProfiles[0][6])
        
def profileKeyPressed(event, data):
    pass

def profileRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="green")
    canvas.create_image(0,0,anchor="nw",image=data.background)
    if len(data.otherProfiles) > 0:
        #Name
        canvas.create_rectangle(data.width//2+5,10,data.width-10,data.height//2,fill="white")
        canvas.create_text(data.width//2+10,data.size,anchor="nw",font=("Comic Sans MS","24","bold"),text="AndrewID: "+data.otherProfiles[0][0])
        #Picture
        try:
            canvas.create_image(10, 10, anchor="nw", image=data.profileImage)
        except: 
            canvas.create_rectangle(10,10,data.width//2,data.height//2,fill="black")
            canvas.create_oval(120-40,80-40,160,120,width=3,outline="white")
            canvas.create_line(120,120,120,250,width=3,fill="white")
            canvas.create_line(120,140,200,200,width=3,fill="white")
            canvas.create_line(120,140,40,200,width=3,fill="white")
            canvas.create_text(120,70,anchor="center",text="O   O",font=("32"),fill="white")
            canvas.create_line(100,90,120,110,140,90,smooth=1,width=3,fill="white")
        #GPA
        canvas.create_text(data.width//2+10,2.5*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="GPA: "+data.otherProfiles[0][2])
        #College
        canvas.create_text(data.width//2+10,4*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="School: "+data.otherProfiles[0][3])
        #Bio
        canvas.create_text(data.width//2+10,5.5*data.size,anchor="nw",font=("Comic Sans MS","16","bold"),text="Bio: "+data.otherProfiles[0][4])
        #Go on a date
        canvas.create_rectangle(10,2*data.size+data.height//2,data.width//3-10,data.height-2*data.size,fill=data.color1,activefill="yellow")
        canvas.create_text(data.width//5-data.size//2,4*data.height//5-data.size,anchor="c",text="ask "+data.otherProfiles[0][0]+" on a date",font=("Comic Sans MS","12","bold"))
        #Message
        canvas.create_rectangle(10+data.width//3,2*data.size+data.height//2,2*data.width//3-10,data.height-2*data.size,fill="white",activefill="yellow")
        canvas.create_text(data.width//2,4*data.height//5-data.size,anchor="c",text="message "+data.otherProfiles[0][0],font=("Comic Sans MS","12","bold"))
        #Next
        canvas.create_polygon(2*data.width//3+10,data.height-3.5*data.size,10+2*data.width//3,data.height-5*data.size,10+2*data.width//3+2*data.size,data.height-5*data.size,10+2*data.width//3+2*data.size,data.height-6*data.size,10+2*data.width//3+3.5*data.size,data.height-4.25*data.size,10+2*data.width//3+2*data.size,data.height-2.5*data.size,10+2*data.width//3+2*data.size,data.height-3.5*data.size,fill="white",activefill="yellow")
        canvas.create_text(2.3*data.width//3+10,data.height-4.25*data.size,anchor="c",text="see more CMU singles",font=("Comic Sans MS","10","bold"))
        #Home
        canvas.create_rectangle(10,10,data.size+10,data.size+10,fill="white",activefill="yellow")
        canvas.create_text(25,25,text="HOME",font=("Comic Sans MS","8","bold"),anchor="center")   
    else:
        canvas.create_text(data.width//2,data.height//2,anchor="center",font=("Comic Sans MS","20","bold"),text="NO OTHER USERS")
        #Home
        canvas.create_rectangle(10,10,data.size+10,data.size+10,fill="white",activefill="yellow")
        canvas.create_text(25,25,text="HOME",font=("Comic Sans MS","8","bold"),anchor="center")  
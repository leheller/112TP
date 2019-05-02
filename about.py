#Tells the user about my program
###########
#about.py citation comment
#basic animation framework from 112 website
#lines 7-27: original code
###########
from tkinter import *

def aboutMousePressed(event, data):
    if event.x>=10 and event.x<=data.size+10:
        if event.y>=10 and event.y<=data.size+10:
            data.mode = "home"

def aboutKeyPressed(event, data):
    pass

def aboutRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="forestgreen")
    canvas.create_image(160, 10, anchor="nw", image=data.logo)
    canvas.create_text(250,270,anchor="n",fill="white",font=("Comic Sans MS","17","bold"),text="For the everyday, busy Carnegie Mellon student\n         who still hopes for a love life:")
    canvas.create_text(4,320,anchor="nw",fill="GoldenRod1",font=("Comic Sans MS","12","bold"),text="Look no further! Seeking@CMU offers one-of-a-kind matchmaking based off of\nthe most important qualities of a person: GPA and area of study. If we've found\nsomeone perfectly compatible with you, then a supermatch will appear in your upcoming\ndates. If your ideal partner isn't as similar to yourself, have no fear. Simply search\nthrough profiles of other CMU students and find your special someone. Once you've\nfound a potential partner, shoot them a message, ask them on a date, or both! To\nprotect your pride, nobody will see your message and/or date proposal until they do\nthe same. We know, you're busy. How will you manage finishing your problem set,\nwriting your paper, doing your 112 homework, AND planning a hot date? That's why\nwe do all of the hard work for you. No planning necessary. To be inclusive of all\ngenders, Seeking@CMU has no features based on gender. Have fun!")
    canvas.create_rectangle(10,10,data.size+10,data.size+10,fill="white",activefill="yellow")
    canvas.create_text(25,25,text="HOME",font=("Comic Sans MS","8","bold"),anchor="center") 
    canvas.create_text(350,10,fill="white",font=("Comic Sans MS","10","bold"),text="Seeking@CMU\ncreated by\nLauren Heller\n15-112 Spring 2019",anchor="nw")
    canvas.create_text(10,2*data.size,text='"I would rather share one\nlifetime with you than face all\nthe ages of this world alone"\n- Seeking@CMU User',fill="white",font=("Comic Sans MS","10","bold"),anchor="nw")
    canvas.create_text(10,5*data.size,text='"Its so easy to fall in love\nbut hard to find someone who\nwill catch you."\n- Seeking@CMU User',fill="white",font=("Comic Sans MS","10","bold"),anchor="nw")

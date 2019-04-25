from cv2 import *
from PIL import Image
messages = {("Lauren","Bob","hi"),("Bob","Lauren","aloha","whats good?"),("Dan","Lauren","hehehe"),("Sophie","Steph","lol")}
def messageReader(set):
    myName = "Lauren"
    mySent = []
    myReceived = []
    for message in set:
        if message[0] == myName: 
            mySent += [message]
        elif message[1] == myName:
            myReceived += [message]
    return myReceived

def messageReaderReverse(data, oneMessage):
    otherName = oneMessage[1]
    for message in data.messages:
        if message[0] == otherName:
            messages = message[2:]
    return messages
    

messages = {("Lauren","Bob","hi"),("Bob","Lauren","aloha","whats good?"),("Dan","Lauren","hehehe"),("Sophie","Steph","lol")}
newMessage = ("Bob","Lauren","heyyy")
def addMessages(list, messages):
    person1 = list[0]
    person2 = list[1]
    text = list[2]
    for message in messages:
        if message[0] == person1 and message[1] == person2:
            messages.remove(message)
            message2 = [message[0],message[1]]
            for texts in message[2:]:
                message2 += [texts]
            message2 += [text]
            message = tuple(message2)
            messages.add(message)
            break
    print(messages)
    
addMessages(newMessage,messages)
    
    
def processPicture(image):
    img = Image.open(image)
    cropped = img.crop([520, 270, 760, 510])
    cropped.show()
    data = list(cropped.getdata())
    return data

list = processPicture("opencv_frame_0.png")  

def createImage(list):
    im2 = Image.new("RGB",(240,240))
    im2.putdata(list)
    im2.show()
    
createImage(list)

def sendImage(list):
    for px in list:
        pass




         
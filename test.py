from cv2 import *
from PIL import Image
    
def processPicture(image):
    img = Image.open(image)
    cropped = img.crop([520, 270, 760, 510]).convert('LA')
    data = list(cropped.getdata(0))
    s = ""
    for px in data:
        s += str(px) + "&"
    return s
    
list = processPicture("opencv_frame_0.png")  

def createImage(list):
    im2 = Image.new('LA',(240,240))
    im2.putdata(list)
    im2.show()
    

def recreate(s):
    s = s.split('&')
    for i in range(len(s)):
        if s[i] == "":
            s.pop(i)
        else:
            t = (int(s[i]),255) 
            s[i] = t
    im2 = Image.new('LA',(240,240))
    im2.putdata(s)
    im2.show()
    return im2

    
recreate(list)
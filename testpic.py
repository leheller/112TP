from cv2 import *
from tkinter import *
from PIL import ImageTk,Image  
import os

def takePicture():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("seeking@CMU")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
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
    #Next few lines inspired from online (https://stackoverflow.com/questions/52375035/cropping-an-image-in-tkinter/52375463#52375463)
    im = Image.open(img_name)
    cropped = im.crop([520, 270, 760, 510])
    return ImageTk.PhotoImage(cropped) 
    
def processPicture():
    image = cv2.imread(takePicture())
    y=image.shape[0] #length in first dimension
    x=image.shape[1] #length in second dimension
    pixels = ()
    for i in range(0,y):
        for j in range(0,x):
            pixels += image[i][j] 
    print(pixels) 
          

def draw(canvas,width,height): 
    img = PhotoImage(file="opencv_frame_0.png")
    img2 = ImageTk.PhotoImage(img) 
    # canvas.create_rectangle(0,0,100,100,fill="red")
    canvas.create_image(0, 0, anchor="nw", image=img2)

def runDrawing(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing(500, 500)
##########################
# Message Class
# by Lauren
##########################

class Message(object):

    def __init__(self, PID, x, y):
        self.PID = PID
        self.text = ""
        self.size = 100
        self.x = x
        self.y = y

    def changePID(self, PID):
        self.PID = PID
        
    def writeText(self,text):
        self.text += text
        if len(self.text) > 25:
            self.text = self.text[1:]
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def drawMessage(self, canvas, color):
        canvas.create_rectangle(self.x-self.size,self.y-self.size,\
        self.x+self.size,self.y+self.size,fill=color)
        canvas.create_text(self.x,self.y,text=self.text)




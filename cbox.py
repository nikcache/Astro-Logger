#Checkbox class

from graphics import *

class checkbox:
    
    def __init__(self, x, y, vwin, text):
        self.box = Rectangle(Point((x+10),(y+10)),Point((x-10),(y-10)))
        self.box.setFill("white")
        self.box.draw(vwin)
        self.xmax, self.xmin = x+10, x-10
        self.ymax, self.ymin = y+10, y-10
        self.boxCol = False
        self.text = Text(Point(x, y), text)
        self.text.draw(vwin)

    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        if(p.getX() >= self.xmin and p.getX() <= self.xmax and p.getY() >= self.ymin\
           and p.getY() <= self.ymax):
            if (self.boxCol == True):
                self.box.setFill("white")
                self.boxCol = False
            else:
                self.box.setFill("green")
                self.boxCol = True
            return (p.getX() >= self.xmin and p.getX() <= self.xmax and p.getY() >= self.ymin\
                    and p.getY() <= self.ymax)

    def getVal(self):
        return self.boxCol

    def setTrue(self):
        self.isClicked(Point(self.xmax, self.ymax))
        

#Nik G and Charlie S
#Button Class
#9th of November, 2018

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        #win is the window its drawn in, center a point, width of button, height of button, and lable on the button
        
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        #first point and second points coordinated defined here
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h

        #Points actually created using above variable
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        #Rectangle then drawn with two points
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)

        #Label then drawn in the center of drawn rectangle
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate() ##this line was not there in class, what does it do?

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill("darkgray") ##color the text "darkgray"
        self.rect.setWidth(1) ##set the outline to look finer/thinner
        self.active = False ##set the boolean variable that tracks "active"-ness to False

    ##check 4.  complete the clicked() method
    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        return (self.active) and (p.getX() >= self.xmin and p.getX() <= self.xmax and p.getY() >= self.ymin\
                            and p.getY() <= self.ymax)

    
# def main():
#     ##check 2. create a graphical window in which to test the Button class
#     win = GraphWin("Button", 600, 600)

    
#     ##check 3. test the Button constructor method...
#     rButton = Button(win, Point(300, 100), 75, 30, "Roll")
#     qButton = Button(win, Point(300, 500), 50, 20, "Quit")
#     ##create two Button objects, one for "Roll Dice" and the other for "Quit"
#     ##activate the Roll button
#     rButton.activate()

#     ##check 4. now test the deactivate() method...
#     ##deactivate the "Quit" button
#     qButton.deactivate()

#     pt = win.getMouse()

#     while not (qButton.isClicked(pt)):
#         pt = win.getMouse()
#         if rButton.isClicked(pt):
#             print("roll button clicked")
#             qButton.activate()
# ##    if rButton.isClicked(pt):
# ##        print("roll button clicked")
#     ##check 5. test the .clicked() method with an if statement
#     ##(remove this test code before moving onto the next check)

#     ##check 6: 
#     ##loop until the "Quit" button is clicked...
#         ##if the roll button is clicked
#             ##activate the quit button
#         ##take the next mouse click
            
        
#     #we reach this line of code when quit button is clicked b/c loop condition breaks
#     win.close() #so close the window, ending the program
    
# if __name__ == "__main__": 
#     main()

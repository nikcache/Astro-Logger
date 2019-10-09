from graphics import *

box_list = []

def entryBox(x, y, width, text, vwin):
    ent1 = Entry(Point(x, y), width)
    ent1.setText(text)
    box_list.append(ent1)
    ent1.draw(vwin)

def BoxList():
    return box_list
from graphics import *

def txt(text, x, y, vwin, size, color, style):
    tx1 = Text(Point(x, y), text)
    tx1.setFill(color)
    tx1.setStyle(style)
    tx1.setSize(size)
    tx1.draw(vwin)

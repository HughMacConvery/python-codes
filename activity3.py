def drawHorizLine(picture,yValue):
  for p in getPixels(picture):
    y=getY(p)
    if (y == yValue):
      p.setColor(makeColor(0,0,0))

def drawbox(picture,startx, starty, boxwidth, boxheight):
  for p in getPixels(picture):
    x = getX(p)
    y = getY(p)
    if (starty <= y < starty + boxheight) and (startx <= x < startx + boxwidth):
      p.setColor(makeColor(0,0,0))
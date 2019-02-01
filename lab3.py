#Jacy MacConvery, Vinay Chandra
def drawBoxLine(picture,startx, starty, boxwidth, boxheight):
  for p in getPixels(picture):
    x = getX(p)
    y = getY(p)
    if (y == starty) and (startx < x < startx + boxwidth):
      p.setColor(makeColor(0,0,0)) 
    if(x == startx) and (starty < y < starty + boxheight):
      p.setColor(makeColor(0,0,0))
    if(x == startx + boxwidth) and (starty < y < starty + boxheight):
      p.setColor(makeColor(0,0,0))
    if (y == starty + boxheight) and (startx < x <startx + boxwidth):
      p.setColor(makeColor(0,0,0))
      
def authenticate(picture1,picture2):
  result = makeEmptyPicture(getWidth(picture1),getHeight(picture1))
  pixel1 = getPixels(picture1)
  pixel2 = getPixels(picture2)
  pixel3 = getPixels(result)
  if len(pixel1) == len(pixel2):
    for i in range(0,len(pixel1)):
      c1 = getColor(pixel1[i]) 
      c2 = getColor(pixel2[i])
      if c1 != c2:
        setColor(pixel3[i],makeColor(0,0,0)) 
  else:
    result = makeEmptyPicture(getWidth(pictuer1),getHeight(picture1))
    for p in getPixels(result):
      setColor(p,makeColor(0,0,0))
  return result
      
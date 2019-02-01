# Jacy MacConvery, Jazmine Williams
def flip(picture):
  result = makeEmptyPicture(getWidth(picture),getHeight(picture))
  width = getWidth(picture)
  height = getHeight(picture)
  for x in range(0, width):
    for y in range(0, height):
      p1 = getPixel(picture,x ,y)
      p2 = getPixel(result, width - x - 1, y)
      setColor(p2, getColor(p1))
  return result

def overlay(picture, background, x, y):
  result = duplicatePicture(background)  
  width = getWidth(picture)
  height = getHeight(picture)
  for i in range(0, width):
    for j in range(0, height):
      p1 = getPixel(picture, i, j)
      p2 = getPixel(result,x+i,y+j)
      setColor(p2,getColor(p1))
  return result
  
def triangelCrop(picture, x, y, h):
  result = makeEmptyPicture(h,h) 
  for i in range(0,h):
    for j in range(i):
      p1 = getPixel(picture, x+i, y+j)
      p2 = getPixel(result,j,i)
      setColor(p2,getColor(p1))
  return result
  
# squish vertically  
def squishV(picture):
  result = makeEmptyPicture(getWidth(picture),getHeight(picture))
  width = getWidth(picture)
  height = getHeight(picture)
  for y in range(0,height, 2):
    for x in range(0, width):
      p1 = getPixel(picture,x ,y)
      p2 = getPixel(result, x, y/2)
      setColor(p2, getColor(p1))
  return result
  
# squish horizontally
def squishH(picture):
  result = makeEmptyPicture(getWidth(picture),getHeight(picture))
  width = getWidth(picture)
  height = getHeight(picture)
  for x in range(0,width, 2):
    for y in range(0, height):
      p1 = getPixel(picture,x ,y)
      p2 = getPixel(result, x/2, y)
      setColor(p2, getColor(p1))
  return result  
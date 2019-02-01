def draw(picture, startX, endX, startY, endY):
  for y in range(startY, endY,2):
    for x in range(startX, endX):
      p = getPixel(picture,x,y)
      setColor(p,makeColor(0,0,0))
    
def crop(picture, x, y, w, h):
  result = makeEmptyPicture(w,h)
  for i in range(0,w):
    for j in range(0,h):
      p1 = getPixel(picture,x+i,y+j)
      p2 = getPixel(result,i,j)
      setColor(p2,getColor(p1))
  return result
def switchRegions(picture,w,h,x1,y1,x2,y2):
  for x in range(0,w):
    for y in range(0,h):
      p1 = getPixel(picture,x1+x,y1+y)
      p2 = getPixel(picture,x2+x,y2+y)
      c1 = getColor(p1)
      c2 = getColor(p2)
      setColor(p1,makeColor(c2))
      setColor(p2,makeColor(c1))
    
def countWhite(picture):
  count = 0
  for p in getPixels(picture):
    if getColor(p) == white:
      count = count + 1
  return count

def countCloseToColor(picture, cr, cb, cg):
  count = 0
  for p in getPixels(picture):
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    if (|r - cr| <= 10) and (|b - cb| <= 10) and (|g - cg| <= 10):
      count = count + 1
  return count

#def getUL(picture): 
  #w = getWidth(picture)
  #h = getHeight(picture)
  #result = makeEmptyPicture((w/2), (h/2))'''
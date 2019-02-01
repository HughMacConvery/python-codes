#Jacob S., Jacy M., Wade Howard 
def keepBlue(picture):
  for p in getPixels(picture):
    setRed(p,0)
    setGreen(p,0)
  show(picture)
  
def maximizeBlue(picture):
  for p in getPixels(picture):
    setBlue(p,255)
  show(picture)
  
def averageRed(picture)
  result = makeEmptyPicture(getWidth(picture),getHeight(picture))
  
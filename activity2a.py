def picture():
  p = makePicture(pickAFile())
  show (p)
  explore(p)
  
def printRed(picture):
  pixels = getPixels(picture)
  for p in pixels():
    print getRed(p)
    
def printR(picture):
  pixels = getPixels(picture)
  for i in range(0,len(pixels)):
    print getRed(pixels[i])
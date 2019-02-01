def copyPicture(picture):
  result = makeEmptyPicture(getWidth(picture),getHeight(picture))
  pixels1 = getPixels(picture)
  pixels2 = getPixels(result)
  for i in range(0, len(pixels1)):
     c = getColor(pixels1[i])
     setColor(pixels2[i],c) 
  return result
  
def set(picture,pixel):
  result = makeEmptyPicture(getWidth(picture),getHeight(picture))
  pixel1 = getPixels(result)
  pixels = getPixels(picture)
  for i in range(0,len(pixels)):
    color = getColor(pixels[i])
    setColor(pixel1[i], makeColor(pixel))
  return result
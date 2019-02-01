#Jacy MacConvery,Jacob Smith, Thomas Mangan
def kthMorphPicture(start,end,n,k):
  result = makeEmptyPicture(getWidth(start),getHeight(start))
  pixels1 = getPixels(start)
  pixels2 = getPixels(end)
  pixels3 = getPixels(result)
  for i in range(0,len(pixels1)):
    startRed = getRed(pixels1[i])
    endRed = getRed(pixels2[i])
    setRed(pixels3[i], startRed + ((endRed - startRed)/n) * k)
    
    startGreen = getGreen(pixels1[i])
    endGreen = getGreen(pixels2[i])
    setGreen(pixels3[i], startGreen + ((endGreen - startGreen)/n) * k)
    
    startBlue = getBlue(pixels1[i])
    endBlue= getBlue(pixels2[i])
    setBlue(pixels3[i],startBlue + ((endBlue - startBlue)/n) * k) 
  return result
    
def morph(start,end,n):
  for c in range(0, n):
    show(kthMorphPicture(start,end,n,c))
  
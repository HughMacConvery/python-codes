def palindrome(word):
  length = len(word)
  if len(word) <= 1:
    return True
  else:
    return word[0] == word[-1] and palindrome(word[1: -1])

#def functionName(parameters):
  #if (base condition):
  # return a value or do an operation
  #else:
  # use the function with new (smaller) parameter values
  # and use this result in some way to solve the original problem

#def blob(pic,x,y):
  # if the pixel is outside the picture then don't count it
  #if x<0 or y<0 or x>getWidth(pic) or y>getHeight(pic):
    #return 0
  # if the pixel is white(ish) then we don't count it
  #elif distance(getColor(getPixel(pic,x,y)),white) < 10:
    #return 0
  #else:
    # mark the pixel as white so it doesn't get counted again
    #setColor(getPixel(pic,x,y),white)
    # count the pixel plus the blob counts of all its neighbors
    #return 1 + blob(pic,x-1,y) + blob(pic,x+1,y) + blob(pic,x,y-1) + blob(pic,x,y+1)
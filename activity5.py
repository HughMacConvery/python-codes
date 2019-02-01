def changeVolume(sound,factor):
  result = makeEmptySound(getLength(sound))
  for index in range(0,getLength(sound)):
    value = getSampleValueAt(sound,index)
    setSampleValueAt(result,index,value*factor)
  return result
    
def normalize(sound):
  largest = 0
  for index in range(0,getLength(sound)):
    value = getSampleValueAt(sound,index)
    if (value > largest):
      largest = value
      
  factor = 32767.0 / largest
  return changeVolume(sound,factor)
  
def findFirstZero(sound):
  for index in range (0,getLength(sound)):
     value = getSampleValueAt(sound,index)
     if (value == 0):
       return index 
  return -1
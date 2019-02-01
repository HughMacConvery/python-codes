# Jacy MacConvery, Ryland Collinson
def taperEnd(sound,num):
  result = duplicateSound(sound)
  for index in range(0, num):
    value = getSampleValueAt(sound, index + (getLength(sound)) -  num)
    setSampleValueAt (result, index + (getLength(sound)) -  num, value*(num - index)/num)
  return result
  
def overlay(sound, background, start):
  result = duplicateSound(background)
  for index in range(0, getLength(sound)):
    value =  getSampleValueAt(sound, index)
    back =  getSampleValueAt(background, index)
    setSampleValueAt (result, index + start, value + back)
  return result
  
def stutter(sound, start, end, numRepeats):
  len1 = getLength(sound)
  len2 = (end - start)
  result = makeEmptySound(len1 + (len2*(numRepeats - 1)))
  for index in range(0, start):
    value = getSampleValueAt(sound, index)
    setSampleValueAt (result, index, value)
  for c in range(0, numRepeats):
    for i in range(0, (end - start)):
      value1 = getSampleValueAt(sound, (i + start))
      setSampleValueAt(result, (i + start + (c*len2)), value1)
  for x in range(0, (getLength(sound) - end)):
     value2 = getSampleValueAt(sound, (x + end))
     setSampleValueAt(result, (x + end+(numRepeats-1)*len2), value2)  
  return result
    
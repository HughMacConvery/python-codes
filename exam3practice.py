def countZero(sound):
  count = 0
  for index in range (0, getLength(sound)):
    value = getSampleValueAt(sound, index)
    if (value == 0):
      count = count + 1
  return count

def chunk(sound, start, end):
  len1 = getLength(sound)
  len2 = (start + end)
  result = makeEmptySound(len2)
  for index in range (start, end):
    value = getSampleValueAt(sound, index)
    setSampleValueAt (result, index, value)
  return result
  
def doubleSound(sound):
  len1 = getLength(sound)
  result = makeEmptySound(len1 + len1)
  for index in range(0, len1):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(result, index, value)
  return result
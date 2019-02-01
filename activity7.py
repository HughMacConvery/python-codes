def soundToFile(sound, fileName):
  file = open(fileName, "wt")
  for s in getSamples(sound):
    value = getSampleValue(s)
    file.write(str(value)+'\n')
  file.close()
  
def fileToSound(fileName):
  file = open(fileName,"rt")
  sound = makeEmptySound(500000)
  line = file.readline()
  index = 0
  while line <> "":
    setSampleValueAt(sound,index,int(line))
    index += 1
    line = file.readline()
  file.close()
  return sound
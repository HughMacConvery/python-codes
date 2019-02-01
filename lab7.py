def find(sourcefile, targetfile, key):
  file = open(sourcefile, "rt")
  outFile = open(targetfile, "wt")
  line = file.readline()
  while line <>"":
    index = line.find(key)
    newLine = ""
    if index <> -1:
      for i in range(0,len(line)):
        if i in range (index, index+ len(key)): 
          newLine = newLine + line[i].upper()
        else:
            newLine = newLine + line[i]
      outFile.write(newLine)
    line = file.readline()
  file.close()
  outFile.close()
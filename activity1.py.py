def lineOfStars(n):
  print"*"*n
  
def square(n):
  for line in range(0,n):
    lineOfStars(n)
    
def triangel(n):
  for row in range(0,n):
    for col in range(row):
     lineOfStars(n)
     
def shout(string):
  answer = ""
  for letter in string:
    answer = answer + letter.upper()
  print answer
  
def myProgram(string):
  x = ""
  for i in range(0,len(string)):
    x = x + string[i].upper()
  print x
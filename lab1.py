def spaceitout(sentence, n):
  for i in range(0,n):
    print "" 
  x = sentence
  print x
  
def spaceout(sentence,n):
  x = sentence
  list = x.split()
  print list
  space = " "*n
  print space.join(list)
    
def encrypt(letter, n):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  for i in range(len(alpha)):
    if alpha[i] == letter:
      return alpha[(i + n)%len(alpha)]
  return letter 
  
def caesar(text, n):
  result = ''
  for i in text:
    result += encrypt(i, n)
  return result
  
def charactersBetween(string,start,end):
  s = len(string) + start
  e = len(string)
  for i in range(0,len(string)):
    print string[]
import random
class DrunkTurtle(Turtle):
  def randomWalk(self):
    x = self.getXPos()
    y = self.getYPos()
    md = self.getModelDisplay()
    width = md.getWidth()
    height = md.getHeight()
    while (x > 0 and x < width) and (y > 0 and y < height): 
      r = random.randint(0,3)
      if r == 0:
        self.setHeading(90)
        self.forward(10)
      if r == 1:
        self.setHeading(180)
        self.forward(10)
      if r == 2:
        self.setHeading(270)
        self.forward(10)
      if r == 3:
        self.setHeading(0)
        self.forward(10)
      x = self.getXPos()
      y = self.getYPos()
  def multipleTurtles(self):
    world = World()
    T1 = DrunkTurtle(world)
    T2 = DrunkTurtle(world)
    T3 = DrunkTurtle(world)
    T4 = DrunkTurtle(world)
    T1.randomWalk()
    T2.randomWalk()
    T3.randomWalk()
    T4.randomWalk()
  
class Song:
  def __init__(self, title, filename):
    self.title = title
    self.filename = filename
    self.songList = []
  def setTitle(self):
    return self.title
  def setSound(self):
    return self.sound 
  def getTimesPlayed(self, title):
     if setSound() called:
      self.songList.append(1)
class PlayList:
  def __init__(self, title):
    self.title = title
    self.songs = []
  def setSong(self, song):
    self.Songs.append(Song())
  def playTitle(self, title):
    title = PlayList(self.songs)
    play title
    
    
    
    
    
    
    
    
    
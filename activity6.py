ghost = 0

def playGame():
  location = "Porch"
  showIntroduction()
  while not (location == "Exit"):
    showRoom(location)
    direction = requestString("Which direction?")
    print "You typed ",direction
    location = pickRoom(direction, location)
    
def showIntroduction():
  print "Welcome to the Adventure House!"
  print "In each room you will be told which directions you can go."
  print "You can move north, south, east or west by typing that direction."
  print "Type help to replay this introduction"
  print "Type quit or exit to end the program"
  
def showRoom(room):
  print "========================"
  if room == "Porch":
    showPorch()
  if room == "Entryway":
    showEntryway()
  if room == "Kitchen":
    showKitchen()
  if room == "Livingroom":
    showLR()
  if room == "DiningRoom":
    showDR()
    
def showPorch():
  print "You are on the porch of a frightening looking house."
  print "The windows are broken.  It is a dark and stormy night."
  print "You can go north into the house.  If you dare."
  
def showEntryway():
  global ghost
  print "You are in the entry way of the house."
  print "There are cobwebs in the corner."
  print "You feel a sense of dread."
  if ghost == 0:
    print "You suddenly feel cold"
    print "You look up and see a thick mist."
    print "It seems to be moaning."
    print "Then it disappears."
    ghost = 1
  print "There is a passageway to the north and another to the east."
  print "The porch is behind you to the south."
  
def showKitchen():
  global ghost
  print "You are in the kitchen."
  print "All the surfaces are covered with pots, pans, food pieces, and pools of blood."
  print "You think you hear something up the stairs that go up the west side of the room."
  print "It's a scraping noise, like something being dragged along the floor."
  if ghost == 1:
    print "You see the mist you saw earlier."
    print "But now it's darker, and red."
    print "The moan increases in pitch and volume so now it sounds like  yell."
    print "Then it is gone."
    ghost = 0
  print "You can go to the south or east."
  
def showLR():
  print "You are in a living room."
  print "There are couches, chairs, and small tables."
  print "Everything is covered in dust and spider webs."
  print "You hear a crashing noise in another room."
  print "You can go north or west"
  
def showDR():
  print "You are in the dining room."
  print "There are remains of a meal on the table."
  print "You can't tell what it is, and maybe you don't want to."
  print "Was that a thump to the west?"
  print "You can go south or west."
  
def pickRoom(direction, room):
  if (direction == "quit") or (direction == "exit"):
    print "Goodbye"
    return "Exit"
  if direction == "help":
    showIntroduction()
    return room
  if room == "Porch":
    if direction == "north":
      return "Entryway"
  if room == "Entryway":
    if direction == "north":
      return "Kitchen"
    if direction == "east":
      return "LivingRoom"
    if direction == "south":
      return "Porch"
  if room == "Kitchen":
    if direction == "east":
      return "DiningRoom"
    if direction == "south":
      return "Entryway"
  if room == "LivingRoom":
    if direction == "west":
      return "Entryway"
    if direction == "north":
      return "DiningRoom"
  if room == "DiningRoom":
    if direction == "west":
      return "Kitchen"
    if direction == "south":
      return "LivingRoom"
  print "You can't (or don't want to) go in that direction."
  return room
  
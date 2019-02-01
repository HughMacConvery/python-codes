ghost = 0
hand = []
xp = []
win = 0
def playGame():
  location = "Porch"
  showIntroduction()
  while not (location == "Exit"):
    if win == 3:
       print "You Win"
    else:
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
  if room == "LivingRoom":
    showLR()
  if room == "DiningRoom":
    showDR()
  if room == "2ndHallway":
    show2ndF()
  if room == "MasterBedroom":
    showMB()
  if room == "underGround":
    showUG()
  if room == "under1":
    showU1()
  if room == "under2":
    showU2()    
def showPorch():
  global hand
  print "You are on the porch of a frightening looking house."
  print "The windows are broken.  It is a dark and stormy night."
  if "lantern" in hand:
    print "with the lantern in hand you notice a secret passage way underneth the porch"
    print "You can go south to go under the house. If you dare."
    print "Or you can go north into the house.  If you dare."
  else:
    print "you can go north into the house.  If you dare."
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
  global hand
  print "You are in the kitchen."
  print "All the surfaces are covered with pots, pans, food pieces, and pools of blood."
  print "You think you hear something up the stairs that go up the west side of the room."
  print "It's a scraping noise, like something being dragged along the floor."
  if "key" in hand:
    print "with the key in hand a stair way opens up"
    print "you can go west up the stairs"
  if ghost == 1:
    print "You see the mist you saw earlier."
    print "But now it's darker, and red."
    print "The moan increases in pitch and volume so now it sounds like  yell."
    print "Then it is gone."
    ghost = 0
  print "You can go to the south or east."  
def showLR():
  global hand
  if "key" in hand:
    print "You are in a living room."
    print "There are couches, chairs, and small tables."
    print "Everything is covered in dust and spider webs."
    print "You hear a crashing noise in another room."
    print "You can go north or west"
  else:
    print "You are in a living room."
    print "There are couches, chairs, and small tables."
    print "Everything is covered in dust and spider webs."
    print "There is a key on the tabel"
    print "do you want to pick it up?"
    print "if so enter key"  
def showDR():
  global hand
  global win
  win = win + 1
  if "lantern" in hand:
    print "You are in the dining room."
    print "There are remains of a meal on the table."
    print "You can't tell what it is, and maybe you don't want to."
    print "Was that a thump to the west?"
    print "You can go south or west."
  else:
    print "You are in the dining room."
    print "There are remains of a meal on the table."
    print "You can't tell what it is, and maybe you don't want to."
    print "You notice a latern on the counter with some oil in it"
    print "do you want to pick it up?"
    print "if so enter lantern"
def show2ndF():
  print "Your are now on the 2nd floor"
  print "in front of you is a giant door"
  print "You hear a roar coming from the room do you want to enter"
  print "To go forward continue on north"
def showMB():
  print "You enter the Master Bedroom"
  print "you see a ginat oger protecting a beautiful designed chest"
  if "bomb" in hand and xp == 1:
    print "The Oger start moving towards you you see it lift its club"
    print "As the Oger swings it down at you"
    print "You back step while tossing a bomb from your bomb bag at it"
    print "The bomb explodes sending Oger bits all over the room"
    print "As if programed to the chest opens up as soon as you kill the Oger"
    print "Inside is a simple piece of paper saying" 
    print "if you want more adventuer"
    print "and a greater chance of getting a true treasuer"
    print "go to this house"
    print "it then gives a location"
    print "Do you want to countine on this quest or stop now"
  if "bomb" in hand:
    print "The Oger start moving towards you you see it lift its club"
    print "As the Oger swings it down at you"
    print "You quickly take out one of the bombs from your bag"
    print "not knowing how long it takes to detonate you blow your self up" 
    print "along with the Oger"
    print "the last thing you hear is the sound of a chest unlocking"
    print "YOU HAVE DIED, Retunr to the start to try again" 
  else:
    print "The Oger start moving towards you you see it lift its club"
    print "As the Oger swings it down at you"
    print "you relize you have nothing to deffend your self with"
    print "The Oger clubs you to death with no effort at all"  
    print "YOU HAVE DIED, Retunr to the start to try again" 
def showUG():
  print "With the glow form the lantern" 
  print "You notice two paths ahead of you"
  print "You can go either east or west"
def showU1():
  global hand
  if "bomb" in hand:
    print "You have already been to this room "
    print "go east and chose a diffrent direction"
  else:
    print "You see a door up ahead and you notice it is unlocked"
    print "You enter the room not seeing the harm in it"
    print "You see a chest in the back wall"
    print "You approch the chest and notice it is locked"
    print "The lock is old and you can esaly break it open with your foot"
    print "Inside is a bag of bombs do you want to pick them up"
    print "if so type in bomb"
def showU2():
  global xp
  xp = 1
  print "You see a door up ahead and you notice it is unlocked"
  print "You enter the room not seeing the harm in it"
  print "As you enter the room the door locks behind you"
  print "The walls begen to close in on you"
  if "bomb" in hand:
    print "Thinking quickly you toss a bomb at the door"
    print "It explodes causing a hole to apperr" 
    print "You take some damage from exploson however"
    print "you can go wset to escape the death room"
  else:
    print "With nothing to free your self"
    print "The walls crush you until death"
    print "YOU HAVE DIED, Retunr to the start to try again" 
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
    if direction == "south":
      return "underGround"
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
    if direction == "west":
      return "2ndHallway" 
    if direction == "south":
      return "Entryway"
  if room == "LivingRoom":
    if direction == "west":
      return "Entryway"
    if direction == "north":
      return "DiningRoom"
    if direction == "key":
      hand.append("key")
  if room == "DiningRoom":
    if direction == "west":
      return "Kitchen"
    if direction == "south":
      return "LivingRoom"
    if direction == "lantern":
      hand.append("lantern")
  if room == "2ndHallway":
    if direction == "north":
      return "MasterBedroom"
    if direction == "south":
      return "Kitchen"
  if room == "MasterBedroom":
    if direction == "south":
      return "2ndHallway"
  if room == "underGround":
    if direction == "west":
      return "under1"
    if direction == "east":
      return "under2"
    if direction == "north":
     return "Porch"
  if room == "under1":
    if direction == "east":
      return "underGround"
    if direction == "bomb":
      hand.append("bomb")
  if room == "under2":
    if direction == "west":
      return "underGround"
  print "You can't (or don't want to) go in that direction."
  return room
  
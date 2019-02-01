class Student:
  def __init__(self, name, picFile):
    self.name = name
    self.grades = []
    self.picture = makePicture(picfile)
  def addGrade(self, grade):
    self.grades.append(grade)
  def avgGrade():
    sum = 0
    for g in self.grades:
      sum = sum + g
    return sum / len(self.grades)
  def showPicture(self):
    show(self.picture)
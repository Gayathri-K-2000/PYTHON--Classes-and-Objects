class Parent:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printdet(self):
    print("PARENTS NAME:  "+self.name+"\nPARENT'S AGE:  "+ self.age)

class Child(Parent):
  def __init__(self, name, age):
    Parent.__init__(self, name, age)

x = Child("Mike", "44")
x.printdet()

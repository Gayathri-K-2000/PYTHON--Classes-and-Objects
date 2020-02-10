class Parent:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printdet(self):
    print("PARENTS NAME:  "+self.name+"\nPARENT'S AGE:  "+ self.age)

class Child(Parent):
  def __init__(self, name, age):
    Parent.__init__(self, name, age)
    
  def printdetail(self):
  	print("CHILD'S NAME:  "+self.name+"\nCHILD'S AGE:  "+ self.age)

  	

x = Child("mike","34")
y= Child("ken","13")
x.printdet()
y.printdetail()

class Person:
    
    def __init__(self,name):
        self.name= name
    def talk(self):
        print("HI! I am "+self.name)
    
    def branch(self):
        if self.name=="Neha":
            branch="CSE"
        elif self.name=="Seha":
            branch="ECE"
        print("MY BRANCH IS "+branch)
a=str(input("enter a name option:\nn1- Neha\n n2- Seha\n"))
if a=="n1":
    n1= Person("Neha")
    n1.talk()
    n1.branch()
elif a=="n2":
    n1= Person("Seha")
    n1.talk()
    n1.branch()
else:
    print("invalid option....!!!!")

class Students:
    count=0
    name=""

    def __init__(self, name):
        self.name= name
        print(self.name +" Joined")

    def counting(self):
        self.count= self.count +1
        print("Count of " ,self.name, " is " ,self.count)

    def __del__(self):
        print("Class going on..")
     
a=Students("HENRY")
b=Students("SANA")
c=Students("RAY")
d=Students("JIM")
a.counting()
b.counting()
a.counting()
c.counting()
d.counting()
c.counting()


           

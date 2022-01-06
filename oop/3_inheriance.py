class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return f"Your name is {self.name} and age is {self.age}"
class Ruser(User):
    def __init__(self,name,age,hieght):
        User.__init__(self,name,age)
        self.hieght=hieght
p0=User('Haider',15)
p1=Ruser('Ali',18,'156cm')
print(p0.info())
print(p1.info())
input()
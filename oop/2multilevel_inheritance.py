class Inheritance:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return f"Your name is {self.name} And Your age is {self.age}"
    def height_1(self):
        return f"Your Height is {self.height}"
class Inheritance_2(Inheritance):
    def __init__(self,name,age,height):
        Inheritance.__init__(self,name,age)
        self.height=height
p1=Inheritance_2('Haider Ali',15,'157cm')
p2=Inheritance('Ali',20)
print(p1.info())
print(p1.height_1())
print(p2.info())

input()
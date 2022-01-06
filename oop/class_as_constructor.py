class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def string(cls,string):
        name,age=string.split(',')
        return cls(name,age)
    def info(self):
        return f"your name is {self.name} and your age is {self.age}"
p1=Person.string('Haider,15')
print(p1.info())
input()
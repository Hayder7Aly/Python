class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod 
    def from_string(cls,string):
        name,age=string.split(',')
        return cls(name,age)
    @staticmethod
    def hello():
        return 'this is staticmethod'
p1=Person.from_string('haider,15')
print(p1.hello())
input()
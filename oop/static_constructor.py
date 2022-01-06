class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def info_string(cls,string):
        name,age=string.split(',')
        return cls(name,age)
    @staticmethod
    def hello():
        return 'this is a staticmethod'
p1=Person.info_string('haider,15')
print(p1.hello())
input()
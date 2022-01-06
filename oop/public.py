class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def info(self):
        return f"your name is {self.name} and your age is {self._Person__age}"
p1=Person('hider',25)
p1._Person__age=15
print(p1._Person__age)
print(p1.info())
input()
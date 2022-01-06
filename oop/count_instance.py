class Person:
    count_instances=0
    def __init__(self,name,age):
        Person.count_instances+=1
        self.name=name
        self.age=age
    def info(self):
        return f"hell {self.name} your age is {self.age}"
p1=Person('haider',15)
p1=Person('haider',15)
print(p1.info())
print(Person.count_instances)
input()
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
p1=Person('haider','ali',15)
p2=Person('farman','ali',22)
print(p1.age)
print(p2.first_name)
input()
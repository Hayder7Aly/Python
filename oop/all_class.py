class Person:
    count_instances=0
    def __init__(self,name,age):
        Person.count_instances+=1
        self.name=name
        self.age=age
    @classmethod
    def info(cls):
        return f"YOU HAVE CREATED {cls.count_instances} instances of {cls.__name__}"
user=int(input('How many object created in programe:'))
for i in range(user):
    p1=Person('HAIDER ALI JUTT',15)
    print(p1.name)
print(p1.info())
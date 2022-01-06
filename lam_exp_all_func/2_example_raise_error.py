class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError('This class have more subclasses')
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return f"voice of cat is meaon meaon"
class Dog(Cat):
    def __init__(self,name,breed,inhert):
        super().__init__(name,breed)
        self.inhert=inhert
    def sound(self):
        return f"voice of dog is bhow bhow "
doggy=Dog('tony','pug','3d3')
ctt=Cat('geramny','tueg')
Animal_1=Animal('why')
user=input('which animal voice print :')
if user==doggy:
    print(doggy.sound())
elif user==ctt:
    print(ctt.sound())
elif user==Animal_1:
    print(Animal_1.sound())
else:
    print('InVlaid')
input()
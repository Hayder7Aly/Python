class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError('You have each class subclass')
class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return f"meon meon"
class Dog(Cat):
    def __init__(self,name,breed):
        super().__init__(name,breed)
        self.breed=breed
    def sound(self):
        return f"Bhow Bhow"
doggy=Dog('boony','pug')
catt=Cat('sty','tug')
animi=Animal('wolf')
user=input('Which animal voice print:')
if user=='doggy':
    print(doggy.sound())
elif user=='catt':
    print(catt.sound())
elif user=='animi':
    print(animi.sound())
else:
    print('You have enter wrong value:')
input()
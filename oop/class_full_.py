class Car:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
        self.total_quality=name+' '+model+' '+price
name=input('ENTER THE NAME OF CAR :')
model=input('ENTER THE MODEL OF CAR :')
price=input('ENTER THE PRICE OF CAR :')
p1=Car(name,model,price)
print(p1.total_quality)
input()
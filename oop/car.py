class Car:
    dis_percentage=10
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def apply_discount(self):
        o_r_p=(self.dis_percentage/100)*self.price
        return self.price-o_r_p
name=input('Enter the 1st car name:')
price=int(input('Enter the price of car :'))
name_1=input('Enter the 2nd car name :')
price_1=int(input('Enter the price of car :'))
c=Car(name,price)
c1=Car(name_1,price_1)
c1.dis_percentage=50
print(c.apply_discount())
print(c1.apply_discount())
input()
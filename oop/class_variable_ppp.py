class Brand:
    discount=10
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def info(self):
        return f"Product name is {self.name}  and  your brand price is Rs.{self.price}"
    def app_discount(self):
        or_price=(self.discount/100)*self.price
        return f"Your Price is apply on {self.discount}% Discount: {self.price-or_price}"
name=input('Enter the name of your brand is :')
price=int(input('Enter ther price of your brand is :'))
p1=Brand(name,price)
name_1=input('Enter the name of your brand is :')
price_1=int(input('Enter ther price of your brand is :'))
p2=Brand(name_1,price_1)
p2.discount=20
print('\n\t This statement for first date entery :')
print('\t',p1.info())
print('\t',p1.app_discount())
print('\t This statement for second data entery :')
print('\t',p2.info())
print('\t',p2.app_discount())
input()